<template>

    <el-form ref="form" :model="form" label-width="80px" >
      <el-form-item label="停车场">
        <el-select v-model="form.region" placeholder="请选择停车场">
          <el-option label="工技大松江停车场" value="P1"></el-option>
          <el-option label="东华松江停车场" value="P2"></el-option>
          <el-option label="交大闵行停车场" value="P3"></el-option>
          <el-option label="工技大长宁停车场" value="P4"></el-option>
          <el-option label="东华长宁停车场" value="P5"></el-option>
          <el-option label="交大徐汇停车场" value="P6"></el-option>
          <el-option label="上理杨浦停车场" value="P7"></el-option>
        </el-select>
      </el-form-item>
      <el-form-item label="预计停车时间">
        <el-col :span="100">
          <el-date-picker type="date" placeholder="选择日期" v-model="form.date1" style="width: 100%;"></el-date-picker>
        </el-col>
        <el-col class="line" :span="2">-</el-col>
        <el-col :span="100">
          <el-time-picker placeholder="选择时间" v-model="form.date2" style="width: 100%;"></el-time-picker>
        </el-col>
      </el-form-item>
      <el-form-item label="充电桩">
        <el-switch
            style="display: block"
            v-model="value2"
            active-color="#3f13ce"
            inactive-color="#13ceac"

            active-text="不需要充电"
            inactive-text="需要充电">
        </el-switch>
      </el-form-item>
      <el-form-item label="车型">
        <el-radio-group v-model="form.resource">
          <el-radio label="小轿车"></el-radio>
          <el-radio label="SUV"></el-radio>
          <el-radio label="面包车"></el-radio>
          <el-radio label="皮卡"></el-radio>
          <el-radio label="其他"></el-radio>
        </el-radio-group>
      </el-form-item>
      <el-form-item label="备注">
        <el-input type="textarea" placeholder="请输入其他您想要备注的信息" v-model="form.desc" style="width: 45%"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="order">预订</el-button>

      </el-form-item>
    </el-form>



</template>

<script>
export default {

  data() {
    return {

      form: {
        name: '',
        region: '',
        date1: '',
        date2: '',
        delivery: false,
        type: [],
        resource: '',
        desc: ''
      },

      value1: true,
      value2: true
    };
  },
  methods: {
    onSubmit() {
      console.log('submit!');
    },

    order() {
      this.showMessage("预订成功", "success");
      setTimeout(() => {
        this.showMessage("其他信息可进入联系我们查看具体停车场信息！", "info");
      }, 200);
    },

    showMessage(message, type) {
      this.$message[type](message);
    }
  }

};
</script>

<style scoped>

</style>