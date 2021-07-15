<template id = "car-big-data-feedback-template">
  <div id="feedback">
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
          <span>王小虎</span>
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
            <span slot="title">填写分析信息</span>
          </template>
          <el-menu-item-group>
            <template slot="title">填写汽车型号</template>
            <el-input placeholder="请输入汽车型号" v-model="input" clearable>
            </el-input>
          </el-menu-item-group>
          <el-menu-item-group>
            <template slot="title">选择查看价位</template>

            <!--下拉框-->
            <el-select v-model="value" placeholder="请选择">
              <el-option
                v-for="item in options"
                :key="item.value"
                :label="item.label"
                :value="item.value"
              >
              </el-option>
            </el-select>
          </el-menu-item-group>
        </el-submenu>
        <el-submenu index="2">
          <template slot="title">
            <i class="el-icon-menu"></i>
            <span slot="title">功能选择</span>
          </template>
          <el-menu-item-group>
            <el-menu-item index="2-1">购车目的</el-menu-item>
            <el-menu-item index="2-2">用户评价</el-menu-item>
          </el-menu-item-group>
        </el-submenu>
        <el-submenu index="3">
          <template slot="title">
            <i class="el-icon-menu"></i>
            <span slot="title">系统设置</span>
          </template>
          <el-menu-item-group>
            <router-link to="/Login" tag="el-menu-item">登录界面</router-link>
          </el-menu-item-group>
        </el-submenu>
      </el-menu>
      <!-- </el-aside> -->
      <el-container>
        <router-view></router-view>
      </el-container>
    </el-container>
  </div>
</template>

<script>


export default {
  name: "Feedback",
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
