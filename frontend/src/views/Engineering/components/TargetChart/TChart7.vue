<template>
  <div id="tchart7" style="width: 600px; height: 400px" ref="tc7"></div>
</template>

<script>
import * as echarts from "echarts";
import axios from "axios";
export default {
  data() {
    return {
      tChart7: [1,2,3]
    };
  },
  name: "tchart7",
  methods: {
    async getCarSellingData () {
      await axios.post("http://127.0.0.1:5000/TChart7.json").then((response) => {
      console.log("origin:", this.tChart7);
      this.tChart7 = response.data;
      console.log("after:", this.tChart7);
    });
    },
    myEcharts() {
      // 基于准备好的dom，初始化echarts实例
      //var myChart = this.$echarts.init(document.getElementById('chart3'));
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
            data: this.tChart7,
            showBackground: true,
            backgroundStyle: {
              color: "rgba(180, 180, 180, 0.2)",
            },
            color: "#44fdc5",
          },
        ],
      };

      // 使用刚指定的配置项和数据显示图表。
      console.log("before draw:", this.tChart7);
      myChart.setOption(option);
      console.log("after draw", this.tChart7);
    },
  },
  mounted() {
    this.myEcharts();
  },
};
</script>

<style>
</style>