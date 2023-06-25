<template>
  <div class="wrapper">
    <div style="margin: 100px 0; text-align: center; font-size: 32px; color: #242833"><b>欢迎来到停车管理系统!</b></div>


    <div style="margin: 120px auto; background-color: rgba(255,255,255,0.53); width: 350px; height: 300px; padding: 20px; border-radius: 10px">
      <div style="margin: 20px 0; text-align: center; font-size: 24px; color: rgba(36,40,51,0.8)"><b>登录</b></div>
      <el-form :model="user" :rules="rules" ref="userForm">
        <el-form-item prop="username">
          <el-input placeholder="请输入用户名" size="medium" style="margin: 10px 0" prefix-icon="el-icon-user" v-model="user.username"></el-input>
        </el-form-item>
        <el-form-item prop="password">
          <el-input placeholder="请输入密码" size="medium" style="margin: 10px 0" prefix-icon="el-icon-lock" show-password v-model="user.password"></el-input>
        </el-form-item>
        <el-form-item style="margin: 10px 0; text-align: right">
          <el-button type="primary" size="small"  autocomplete="off" @click="login">登录</el-button>
          <el-button type="warning" size="small"  autocomplete="off" @click="$router.push('/register')">注册</el-button>
        </el-form-item>
      </el-form>
    </div>
  </div>
</template>

<script>
export default {
  // eslint-disable-next-line vue/multi-word-component-names
  name: "Login",
  data() {
    return {
      user: {},
      rules: {
        username: [
          { required: true, message: '请输入用户名', trigger: 'blur' },
          // { min: 3, max: 10, message: '长度在 3 到 5 个字符', trigger: 'blur' }
        ],
        password: [
          { required: true, message: '请输入密码', trigger: 'blur' },
          // { min: 1, max: 20, message: '长度在 1 到 20 个字符', trigger: 'blur' }
        ],
      }
    }
  },
  methods: {
    login() {

      this.request.post("/user/login", this.user).then(res => {
        if(!res){
          this.$message.error("用户名或密码错误")
        }else {
          if(res.state!=3){
            localStorage.setItem("user",JSON.stringify(res.data))//存储用户信息到浏览器中
            this.$message.success("管理员用户登陆成功")
            this.$router.push("/")
          }
          else if(res.state==3){
            this.$message.success("停车用户登陆成功")
            this.$router.push("/")
          }

        }
      })



      // this.$refs['userForm'].validate((valid) => {
      //   if (valid) {  // 表单校验合法
      //     this.request.post("/user/login", this.user).then(res => {
      //       if(res.code==='200') {
      //         localStorage.setItem("user",JSON.stringify(res.data))//存储用户信息到浏览器
      //         this.$router.push("/")
      //         this.$message.success("登陆成功")
      //       } else {
      //         this.$message.error("用户名或密码错误")
      //       }
      //     })
      //   }
      // });
    }
  }
}
</script>

<style>
.wrapper {
  height: 100vh;
  background-image: linear-gradient(to bottom right, #35bb51, #4ED29CFC, rgba(54, 171, 206, 0.99), #3550bb);
  overflow: hidden;
}
</style>
