<template>
  <div>
        <div id="main" style="width: 100%; height: 90vh; "></div>
  </div>

</template>

<script>

import * as echarts from 'echarts';

export default {
  name: "Echart_user",
  data(){
    return{

    }
  },
  // mounted(){
  //   var option = {
  //     title: {
  //       text: '各季度会员数量统计',
  //       subtext: '趋势图',
  //       left: 'center'
  //     },
  //     tooltip:{
  //       trigger:'item'
  //     },
  //     xAxis: {
  //       type: 'category',
  //       data: ["第一季度", "第二季度", "第三季度", "第四季度"]
  //     },
  //     yAxis: {
  //       type: 'value',
  //
  //     },
  //     series: [
  //       {
  //         data:[2,11,5,55],
  //         type: 'line'
  //       },
  //       {
  //         data:[2,11,5,55],
  //         type: 'bar',
  //
  //       }
  //     ]
  //   };
  //
  //   var chartDom = document.getElementById('main');
  //   var myChart = echarts.init(chartDom);
  //
  //   this.request.get("/Echart_user/members").then(res => {
  //     // 填空
  //     // option.xAxis.data = res.data.x
  //     option.series[0].data = res.data
  //     option.series[1].data = res.data
  //     // 数据准备完毕之后再set
  //     myChart.setOption(option);
  //
  //   })
  //
  //
  // }
  mounted(){

    var chartDom = document.getElementById('main');
    var myChart = echarts.init(chartDom);
    var option = {
      title: {
        text: '各季度会员数量统计',
        subtext: '趋势图',
        left: 'center'
      },
      tooltip:{
        trigger:'item'
      },
      xAxis: {
        type: 'category',
        data: ["第一季度", "第二季度", "第三季度", "第四季度"],
        axisLabel: {
          formatter: function (value, index) {

            var names = ["第一季度", "第二季度", "第三季度", "第四季度"];
            return names[index];
          }
        }

      },
      yAxis: {
        type: 'value'
      },
      series: [
        {
          data: [2,11,5,55],
          type: 'line',
          itemStyle: {
            color: '#a94545'  // 设置折线图的颜色为红色
          }
        },
        {
          data: [2,11,5,55],
          type: 'bar',
          itemStyle: {
            color: '#5f8cb9'  // 设置柱状图的颜色为蓝色
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