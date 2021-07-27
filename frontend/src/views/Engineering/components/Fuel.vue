<template>
<div>
  <!-- <el-table
    :data="tableData"
    size="medium"
    :cell-style="cellStyle"
    :header-cell-style="{
      color: '#fff',
      background: 'rgba(78, 131, 211, 0.8)',
    }"
    stripe
    :height="clientHeight - 62 < 370 ? 370 : clientHeight - 62"
  >
    <el-table-column prop="carType" label="能源类型" width="250"></el-table-column>
    <el-table-column prop="userComment" label="NEDC综合油耗(L/100km)" width="250"></el-table-column>
    <el-table-column prop="carType" label="实测油耗(L/100km)" width="250"></el-table-column>
  </el-table> -->
  <div class="fchart">
    <div class="f1">
      <f-chart-1 class="fchart1"/>
    </div>
    <div class="f2">
      <f-chart-2 class="fchart2"/>
    </div>
  </div>
</div>
</template>

<script > 
import FChart1 from './FuelChart/FChart1'
import FChart2 from './FuelChart/FChart2'
export default {
  name: "Fuel",
  components: {
    FChart1,
    FChart2
  },
  data() {
    const item = {
      carType: "兰博基尼",
      userComment: "不错，挺好",
    };
    return {
      clientWidth: document.documentElement.clientWidth,
      clientHeight: document.documentElement.clientHeight,
      tableData: Array(20).fill(item),
      document,
    };
  },
  methods: {
    cellStyle({ row, column, rowIndex, columnIndex }) {
      if (rowIndex % 2 == 1) {
        return "background:rgba(160,188,231,0.3)";
      }
    },
  },
  mounted() {
    window.onresize = () => {
      this.clientHeight = document.body.clientHeight;
      this.clientWidth = document.body.clientWidth;
    };
  },
};
</script>

<style scoped>
.f1{
	float: left;
	width: 650px;
}
.f2{
	float: left;
	width: 650px;
}
</style>