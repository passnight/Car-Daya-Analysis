<template>
  <el-row style="flex: none; display: flex; height: 60px">
    <div
      style="display: flex; align-items: center; margin-left: 10px; flex: none"
    ></div>
    <el-menu
      class="el-menu-demo"
      mode="horizontal"
      router
      default-active="/feedback"
      @select="handleSelect"
      background-color="transparent"
      text-color="#fff"
      active-text-color="#ffd04b"
      style="flex: auto; display: flex"
    >
      <el-menu-item index="/home" style="margin-left: 70px; margin-right: 10px"
        >主页</el-menu-item
      >
      <el-menu-item index="/feedback">用户反馈</el-menu-item>
      <el-menu-item index="/engineering" style="margin-left: auto"
        >指标分析</el-menu-item
      >
      <el-menu-item index="/sale" style="margin-right: 40px"
        >销售分析</el-menu-item
      >
    </el-menu>
    <div
      style="
        margin-left: auto;
        display: flex;
        align-items: center;
        margin-right: 10px;
        flex: none;
      "
    >
      <el-dropdown>
        <i
          class="el-icon-setting"
          style="margin-right: 10px; color: #ffffff"
        ></i>
        <el-dropdown-menu slot="dropdown">
          <el-button @click="changeData">修改密码</el-button>
          <el-button @click="destoryUser">注销用户</el-button>
        </el-dropdown-menu>
      </el-dropdown>

      <span style="color: white"> 王小虎 </span>
    </div>
  </el-row>
</template>

<script>
export default {
    methods: {
    //注销用户
    destoryUser() {
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
    handleSelect(key, keyPath) {
      console.log(key, keyPath);
    },
    //修改密码
    changeData() {
      this.$prompt("请输入新密码，为6~20位数字+字母", "提示", {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
        //密码格式为6~20位有字母和数字
        inputPattern: /^(?=.*[0-9])(?=.*[a-zA-Z])([a-zA-Z0-9]{6,20})$/,
        inputErrorMessage: "密码格式不正确",
      })
        .then(({ value }) => {
          this.$message({
            type: "success",
            message: "修改密码成功",
          });
        })
        .catch(() => {
          this.$message({
            type: "info",
            message: "取消修改密码",
          });
        });
    },
  },
};
</script>

<style>
</style>