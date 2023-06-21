<template>
  <el-container style="min-height: 100vh">

    <el-aside :width="sideWidth + 'px'" style="box-shadow: 2px 0 6px rgb(0 21 41 / 35%);">
      <Aside :isCollapse="isCollapse" :logoTextShow="logoTextShow" />
<!--      <el-menu :default-openeds="['1', '3']" style="min-height: 100%; overflow-x: hidden"-->
<!--               background-color="rgb(48, 65, 86)"-->
<!--               text-color="#fff"-->
<!--               active-text-color="#ffd04b"-->
<!--               :collapse-transition="false"-->
<!--               :collapse="isCollapse"-->
<!--      >-->
<!--        <div style="height: 60px; line-height: 60px; text-align: center">-->
<!--          <img src="../assets/logo.png" alt="" style="width: 20px; position: relative; top: 5px; right: 5px">-->
<!--          <b style="color: white" v-show="logoTextShow">停车管理系统</b>-->
<!--        </div>-->
<!--        <el-submenu index="1">-->
<!--          <template slot="title">-->
<!--            <i class="el-icon-message"></i>-->
<!--            <span slot="title">查看订单信息</span>-->
<!--          </template>-->
<!--          <el-menu-item-group title="待开发2">-->
<!--            <el-menu-item index="1-3">待开发3</el-menu-item>-->
<!--          </el-menu-item-group>-->
<!--          <el-submenu index="1-4">-->
<!--            <template slot="title">待开发4</template>-->
<!--            <el-menu-item index="1-4-1">待开发4-1</el-menu-item>-->
<!--          </el-submenu>-->
<!--        </el-submenu>-->
<!--        <el-submenu index="2">-->
<!--          <template slot="title">-->
<!--            <i class="el-icon-menu"></i>-->
<!--            <span slot="title">查看停车场信息</span>-->
<!--          </template>-->
<!--          <el-submenu index="2-4">-->
<!--            <template slot="title">待开发5</template>-->
<!--            <el-menu-item index="2-4-1">待开发5-1</el-menu-item>-->
<!--          </el-submenu>-->
<!--        </el-submenu>-->
<!--        <el-submenu index="3">-->
<!--          <template slot="title">-->
<!--            <i class="el-icon-setting"></i>-->
<!--            <span slot="title">联系信息</span>-->
<!--          </template>-->
<!--          <el-submenu index="3-4">-->
<!--            <template slot="title">待开发6</template>-->
<!--            <el-menu-item index="3-4-1">待开发6-1</el-menu-item>-->
<!--          </el-submenu>-->
<!--        </el-submenu>-->
<!--      </el-menu>-->
    </el-aside>

    <el-container>
      <el-header style="border-bottom: 1px solid #ccc;">
        <Header :collapseBtnClass="collapseBtnClass" :collapse="collapse"  />
<!--        <div style="flex: 1; font-size: 20px">-->
<!--          <span :class="collapseBtnClass" style="cursor: pointer" @click="collapse"></span>-->
<!--        </div>-->
<!--        <el-dropdown style="width: 70px; cursor: pointer">-->
<!--          <span>GSH</span><i class="el-icon-arrow-down" style="margin-left: 5px"></i>-->
<!--          <el-dropdown-menu slot="dropdown" >-->
<!--            <el-dropdown-item style="font-size: 14px; padding: 5px 0">个人信息</el-dropdown-item>-->
<!--            <el-dropdown-item style="font-size: 14px; padding: 5px 0">退出</el-dropdown-item>-->
<!--          </el-dropdown-menu>-->
<!--        </el-dropdown>-->

      </el-header>

      <el-main>
<!--        表示当前页面的子路由会在《router-view》中展示-->
        <router-view />

<!--        <div style="margin-bottom: 30px">-->
<!--          <el-breadcrumb separator="/">-->
<!--            <el-breadcrumb-item :to="{ path: '/' }">首页</el-breadcrumb-item>-->
<!--            <el-breadcrumb-item>用户管理</el-breadcrumb-item>-->
<!--          </el-breadcrumb>-->
<!--        </div>-->

<!--        <div style="margin: 10px 0">-->
<!--          <el-input style="width: 200px" placeholder="请输入用户名" suffix-icon="el-icon-search" v-model="username"></el-input>-->
<!--          <el-input style="width: 200px" placeholder="请输入邮箱" suffix-icon="el-icon-message" v-model="email" class="ml-5"></el-input>-->
<!--&lt;!&ndash;          <el-input style="width: 200px" placeholder="请输入车牌号" suffix-icon="el-icon-position" class="ml-5"></el-input>&ndash;&gt;-->
<!--          <el-button class="ml-5" type="primary" @click="load">搜索</el-button>-->
<!--          <el-button  type="warning" @click="reset">重置</el-button>-->

<!--        </div>-->



