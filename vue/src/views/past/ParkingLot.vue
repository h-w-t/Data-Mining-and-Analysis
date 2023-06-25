<template>
  <div>
    <div style="margin: 10px 0">
      <el-input style="width: 200px" placeholder="请输入停车场名" suffix-icon="el-icon-search" v-model="parkname"></el-input>
      <el-input style="width: 200px" placeholder="请输入停车场地址" suffix-icon="el-icon-message" v-model="parkaddress" class="ml-5"></el-input>
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
        <el-button type="danger" slot="reference" @click="mess_succ">批量删除 <i class="el-icon-remove-outline"></i></el-button>
      </el-popconfirm>

      <el-upload action="http://localhost:9090/ParkingLot/import" :show-file-list="false" accept="xlsx" :on-success="handleExcelImportSuccess" style="display: inline-block">
        <el-button type="primary" class="ml-5">导入 <i class="el-icon-bottom"></i></el-button>
      </el-upload>

      <el-button type="primary" @click="exp" class="ml-5">导出 <i class="el-icon-top"></i></el-button>
    </div>

    <el-table :data="tableData" border stripe :header-cell-class-name="'headerBg'"  @selection-change="handleSelectionChange">
      <el-table-column type="selection" width="55"></el-table-column>
      <el-table-column prop="parkid" label="停车场ID" width="120"> </el-table-column>
      <el-table-column prop="parkname" label="停车场名" width="140"></el-table-column>
      <el-table-column prop="parkaddress" label="停车场地址" width="140"></el-table-column>
      <el-table-column prop="parktotal" label="停车场车位总数" width="140"></el-table-column>
      <el-table-column prop="parkresult" label="停车场剩余车位数量" width="140"></el-table-column>
      <el-table-column prop="userid" label="管理员id"></el-table-column>

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
            <el-button type="danger" slot="reference" @click="mess_succ">删除 <i class="el-icon-remove-outline"></i></el-button>
          </el-popconfirm>



        </template>
      </el-table-column>
    </el-table>
    <div style="padding: 10px 0">
      <el-pagination
          @size-change="handleSizeChange"
          @current-change="handleCurrentChange"
          :current-page="pageNum"
          :page-sizes="[2, 5, 7, 12, 20,30,50,100]"
          :page-size="pageSize"
          layout="total, sizes, prev, pager, next, jumper"
          :total="total">
      </el-pagination>
    </div>

    <el-dialog title="停车场信息" :visible.sync="dialogFormVisible" width="22%">
      <el-form label-width="115px" size="small">
        <el-form-item label="userid" :label-width="formLabWidth">
          <el-input v-model="form.userid" autocomplete="off"></el-input>
        </el-form-item>

        <el-form-item label="parkname" :label-width="formLabWidth">
          <el-input v-model="form.parkname" autocomplete="off"></el-input>
        </el-form-item>

        <el-form-item label="parkaddress" :label-width="formLabWidth">
          <el-input v-model="form.parkaddress" autocomplete="off"></el-input>
        </el-form-item>

        <el-form-item label="parktotal" :label-width="formLabWidth">
          <el-input v-model="form.parktotal" autocomplete="off"></el-input>
        </el-form-item>

        <el-form-item label="parkresult" :label-width="formLabWidth">
          <el-input v-model="form.parkresult" autocomplete="off"></el-input>
        </el-form-item>


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
  name: "ParkingLot",
  data(){
    return {
      tableData: [],
      total: 0,
      pageNum: 1,
      pageSize: 10,
      parkname: "",
      parkaddress:"",
      form:{},
      dialogFormVisible: false,
      formLabWidth: 0
    }
  },
  created(){
    this.load()

  },
  methods:{
    load() {
      fetch("http://localhost:9090/ParkingLot/page?pageNum="+this.pageNum+
          "&pageSize=" + this.pageSize +
          "&parkname=" + this.parkname +
          "&parkaddress=" + this.parkaddress)
          .then(res => res.json()).then(res => {
        console.log(res)
        this.tableData = res.data
        this.total = res.total
      })

      request.get("/ParkingLot/page", {
        params: {
          pageNum: this.pageNum,
          pageSize: this.pageSize,
        }
      }).then(res => {
        console.log(res)
        this.tableData = res.data
        this.total = res.total
      })

    },
    reset(){
      this.parkname=""
      this.parkaddress=""
      this.load()
    },

    save(){
      this.request.post("http://localhost:9090/ParkingLot",this.form).then(res=>{
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
      this.load()
    },
    del(id) {
      this.request.delete("http://localhost:9090/ParkingLot/" + id).then(res => {
        if (!res) {
          this.$message.error("删除失败")

        } else {
          this.$message.success("删除成功")
          this.load()
        }
      })
    },
    delBatch() {
      let ids = this.multipleSelection.map(v => v.id)  // [{}, {}, {}] => [1,2,3]
      this.request.post("http://localhost:9090/ParkingLot/del/batch", ids).then(res => {
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
      window.open("http://localhost:9090/ParkingLot/export")
    },
    handleExcelImportSuccess() {
      this.$message.success("导入成功")
      this.load()
    },
    mess_succ(){
      this.$message.success("删除成功")
    }

  },
}
</script>

<style scoped>
.heaferBg{
  background: #eee!important;
}

</style>