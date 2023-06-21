<template>
  <div>
    <div class="settings"  >
      <!--      <div class="settings" style="display: flex; justify-content: center;">-->
      <el-row>
        <el-col :span="12" class="centered-col">
          <el-card style="width: 80%; height: 40%;" class="box-card">
            <div slot="header" class="clearfix">
              <span>数据准备</span>
              <el-button style="float: right; padding: 3px 0" type="text">分析数据</el-button>
            </div>
            <el-upload
                class="upload-demo"
                action="https://jsonplaceholder.typicode.com/posts/"
                :on-preview="handlePreview"
                :on-remove="handleRemove"
                :before-remove="beforeRemove"
                multiple
                :limit="3"
                :on-exceed="handleExceed"
                :file-list="fileList">
              <div class="upload-container">
                <el-button size="medium" type="primary">上传数据文件</el-button>
                <div class="upload-tip">请上传 CSV 文件</div>
              </div>
            </el-upload>
            <el-input
                placeholder="请输入k值"
                v-model="input1"
                clearable>
            </el-input>


          </el-card>
        </el-col>
        <el-col :span="12" class="centered-col">
          <el-card style="width: 80%; height: 40%;" class="box-card">
            <div slot="header" class="clearfix">
              <span>聚类情况</span>

            </div>
            <div>{{"聚类"}}</div>
          </el-card>
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
                  label="日期"
                  width="180">
              </el-table-column>
              <el-table-column
                  prop="name"
                  label="姓名"
                  width="180">
              </el-table-column>
              <el-table-column
                  prop="address"
                  label="地址">
              </el-table-column>
            </el-table>

          </el-card>
        </el-col>
        <el-col :span="12" class="centered-col">
          <el-card style="width: 80%; height: 40%;" class="box-card">
            <div slot="header" class="clearfix">
              <span>散点图输出</span>
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
              //散点图的横纵数据，不过这个样例没有带不同颜色的聚类效果，后续再后面根据不同聚类情况可以再加
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
      input1: '',//聚类的k值

      tableData: [{
        date: '2016-05-03',
        name: '王小虎',
        address: '上海市普陀区金沙江路 1518 弄'
      }, {
        date: '2016-05-02',
        name: '王小虎',
        address: '上海市普陀区金沙江路 1518 弄'
      }, {
        date: '2016-05-04',
        name: '王小虎',
        address: '上海市普陀区金沙江路 1518 弄'
      },{
        date: '2016-05-04',
        name: '王小虎',
        address: '上海市普陀区金沙江路 1518 弄'
      },{
        date: '2016-05-04',
        name: '王小虎',
        address: '上海市普陀区金沙江路 1518 弄'
      },],
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