<!--        <div style="margin: 10px 0">-->
<!--          <el-button type="primary" @click="handleAdd">新增 <i class="el-icon-circle-plus-outline"></i></el-button>-->

<!--          <el-popconfirm-->
<!--              class="ml-5"-->
<!--              confirm-button-text='确定'-->
<!--              cancel-button-text='我再想想'-->
<!--              icon="el-icon-info"-->
<!--              icon-color="red"-->
<!--              title="您确定批量删除这些数据吗？"-->
<!--              @confirm="delBatch"-->
<!--          >-->
<!--            <el-button type="danger" slot="reference">批量删除 <i class="el-icon-remove-outline"></i></el-button>-->
<!--          </el-popconfirm>-->

<!--          <el-button type="primary">导入 <i class="el-icon-bottom"></i></el-button>-->
<!--          <el-button type="primary">导出 <i class="el-icon-top"></i></el-button>-->
<!--        </div>-->

<!--        <el-table :data="tableData" border stripe :header-cell-class-name="headerBg"  @selection-change="handleSelectionChange">-->
<!--          <el-table-column type="selection" width="55"></el-table-column>-->
<!--          <el-table-column prop="userid" label="ID" width="120"> </el-table-column>-->
<!--          <el-table-column prop="username" label="用户姓名" width="140"></el-table-column>-->
<!--          <el-table-column prop="password" label="账号密码" width="140"></el-table-column>-->
<!--          <el-table-column prop="phonenumber" label="电话号码" width="140"></el-table-column>-->
<!--          <el-table-column prop="carnumber" label="用户车牌号" width="140"></el-table-column>-->
<!--          <el-table-column prop="email" label="电子邮箱"></el-table-column>-->
<!--&lt;!&ndash;          <el-table-column prop="createuser_time" label="账户创建时间"></el-table-column>&ndash;&gt;-->


<!--          <el-table-column label="操作"  width="300" align="center">-->
<!--            <template slot-scope="scope">-->
<!--              <el-button type="success" @click="handleEdit(scope.row)">编辑 <i class="el-icon-edit"></i></el-button>-->
<!--              <el-popconfirm-->
<!--                  class="ml-5"-->
<!--                  confirm-button-text='确定'-->
<!--                  cancel-button-text='我再想想'-->
<!--                  icon="el-icon-info"-->
<!--                  icon-color="red"-->
<!--                  title="您确定删除吗？"-->
<!--                  @confirm="del(scope.row.userid)"-->
<!--              >-->


<!--                <el-button type="danger" slot="reference">删除 <i class="el-icon-remove-outline"></i></el-button>-->
<!--              </el-popconfirm>-->



<!--            </template>-->
<!--          </el-table-column>-->
<!--        </el-table>-->
<!--        <div style="padding: 10px 0">-->
<!--          <el-pagination-->
<!--              @size-change="handleSizeChange"-->
<!--              @current-change="handleCurrentChange"-->
<!--              :current-page="pageNum"-->
<!--              :page-sizes="[2, 5, 10, 20,50,100,500]"-->
<!--              :page-size="pageSize"-->
<!--              layout="total, sizes, prev, pager, next, jumper"-->
<!--              :total="total">-->
<!--          </el-pagination>-->
<!--        </div>-->

<!--        <el-dialog title="用户信息" :visible.sync="dialogFormVisible" width="22%">-->
<!--          <el-form label-width="115px" size="small">-->
<!--            <el-form-item label="username" :label-width="formLabWidth">-->
<!--              <el-input v-model="form.username" autocomplete="off"></el-input>-->
<!--            </el-form-item>-->

<!--            <el-form-item label="password" :label-width="formLabWidth">-->
<!--              <el-input v-model="form.password" autocomplete="off"></el-input>-->
<!--            </el-form-item>-->

<!--            <el-form-item label="phone number" :label-width="formLabWidth">-->
<!--              <el-input v-model="form.phonenumber" autocomplete="off"></el-input>-->
<!--            </el-form-item>-->

<!--            <el-form-item label="car number" :label-width="formLabWidth">-->
<!--              <el-input v-model="form.carnumber" autocomplete="off"></el-input>-->
<!--            </el-form-item>-->

<!--            <el-form-item label="email" :label-width="formLabWidth">-->
<!--              <el-input v-model="form.email" autocomplete="off"></el-input>-->
<!--            </el-form-item>-->


<!--&lt;!&ndash;            <el-form-item label="活动区域" :label-width="formLabWidth">&ndash;&gt;-->
<!--&lt;!&ndash;              <el-select v-model="form.region" placeholder="选择活动区域">&ndash;&gt;-->
<!--&lt;!&ndash;                <el-option label="part1" value="shanghai"></el-option>&ndash;&gt;-->
<!--&lt;!&ndash;                <el-option label="part2" value="beijing"></el-option>&ndash;&gt;-->
<!--&lt;!&ndash;              </el-select>&ndash;&gt;-->
<!--&lt;!&ndash;            </el-form-item>&ndash;&gt;-->
<!--          </el-form>-->
<!--          <div slot="footer" class="dialog-footer">-->
<!--            <el-button @click="dialogFormVisible = false">取 消</el-button>-->
<!--            <el-button type="primary" @click="save">确 定</el-button>-->
<!--          </div>-->
<!--        </el-dialog>-->



      </el-main>

    </el-container>
  </el-container>
