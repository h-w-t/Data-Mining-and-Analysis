<template>
  <div>
    <el-row style=" margin-bottom: 20px;width: 100%; height: 30%; display: flex; justify-content: center; align-items: center;">
    <el-card style="width: 40%; height: 30%;" class="box-card">
            <div slot="header" class="clearfix">
              <span>数据准备</span>
              <el-button size="medium" type="primary" class="ml-5" style="  float: right; padding: 3px 0" @click="analyzeData" >分析数据<i class="el-icon-bottom"></i></el-button>
              <el-button size="medium" type="primary" class="ml-5" style="  float: right; padding: 3px 0" @click="loadTable" >载入数据<i class="el-icon-bottom"></i></el-button>
              <el-button size="medium" type="primary" class="ml-5" style="  float: right; padding: 3px 0" @click="cleananalyze" >清除分析<i class="el-icon-bottom"></i></el-button>
            </div>
            <el-upload action="http://localhost:9090/cluster/import" :show-file-list="true" accept="xlsx" :on-success="handleExcelImportSuccess" style="display: inline-block">
              <el-button type="primary" class="ml-5">导入数据 <i class="el-icon-bottom"></i></el-button>
            </el-upload>
            <el-input placeholder="请输入k值" v-model="input1" clearable></el-input>
          </el-card>
    </el-row>

    <el-row style=" margin-bottom: 20px;width: 100%; height: 30%; display: flex; justify-content: center; align-items: center;">
          <el-card v-if="showTable" style="width: 50%; height: 40%;margin: 0 auto;" class="box-card">
            <div slot="header" class="clearfix">
              <span>原始数据表</span>
            </div>
            <el-table :data="tableData" height="250" border style="width: 100%">
              <el-table-column prop="id" label="ID" ></el-table-column>
              <el-table-column prop="x" label="X" ></el-table-column>
              <el-table-column prop="y" label="Y" ></el-table-column>
              </el-table>
          </el-card>
    </el-row>

    <el-row style=" margin-bottom: 20px;width: 100%; height: 30%; display: flex; justify-content: center; align-items: center;">
    <el-card v-if="showResult" style="width: 80%; height: 40%;" class="box-card">
            <div slot="header" class="clearfix">
              <span>聚类情况输出</span>
            </div>
            <div>
              <div id="main" style="width: 70%; height: 90vh; "></div>
            </div>
          </el-card>

</el-row>

  </div>
</template>

<script>
// import * as echarts from 'echarts';
import axios from "axios";
// import ecStat from 'echarts-stat';

export default {

  mounted(){
    this.fetchDataFromBackend(); // 调用后端数据获取函数
    this.fetchData();



  },
  // eslint-disable-next-line vue/multi-word-component-names
  name: "rules",
  data() {
    return {
      input1: '',//聚类的k值
      clusterCount: '', // echarts的clusterCount属性值
      tableData: [],
      showTable: false,
      showResult:false,
      originalData: [], // 原始数据
    };
  },
  methods: {
    fetchData() {
      // 进行 API 调用以获取数据
      axios
          .get('http://localhost:9090/cluster/data')
          .then((response) => {
            this.tableData = response.data;
            this.showTable = true;
          })
          .catch((error) => {
            console.log(error);
          });
    },

    doSomethingWithInput1Value(value) {
      // 在这里根据需要对 input1 的值进行处理
      console.log('Input1 value:', value);
      // 其他处理逻辑...
    },

    analyzeData() {

      // 获取输入框的值
      const input1Value = this.input1;

      // 在前端使用 input1Value 的值
      this.doSomethingWithInput1Value(input1Value);
      // 构造要发送给后端的数据对象
      const data = {
        input1: input1Value,

      };
      this.clusterCount = input1Value;

      const url = `http://localhost:8000/apis/iris/classify/${input1Value}/`;

      // 发送数据到后端
      axios.post(url, data)
          .then(response => {
            // 处理成功响应
            console.log(response.data);
          })
          .catch(error => {
            // 处理错误响应
            console.error(error);
          });
    },
    fetchDataFromBackend() {
      const url_blobs = 'http://localhost:8000/apis/cluster/data/blobs/echarts/';
      axios.get(url_blobs)
          .then(response => {
            const responseData = response.data.data;
            // 将后端传来的数据转换为表格组件需要的格式
            const tableData = responseData.map(item => {
              return {
                id:item.id,
                x:item.x,
                y:item.y,
              };
            });
            this.tableData = tableData;
            console.log(this.tableData);
          })
          .catch(error => {
            console.error(error);
          });
    },
    loadTable(){
      this.showTable=true;
    },
    cleananalyze(){
      this.showTable=false;
      this.showResult=false
    },
    handleExcelImportSuccess() {
      this.$message.success("导入成功")
      this.load()
      this.fetchData();
    },
    indexMethod(index){
      return index+1;
    },
    handleRemove(file, fileList) {
      console.log(file, fileList);
    },
    handlePreview(file) {
      console.log(file);
    },
    handleExceed(files, fileList) {
      this.$message.warning(`当前限制选择 3 个文件，本次选择了 ${files.length} 个文件，共选择了 ${files.length + fileList.length} 个文件`);
    },
    // eslint-disable-next-line no-unused-vars
    beforeRemove(file, fileList) {
      return this.$confirm(`确定移除 ${ file.name }？`);
    }
  }
};
</script>

<style>

</style>
