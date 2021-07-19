<template>
  <div id="柱状图" style="width: 100%; height: 500px"></div>
</template>


<script>
import * as echarts from "echarts";
import axios from "axios";
export default {
  data() {
    return {
      chartColumn: null,
      carSaleData: null,
    };
  },
  mounted() {
    axios.get("http://localhost:8080/static/data/carSaleNumber.json").then((response) => {
      this.carSaleData = response.data.options;
    });
    this.drawLine();
  },
  methods: {
    drawLine() {
      this.chartDom = echarts.init(document.getElementById("柱状图"));

      this.chartDom.setOption(this.carSaleData);
    },
  },
};
</script>