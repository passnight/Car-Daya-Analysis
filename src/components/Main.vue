<template id = "car-big-data-main-template">

</template>

<script>
import Vue from 'vue'
Vue.component("car-big-data-main", {
  template: "#car-big-data-main-template"
});

export default {
  name: "Main",
  data() {
    return {
      //收缩和弹出
      isCollapse: false,

      //输出信息
      input: "",

      //下拉框信息
      options: [
        {
          value: "选项1",
          label: "1万以下",
        },
        {
          value: "选项2",
          label: "1万到5万",
        },
        {
          value: "选项3",
          label: "5万到10万",
        },
        {
          value: "选项4",
          label: "10万到20万",
        },
        {
          value: "选项5",
          label: "20万到50万",
        },
        {
          value: "选项6",
          label: "50万到100万",
        },
        {
          value: "选项7",
          label: "100万以上",
        },
      ],
      value: "",
    };
  },

  methods: {
    //注销用户
    open() {
      this.$confirm("此操作将永久删除该用户, 是否继续?", "提示", {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
        type: "warning",
      })
        .then(() => {
          this.$message({
            type: "success",
            message: "删除成功!",
          });
        })
        .catch(() => {
          this.$message({
            type: "info",
            message: "已取消删除",
          });
        });
    },
  },
};
</script>

<style>
.el-header {
  background-color: #134194;
  color: #ffffff;
  line-height: 60px;
}

.el-aside {
  color: #333;
}
</style>
