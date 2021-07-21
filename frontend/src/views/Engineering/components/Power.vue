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
    <el-table-column prop="carType" label="最大功率(KW)" width="120"></el-table-column>
    <el-table-column prop="userComment" label="最大扭矩(N-m)" width="150"></el-table-column>
    <el-table-column prop="carType" label="最高车速(km/h)" width="150"></el-table-column>
    <el-table-column prop="carType" label="官方0-100km/h加速(s)" width="200"></el-table-column>
    <el-table-column prop="carType" label="最大马力(Ps)" width="120"></el-table-column>
  </el-table> -->
  <div class="pchart">
    <div class="p1">
      <p-chart-1 class="pchart1"/>
    </div>
    <div class="p2">
      <p-chart-2 class="pchart2"/>
    </div>
  </div>
</div>
</template>

<script >
import PChart1 from './PowerChart/PChart1'
import PChart2 from './PowerChart/PChart2'
export default {
  name: "Brake",
  components: {
    PChart1,
    PChart2
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
.p1{
	float: left;
	width: 650px;
}
.p2{
	float: left;
	width: 650px;
}
</style>
