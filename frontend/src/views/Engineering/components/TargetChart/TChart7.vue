<template>
  <div id="tchart7" style="width: 730px; height: 600px" ref="tc7"></div>
</template>

<script>
import cdw from "../../../../assets/theme/cdw.json";
import * as echarts from "echarts";
import axios from "axios";
export default {
  data() {
    return {
      tChart7: null
    };
  },
  name: "tchart7",
  methods: {
    myEcharts() {
      // 基于准备好的dom，初始化echarts实例
      let obj = cdw;
      echarts.registerTheme('cdw', obj)
      //var myChart = this.$echarts.init(document.getElementById('chart3'));
      // var myChart = echarts.init(this.$refs.tc7,'cdw');  使用主题
      var myChart = echarts.init(this.$refs.tc7);
      // 指定图表的配置项和数据
      var option = {
        title: {
          text: "指标分析",
          textStyle: {
            fontSize: 25,
            color: "#ffffff",
          },
        },
        tooltip: {},
        legend: {
          data: ["百分比"],
        },
        xAxis: {
          data: ["空间", "操控", "外观", "内饰", "舒适性", "性价比"],
          nameTextStyle: {
            color: "rgba(255, 255, 255, 1)",
          },
        },
        //   [66, 23, 52, 77, 37, 90],
        yAxis: {},
        series: [
          {
            name: "百分比",
            type: "bar",
            data: [],
            showBackground: true,
            backgroundStyle: {
              color: "rgba(180, 180, 180, 0.2)",
            },
            color: "#44fdc5",
          },
        ],
      };

      // 使用刚指定的配置项和数据显示图表。
      myChart.setOption(option);
      axios.post("http://127.0.0.1:5000/TChart7.json").then((response) => {
        this.tChart7 = response.data;
        myChart.setOption({  //动画的配置
                        series: [{
                        data: this.tChart7 //这里数据是一个数组的形似
                        }]
                    })
      });
    },
  },
  mounted() {
    this.myEcharts();
  },
};
</script>

<style>
</style>