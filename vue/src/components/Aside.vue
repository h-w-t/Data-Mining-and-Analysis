<template>
  <el-menu :default-openeds="['0', '99999']" style="min-height: 100%; overflow-x: hidden"
           background-color="#445157"
           text-color="#fff"
           active-text-color="#ffd04b"
           :collapse-transition="false"
           :collapse="isCollapse"
           router
  >
    <div style="height: 60px; line-height: 60px; text-align: center">
      <img src="../assets/parklogo.jpg" alt="" style="width: 20px; position: relative; top: 5px; right: 5px">
      <b style="color: white" v-show="logoTextShow">数据分析可视化系统</b>

    </div>


    <el-menu-item index="/home">
      <template slot="title">
        <i class="el-icon-house"></i>
        <span slot="title">首页</span>
      </template>
    </el-menu-item>

    <el-submenu index="2">
      <template slot="title">
        <i class="el-icon-s-custom"></i>
        <span slot="title">数据分析</span>
      </template>
      <el-menu-item index="/rules"><i class="el-icon-user"></i>关联规则</el-menu-item>
      <el-menu-item index="/cluster"><i class="el-icon-aim"></i>聚类分析</el-menu-item>
      <el-menu-item index="/classify"><i class="el-icon-shopping-cart-1"></i>分类分析</el-menu-item>
      <el-menu-item index="/regression"><i class="el-icon-s-order"></i>回归分析</el-menu-item>
    </el-submenu>



    <el-submenu index="1">
      <template slot="title">
        <i class="el-icon-s-custom"></i>
        <span slot="title">以往功能</span>
      </template>
      <el-submenu index="1-2">
        <template slot="title">
          <i class="el-icon-s-custom"></i>
          <span slot="title">信息管理</span>
        </template>
        <el-menu-item index="/user"><i class="el-icon-user"></i>用户信息</el-menu-item>
        <el-menu-item index="/parkinglot"><i class="el-icon-aim"></i>停车场信息</el-menu-item>
        <el-menu-item index="/parkingspace"><i class="el-icon-shopping-cart-1"></i>停车位信息</el-menu-item>
        <el-menu-item index="/Order"><i class="el-icon-s-order"></i>订单信息</el-menu-item>
      </el-submenu>

      <el-submenu index="1-3">
        <template slot="title">
          <i class="el-icon-s-data"></i>
          <span slot="title">数据统计</span>
        </template>
        <el-menu-item index="/Echart_user"><i class="el-icon-s-marketing"></i>用户注册趋势</el-menu-item>
        <el-menu-item index="/Echart_park"><i class="el-icon-position"></i>停车场数量可视化</el-menu-item>
      </el-submenu>


      <el-submenu index="1-4">
        <template slot="title">
          <i class="el-icon-s-opportunity"></i>
          <span slot="title">业务功能</span>
        </template>
        <el-menu-item index="/BookSpace"><i class="el-icon-edit"></i>预订停车位</el-menu-item>
        <el-menu-item index="/Park"><i class="el-icon-truck"></i>停车</el-menu-item>


      </el-submenu>


      <el-submenu index="1-5">
        <template slot="title">
          <i class="el-icon-menu"></i>
          <span slot="title">便捷功能</span>
        </template>
        <el-menu-item index="/time_ui"><i class="el-icon-time"></i>时间校验</el-menu-item>
        <el-menu-item index="/gdmap"><i class="el-icon-map-location"></i>高德地图</el-menu-item>
      </el-submenu>


      <el-submenu index="1-6">
        <template slot="title">
          <i class="el-icon-question"></i>
          <span slot="title">如有疑问？</span>
        </template>
        <el-menu-item index="/explain"><i class="el-icon-document"></i>说明文档</el-menu-item>
        <el-menu-item index="/linkus"><i class="el-icon-phone"></i>联系我们</el-menu-item>
      </el-submenu>

      <el-menu-item index="1-7"><i class="el-icon-setting"></i>系统备份与恢复</el-menu-item>
    </el-submenu>






  </el-menu>



</template>

<script>
export default {
  // eslint-disable-next-line vue/multi-word-component-names
  name: "Aside",
  data(){
    return {
      collapse: false,
    }
  },
  props:{
    isCollapse:Boolean,
    logoTextShow:Boolean
  }
}
</script>

<style scoped>

</style>