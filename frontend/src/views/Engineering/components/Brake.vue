<template>
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
    <el-table-column prop="carType" label="实测100-0km/h制动(m)" width="250"></el-table-column>
    <el-table-column prop="userComment" label="前制动器类型" width="250"></el-table-column>
    <el-table-column prop="carType" label="后制动器类型" width="250"></el-table-column>
    <el-table-column prop="carType" label="驻车制动类型" width="250"></el-table-column>
  </el-table> -->
  <div class="bchart">
    <div class="b1">
      <b-chart-1 class="bchart1"/>
    </div>
    <div class="b2">
      <b-chart-2 class="bchart2"/>
    </div>
  </div>
</template>

<script >
import BChart1 from './BrakeChart/BChart1'
import BChart2 from './BrakeChart/BChart2'
export default {
  name: "Brake",
  components: {
    BChart1,
    BChart2
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
.b1{
	float: left;
	width: 650px;
}
.b2{
	float: left;
	width: 650px;
}
</style>