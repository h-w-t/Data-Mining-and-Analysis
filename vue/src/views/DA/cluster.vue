<template>
  <div>
    <el-row style=" margin-bottom: 20px;width: 100%; height: 30%; display: flex; justify-content: center; align-items: center;">
      <el-card shadow="hover" style="width: 40%; height: 30%;" class="box-card">
        <div slot="header" class="clearfix">
          <span>数据准备</span>
        </div>
        <el-col>

          <el-row style="margin-bottom: 20px; display: flex; justify-content: center; align-items: center;">
            <el-dropdown size="mini" split-button type="primary" @command="handleCommand">
              <span >载入数据</span>
              <el-dropdown-menu slot="dropdown">
                <el-dropdown-item command="a" @click="loadTable">blobs数据集</el-dropdown-item>
                <el-dropdown-item command="b" @click="loadTable" >moons数据集</el-dropdown-item>
              </el-dropdown-menu>
            </el-dropdown>

            <el-upload action="http://localhost:9090/rules/import" :show-file-list="true" accept=".xlsx, .csv" style="display: inline-block">
              <el-button type="primary" class="ml-5" >导入数据文件 <i class="el-icon-bottom"></i></el-button>
            </el-upload>
          </el-row>

          <el-row style="margin-bottom: 20px; display: flex; justify-content: center; align-items: center;">
            <el-link :underline="false">k值:  <el-input-number  v-model="input1" :precision="0" :step="1" :min="1" ></el-input-number></el-link>
          </el-row>

          <el-row style="margin-bottom: 20px; display: flex; justify-content: center; align-items: center;">
            <el-button type="info" class="ml-5" style=" margin-bottom: 20px;justify-content: center; align-items: center;" @click="cleananalyze" >清除分析<i class="el-icon-bottom"></i></el-button>
            <el-button type="warning" class="ml-5" style=" margin-bottom: 20px;justify-content: center; align-items: center;" @click="analyzeData(command)"  >分析数据<i class="el-icon-bottom"></i></el-button>
          </el-row>
        </el-col>

        <el-col>

        </el-col>

      </el-card>
    </el-row>

    <el-row style=" margin-bottom: 20px;width: 100%; height: 30%; display: flex; justify-content: center; align-items: center;">
      <el-card shadow="hover" v-if="showTable" style="width: 60%; height: 40%;margin: 0 auto;" class="box-card">
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
      <el-card shadow="hover" v-if="showResult" style="width: 60%; height: 40%;" class="box-card">
        <div slot="header" class="clearfix">
          <span>聚类情况可视化</span>
        </div>
        <div>
          <div id="main" style="width: 70%; height: 90vh; "></div>
        </div>
      </el-card>

    </el-row>

  </div>
</template>

<script>
import axios from "axios";

import * as echarts from 'echarts';

import ecStat from 'echarts-stat';

