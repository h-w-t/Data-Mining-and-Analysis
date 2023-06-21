<template>
  <el-form ref="form" :model="form" label-width="70px">
    <el-form-item label="活动名称">
      <el-input placeholder="Gsh" v-model="form.name" :disabled="true"></el-input>
    </el-form-item>
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

    <el-form-item label="充电桩">
      <el-switch
          style="display: block"
          v-model="value2"
          active-color="#3f13ce"
          inactive-color="#13ceac"
          active-text="不需要充电"
          inactive-text="需要充电"
      ></el-switch>
    </el-form-item>
    <el-form-item label="开始停车时间">
      <el-col :span="100">
        <el-date-picker type="date" v-model="form.date1" :disabled="true" style="width: 100%;"></el-date-picker>
      </el-col>
      <el-col class="line" :span="2">-</el-col>
      <el-col :span="100">
        <el-time-picker v-model="form.date2" :disabled="true" style="width: 100%;"></el-time-picker>
      </el-col>
    </el-form-item>
    <el-form-item>
      <el-button type="primary" @click="order">停车</el-button>
    </el-form-item>
  </el-form>
</template>

<script>
export default {
  // eslint-disable-next-line vue/multi-word-component-names
  name: "Park",
  data() {
    return {
      value2: true,
      form: {
        name: '', // 活动名称
        region: '', // 停车场
        date1: '', // 开始停车日期
        date2: '', // 开始停车时间
        delivery: false,
        type: [],
        resource: '',
        desc: '',
      },
    };
  },
  mounted() {
    const currentDate = new Date();
    const hours = String(currentDate.getHours()).padStart(2, '0'); // 获取当前小时，不足两位数补零
    const minutes = String(currentDate.getMinutes()).padStart(2, '0'); // 获取当前分钟，不足两位数补零

    this.form.date1 = currentDate.toISOString().slice(0, 10); // 设置日期为当前日期，格式为 "YYYY-MM-DD"
    this.form.date2 = `${hours}:${minutes}`; // 设置时间为当前时间，格式为 "HH:MM"
  },

  methods: {
    order() {
      this.showMessage("停车成功", "success");
      setTimeout(() => {
        this.showMessage("请检查停车是否规范，以免发生剐蹭问题！", "info");
      }, 200);
    },

    showMessage(message, type) {
      this.$message[type](message);
    }
  },
};
</script>

<style scoped>

</style>
