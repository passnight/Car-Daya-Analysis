<template>
  <div id="app">
    <el-row>
      <el-col style="height: 60px">
        <el-header style="text-align: right; font-size: 12px">
          <el-dropdown>
            <i
              class="el-icon-setting"
              style="margin-right: 15px; color: #ffffff"
            ></i>
            <el-dropdown-menu slot="dropdown">
              <el-dropdown-item>修改密码</el-dropdown-item>
              <el-button @click="open">注销用户</el-button>
            </el-dropdown-menu>
          </el-dropdown>
          <span>
            <router-link to="sale" tag="el-button" id="router-sale"
              >Sale</router-link
            >
            <router-link to="login" tag="el-button" id="router-login"
              >Login</router-link
            >
            <router-link to="feedback" tag="el-button" id="router-feedback"
              >feedback</router-link
            >
            <router-link to="manager" tag="el-button" id="router-manager"
              >manager</router-link
            >

            王小虎
          </span>
        </el-header>
      </el-col>
    </el-row>
    <el-row>
      <el-button style="color = transprant" @click="isCollapse = !isCollapse"
        ><i class="el-icon-s-fold"></i
      ></el-button>
    </el-row>
    <el-container style="height: 500px; border: 1px solid #eee">
      <!-- <el-aside width="200px" style="background-color: #024195"> -->

      <el-menu
        :default-openeds="['1', '2']"
        :collapse="isCollapse"
        :collapse-transition="false"
      >
        <el-submenu index="1">
          <template slot="title">
            <i class="el-icon-message"></i>
            <span slot="title">填写销售分析信息</span>
          </template>
          <el-menu-item-group>
            <template slot="title">填写A汽车型号</template>
            <el-input placeholder="请输入汽车型号" v-model="input" clearable>
            </el-input>
          </el-menu-item-group>

          <el-menu-item-group>
            <template slot="title">填写B汽车型号</template>
            <el-input placeholder="请输入汽车型号" v-model="input" clearable>
            </el-input>
          </el-menu-item-group>

          <el-menu-item-group>
            <template slot="title">选择分析时间区间</template>

            <div class="block">
              <el-date-picker
                v-model="value2"
                type="datetimerange"
                :picker-options="pickerOptions"
                range-separator="至"
                start-placeholder="开始日期"
                end-placeholder="结束日期"
                align="right"
              >
              </el-date-picker>
            </div>
          </el-menu-item-group>
        </el-submenu>
        <el-submenu index="2">
          <template slot="title">
            <i class="el-icon-menu"></i>
            <span slot="title">功能选择</span>
          </template>
          <el-menu-item-group>
            <el-menu-item index="2-1">销售趋势分析</el-menu-item>
            <el-menu-item index="2-2">销量对比</el-menu-item>
            <el-menu-item index="2-3">价格对比</el-menu-item>
          </el-menu-item-group>
        </el-submenu>
      </el-menu>
      <!-- </el-aside> -->
      <el-container>
        <router-view> </router-view>
      </el-container>
    </el-container>
  </div>
</template>

<script>
export default {
  name: "Sale",
  data() {
    return {
      //收缩和弹出
      isCollapse: false,

      pickerOptions: {
        shortcuts: [
          {
            text: "最近一周",
            onClick(picker) {
              const end = new Date();
              const start = new Date();
              start.setTime(start.getTime() - 3600 * 1000 * 24 * 7);
              picker.$emit("pick", [start, end]);
            },
          },
          {
            text: "最近一个月",
            onClick(picker) {
              const end = new Date();
              const start = new Date();
              start.setTime(start.getTime() - 3600 * 1000 * 24 * 30);
              picker.$emit("pick", [start, end]);
            },
          },
          {
            text: "最近三个月",
            onClick(picker) {
              const end = new Date();
              const start = new Date();
              start.setTime(start.getTime() - 3600 * 1000 * 24 * 90);
              picker.$emit("pick", [start, end]);
            },
          },
        ],
      },
      value1: [new Date(2000, 10, 10, 10, 10), new Date(2000, 10, 11, 10, 10)],
      value2: "",
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
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
.el-header {
  background-color: #134194;
  color: #ffffff;
  line-height: 60px;
}

.el-aside {
  color: #333;
}
#app {
  margin: 0;
  padding: 0;
}
</style>
