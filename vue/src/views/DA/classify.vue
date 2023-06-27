<template>
  <div>
    <el-row style=" margin-bottom: 20px;width: 100%; height: 30%; display: flex; justify-content: center; align-items: center;">
      <el-card style="width: 40%; height: 40%;">
        <div slot="header" class="clearfix">
          <span>数据准备</span>
        </div>

        <el-row style="margin-bottom: 20px; display: flex; justify-content: center; align-items: center;">
          <el-button type="primary" class="ml-5"  @click="loadTable" round >载入数据<i class="el-icon-bottom"></i></el-button>
          <el-upload action="http://localhost:9090/classify/import" :show-file-list="true" accept="xlsx" style="display: inline-block;">
            <el-button round type="primary"  class="ml-5">导入数据文件<i class="el-icon-bottom"></i></el-button>
          </el-upload>
        </el-row>

        <el-row style="margin-bottom: 20px; display: flex; justify-content: center; align-items: center;">
          <el-link :underline="false">树的高度:  <el-input-number  v-model="input1" :precision="0" :step="1" :min="1" :max="10"></el-input-number></el-link>
        </el-row>
        <el-row style="margin-bottom: 20px; display: flex; justify-content: center; align-items: center;">
          <el-link :underline="false">叶子节点:  <el-input-number  v-model="input2" :precision="0" :step="1" :min="1" :max="10"></el-input-number></el-link>
        </el-row>


        <el-row style="margin-bottom: 20px; display: flex; justify-content: center; align-items: center;">
          <el-button type="info" class="ml-5" style=" margin-bottom: 20px;justify-content: center; align-items: center;" @click="cleananalyze" round>清除分析<i class="el-icon-bottom"></i></el-button>
          <el-button type="warning" class="ml-5" style=" margin-bottom: 20px;justify-content: center; align-items: center;" @click="analyzeData" round >分析数据<i class="el-icon-bottom"></i></el-button>
        </el-row>

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
          <el-image style="width: 100px; height: 100px" :src="url" :preview-src-list="srcList"></el-image>
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
      url: '',
      srcList: [],
      input1: '',//树的高度
      input2: '',//叶子节点数
      fileList:[],
      showTable:false,
      showResult:false,

    };
  },

  mounted() {
    //this.fetchDataFromBackend();
  },
  methods: {
    loadTable(){
      this.fetchDataFromBackend();
      this.showTable=true;
    },
    cleananalyze(){
      this.input1=''
      this.input2=''
      this.showTable=false;
      this.showResult=false
    },
    analyzeData() {
      // 获取输入框的值
      const input1Value = this.input1;
      const input2Value = this.input2;
      // 构造要发送给后端的数据对象

      const url = `http://localhost:8000/apis/classify/${input1Value}&${input2Value}/`;
      // 发送数据到后端
      axios.post(url)
          .then(response => {
            // 处理成功响应
            console.log(response.data);
            this.url = response.data.data
            this.srcList = [response.data.data];
            this.showResult=true;


          })
          .catch(error => {
            // 处理错误响应
            console.error('Failed to fetch image data:', error);
          });
      // this.fetchImageData();
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
    async fetchImageData() {
      try {
        // 获取输入框的值
        const input1Value = this.input1;
        const input2Value = this.input2;
        // 构造要发送给后端的数据对象
        const url_img = `http://localhost:8000/apis/classify/${input1Value}&${input2Value}/`;
        const response = await fetch(url_img);
        const data = await response.json();

        // 将后端返回的 base64 编码设置为图片的 URL
        this.url = data.base64;
        this.srcList = [data.base64];
      } catch (error) {
        console.error('Failed to fetch image data:', error);
      }
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
