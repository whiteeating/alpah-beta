<?php

// 对js的escape编码进行解码
function js_unescape($str)
{
	$ret = '';
	$len = strlen($str);
	for ($i = 0; $i < $len; $i++) {
		if ($str[$i] == '%' && $str[$i+1] == 'u') {
			$val = hexdec(substr($str, $i+2, 4));
			if ($val < 0x7f) $ret .= chr($val);
			else if($val < 0x800) $ret .= chr(0xc0|($val>>6)).chr(0x80|($val&0x3f));
			else $ret .= chr(0xe0|($val>>12)).chr(0x80|(($val>>6)&0x3f)).chr(0x80|($val&0x3f));
			$i += 5;
		} else if ($str[$i] == '%') {
			$ret .= urldecode(substr($str, $i, 3));
			$i += 2;
		} else $ret .= $str[$i];
	}
	return $ret;
}

// 引入数据库头文件
require_once ('./db.php');
// 连接数据库
$conn = new mysqli(HOST, USERNAME, PASSWORD, DATABASE);
$conn -> set_charset('utf8');
// 获得动作
$op = $_POST['op'] ? $_POST['op'] : $_GET['op'];
// 分支处理
if (empty($op)) {
	include ('./index.html');
} elseif ($op == 'addquestion') {
	// 题目
	$title = $_POST['title'];
	$label=$_POST['label'];
	// 答案
	$tmp_file = $_FILES['answer']['tmp_name'];
	$file_types = explode(".", $_FILES['answer']['name']);
	$file_type = $file_types[count($file_types) - 1];
	$savePath = '/usr/local/nginx/html/api/upload/question/';
	$file_name = time() . "." . $file_type;

	copy($tmp_file, $savePath . $file_name);
	// 查询语句
	$conn -> query("INSERT INTO question (title,answer,label) VALUES ('$title','$file_name','$label')");
	// 关闭数据库
	$conn -> close();
	// 返回主页
	header("location:" . "./api.php");
} elseif ($op == 'searchfood') {
	$keyword = js_unescape($_GET['wd']);
	$res = $conn -> query("SELECT * FROM classes");
	$max_percent = 0.0;
	$result = null;
	while ($row = $res -> fetch_assoc()) {
		similar_text($row['class_name'], $keyword, $percent);
		if ($percent >= $max_percent) {
			$max_percent = $percent;
			$result = $row;
		}
	}
	if ($max_percent > 0.0) {
		echo json_encode(array(
			'errCode' => 0,
			'errMsg' => 'ok',
			'result' => $result,
			'ratio' => $max_percent
		));
	} else {
		echo json_encode(array(
			'errCode' => 1,
			'errMsg' => '查询无结果'
		));
	}
	exit();
} elseif ($op == 'delquestion') {
	$id = $_GET['id'];
	$conn -> query("delete from question where id=$id");
	$conn -> close();
	header("location:" . "./api.php");
} elseif ($op == 'addproblem') {// 提问题
	$openid = $_POST['openid'];
	$avatar = $_POST['avatar'];
	$nickname = $_POST['nickname'];
	$subtime = date("Y年m月d日 H:i", time());
	$title = $_POST['title'];
	$ratio = doubleval($_POST['ratio']);
	$label = $_POST['label'];
	
	$file_name="";
	if (!empty($_FILES['picture'])){
		// 处理上传的图片
		$tmp_file = $_FILES['picture']['tmp_name'];
		$file_types = explode(".", $_FILES['picture']['name']);
		$file_type = $file_types[count($file_types) - 1];
		$savePath = '/usr/local/nginx/html/api/upload/problem/';
		$file_name = time() . "." . $file_type;
		copy($tmp_file, $savePath . $file_name);
	}

	// SQL
	$conn -> query("INSERT INTO problem (openid, avatar, nickname, subtime, title, picture, ratio, label, answer_num) VALUES ('$openid', '$avatar', '$nickname', '$subtime', '$title', '$file_name', '$ratio', '$label', '0')");
	$conn -> close();
//	echo json_encode(array('data' => $_FILES['picture']));
} elseif ($op == 'problemlist') {// 获取问题列表
	$problem_list = array();
	// SQL
	$res = $conn -> query("SELECT * FROM problem ORDER BY id DESC");
	while ($row = $res -> fetch_assoc()) {
		$problem_list[] = $row;
	}
	echo json_encode(array('problem_list' => $problem_list));
} elseif ($op == 'addresponse') {// 回答问题
	$openid = $_POST['openid'];
	$pid = intval($_POST['pid']);
	$avatar = $_POST['avatar'];
	$nickname = $_POST['nickname'];
	$subtime = date("Y年m月d日 H:i", time());
	$title = $_POST['title'];
	$ratio = doubleval($_POST['ratio']);

	$file_name="";
	if (!empty($_FILES['picture'])){
		// 处理上传的图片
		$tmp_file = $_FILES['picture']['tmp_name'];
		$file_types = explode(".", $_FILES['picture']['name']);
		$file_type = $file_types[count($file_types) - 1];
		$savePath = '/usr/local/nginx/html/api/upload/response/';
		$file_name = time() . "." . $file_type;
		copy($tmp_file, $savePath . $file_name);
	}

	// SQL
	$conn -> query("INSERT INTO response (openid, pid, avatar, nickname, subtime, title, picture, ratio) VALUES ('$openid', '$pid', '$avatar', '$nickname', '$subtime', '$title', '$file_name', '$ratio')");
	$conn -> close();
} elseif ($op == 'responselist') {// 获取回答列表
	$pid = intval($_GET['pid']);
	$response_list = array();
	// SQL
	$res = $conn -> query("SELECT * FROM response WHERE pid = $pid ORDER BY id DESC");
	while ($row = $res -> fetch_assoc()) {
		$response_list[] = $row;
	}
	echo json_encode(array('response_list' => $response_list));
}elseif ($op=='myproblem'){
	$openid=$_POST['openid'];
	$problem_list=array();
	// SQL
	$res = $conn -> query("SELECT * FROM problem WHERE openid = '{$openid}' ORDER BY id DESC");
	while ($row = $res -> fetch_assoc()) {
		$pid=intval($row['id']);
		$query = $conn -> query("SELECT * FROM response WHERE pid = $pid ORDER BY id DESC");
		$response_num=$query->num_rows;
		$avatars=array();
		while($each=$query-> fetch_assoc()){
			if (count($avatars)<3){
				$avatars[]=$each['avatar'];
			}
		}
		$row['avatars']=$avatars;
		$row['response_num']=$response_num;
		$problem_list[] = $row;
	}
	echo json_encode(array('problem_list' => $problem_list));
}elseif ($op=='delmyproblem'){
	$pid=intval($_GET['pid']);
	// SQL
	$conn -> query("DELETE FROM problem WHERE id=$pid");
	$conn->query("DELETE FROM response WHERE pid=$pid");
}elseif ($op=='addcollection_q'){
	$openid=$_POST['openid'];
	$qid=intval($_POST['qid']);
	$url=$_POST['url'];
	
	// SQL
	$conn -> query("INSERT INTO collection_q (openid, qid, url) VALUES ('$openid', '$qid', '$url')");
	$conn -> close();
}elseif ($op=='collection_q_list'){
	$openid=$_POST['openid'];
	
	$savePath = '/usr/local/nginx/html/api/upload/question/';
	
	$list = array();
	// SQL
	$res = $conn -> query("SELECT * FROM collection_q cq, question q WHERE cq.qid = q.id AND cq.openid = '$openid' ORDER BY cq.id DESC");
	while ($row = $res -> fetch_assoc()) {
		$image_info=getimagesize($savePath.$row['answer']);
		$ratio=$image_info[0]/$image_info[1];
		$row['ratio']=$ratio;
		$list[] = $row;
	}
	echo json_encode(array('collectionList' => $list));
}elseif ($op=='iscollected'){
	$openid=$_GET['openid'];
	$qid=intval($_GET['qid']);
	
	// SQL
	$res=$conn -> query("SELECT * FROM collection_q WHERE openid='$openid' AND qid=$qid");
	if ($res->num_rows>0){
		echo json_encode(array('collected'=>TRUE));
	}else{
		echo json_encode(array('collected'=>FALSE));
	}
}elseif ($op=='delcollection_q'){
	$openid=$_POST['openid'];
	$qid=intval($_POST['qid']);
	
	// SQL
	$conn -> query("DELETE FROM collection_q WHERE openid='$openid' AND qid=$qid");
	$conn -> close();
}
