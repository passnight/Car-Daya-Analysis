<template>
  <div id="engineering" style="display: flex; flex-direction: column">
    <el-row style="flex: none; display: flex; height: 60px">
      <div style="display: flex; align-items: center; margin-left: 10px">
        <el-button stytle="color = #ffffff" @click="isCollapse = !isCollapse">
          <i class="el-icon-s-fold"></i>
        </el-button>
      </div>
      <el-menu
        class="el-menu-demo"
        mode="horizontal"
        router
        default-active="/engineering"
        @select="handleSelect"
        background-color="transparent"
        text-color="#fff"
        active-text-color="#ffd04b"
        style="flex: auto; display: flex"
      >
        <el-menu-item
          index="/home"
          style="margin-left: 70px; margin-right: 10px"
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
        "
      >
        <el-dropdown>
          <i
            class="el-icon-setting"
            style="margin-right: 10px; color: #ffffff"
          ></i>
          <el-dropdown-menu slot="dropdown">
            <el-button @click="changePassword">修改密码</el-button>
            <el-button @click="destroyUser">注销用户</el-button>
          </el-dropdown-menu>
        </el-dropdown>
        <span style="color: white">{{ userName }} </span>
      </div>
    </el-row>
    <el-container style="border: 1px solid #eee; display: flex; flex: auto">
      <!-- <el-aside width="200px" style="background-color: #024195"> -->
      <el-menu
        style="flex: none"
        :default-openeds="['1', '2']"
        :collapse="isCollapse"
        :collapse-transition="false"
        background-color="rgba(35,81,162,0.5)"
        text-color="#fff"
        active-text-color="white"
      >
        <el-submenu index="1">
          <template slot="title">
            <i class="el-icon-message"></i>
            <span slot="title">填写分析信息</span>
          </template>
          <el-menu-item-group>
            <template slot="title">请选择型号</template>

            <!--型号绑定-->
            <el-select
              v-model="chooseModel"
              placeholder="请选择"
              @change="sendParameter"
            >
              <el-option
                v-for="item in this.carModels"
                :key="item.model"
                :label="item.model"
                :value="item.model"
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
            <router-link to="/Engineering/Fuel" tag="el-menu-item"
              >油耗分析</router-link
            >
            <router-link to="/Engineering/power" tag="el-menu-item"
              >动力分析</router-link
            >
            <router-link to="/Engineering/Brake" tag="el-menu-item"
              >制动分析</router-link
            >
            <router-link to="/Engineering/Target" tag="el-menu-item"
              >指标分析</router-link
            >
          </el-menu-item-group>
        </el-submenu>
      </el-menu>
      <!-- </el-aside> -->
      <div id="Content">
        <el-container style="flex: auto">
          <router-view></router-view>
        </el-container>
      </div>
    </el-container>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "Engineering",
  mounted() {
    this.chooseModel = "";
    axios
      .get("http://127.0.0.1:5000/Engineering/CarModel.json")
      .then((response) => {
        this.carModels = response.data;
      });
    axios.get("http://127.0.0.1:5000/UserName").then((response) => {
      this.userName = response.data;
      console.log("user anme:" + this.userName);
    });
  },
  data() {
    const item = {
      date: "2016-05-02",
      name: "王小虎",
      address: "上海市普陀区金沙江路 1518 弄",
    };
    return {
      userName: "1111",
      //收缩和弹出
      isCollapse: false,

      tableData: Array(20).fill(item),

      //输出信息
      input: "",

      //汽车型号
      carModels: [],
      chooseModel: "",
    };
  },
  methods: {
    cellStyle({ row, column, rowIndex, columnIndex }) {
      if (rowIndex % 2 == 1) {
        return "background:rgba(160,188,231,0.3)";
      }
    },
    sendParameter() {
      let dataForm = new FormData();
      dataForm.append("chooseModel", this.chooseModel);
      axios
        .post("http://127.0.0.1:5000/Engineering/SendParameter.json", dataForm)
        .then((response) => {
          this.tableData = response.data;
        });
    },
    changePassword() {
      let pwd = this.$prompt("请输入新密码，为6~20位数字+字母", "提示", {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
        //密码格式为6~20位有字母和数字
        inputPattern: /^(?=.*[0-9])(?=.*[a-zA-Z])([a-zA-Z0-9]{6,20})$/,
        inputErrorMessage: "密码格式不正确",
      })
        .then(({ value }) => {
          console.log(value);
          let data = new FormData();
          data.append("username", this.userName);
          data.append("password", value);
          console.log(data);
          axios
            .post("http://127.0.0.1:5000/Manager/ChangeUserInfo", data)
            .then((response) => {});
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
    //注销用户
    destroyUser() {
      this.$confirm("此操作将永久删除该用户, 是否继续?", "提示", {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
        type: "warning",
      })
        .then(() => {
          let data = new FormData();
          data.append("username", this.userName);
          console.log(data);
          axios
            .post("http://127.0.0.1:5000/Manager/DeleteUser", data)
            .then((response) => {});
          this.$message({
            type: "success",
            message: "删除成功!",
          });
          this.$router.push("/");
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
#engineering {
  background: url("../../assets/img/home-background.png") no-repeat;
  background-position: center;
  height: 100%;
  width: 100%;
  background-size: cover;
  background-position: top;
}
html,
body {
  margin: 0;
  height: 100%;
  width: 100%;
}

.el-header {
  background-color: transparent;
  color: #ffffff;
  line-height: 60px;
}

.el-aside {
  color: #333;
}
</style>
