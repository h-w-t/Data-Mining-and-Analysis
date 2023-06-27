<template>
  <div>
    <el-row style=" margin-bottom: 20px;width: 100%; height: 30%; display: flex; justify-content: center; align-items: center;">
      <el-card style="width: 40%; height: 30%;" class="box-card">
        <div slot="header" class="clearfix">
          <span>数据准备</span>
          <el-button size="medium" type="primary" class="ml-5" style="  float: right; padding: 3px 0" @click="analyzeData" >分析数据<i class="el-icon-bottom"></i></el-button>
          <el-button size="medium" type="primary" class="ml-5" style="  float: right; padding: 3px 0" @click="loadTable" >载入数据<i class="el-icon-bottom"></i></el-button>
          <el-button size="medium" type="primary" class="ml-5" style="  float: right; padding: 3px 0" @click="cleananalyze" >清除分析<i class="el-icon-bottom"></i></el-button>            </div>
        <el-upload action="http://localhost:9090/regression/import" :show-file-list="true" accept="xlsx" :on-success="handleExcelImportSuccess" style="display: inline-block">
          <el-button type="primary" class="ml-5">导入数据 <i class="el-icon-bottom"></i></el-button>
        </el-upload>
      </el-card>
    </el-row>


    <el-row style=" margin-bottom: 20px;width: 100%; height: 30%; display: flex; justify-content: center; align-items: center;">
      <el-card v-if="showTable" style="width: 80%; height: 40%;margin: 0 auto;" class="box-card">
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
          <span>回归图</span>
        </div>
        <div>
          <div id="main" style="width: 100%; height: 90vh; "></div>
        </div>
      </el-card>
    </el-row>

  </div>
</template>

<script>
import * as echarts from 'echarts';

import ecStat from 'echarts-stat';
import axios from "axios";

export default {
  //回归的图目前只有散点的，另一个线性回归的样例需要连接github的echart-start，来进来有报错，这个我后头再看看，回归先放缓
  mounted(){


    this.fetchDataFromBackend();

  },
  // eslint-disable-next-line vue/multi-word-component-names
  name: "huiguitest",
  data() {
    return {
      tableData: [],
      fileList:[],
      showTable:false,
      showResult:false,

    };
  },
  methods: {

    generateRegression() {
      const url = 'http://localhost:8000/apis/regression/data/echarts/';
      axios.get(url)
          .then(response => {
            const RegressionData = response.data.data;
            this.renderRegression(RegressionData);
          })
          .catch(error => {
            console.error(error);
          });
    },
    renderRegression(RegressionData) {
      var chartDom = document.getElementById('main');
      var myChart = echarts.init(chartDom);
      var option;
      echarts.registerTransform(ecStat.transform.regression);

      option = {
        dataset: [
          {
            source: RegressionData
          },
          {
            transform: {
              type: 'ecStat:regression'
              // 'linear' by default.
              // config: { method: 'linear', formulaOn: 'end'}
            }
          }
        ],
        title: {
          text: 'Linear Regression',
          subtext: 'By ecStat.regression',
          sublink: 'https://github.com/ecomfe/echarts-stat',
          left: 'center'
        },
        legend: {
          bottom: 5
        },
        tooltip: {
          trigger: 'axis',
          axisPointer: {
            type: 'cross'
          }
        },
        // xAxis: {
        //   type: 'category',
        //   data: ['-6', '-3', '0', '3', '6'] // 修改横轴的数据
        // },
        // yAxis: {
        //   type: 'category',
        //   data: ['-30', '-15', '0', '15', '30'] // 修改纵轴的数据
        // },
        xAxis: {
          min:-3,
          max:5,
          splitLine: {
            lineStyle: {
              type: 'dashed'
            }
          }
        },
        yAxis: {
          min:-300,
          max:300,
          splitLine: {
            lineStyle: {
              type: 'dashed'
            }
          }
        },
        series: [
          {
            name: 'scatter',
            type: 'scatter'
          },
          {
            name: 'line',
            type: 'line',
            datasetIndex: 1,
            symbolSize: 0.1,
            symbol: 'circle',
            label: { show: true, fontSize: 16 },
            labelLayout: { dx: -20 },
            encode: { label: 2, tooltip: 1 }
          }
        ]
      };

      option && myChart.setOption(option);

    },
    loadTable(){
      this.showTable=true;
    },
    cleananalyze(){
      this.showTable=false;
      this.showResult=false
    },
    analyzeData() {
      const url = 'http://localhost:8000/apis/regression/data/echarts/'; // 后端接口的URL，请根据实际情况修改
      axios.get(url)
          .then((response) => {
            this.RegressionData = response.data.data; // 假设数据位于 response.data 字段，请根据实际情况修改
            this.generateRegression();
          })
          .catch((error) => {
            console.error(error);
          });
      // 获取输入框的值

      const input1Value = this.input1;
      const input2Value = this.input2;

      // 构造要发送给后端的数据对象
      const data = {
        input1: input1Value,
        input2: input2Value
      };
      //const url = `http://localhost:8000/apis/rules/${input1Value}&${input2Value}/`;

      // 发送数据到后端
      axios.post(url, data)
          .then(response => {
            // 处理成功响应
            console.log(response.data);
            this.showResult=true;
            this.showTable=true;
          })
          .catch(error => {
            // 处理错误响应
            console.error(error);
          });
      this.showResult=true;

    },
    fetchDataFromBackend() {
      axios.get('http://localhost:8000/apis/regression/all/')
          .then(response => {
            const responseData = response.data.data;
            // 将后端传来的数据转换为表格组件需要的格式
            const tableData = responseData.map(item => {
              return {
                id:item.id,
                x: item.x,
                y: item.y,
              };
            });
            this.tableData = tableData;
            console.log(this.tableData);
          })
          .catch(error => {
            console.error(error);
          });
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
