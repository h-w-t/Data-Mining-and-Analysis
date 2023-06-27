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