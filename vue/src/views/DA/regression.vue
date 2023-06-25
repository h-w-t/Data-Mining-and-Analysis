<template>
  <div>
    <div class="settings"  >
      <!--      <div class="settings" style="display: flex; justify-content: center;">-->
      <el-row>
        <el-col :span="12" class="centered-col">
          <el-card style="width: 80%; height: 40%;" class="box-card">
            <div slot="header" class="clearfix">
              <span>数据准备</span>
              <el-button size="medium" style="float: right; padding: 3px 0" type="primary">分析数据</el-button>
            </div>
            <el-upload action="http://localhost:9090/regression/import" :show-file-list="true" accept="xlsx" :on-success="handleExcelImportSuccess" style="display: inline-block">
              <el-button type="primary" class="ml-5">导入数据 <i class="el-icon-bottom"></i></el-button>
            </el-upload>



          </el-card>
        </el-col>
        <el-col :span="12" class="centered-col">
<!--          <el-card style="width: 80%; height: 40%;" class="box-card">-->
<!--            <div slot="header" class="clearfix">-->
<!--              <span>回归情况</span>-->

<!--            </div>-->
<!--            <div>{{"回归"}}</div>-->
<!--          </el-card>-->
        </el-col>
      </el-row>
    </div>



    <div class="settings"  >
      <!--      <div class="settings" style="display: flex; justify-content: center;">-->
      <el-row>
        <el-col :span="12" class="centered-col">

          <el-card style="width: 80%; height: 40%;" class="box-card">
            <div slot="header" class="clearfix">
              <span>原始数据表</span>
            </div>
            <el-table
                :data="tableData"
                style="width: 100%">
              <el-table-column
                  type="index"
                  :index="indexMethod">
              </el-table-column>
              <el-table-column
                  prop="date"
                  label="x"
                  width="180">
              </el-table-column>
              <el-table-column
                  prop="name"
                  label="x"
                  width="180">
              </el-table-column>

            </el-table>

          </el-card>
        </el-col>
        <el-col :span="12" class="centered-col">
          <el-card style="width: 80%; height: 40%;" class="box-card">
            <div slot="header" class="clearfix">
              <span>回归图</span>
            </div>
            <div>
                            <div id="main" style="width: 100%; height: 90vh; "></div>
            </div>
          </el-card>
        </el-col>
      </el-row>
    </div>

  </div>
</template>

<script>
import * as echarts from 'echarts';


export default {


  //回归的图目前只有散点的，另一个线性回归的样例需要连接github的echart-start，来进来有报错，这个我后头再看看，回归先放缓
  mounted(){
    var chartDom = document.getElementById('main');
    var myChart = echarts.init(chartDom);
    var option;

    option = {
      xAxis: {},
      yAxis: {},
      series: [
        {
          symbolSize: 20,
          data: [
            [10.0, 8.04],
            [8.07, 6.95],
            [13.0, 7.58],
            [9.05, 8.81],
            [11.0, 8.33],
            [14.0, 7.66],
            [13.4, 6.81],
            [10.0, 6.33],
            [14.0, 8.96],
            [12.5, 6.82],
            [9.15, 7.2],
            [11.5, 7.2],
            [3.03, 4.23],
            [12.2, 7.83],
            [2.02, 4.47],
            [1.05, 3.33],
            [4.05, 4.96],
            [6.03, 7.24],
            [12.0, 6.26],
            [12.0, 8.84],
            [7.08, 5.82],
            [5.02, 5.68]
          ],
          type: 'scatter'
        }
      ]
    };

    option && myChart.setOption(option);
  },
  // eslint-disable-next-line vue/multi-word-component-names
  name: "rules",
  data() {
    return {
      input1: '',
      input2:'',
      tableData: [{
        date: '10', name: '20.7',},
        {date: '6.95', name: '8.07',},
        {date: '13.0', name: '7.58',},
        {date: '14.0', name: '7.2',},
        { date: '10.0', name: '8.04' },
        { date: '8.07', name: '6.95' },
        { date: '13.0', name: '7.58' },
        { date: '9.05', name: '8.81' },
        { date: '11.0', name: '8.33' },
        { date: '14.0', name: '7.66' },
        { date: '13.4', name: '6.81' },
        { date: '10.0', name: '6.33' },
        { date: '14.0', name: '8.96' },
        { date: '12.5', name: '6.82' },
        { date: '9.15', name: '7.2' },
        { date: '11.5', name: '7.2' },
        { date: '3.03', name: '4.23' },
      ],
      fileList:[],
      // fileList: [{name: 'food.jpeg', url: 'https://fuss10.elemecdn.com/3/63/4e7f3a15429bfda99bce42a18cdd1jpeg.jpeg?imageMogr2/thumbnail/360x360/format/webp/quality/100'},
      //   {name: 'food2.jpeg', url: 'https://fuss10.elemecdn.com/3/63/4e7f3a15429bfda99bce42a18cdd1jpeg.jpeg?imageMogr2/thumbnail/360x360/format/webp/quality/100'}],


    };
  },
  methods: {
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
.container {
  display: flex;
  justify-content: center;
}

.centered-col {
  display: flex;
  justify-content: center;
}

.settings {
  margin-bottom: 20px;
}
.content {
  margin-bottom: 20px;
}
.actions {
  text-align: center;
}
.upload-container {
  display: flex;
  align-items: center;
}

.upload-tip {
  margin-left: 10px;
}
</style>
