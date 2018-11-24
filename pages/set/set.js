// pages/setting/setting.js
Page({

  /**
   * 页面的初始数据
   */
  /**
   * 生命周期函数--监听页面加载
   */
  data: {
    thumb: '',
    nickname: '',
    
    hasAddress: false,
    address: {},
    shopOpened:true,
    showContent: true
  },
  onHide: function () {
    this.setData({
      showContent: false
    })
  },
  // 开张
  openShop: function () {
    console.log("ok1")
    this.setData({
      shopOpened: false
    })
  },
  // 店铺休息
  rest: function () {
    console.log("ok2")
    this.setData({
      shopOpened: true
    })
  },
  // 店铺打烊
  close: function () {
    this.setData({
      shopOpened: true
    })
  },

  onLoad() {
    var self = this;
    /**
     * 获取用户信息
     */
    wx.getUserInfo({
      success: function (res) {
        self.setData({
          thumb: res.userInfo.avatarUrl,
          nickname: res.userInfo.nickName
        })
      }
    })
  },
  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {

  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {

  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {

  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {

  }
})
