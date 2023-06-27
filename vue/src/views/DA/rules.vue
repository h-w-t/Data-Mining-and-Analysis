<template>
  <div>
    <el-row style=" margin-bottom: 20px;width: 100%; height: 30%; display: flex; justify-content: center; align-items: center;">
      <el-card style="width: 40%; height: 30%;" class="box-card" shadow="hover">
        <div slot="header" class="clearfix">
          <span>数据准备</span>
        </div>

        <el-row style="display: flex; justify-content: center; align-items: center;">
          <el-button type="primary" class="ml-5" style=" margin-bottom: 20px;justify-content: center; align-items: center;" @click="loadTable" round >载入数据<i class="el-icon-bottom"></i></el-button>
          <el-upload action="http://localhost:9090/rules/import" :show-file-list="true" accept=".xlsx, .csv" style="display: inline-block">
            <el-button type="primary" class="ml-5" style=" margin-bottom: 20px;justify-content: center; align-items: center;" round>导入数据文件 <i class="el-icon-bottom"></i></el-button>
          </el-upload>
        </el-row>

        <el-row style="margin-bottom: 20px; display: flex; justify-content: center; align-items: center;">
          <el-link :underline="false">支持度:  <el-input-number  v-model="input1" :precision="2" :step="0.01" :min="0" :max="1"></el-input-number></el-link>
        </el-row>
        <el-row style="margin-bottom: 20px; display: flex; justify-content: center; align-items: center;">
          <el-link :underline="false">置信度:  <el-input-number  v-model="input2" :precision="2" :step="0.01" :min="0" :max="1"></el-input-number></el-link>
        </el-row>

        <el-row style="margin-bottom: 20px; display: flex; justify-content: center; align-items: center;">
          <el-button type="info" class="ml-5" style=" margin-bottom: 20px;justify-content: center; align-items: center;" @click="cleananalyze" round>清除分析<i class="el-icon-bottom"></i></el-button>
          <el-button type="warning" class="ml-5" style=" margin-bottom: 20px;justify-content: center; align-items: center;" @click="analyzeData" round >分析数据<i class="el-icon-bottom"></i></el-button>
        </el-row>

      </el-card>
    </el-row>

    <el-row style=" margin-bottom: 20px;width: 100%; height: 30%; display: flex; justify-content: center; align-items: center;">
      <el-card shadow="hover" v-if="showTable"  style="width: 60%; height: 40%;margin: 0 auto;" class="box-card" >
        <div slot="header" class="clearfix"><span>原始数据表</span></div>
        <el-table  :data="tableData" height="250" border style="width: 100%">
          <el-table-column prop="id" label="ID" ></el-table-column>
          <el-table-column prop="item1" label="item1" ></el-table-column>
          <el-table-column prop="item2" label="item2" ></el-table-column>
          <el-table-column prop="item3" label="item3" ></el-table-column>
          <el-table-column prop="item4" label="item4" ></el-table-column>
        </el-table>
      </el-card>
    </el-row>

    <el-row style="margin-bottom: 20px;width: 100%; height: 30%; display: flex; justify-content: center; align-items: center;">
      <el-card shadow="hover" v-if="showResult" style="width: 60%; height: 40%;" class="box-card">
        <div slot="header" class="clearfix">
          <span>置信度热力图可视化</span>
        </div>
        <div>
          <div id="main" style="width: 100%; height: 90vh;"></div>
        </div>
      </el-card>
    </el-row>


  </div>
</template>

<script>
import * as echarts from 'echarts';
import axios from "axios";

export default {

  mounted(){
    // this.fetchDataFromBackend();
  },
  // eslint-disable-next-line vue/multi-word-component-names
  name: "rules",
  data() {
    return {
      heatmapData: [], // 存储热力图数据
      input1: '0.2',//置信度
      input2: '0.8',//支持度
      // 下面是表单的数据，目前是写定的
      tableData: [],
      showTable:false,
      showResult:false,
      heatData:[],
      chart: null,

    };
  },
  methods: {
    renderHeatmap(heatmapData) {
      var chartDom = document.getElementById('main');
      var myChart = echarts.init(chartDom);
      var option;

      const hours = ['面包', '可乐', '麦片', '牛奶', '鸡蛋'];
      const days = ['面包', '可乐', '麦片', '牛奶', '鸡蛋'];

      option = {
        tooltip: {
          position: 'top'
        },
        grid: {
          height: '50%',
          top: '10%'
        },
        xAxis: {
          type: 'category',
          data: hours,
          splitArea: {
            show: true
          }
        },
        yAxis: {
          type: 'category',
          data: days,
          splitArea: {
            show: true
          }
        },
        visualMap: {
          min: 0,
          max: 1,
          calculable: true,
          orient: 'horizontal',
          left: 'center',
          bottom: '15%'
        },
        series: [{
          name: 'Punch Card',
          type: 'heatmap',
          data: heatmapData.map(item => [item[0], item[1], item[2] || '-']),
          label: {
            show: true
          },
          emphasis: {
            itemStyle: {
              shadowBlur: 10,
              shadowColor: 'rgba(0, 0, 0, 0.5)'
            }
          }
        }]
      };
      option && myChart.setOption(option);
    },

    loadTable(){
      this.fetchDataFromBackend();
      this.showTable=true;
    },
    cleananalyze(){
      this.input1="0.2";
      this.input2="0.8";
      this.showTable=false;
      this.showResult=false
    },
    analyzeData() {

      // 获取输入框的值
      const input1Value = this.input1;
      const input2Value = this.input2;

      // 构造要发送给后端的数据对象
      const url = `http://localhost:8000/apis/rules/parameter/${input1Value}&${input2Value}/`;

      // 发送数据到后端
      axios.post(url)
          .then(response => {
            // 处理成功响应
            console.log(response.data);
            this.heatmapData = response.data.data; // 假设数据位于 response.data 字段，请根据实际情况修改
            this.renderHeatmap(this.heatmapData);
            this.showResult=true;
          })
          .catch(error => {
            // 处理错误响应
            console.error(error);
          });
      this.showResult=true;
    },

    fetchDataFromBackend() {
      axios.get('http://localhost:8000/apis/rules/all/')
          .then(response => {
            const responseData = response.data.data;
            // 将后端传来的数据转换为表格组件需要的格式
            const tableData = responseData.map(item => {
              return {
                id:item.id,
                item1: item.item1,
                item2: item.item2,
                item3: item.item3,
                item4: item.item4,
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
