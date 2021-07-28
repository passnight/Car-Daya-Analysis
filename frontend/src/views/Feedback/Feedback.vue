<template id = "car-big-data-feedback-template">
  <div id="feedback" style="display: flex; flex-direction: column">
    <el-row style="flex: none; display: flex; height: 60px">
      <div
        style="
          display: flex;
          align-items: center;
          margin-left: 10px;
          flex: none;
        "
      >
        <el-button stytle="color = #719cdc" @click="isCollapse = !isCollapse">
          <i class="el-icon-s-fold"></i>
        </el-button>
      </div>
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

        <span style="color: white"> {{ userName }} </span>
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
          <el-menu-item-group>
            <template slot="title">选择查看价位</template>

            <!--下拉框-->
            <el-select
              v-model="priceLevel"
              placeholder="请选择"
              @change="sendParameter"
            >
              <el-option
                v-for="item in this.options"
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
            <router-link to="/feedback/feedbackTarget" tag="el-menu-item"
              >购车目的</router-link
            >
            <router-link to="/feedback/feedbackComment" tag="el-menu-item"
              >用户评价</router-link
            >
          </el-menu-item-group>
        </el-submenu>
      </el-menu>
      <!-- </el-aside> -->
      <el-container style="flex: auto">
        <router-view></router-view>
      </el-container>
    </el-container>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Feedback",

  mounted() {
    this.chooseModel = "无限制";
    this.priceLevel = "无限制";
    axios.get("http://127.0.0.1:5000/UserName").then((response) => {
      this.userName = response.data;
      console.log("user anme:" + this.userName);
    });
    axios
      .get("http://127.0.0.1:5000/Feedback/CarModel.json")
      .then((response) => {
        this.carModels = response.data;
      });
    axios.get("http://127.0.0.1:5000/Feedback/price.json").then((response) => {
      this.options = response.data;
    });
  },

  data() {
    return {
      //收缩和弹出
      isCollapse: false,

      activeIndex: "1",

      //输出信息
      input: "",
      userName: "1111",
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
      ],
      //汽车型号
      carModels: [],
      priceLevel: "无限制",
      chooseModel: "无限制",
    };
  },

  methods: {
    sendParameter() {
      let dataForm = new FormData();
      dataForm.append("priceLevel", this.priceLevel);
      dataForm.append("chooseModel", this.chooseModel);
      axios
        .post("http://127.0.0.1:5000/Feedback/SendParameter", dataForm)
        .then((response) => {
          this.tableData = response.data;
        });
    }, //修改密码
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
    handleSelect(key, keyPath) {
      console.log(key, keyPath);
    },
  },
};
</script>

<style>
.el-header {
  background-color: transparent;
  color: #ffffff;
  line-height: 60px;
}

html,
body {
  margin: 0;
  height: 100%;
  width: 100%;
}

.el-aside {
  color: #333;
}

#feedback {
  background: url("./resource/b01.png") no-repeat;
  background-position: center;
  height: 100%;
  width: 100%;
  background-size: cover;
  background-position: top;
}

.el-menu.el-menu--horizontal {
  border-bottom: none;
}
</style>
