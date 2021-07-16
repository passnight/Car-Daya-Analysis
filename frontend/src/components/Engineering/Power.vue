<template>
  <el-table
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
    <el-table-column prop="carType" label="最大功率(KW)" width="250"></el-table-column>
    <el-table-column prop="userComment" label="最大扭矩(N-m)" width="250"></el-table-column>
    <el-table-column prop="carType" label="最高车速(km/h)" width="250"></el-table-column>
    <el-table-column prop="carType" label="官方0-100km/h加速(s)" width="250"></el-table-column>
    <el-table-column prop="carType" label="最大马力(Ps)" width="250"></el-table-column>
  </el-table>
</template>

<script >
export default {
  name: "Brake",
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
</style>
