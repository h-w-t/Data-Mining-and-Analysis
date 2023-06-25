<template>
  <div>
    <div class="settings"  >
      <!--      <div class="settings" style="display: flex; justify-content: center;">-->
      <el-row>
        <el-col :span="12" class="centered-col">
          <el-card style="width: 80%; height: 40%;" class="box-card">
            <div slot="header" class="clearfix">
              <span>数据准备</span>
              <el-button  size="medium" type="primary" style="  float: right; padding: 3px 0" >分析数据</el-button>
            </div>
            <el-upload action="http://localhost:9090/classify/import" :show-file-list="true" accept="xlsx" style="display: inline-block">
              <el-button type="primary" class="ml-5">导入数据 <i class="el-icon-bottom"></i></el-button>
            </el-upload>
            <el-input
                placeholder="请输入树的高度"
                v-model="input1"
                clearable>
            </el-input>
            <el-input
                placeholder="请输入叶子节点参数"
                v-model="input2"
                clearable>
            </el-input>


          </el-card>
        </el-col>
        <el-col :span="12" class="centered-col">
          <el-card style="width: 80%; height: 40%;" class="box-card">
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
            <div>
            </div>
          </el-card>
        </el-col>
      </el-row>
    </div>


    <div class="settings"  >
      <el-row>
        <el-col :span="12" class="centered-col">
          <el-card style="width: 80%; height: 40%;" class="box-card">
            <div slot="header" class="clearfix">
              <span>原始数据表</span>
            </div>
<!--            <el-table-->
<!--                :data="tableData"-->
<!--                style="width: 100%">-->
<!--              <el-table-column-->
<!--                  type="index"-->
<!--                  :index="indexMethod">-->
<!--              </el-table-column>-->
<!--              <el-table-column-->
<!--                  prop="SepL"-->
<!--                  label="SepL"-->
<!--                  width="180">-->
<!--              </el-table-column>-->
<!--              <el-table-column-->
<!--                  prop="SepW"-->
<!--                  label="SepW"-->
<!--                  width="180">-->
<!--              </el-table-column>-->
<!--              <el-table-column-->
<!--                  prop="PetL"-->
<!--                  label="PetL"-->
<!--                  width="180">-->
<!--              </el-table-column>-->
<!--              <el-table-column-->
<!--                  prop="PetW"-->
<!--                  label="PetW"-->
<!--                  width="180">-->
<!--              </el-table-column>-->
<!--              <el-table-column-->
<!--                  prop="Species"-->
<!--                  label="Species"-->
<!--                  width="180">-->
<!--              </el-table-column>-->
<!--            </el-table>-->
            <el-table :data="tableData" style="width: 100%">
              <el-table-column prop="SepL" label="SepL" width="180"></el-table-column>
              <el-table-column prop="SepW" label="SepW" width="180"></el-table-column>
              <el-table-column prop="PetL" label="PetL" width="180"></el-table-column>
              <el-table-column prop="PetW" label="PetW" width="180"></el-table-column>
              <el-table-column prop="Species" label="Species" width="180"></el-table-column>
            </el-table>


          </el-card>
        </el-col>
      </el-row>
    </div>

  </div>
</template>

<script>

// import csvtojson from 'csvtojson';
import axios from "axios";


export default {


  // eslint-disable-next-line vue/multi-word-component-names
  name: "rules",
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
      // tableData: [{ SepL: '3.5', SepW: '5.1', PetL: '0.2', PetW: '1.4', Species: 'setosa' },
      //   { SepL: '3', SepW: '4.9', PetL: '0.2', PetW: '1.4', Species: 'setosa' },
      //   { SepL: '3.2', SepW: '4.7', PetL: '0.2', PetW: '1.3', Species: 'setosa' },
      //   { SepL: '3.1', SepW: '4.6', PetL: '0.2', PetW: '1.5', Species: 'setosa' },
      //   { SepL: '3.6', SepW: '5', PetL: '0.2', PetW: '1.4', Species: 'setosa' },
      //   { SepL: '3.9', SepW: '5.4', PetL: '0.4', PetW: '1.7', Species: 'setosa' },
      //   { SepL: '3.4', SepW: '4.6', PetL: '0.3', PetW: '1.4', Species: 'setosa' },
      //   { SepL: '3.4', SepW: '5', PetL: '0.2', PetW: '1.5', Species: 'setosa' },
      //   { SepL: '2.9', SepW: '4.4', PetL: '0.2', PetW: '1.4', Species: 'setosa' },
      //   { SepL: '3.1', SepW: '4.9', PetL: '0.1', PetW: '1.5', Species: 'setosa' },
      // ],
      fileList:[],
    };
  },

  mounted() {
    this.fetchDataFromBackend();
  },
  methods: {
    fetchDataFromBackend() {
      axios.get('http://localhost:8000/apis/classify/all/')
          .then(response => {
            const responseData = response.data.data;
            // 将后端传来的数据转换为表格组件需要的格式
            const tableData = responseData.map(item => {
              return {
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
