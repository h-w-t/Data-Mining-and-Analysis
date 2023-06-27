<template>
  <div>
    <el-row style=" margin-bottom: 20px;width: 100%; height: 30%; display: flex; justify-content: center; align-items: center;">
      <el-card style="width: 40%; height: 40%;">
        <div slot="header" class="clearfix">
          <span>数据准备</span>
          <el-button size="medium" type="primary" class="ml-5" style="  float: right; padding: 3px 0" @click="analyzeData" >分析数据<i class="el-icon-bottom"></i></el-button>
          <el-button size="medium" type="primary" class="ml-5" style="  float: right; padding: 3px 0" @click="loadTable" >载入数据<i class="el-icon-bottom"></i></el-button>
          <el-button size="medium" type="primary" class="ml-5" style="  float: right; padding: 3px 0" @click="cleananalyze" >清除分析<i class="el-icon-bottom"></i></el-button>
        </div>
        <el-upload action="http://localhost:9090/classify/import" :show-file-list="true" accept="xlsx" style="display: inline-block; margin-bottom: 10px;">
          <el-button type="primary" class="ml-5">导入数据 <i class="el-icon-bottom"></i></el-button>
        </el-upload>
        <el-input
            placeholder="请输入树的高度"
            v-model="input1"
            clearable
            style="margin-bottom: 10px;">
        </el-input>
        <el-input
            placeholder="请输入叶子节点参数"
            v-model="input2"
            clearable
            style="margin-bottom: 10px;">
        </el-input>
      </el-card>
    </el-row>

    <el-row style=" margin-bottom: 20px;width: 100%; height: 30%; display: flex; justify-content: center; align-items: center;">
    <el-card v-if="showTable" style="width: 70%; height: 40%; margin: 0 auto;" class="box-card">
      <div slot="header" class="clearfix">
        <span>原始数据表</span>
      </div>
      <el-table :data="tableData" height="250" border style="width: 100%">
        <el-table-column prop="id" label="ID"></el-table-column>
        <el-table-column prop="SepL" label="花萼长度"></el-table-column>
        <el-table-column prop="SepW" label="花萼宽度"></el-table-column>
        <el-table-column prop="PetL" label="花瓣长度"></el-table-column>
        <el-table-column prop="PetW" label="花瓣宽度"></el-table-column>
        <el-table-column prop="Species" label="种类"></el-table-column>
      </el-table>
    </el-card>
    </el-row>


    <el-row style=" margin-bottom: 20px;width: 100%; height: 30%; display: flex; justify-content: center; align-items: center;">
      <el-card v-if="showResult" style="width: 70%; height: 40%;" class="box-card">
        <div slot="header" class="clearfix">
          <span>决策树</span>
        </div>
        <div class="demo-image__preview">
          <el-image
              style="width: 100px; height: 100px"
              :src="url"
              :preview-src-list="srcList">
          </el-image>
        </div>
      </el-card>

    </el-row>

    </div>

</template>

<script>

// import csvtojson from 'csvtojson';
import axios from "axios";


export default {


  // eslint-disable-next-line vue/multi-word-component-names
  name: "classify",
  data() {
    return {
      tableData:[],
        url: 'https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg',
        srcList: [
          'https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg',
          'src/assets/tree.png'
        ],
      input1: '',//树的高度
      input2: '',//叶子节点数
      fileList:[],
      showTable:false,
      showResult:false,

    };
  },

  mounted() {
    this.fetchDataFromBackend();
  },
  methods: {
    loadTable(){
      this.showTable=true;
    },
    cleananalyze(){
      this.showTable=false;
      this.showResult=false
    },
    analyzeData() {
      //this.showTable=true;
      this.showResult=true;
      // 获取输入框的值
      const input1Value = this.input1;
      const input2Value = this.input2;

      // 构造要发送给后端的数据对象
      const data = {
        input1: input1Value,
        input2: input2Value
      };
      const url = `http://localhost:8000/apis/iris/classify/${input1Value}&${input2Value}/`;

      // 发送数据到后端
      axios.post(url, data)
          .then(response => {
            // 处理成功响应
            console.log(response.data);
            this.showTable=true;
          })
          .catch(error => {
            // 处理错误响应
            console.error(error);
          });
    },
    fetchDataFromBackend() {
      axios.get('http://localhost:8000/apis/classify/all/')
          .then(response => {
            const responseData = response.data.data;
            // 将后端传来的数据转换为表格组件需要的格式
            const tableData = responseData.map(item => {
              return {
                id:item.id,
                SepL: item.SpeL,
                SepW: item.SpeW,
                PetL: item.PetL,
                PetW: item.PetW,
                Species: item.Species
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
