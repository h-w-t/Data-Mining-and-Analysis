<template>
<div>
  <el-carousel :interval="3500" type="card" height="200px">
    <el-carousel-item v-for="item in imagebox" :key="item.id">
      <img :src="item.idView" style="width:100%;height:100%" class="image">
    </el-carousel-item>
  </el-carousel>




  <el-collapse accordion>
    <el-collapse-item>
      <template slot="title">价格展示<i class="header-icon el-icon-s-marketing"></i></template>

      <el-carousel :interval="2500" type="card" height="200px">
        <el-carousel-item v-for="item in cardbox" :key="item.id">
          <el-card class="box-card" style="width: 100%;height: 100%">
            <div slot="header" class="clearfix">
              <span>{{ item.title }}</span>
            </div>
            <div v-for="content in item.contents" :key="content" class="text item">
              {{ content }}
            </div>
          </el-card>
        </el-carousel-item>
      </el-carousel>

    </el-collapse-item>

    <el-collapse-item>
      <template slot="title">特惠信息<i class="header-icon el-icon-present"></i></template>
      <div>暂无,敬请期待！</div>
    </el-collapse-item>





  </el-collapse>

</div>

</template>

<script>
export default {
  // eslint-disable-next-line vue/multi-word-component-names
  name: "Home",


  data: function () {
    return {
      imagebox: [
        // {id: 0, idView: require('../assets/1.jpg')},
        // {id: 1, idView: require('../assets/2.jpg')},
        // {id: 2, idView: require('../assets/3.jpg')},
        // {id: 3, idView: require('../assets/4.jpg')},
        // {id: 4, idView: require('../assets/5.jpg')},
        // {id: 5, idView: require('../assets/6.jpg')},
        {id: 0, idView: require('../../assets/R1.jpg')},
        {id: 1, idView: require('../../assets/R2.jpg')},
        {id: 2, idView: require('../../assets/R3.jpg')},
        {id: 3, idView: require('../../assets/R4.jpg')},
        {id: 4, idView: require('../../assets/R6.jpg')},
        {id: 5, idView: require('../../assets/R5.jpg')},
        {id: 6, idView: require('../../assets/R7.jpg')},
        {id: 7, idView: require('../../assets/R8.jpeg')},

      ],
      cardbox: [
        {
          id: 1,
          title: '工技大松江停车场',
          contents: ['本停车场5元/小时，前15分钟免费\n超过10小时为10元/小时'],
          contents1: ['超过10小时为10元/小时']
        },
        {
          id: 2,
          title: '东华松江停车场',
          contents: ['本停车场5元/小时，前15分钟免费\n超过10小时为10元/小时']
        },
        {
          id: 3,
          title: '交大闵行停车场',
          contents: ['本停车场5元/小时，前15分钟免费\n超过10小时为10元/小时']
        },
        {
          id: 4,
          title: '工技大长宁停车场',
          contents: ['本停车场5元/小时，前15分钟免费\n超过10小时为10元/小时']
        },
        {
          id: 5,
          title: '东华长宁停车场',
          contents: ['本停车场5元/小时，前15分钟免费\n超过10小时为10元/小时']
        },
        {
          id: 6,
          title: '东华长宁停车场',
          contents: ['本停车场5元/小时，前15分钟免费\n超过10小时为10元/小时']
        },
        {
          id: 7,
          title: '上理杨浦停车场dong',
          contents: ['本停车场5元/小时，前15分钟免费\n超过10小时为10元/小时']
        },
        // Add more card objects as needed
      ],

      // 浏览器宽度
      screenWidth: 0
    }


  },



}
</script>

<style scoped>

</style>

<style>
.el-carousel__item h3 {
  color: #475669;
  font-size: 14px;
  opacity: 0.75;
  line-height: 200px;
  margin: 0;
}

.el-carousel__item:nth-child(2n) {
  background-color: #99a9bf;
}

.el-carousel__item:nth-child(2n+1) {
  background-color: #d3dce6;
}

.el-card {
  min-width: 380px;
  margin-right: 20px;
  transition: all .5s;
}
.el-card:hover{
  margin-top: -5px;
}

.mid{
  margin-top: 25%;
  height: 50%;
}
</style>