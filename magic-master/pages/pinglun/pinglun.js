
Page({ 
data: {
  axis:[
    {
      time:'2018-2-15',
      name:'张三医生',
      event:'垃圾太多'
    },
    {
      time: '2018-2-15',
      name: '王三医生',
      event: '垃圾太多'
    },
    {
      time: '2018-2-15',
      name: '张三医生',
      event: '垃圾太多'
    },
    {
      time: '2018-2-15',
      name: '张三',
      event: '垃圾太多'
    },
    {
      time: '2018-2-15',
      name: '张三',
      event: '垃圾太多'
    },
    {
      time: '2018-2-15',
      name: '张三',
      event: '垃圾太多'
    },
    {
      time: '2018-2-15',
      name: '张三',
      event: '垃圾太多'
    },
    {
      time: '2018-2-15',
      name: '张三',
      event: '垃圾太多'
    },{
      time: '2018-2-15',
      name: '张三',
      event: '垃圾太多'
    },
    {
      time: '2018-2-15',
      name: '张三',
      event: '垃圾太多'
    },
    {
      time: '2018-2-15',
      name: '张三',
      event: '垃圾太多'
    },

  ],
},
 
radioChange: function (e) {
  console.log(e.detail.value)
},

change:function(e){
  var that = this;
    console.log(e)
    that.setData({
       id: e.detail.current
    });
},

 
showBuyModal () {
  // 显示遮罩层
  var animation = wx.createAnimation({
      duration: 200,
      /**
        * http://cubic-bezier.com/ 
        * linear 动画一直较为均匀
        * ease 从匀速到加速在到匀速
        * ease-in 缓慢到匀速
        * ease-in-out 从缓慢到匀速再到缓慢
        * 
        * http://www.tuicool.com/articles/neqMVr
        * step-start 动画一开始就跳到 100% 直到动画持续时间结束 一闪而过
        * step-end 保持 0% 的样式直到动画持续时间结束 一闪而过
        */
      timingFunction: "ease",
      delay: 0
  })
  this.animation = animation
  animation.translateY(300).step()
  this.setData({
      animationData: animation.export(), // export 方法每次调用后会清掉之前的动画操作。
      showModalStatus: true
  })
  setTimeout(() => {
      animation.translateY(0).step()
      this.setData({
          animationData: animation.export()  // export 方法每次调用后会清掉之前的动画操作。
      })
      console.log(this)
  }, 200)
},

hideBuyModal () {
  // 隐藏遮罩层
  var animation = wx.createAnimation({
      duration: 200,
      timingFunction: "ease",
      delay: 0
  })
  this.animation = animation
  animation.translateY(300).step()
  this.setData({
      animationData: animation.export(),
  })
  setTimeout(function () {
      animation.translateY(0).step()
      this.setData({
          animationData: animation.export(),
          showModalStatus: false
      })
      console.log(this)
  }.bind(this), 200)
},
 
})
