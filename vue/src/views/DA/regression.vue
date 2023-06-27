<template>
  <div>
    <el-row style=" margin-bottom: 20px;width: 100%; height: 30%; display: flex; justify-content: center; align-items: center;">
      <el-card shadow="hover" style="width: 40%; height: 30%;" class="box-card">
        <div slot="header" class="clearfix">
          <span>数据准备</span>
        </div>

        <el-row style="margin-bottom: 20px; display: flex; justify-content: center; align-items: center;">
          <el-button type="primary" class="ml-5" style=" margin-bottom: 20px;justify-content: center; align-items: center;" @click="loadTable" round >载入数据<i class="el-icon-bottom"></i></el-button>
          <el-upload action="http://localhost:9090/regression/import" :show-file-list="true" accept=".xlsx, .csv" style="display: inline-block">
            <el-button type="primary" class="ml-5" style=" margin-bottom: 20px;justify-content: center; align-items: center;" round>导入数据文件 <i class="el-icon-bottom"></i></el-button>
          </el-upload>
        </el-row>
        <el-row style="margin-bottom: 20px; display: flex; justify-content: center; align-items: center;">
          <el-button type="info" class="ml-5" style=" margin-bottom: 20px;justify-content: center; align-items: center;" @click="cleananalyze" round>清除分析<i class="el-icon-bottom"></i></el-button>
          <el-button type="warning" class="ml-5" style=" margin-bottom: 20px;justify-content: center; align-items: center;" @click="analyzeData" round >分析数据<i class="el-icon-bottom"></i></el-button>
        </el-row>
      </el-card>
    </el-row>


    <el-row style=" margin-bottom: 20px;width: 100%; height: 30%; display: flex; justify-content: center; align-items: center;">
      <el-card shadow="hover" v-if="showTable" style="width: 80%; height: 40%;margin: 0 auto;" class="box-card">
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
      <el-card shadow="hover" v-if="showResult" style="width: 80%; height: 40%;" class="box-card">
        <div slot="header" class="clearfix">
          <span>回归结果可视化</span>
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

    //this.fetchDataFromBackend();

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
              type: 'ecStat:regression',
              config: { method: 'linear', formulaOn: 'end' }
            }
          },
          {
            transform: {
              type: 'ecStat:regression',
              config: { method: 'polynomial', order: 2, formulaOn: 'end' }
            }
          }
        ],
        title: {
          text: '回归分析',
          //subtext: 'By ecStat.regression',
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
            name: '数据集',
            type: 'scatter'
          },
          {
            name: '线性回归',
            type: 'line',
            datasetIndex: 1,
            symbolSize: 0.1,
            symbol: 'circle',
            label: { show: true, fontSize: 16 },
            labelLayout: { dx: -20 },
            encode: { label: 2, tooltip: 1 },
            lineStyle: {
              width: 3 // 设置线条粗细为2
            }
          },
          {
            name: '二阶回归',
            type: 'line',
            datasetIndex: 2,
            symbolSize: 0.1,
            symbol: 'circle',
            label: { show: true, fontSize: 16 },
            labelLayout: { dx: -20 },
            encode: { label: 2, tooltip: 1 },
            lineStyle: {
              width: 3 // 设置线条粗细为2
            }
          }
        ]
      };

      option && myChart.setOption(option);

    },
    loadTable(){
      this.fetchDataFromBackend();
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
