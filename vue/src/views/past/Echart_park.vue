<template>
  <div>
        <div id="main" style="width: 100%; height: 90vh; "></div>

  </div>

</template>

<script>

import * as echarts from 'echarts';

export default {
  name: "Echart_park",
  data(){
    return{

    }
  },
  mounted(){

    var chartDom = document.getElementById('main');
    var myChart = echarts.init(chartDom);
    var option = {
      title: {
        text: '各停车场停车位数量统计',
        subtext: '趋势图',
        left: 'center'
      },
      tooltip:{
        trigger:'item'
      },
      xAxis: {
        // type: 'category',
        // data: ["工技大松江停车场", "东华松江停车场", "交大闵行停车场", "工技大长宁停车场","东华长宁停车场","交大徐汇停车场","上理杨浦停车场"]
        type: 'category',
        data: ["工技大松江停车场", "东华松江停车场", "交大闵行停车场", "工技大长宁停车场","东华长宁停车场","交大徐汇停车场","上理杨浦停车场"],
        // data: ["P1", "P2", "P3", "P4", "P5", "P6", "P7"], // 使用简化的标签
        axisLabel: {
          formatter: function (value, index) {
            // 使用完整的停车场名称作为标签
            var names = ["P1", "P2", "P3", "P4", "P5", "P6", "P7"];
            return names[index];
          }
        }

      },
      yAxis: {
        type: 'value'
      },
      series: [
        {
          data: [500, 700, 900, 200, 700, 750, 700],
          type: 'line',
          itemStyle: {
            color: '#5f8cb9'  // 设置折线图的颜色为红色
          }
        },
        {
          data: [500, 700, 900, 200, 700, 750, 700],
          type: 'bar',
          itemStyle: {
            color: '#8bd2ac'  // 设置柱状图的颜色为蓝色
          }
        }
      ]
    };
    myChart.setOption(option);







  }


}
</script>


<style>

</style>