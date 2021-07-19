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
    <el-table-column prop="carType" label="汽车型号" width="150">
    </el-table-column>
    <el-table-column prop="price" label="汽车价位" width="150">
    </el-table-column>
    <el-table-column prop="purchaseTarget" label="购车目的"> </el-table-column>
  </el-table>
</template>

<script >
export default {
  data() {
    const item = {
      carType: "兰博基尼",
      price: "100万以上",
      purchaseTarget: "装杯啊",
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