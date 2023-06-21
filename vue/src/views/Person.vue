<template>
<el-card style="width: 500px;">
  <el-form label-width="115px" size="small">
    <el-form-item label="username" :label-width="formLabWidth">
      <el-input v-model="form.username" autocomplete="off"></el-input>
    </el-form-item>

    <el-form-item label="password" :label-width="formLabWidth">
      <el-input v-model="form.password" autocomplete="off"></el-input>
    </el-form-item>

    <el-form-item label="phone number" :label-width="formLabWidth">
      <el-input v-model="form.phonenumber" autocomplete="off"></el-input>
    </el-form-item>

    <el-form-item label="car number" :label-width="formLabWidth">
      <el-input v-model="form.carnumber" autocomplete="off"></el-input>
    </el-form-item>

    <el-form-item label="email" :label-width="formLabWidth">
      <el-input v-model="form.email" autocomplete="off"></el-input>
    </el-form-item>

<el-form-item>

  <el-button type="primary" @click="save">确 定</el-button>
</el-form-item>



  </el-form>


</el-card>
</template>

<script>
export default {
  // eslint-disable-next-line vue/multi-word-component-names
  name: "Person",
  data(){
    return{
      form:{},
      user:localStorage.getItem("user")?JSON.parse(localStorage.getItem("user")):{}
    }
  },
  created() {
    this.request.get("/user/username/"+this.user.username).then(res=>{
      if(res.code==='200'){
        this.form=res.data
      }
    })
  },
  methods:{
    save(){
      this.request.post("http://localhost:9090/user",this.form).then(res=>{
        if(res){
          this.$message.success("保存成功")
          this.load()
          this.dialogFormVisible=false
        }else {
          this.$message.error("保存失败")
        }
      })

    },
  }
}
</script>

<style scoped>

</style>