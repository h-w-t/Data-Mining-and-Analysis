<template>
  <div class="wrapper">
    <div style="margin: 30px 0; text-align: center; font-size: 32px; color: #242833"><b>欢迎来到停车管理系统!</b></div>


    <div style="margin: 50px auto; background-color: rgba(255,255,255,0.53); width: 350px; height: 550px; padding: 20px; border-radius: 10px">
      <div style="margin: 20px 0; text-align: center; font-size: 24px; color: rgba(36,40,51,0.8)"><b>注册</b></div>
      <el-form :model="user" :rules="rules" ref="userForm">
        <el-form-item prop="username">
          <el-input placeholder="请输入用户名" size="medium" style="margin: 15px 0" prefix-icon="el-icon-user" v-model="user.username"></el-input>
        </el-form-item>
        <el-form-item prop="password">
          <el-input placeholder="请输入密码" size="medium" style="margin: 5px 0" prefix-icon="el-icon-lock" show-password v-model="user.password"></el-input>
        </el-form-item>
        <el-form-item prop="confirmPassword">
          <el-input placeholder="请确认密码" size="medium" style="margin: 5px 0" prefix-icon="el-icon-lock" show-password v-model="user.confirmPassword"></el-input>
        </el-form-item>
        <el-form-item prop="phonenumber">
          <el-input placeholder="请输入手机号" size="medium" style="margin: 5px 0" prefix-icon="el-icon-lock"  v-model="user.phonenumber"></el-input>
        </el-form-item>
        <el-form-item prop="carnumber">
          <el-input placeholder="请输入车牌号" size="medium" style="margin: 5px 0" prefix-icon="el-icon-lock" v-model="user.carnumber"></el-input>
        </el-form-item>
        <el-form-item prop="email">
          <el-input placeholder="请输入邮箱" size="medium" style="margin: 5px 0" prefix-icon="el-icon-lock" v-model="user.email"></el-input>
        </el-form-item>



        <el-form-item style="margin: 5px 0; text-align: right">
          <el-button type="primary" size="small"  autocomplete="off" @click="login">注册</el-button>
<!--          <el-button type="warning" size="small"  autocomplete="off" @click="$router.push('/login')">返回登录</el-button>-->
          <el-button type="warning" size="small"  autocomplete="off" @click="gotologin">返回登录</el-button>

        </el-form-item>
      </el-form>
    </div>
  </div>
</template>

<script>
export default {
  // eslint-disable-next-line vue/multi-word-component-names
  name: "Register",
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
        confirmPassword: [
          { required: true, message: '请输入密码', trigger: 'blur' },
          { min: 1, max: 20, message: '长度在 1 到 20 个字符', trigger: 'blur' }
        ],
        phonenumber: [
          { required: true, message: '请输入手机号', trigger: 'blur' },
          // { min: 1, max: 20, message: '长度在 1 到 20 个字符', trigger: 'blur' }
        ],
        carnumber: [
          { required: true, message: '请输入车牌号', trigger: 'blur' },
          // { min: 1, max: 20, message: '长度在 1 到 20 个字符', trigger: 'blur' }
        ],
        email: [
          { required: true, message: '请输入邮箱', trigger: 'blur' },
          // { min: 1, max: 20, message: '长度在 1 到 20 个字符', trigger: 'blur' }
        ],
      }
    }
  },
  methods: {

    login() {
      this.$refs['userForm'].validate((valid) => {
        if (valid) {  // 表单校验合法
          if (this.user.password !== this.user.confirmPassword) {
            this.$message.error("两次输入的密码不一致")
            return false
          }
          this.request.post("/user/register", this.user).then(res => {
            if(!res) {
              localStorage.setItem("user",JSON.stringify(res.data))
              this.$router.push("/Login")
              this.$message.success("注册成功")
            } else {

              this.$message.error("注册失败")
            }
          })
        }
      });
    },





    gotologin() {
      this.$router.push('/login').then(() => {
        window.location.reload(); // 刷新当前页面
      });
    }
  }
}
</script>

<style>
.wrapper {
  height: 100vh;
  background-image: linear-gradient(to bottom right, #f14265, #112ecc);
  overflow: hidden;
}
</style>
