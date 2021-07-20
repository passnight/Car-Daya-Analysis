


<template id="chinese_selling_map_template">
<!-- !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!此文件无用!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! -->
  <div id="chinese_selling_map" style="width: 500px; height: 500px"></div>
</template>
<script>
// 导入图表
import * as echarts from "echarts";
import axios from "axios";
import Vue from "vue";

Vue.component("sale-map",{
    template: "<div id='chinese_selling_map' style='width: 1000px; height: 450px'></div>"
});

export default {
  name: "sell-map",
  methods: {
    drawMap() {
      
      axios.get("../../static/json/ChinaMap.json").then((response) => {
        echarts.registerMap("china", response.data);
        this.mapChart = echarts.init(
          document.getElementById("chinese_selling_map")
        );
        let option = {
          title: {
            text: "车辆销售区域分布图",
            x: "center",
            textStyle: {
              color: "#9c0505",
            },
          },

          series: [
            {
              type: "map",
              map: "china",
              label: {
                show: this.showLabel,
                color: "black",
                fontSize: 10,
              },
              // 地图大小倍数
              zoom: 1.2,
              data: this.data,
            },
          ],
          visualMap: {
            min: 800,
            max: 50000,
            text: ["High", "Low"],
            realtime: false,
            calculable: true,
            inRange: {
              color: ["lightskyblue", "yellow", "orangered"],
            },
          },
        };
        this.mapChart.setOption(option);
      });
    },
  },
  data() {
    return {
      mapChart: null,
      showLabel: false,
      data: [
        { name: "北京省", value: 40000 },
        { name: "山西省", value: 30000 },
        { name: "内蒙古自治区", value: 5000 },
        { name: "青海省", value: 7000 },
        { name: "河北省", value: 25000 },
        { name: "广东省", value: 10000 },
        { name: "黑龙江省", value: 40000 },
        { name: "南海诸岛", value: 20000 },
        { name: "四川省", value: 20000 },
      ],
    };
  },
  mounted() {
      console.log("df");
    this.$nextTick(function () {
      this.drawMap();
    });
  },
};
</script>