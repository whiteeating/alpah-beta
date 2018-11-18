import re
import datetime
import matplotlib.pyplot as plt
import jieba
from wordcloud import WordCloud,STOPWORDS
import seaborn as sns
from PIL import Image
import numpy as np

#做Days（天）表格
def get_date(data):
	dates = re.findall(r'\d{4}-\d{2}-\d{2}',data)
	days = [date[-2:] for date in dates]
	plt.subplot(221)#最后的显示分为四部分，Days占第一部分
	sns.countplot(days)#days就是数据集，countplot统计days每一天的重复数量就是每一天聊天数目
	plt.title('Days')
 
	#isocalendar()ISO标准化日期，返回三个值的元组（年份，星期数week number，星期几weekday）星期一为1，星期天为7
	weekdays = [datetime.date(int(date[:4]),int(date[5:7]),int(date[-2:])).isocalendar()[-1]  for date in dates]
	plt.subplot(222)
	sns.countplot(weekdays)
	plt.title('WeekDays')

#一天24h的图
def get_time(data):
	times = re.findall(r'\d+:\d{2}:\d{2}',data)
	hours = [time.split(":")[0] for time in times]#对每一个time分割出代表小时的那部分
 
	plt.subplot(223)
	#因为qq消息导出格式里，小时0-9是以个位形式出现，所以用个位的来对应
	sns.countplot(hours,order=['6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','0','1','2','3','4','5'])
	plt.title("Hours")
#词云制作
def get_wordcloud(text_data):
	word_list = [" ".join(jieba.cut(sententce)) for sententce in text_data]
	new_text = ' '.join(word_list)
	#背景图片的设置，我这里设置了一个小黄人图片
	pic = Image.open('qq.jpg')
	mang_mask = np.array(pic)
 
	plt.subplot(224)
	wordcloud = WordCloud(
		background_color="white",
		font_path = '/home/shen/Downloads/fonts/msyh.ttc',
		mask = mang_mask,
		stopwords = STOPWORDS,).generate(new_text)
	plt.imshow(wordcloud)
	plt.axis('off')
 
#匹配文本内容，调用上一个函数
def get_content(data):
	pa = re.compile(r'\d{4}-\d{2}-\d{2}.*?\d+:\d{2}:\d{2}.*?\n(.*?)\n\n',re.DOTALL)
	content = re.findall(pa,data)
	get_wordcloud(content)


def main():
	filename = "record.txt"
	#encoding一下，防止乱码
	with open(filename,encoding="UTF-8") as f:
		data = f.read()
	get_date(data)
	get_time(data)
	get_content(data)
	plt.show()
 
if __name__ == '__main__':
	main()
