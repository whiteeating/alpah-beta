// pages/setting/setting.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    address: {
    name: '',
    shopname:'',
    phone: ''
    }
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    var self = this;

    wx.getStorage({
      key: 'address',
      success: function (res) {
        self.setData({
          address: res.data
        })
      }
    })
  },
    formSubmit() {
    var self = this;
    if (self.data.address.name && self.data.address.phone && self.data.address.detail) {
      wx.setStorage({
        key: 'address',
        data: self.data.address,
        success() {
          wx.showModal({
            title: '提示',
            content: '修改成功！',
            showCancel: false
          })
        }
      })
      wx.navigateBack();
    }
    else {
      wx.showModal({
        title: '提示',
        content: '请填写完整资料',
        showCancel: false
      })
    }
  },
  bindName(e) {
    this.setData({
      'address.name': e.detail.value
    })
  },
  bindShop(e) {
    this.setData({
      'address.shopname': e.detail.value
    })
  }, 
  bindPhone(e) {
    this.setData({
      'address.phone': e.detail.value
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
