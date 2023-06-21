<template>
<div style="line-height: 60px; display: flex " >

  <div style="flex: 1; ">
<!--    @click="collapse"-->
    <span :class="collapseBtnClass" style="cursor: pointer; font-size: 18px" ></span>

<!--      <el-breadcrumb separator="/" style="display: inline-block; margin-left:10px">-->
<!--        <el-breadcrumb-item :to="{ path: '/' }">首页</el-breadcrumb-item>-->
<!--&lt;!&ndash;        <el-breadcrumb-item>用户管理</el-breadcrumb-item>&ndash;&gt;-->
<!--      </el-breadcrumb>-->

    <el-breadcrumb separator="/" style="display: inline-block; margin-left: 10px">
      <el-breadcrumb-item :to="'/'">首页</el-breadcrumb-item>
      <el-breadcrumb-item v-if="showInformationManagement">信息管理</el-breadcrumb-item>
      <el-breadcrumb-item>{{ currentPathName }}</el-breadcrumb-item>
    </el-breadcrumb>


  </div>
  <el-dropdown style="width: 70px; cursor: pointer">
    <span>{{"Gsh"}}</span><i class="el-icon-arrow-down" style="margin-left: 5px"></i>
    <el-dropdown-menu slot="dropdown" style="width: 100px; text-align: center">
      <el-dropdown-item style="font-size: 14px; padding: 5px 0">
        <router-link to="/person">个人信息</router-link>
        </el-dropdown-item>
      <el-dropdown-item style="font-size: 14px; padding: 5px 0">
        <span to="/login" style="text-decoration: none" @click="logout">退出</span>
        </el-dropdown-item>
    </el-dropdown-menu>
  </el-dropdown>
</div>


</template>

<script>
export default {
  // eslint-disable-next-line vue/multi-word-component-names
  name: "Header",





  props:{
    collapseBtnClass: String,
    // eslint-disable-next-line vue/require-prop-type-constructor
    // collapse: Boolean,

  },
  computed: {
    showInformationManagement() {
      const paths = ['/user', '/Order']; // 定义需要显示 "信息管理" 的路径集合
      return paths.includes(this.currentPathName);
    },
    currentPathName () {
      // eslint-disable-next-line no-irregular-whitespace

      // eslint-disable-next-line no-irregular-whitespace
      return this.$store.state.currentPathName;　　//需要监听的数据
    }
  },
  watch: {
    // eslint-disable-next-line no-unused-vars
    currentPathName (newVal, oldVal) {
      console.log(newVal)
    }
  },
  data(){
    return {
      user:localStorage.getItem("username") ? JSON.parse(localStorage.getItem("username")) : {},
      paths:[],
      formLabWidth: 0, // 设置初始值
    }
  },

  methods:{
    collapse() {
      this.$emit("asideCollapse")
    },
    logout(){
      this.$router.push("/login")
      localStorage.removeItem("user")
      this.$message.success("退出成功")
    }
  }
}
</script>

<style scoped>

</style>