</template>

<script>

// import request from "@/utils/request";

// import request from "@/utils/request";

import Aside from "@/components/Aside";
import Header from "@/components/Header";
import User from "@/views/User";




export default {

  // eslint-disable-next-line vue/multi-word-component-names
  name: 'Home',

  data() {
    return {
      // tableData: [],
      // total: 0,
      // pageNum: 1,
      // pageSize: 20,
      // userid:"",
      // username: "",
      // password:"",
      // phonenumber:"",
      // carnumber:"",
      // email:"",
      // form:{},
      // multipleSelection: [],
      // dialogFormVisible: false,

      collapseBtnClass: 'el-icon-s-fold',
      isCollapse: false,
      sideWidth: 200,
      logoTextShow: true,

    }
  },

//   created(){
// // 请求分页查询数据
//     this.load()
//
//   },
  components: {
    // eslint-disable-next-line vue/no-unused-components
    User,
    // eslint-disable-next-line vue/no-unused-components
    Aside,
    // eslint-disable-next-line vue/no-unused-components
    Header
  },
  methods: {



    collapse() {  // 点击收缩按钮触发
      this.isCollapse = !this.isCollapse
      if (this.isCollapse) {  // 收缩
        this.sideWidth = 64
        this.collapseBtnClass = 'el-icon-s-unfold'
        this.logoTextShow = false
      } else {   // 展开
        this.sideWidth = 200
        this.collapseBtnClass = 'el-icon-s-fold'
        this.logoTextShow = true
      }
    },
    // load() {
    //
    //   // request.get("http://localhost:9090/user/page?pageNum="+this.pageNum+ "&pageSize=" + this.pageSize + "&username=" + this.username + "&email=" + this.email).then(res=>{
    //   //   console.log(res)
    //   //   this.tableData=res.records
    //   //   this.total=res.total
    //   // })
    //
    //
    //   // request.get("http://localhost:9090//user/page", {
    //   //   params: {
    //   //     pageNum: this.pageNum,
    //   //     pageSize: this.pageSize,
    //   //     username: this.username,
    //   //     email: this.email
    //   //   }
    //   // }).then(res => {
    //   //   console.log(res)
    //   //
    //   //   this.tableData = res.records
    //   //   this.total = res.total
    //   //
    //   // })
    //
    //
    //   fetch("http://localhost:9090/user/page?pageNum="+this.pageNum+
    //                                             "&pageSize=" + this.pageSize +
    //                                             "&username=" + this.username +
    //                                             "&email=" + this.email)
    //       .then(res => res.json()).then(res => {
    //     console.log(res)
    //     this.tableData = res.data
    //     this.total = res.total
    //   })
    //
    // },
    // reset(){
    //   this.username=""
    //   this.email=""
    //   //this.carnumber=""
    //   this.load()
    // },
    //
    // save(){
    //   this.request.post("http://localhost:9090/user",this.form).then(res=>{
    //     if(res){
    //       this.$message.success("save successfully")
    //       this.load()
    //       this.dialogFormVisible=false
    //     }else {
    //       this.$message.error("fail to save")
    //     }
    //   })
    //
    // },
    // handleAdd(){
    //   this.dialogFormVisible=true
    //   this.form={}
    // },
    // handleEdit(row) {
    //   this.form = row
    //   this.dialogFormVisible = true
    // },
    // del(id) {
    //   this.request.delete("http://localhost:9090/user/" + id).then(res => {
    //     if (res) {
    //       this.$message.success("删除成功")
    //       this.load()
    //     } else {
    //       this.$message.error("删除失败")
    //     }
    //   })
    // },
    // delBatch() {
    //   let ids = this.multipleSelection.map(v => v.id)  // [{}, {}, {}] => [1,2,3]
    //   this.request.post("http://localhost:9090/user/del/batch", ids).then(res => {
    //     if (res) {
    //       this.$message.success("批量删除成功")
    //       this.load()
    //     } else {
    //       this.$message.error("批量删除失败")
    //     }
    //   })
    // },
    //
    //
    // handleSelectionChange(val) {
    //   console.log(val)
    //   this.multipleSelection = val
    // },
    // handleSizeChange(pageSize) {
    //   console.log(pageSize)
    //   this.pageSize = pageSize
    //   this.load()
    // },
    // handleCurrentChange(pageNum) {
    //   console.log(pageNum)
    //   this.pageNum = pageNum
    //   this.load()
    // }
  }
}
</script>

<style>
.headerBg {
  background: #eee!important;
}
</style>