export default {

  mounted(){


  },
  // eslint-disable-next-line vue/multi-word-component-names
  name: "cluster",
  data() {
    return {
      input1: '1',//聚类的k值
      clusterCount: '', // echarts的clusterCount属性值
      tableData: [],
      showTable: false,
      showResult:false,
      command:'',
      ClusterData:[],
    };
  },
  methods: {
    handleCommand(command) {
      this.command=command;
      this.loadTable(command);

    },

    generateCluster(input1Value,url) {
      const Count=input1Value;
      axios.get(url)
          .then(response => {
            const ClusterData = response.data.data;
            this.renderCluster(ClusterData, Count, this.command);
          })
          .catch(error => {
            console.error(error);
          });

    },
    renderCluster(ClusterData,Count,command) {

      var chartDom = document.getElementById('main');
      var myChart = echarts.init(chartDom);
      var option;
      var xAxisMin, xAxisMax, yAxisMin, yAxisMax;
      if (command == 'a') {
        xAxisMin = -10; // 根据需要设置 x 轴的最小值
        xAxisMax = 15;  // 根据需要设置 x 轴的最大值
        yAxisMin = -15; // 根据需要设置 y 轴的最小值
        yAxisMax = 15;  // 根据需要设置 y 轴的最大值
      } else if (command === 'b') {
        // eslint-disable-next-line no-unused-vars
        xAxisMin = -2;  // 根据需要设置 x 轴的最小值
        // eslint-disable-next-line no-unused-vars
        xAxisMax = 3;   // 根据需要设置 x 轴的最大值
        // eslint-disable-next-line no-unused-vars
        yAxisMin = -2;  // 根据需要设置 y 轴的最小值
        // eslint-disable-next-line no-unused-vars
        yAxisMax = 2;   // 根据需要设置 y 轴的最大值
      }
      // var ClusterCount=Count;
      var DIM_CLUSTER_INDEX = 2;
      var DATA_DIM_IDX = [0, 1];
      var CENTER_DIM_IDX = [3, 4];
// See https://github.com/ecomfe/echarts-stat
      var step = ecStat.clustering.hierarchicalKMeans(ClusterData, {
        clusterCount: Count,
        outputType: 'single',
        outputClusterIndexDimension: DIM_CLUSTER_INDEX,
        outputCentroidDimensions: CENTER_DIM_IDX,
        stepByStep: true
      });
      var colorAll = [
        // '#bbb',
        '#37A2DA',
        '#e06343',
        '#37a354',
        '#b55dba',
        '#b5bd48',
        '#8378EA',
        '#96BFFF'
      ];
      var ANIMATION_DURATION_UPDATE = 1500;
      function renderItemPoint(params, api) {
        var coord = api.coord([api.value(0), api.value(1)]);
        var clusterIdx = api.value(2);
        if (clusterIdx == null || isNaN(clusterIdx)) {
          clusterIdx = 0;
        }
        var isNewCluster = clusterIdx === api.value(3);
        var extra = {
          transition: []
        };
        var contentColor = colorAll[clusterIdx];
        return {
          type: 'circle',
          x: coord[0],
          y: coord[1],
          shape: {
            cx: 0,
            cy: 0,
            r: 5
          },
          extra: extra,
          style: {
            fill: contentColor,
            stroke: '#333',
            lineWidth: 1,
            shadowColor: contentColor,
            shadowBlur: isNewCluster ? 12 : 0,
            transition: ['shadowBlur', 'fill']
          }
        };
      }
      function renderBoundary(params, api) {
        var xVal = api.value(0);
        var yVal = api.value(1);
        var maxDist = api.value(2);
        var center = api.coord([xVal, yVal]);
        var size = api.size([maxDist, maxDist]);
        return {
          type: 'ellipse',
          shape: {
            cx: isNaN(center[0]) ? 0 : center[0],
            cy: isNaN(center[1]) ? 0 : center[1],
            rx: isNaN(size[0]) ? 0 : size[0] + 15,
            ry: isNaN(size[1]) ? 0 : size[1] + 15
          },
          extra: {
            renderProgress: ++targetRenderProgress,
            enterFrom: {
              renderProgress: 0
            },
            transition: 'renderProgress'
          },
          style: {
            fill: null,
            stroke: 'rgba(0,0,0,0.2)',
            lineDash: [4, 4],
            lineWidth: 4
          }
        };
      }
      function makeStepOption(option, data, centroids) {
        var newCluIdx = centroids ? centroids.length - 1 : -1;
        var maxDist = 0;
        for (var i = 0; i < data.length; i++) {
          var line = data[i];
          if (line[DIM_CLUSTER_INDEX] === newCluIdx) {
            var dist0 = Math.pow(line[DATA_DIM_IDX[0]] - line[CENTER_DIM_IDX[0]], 2);
            var dist1 = Math.pow(line[DATA_DIM_IDX[1]] - line[CENTER_DIM_IDX[1]], 2);
            maxDist = Math.max(maxDist, dist0 + dist1);
          }
        }
        var boundaryData = centroids
            ? [[centroids[newCluIdx][0], centroids[newCluIdx][1], Math.sqrt(maxDist)]]
            : [];
        option.options.push({
          series: [
            {
              type: 'custom',
              encode: {
                tooltip: [0, 1]
              },
              renderItem: renderItemPoint,
              data: data
            },
            {
              type: 'custom',
              renderItem: renderBoundary,
              animationDuration: 3000,
              silent: true,
              data: boundaryData
            }
          ]
        });
      }
      var targetRenderProgress = 0;
      option = {
        timeline: {
          top: 'center',
          right: 50,
          height: 300,
          width: 10,
          inverse: true,
          autoPlay: false,
          playInterval: 2500,
          symbol: 'none',
          orient: 'vertical',
          axisType: 'category',
          label: {
            formatter: 'step {value}',
            position: 10
          },
          checkpointStyle: {
            animationDuration: ANIMATION_DURATION_UPDATE
          },
          data: []
        },
        baseOption: {
          animationDurationUpdate: ANIMATION_DURATION_UPDATE,
          transition: ['shape'],
          tooltip: {},
          xAxis: {
            min: xAxisMin,
            max: xAxisMax,

            type: 'value'
          },
          yAxis: {
            min: yAxisMin,
            max: yAxisMax,
            type: 'value'
          },
          series: [
            {
              type: 'scatter'
            }
          ]
        },
        options: []
      };
      makeStepOption(option, ClusterData);
      option.timeline.data.push('0');
      for (var i = 1, stepResult; !(stepResult = step.next()).isEnd; i++) {
        makeStepOption(
            option,
            echarts.util.clone(stepResult.data),
            echarts.util.clone(stepResult.centroids)
        );
        option.timeline.data.push(i + '');
      }

      option && myChart.setOption(option);

    },

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



    analyzeData(command) {
      let url = ``;
      if(command=='a') {
        url=`http://localhost:8000/apis/cluster/data/blobs/echarts/`;
      }
      else if(command=='b') {
        url='http://localhost:8000/apis/cluster/data/moons/echarts/'
      }
      // 获取输入框的值
      const input1Value = this.input1;
      this.generateCluster(input1Value,url);
      // 发送数据到后端
      this.showResult=true;
    },
    fetchDataFromBackend(commond) {
      let url='';
      if(commond=='a')
      {
        // eslint-disable-next-line no-unused-vars
        url='http://localhost:8000/apis/cluster/data/blobs/'
      }
      else if(commond=='b')
      {
        url='http://localhost:8000/apis/cluster/data/moons/'
      }

      axios.get(url)
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
    loadTable(commond){
      this.fetchDataFromBackend(commond);
      this.showTable=true;
    },
    cleananalyze(){
      this.input1='1';
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
