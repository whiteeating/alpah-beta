// pages/shopcart/shopcart.js
Page({
  data: {
    isHaveAddress: false,
    isHaveCoupons: false,
    addressInfo: null,
    allPrice: 0,//总共需要支付的价格
    cartShopList: [
      {
        shopImg: "../../img/0001.jpg",
        shopTitle: "炒圆白菜",
        shopSelectInfo: "",
        shopPrice: "2.00",
        shopCount: 1,
      },
      {
        shopImg: "../../img/0002.jpg",
        shopTitle: "西红柿炒鸡蛋",
        shopSelectInfo: "",
        shopPrice: "2.00",
        shopCount: 1,
      },
      {
        shopImg: "../../img/0003.jpg",
        shopTitle: "红烧排骨",
        shopSelectInfo: "",
        shopPrice: "4.00",
        shopCount: 1,
      },
      {
        shopImg: "../../img/0004.jpg",
        shopTitle: "红烧茄子",
        shopSelectInfo: "",
        shopPrice: "2.00",
        shopCount: 1,
      },
      {
        shopImg: "../../img/0005.jpg",
        shopTitle: "蒸肉片",
        shopSelectInfo: "",
        shopPrice: "5.00",
        shopCount: 1,
      }
    ]

  },

  addAdress: function () {
    wx.navigateTo({
      url: '../../pages/address/address',

    })
  },
  selectToherAdress: function () {
    wx.navigateTo({
      url: '../../pages/addresslist/addresslist',

    })
  },

  //商品数量减少
  itemCountSub: function (e) {
    var index = e.currentTarget.dataset.index;
    var list = this.data.cartShopList;
    if (list[index].shopCount > 0) {
      list[index].shopCount = --list[index].shopCount;
      this.setData({
        cartShopList: list,
      });
    }
    //计算总价格
    this.allShopPrice();

  },

  //商品数量增加
  itemCountAdd: function (e) {
    var index = e.currentTarget.dataset.index;
    var list = this.data.cartShopList;
    list[index].shopCount = ++list[index].shopCount;

    this.setData({
      cartShopList: list,
    });
    //计算总价格
    this.allShopPrice();
  },


  /**
   * 计算总价格
   */
  allShopPrice: function () {
    var shopList = this.data.cartShopList;
    var shopPrice = 0.0;
    for (var key in shopList) {
      shopPrice += shopList[key].shopPrice * shopList[key].shopCount;
    }
    this.setData({
      allPrice: shopPrice,
    });
  },

onItemClick : function(e){
  var index = e.currentTarget.dataset.itemIndex;
  wx.navigateTo({
      url: '../../pages/shopinfo/shopinfo?id=' +e.currentTarget.dataset.itemIndex,
    })
},

goToPay : function(){
  wx.requestPayment({
    timeStamp: 'String1',
    nonceStr: 'String2',
    package: 'String3',
    signType: 'MD5',
    paySign: 'String4',
    success: function(res){
      // success
    },
    fail: function() {
      // fail
    },
    complete: function() {
      // complete
    }
  })
},

  backtochoose: function () {
    wx.navigateTo({
      url: '../../pages/zixuan/zixuan',
    })
  },



  onLoad: function (options) {
    // 页面初始化 options为页面跳转所带来的参数
  },
  onReady: function () {
    // 页面渲染完成
  },
  onShow: function () {
    // 页面显示
    var otherAddressInfo = getApp().globalData.otherAddressInfo;
    if (otherAddressInfo == null) {
      var addressList = wx.getStorageSync('address');
      for (var key in addressList) {
        if (addressList[key].isDefult) {
          this.setData({
            addressInfo: addressList[key],
            isHaveAddress: true,
          });
        }
      }
      if (this.data.addressInfo == null && addressList.length > 0) {
        this.setData({
          addressInfo: addressList[0],
          isHaveAddress: true,
        });
      }
    } else {
      this.setData({
        addressInfo: otherAddressInfo,
        isHaveAddress: true,
      });
    }


    //计算总价格
    this.allShopPrice();



  },
  onHide: function () {
    // 页面隐藏
  },
  onUnload: function () {
    // 页面关闭
    getApp().globalData.otherAddressInfo = null;
  },
   onShareAppMessage: function () {
    return {
      title: '我的购物车',
      desc: '好多好多东西，没钱了',
      path: 'www.baidu.com'
    }
  }



})