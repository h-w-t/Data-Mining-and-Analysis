<template>
  <div>
<!--    <div style="margin-bottom: 30px">-->
<!--      <el-breadcrumb separator="/">-->
<!--        <el-breadcrumb-item :to="{ path: '/' }">首页</el-breadcrumb-item>-->
<!--        <el-breadcrumb-item>用户管理</el-breadcrumb-item>-->
<!--      </el-breadcrumb>-->
<!--    </div>-->

    <div style="margin: 10px 0">
      <el-input style="width: 200px" placeholder="请输入用户名" suffix-icon="el-icon-search" v-model="username"></el-input>
      <el-input style="width: 200px" placeholder="请输入邮箱" suffix-icon="el-icon-message" v-model="email" class="ml-5"></el-input>
      <!--          <el-input style="width: 200px" placeholder="请输入车牌号" suffix-icon="el-icon-position" class="ml-5"></el-input>-->
      <el-button class="ml-5" type="primary" @click="load">搜索</el-button>
      <el-button  type="warning" @click="reset">重置</el-button>
    </div>

    <div style="margin: 10px 0">
      <el-button type="primary" @click="handleAdd">新增 <i class="el-icon-circle-plus-outline"></i></el-button>

      <el-popconfirm
          class="ml-5"
          confirm-button-text='确定'
          cancel-button-text='我再想想'
          icon="el-icon-info"
          icon-color="red"
          title="您确定批量删除这些数据吗？"
          @confirm="delBatch"
      >
        <el-button type="danger" slot="reference">批量删除 <i class="el-icon-remove-outline"></i></el-button>
      </el-popconfirm>

      <el-upload action="http://localhost:9090/user/import" :show-file-list="false" accept="xlsx" :on-success="handleExcelImportSuccess" style="display: inline-block">
        <el-button type="primary" class="ml-5">导入 <i class="el-icon-bottom"></i></el-button>
      </el-upload>

      <el-button type="primary" @click="exp" class="ml-5">导出 <i class="el-icon-top"></i></el-button>
    </div>

    <el-table :data="tableData" border stripe :header-cell-class-name="'headerBg'"  @selection-change="handleSelectionChange">
      <el-table-column type="selection" width="55"></el-table-column>
      <el-table-column prop="userid" label="ID" width="120"> </el-table-column>
      <el-table-column prop="username" label="用户姓名" width="140"></el-table-column>
      <el-table-column prop="password" label="账号密码" width="140"></el-table-column>
      <el-table-column prop="phonenumber" label="电话号码" width="140"></el-table-column>
      <el-table-column prop="carnumber" label="用户车牌号" width="140"></el-table-column>
      <el-table-column prop="email" label="电子邮箱"></el-table-column>

      <el-table-column prop="state" label="用户类型（1、2为管理员，3为普通用户）"></el-table-column>


      <el-table-column label="操作"  width="300" align="center">
        <template slot-scope="scope">
          <el-button type="success" @click="handleEdit(scope.row)">编辑 <i class="el-icon-edit"></i></el-button>
          <el-popconfirm
              class="ml-5"
              confirm-button-text='确定'
              cancel-button-text='我再想想'
              icon="el-icon-info"
              icon-color="red"
              title="您确定删除吗？"
              @confirm="del(scope.row.userid)"
          >


            <el-button type="danger" slot="reference">删除 <i class="el-icon-remove-outline"></i></el-button>
          </el-popconfirm>



        </template>
      </el-table-column>
    </el-table>
    <div style="padding: 10px 0">
      <el-pagination
          @size-change="handleSizeChange"
          @current-change="handleCurrentChange"
          :current-page="pageNum"
          :page-sizes="[2, 5, 10, 20, 50]"
          :page-size="pageSize"
          layout="total, sizes, prev, pager, next, jumper"
          :total="total">
      </el-pagination>
    </div>

            <el-dialog title="用户信息" :visible.sync="dialogFormVisible" width="22%">
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
                <el-form-item label="state" :label-width="formLabWidth">
                  <el-input v-model="form.state" autocomplete="off"></el-input>
                </el-form-item>


        <!--            <el-form-item label="活动区域" :label-width="formLabWidth">-->
        <!--              <el-select v-model="form.region" placeholder="选择活动区域">-->
        <!--                <el-option label="part1" value="shanghai"></el-option>-->
        <!--                <el-option label="part2" value="beijing"></el-option>-->
        <!--              </el-select>-->
        <!--            </el-form-item>-->
      </el-form>

      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogFormVisible = false">取 消</el-button>
        <el-button type="primary" @click="save">确 定</el-button>
      </div>

    </el-dialog>

  </div>

