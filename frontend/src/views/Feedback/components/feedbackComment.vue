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
    <el-table-column prop="carType" label="汽车型号" width="250">
    </el-table-column>
    <el-table-column prop="userComment" label="用户评价"> </el-table-column>
  </el-table>
</template>

<script >
import axios from "axios";

export default {
  name: "FeedbackComment",
  data() {
    const item = {
      carType: "兰博基尼",
      userComment: "不错，挺好",
    };
    return {
      clientWidth: document.documentElement.clientWidth,
      clientHeight: document.documentElement.clientHeight,
      tableData: [],
      document,
      priceLevel: "无限制",
      priceLevel: "无限制",
      chooseModel: "无限制",
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
    axios
      .get("http://127.0.0.1:5000/Feedback/Comment.json")
      .then((response) => {
        this.tableData = response.data;
      });
  },
};
</script>

<style scoped>
</style>