</template>

<script>
// import request from "@/utils/request";

import request from "@/utils/request";

export default {
  // eslint-disable-next-line vue/multi-word-component-names
  name: "User",
  data(){
    return {
      tableData: [],
      total: 0,
      pageNum: 1,
      pageSize: 10,
      //userid:"",
      username: "",
      //password:"",
      //phonenumber:"",
      //carnumber:"",
      email:"",
      state:"",
      form:{},
      //multipleSelection: [],
      dialogFormVisible: false,
      formLabWidth: 0
    }
  },
  created(){
    this.load()

  },
  methods:{


    load() {

      // request.get("http://localhost:9090/user/page?pageNum="+this.pageNum+ "&pageSize=" + this.pageSize + "&username=" + this.username + "&email=" + this.email).then(res=>{
      //   console.log(res)
      //   this.tableData=res.records
      //   this.total=res.total
      // })


      // request.get("http://localhost:9090//user/page", {
      //   params: {
      //     pageNum: this.pageNum,
      //     pageSize: this.pageSize,
      //     username: this.username,
      //     email: this.email
      //   }
      // }).then(res => {
      //   console.log(res)
      //
      //   this.tableData = res.records
      //   this.total = res.total
      //
      // })


      fetch("http://localhost:9090/user/page?pageNum="+this.pageNum+
          "&pageSize=" + this.pageSize +
          "&username=" + this.username +
          "&email=" + this.email)
          .then(res => res.json()).then(res => {
        console.log(res)
        this.tableData = res.data
        this.total = res.total
      })

      request.get("/user/page", {
        params: {
          pageNum: this.pageNum,
          pageSize: this.pageSize,
          // username: this.username,
          // email: this.email,
          //address: this.address,
        }
      }).then(res => {
        console.log(res)

        this.tableData = res.data
        this.total = res.total

      })

    },
    reset(){
      this.username=""
      this.email=""
      //this.carnumber=""
      this.load()
    },

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
    handleAdd(){
      this.dialogFormVisible=true
      this.form={}
    },
    handleEdit(row) {
      this.form = row
      this.dialogFormVisible = true
    },
    del(id) {
      this.request.delete("http://localhost:9090/user/" + id).then(res => {
        if (res) {
          this.$message.success("删除成功")
          this.load()
        } else {
          this.$message.error("删除失败")
        }
      })
    },
    delBatch() {
      let ids = this.multipleSelection.map(v => v.id)  // [{}, {}, {}] => [1,2,3]
      this.request.post("http://localhost:9090/user/del/batch", ids).then(res => {
        if (res) {
          this.$message.success("批量删除成功")
          this.load()
        } else {
          this.$message.error("批量删除失败")
        }
      })
    },


    handleSelectionChange(val) {
      console.log(val)
      this.multipleSelection = val
    },
    handleSizeChange(pageSize) {
      console.log(pageSize)
      this.pageSize = pageSize
      this.load()
    },
    handleCurrentChange(pageNum) {
      console.log(pageNum)
      this.pageNum = pageNum
      this.load()
    },
    exp(){
      window.open("http://localhost:9090/user/export")
    },
    handleExcelImportSuccess() {
      this.$message.success("导入成功")
      this.load()
    }

  },
}
</script>

<style scoped>
.heaferBg{
  background: #eee!important;
}

</style>