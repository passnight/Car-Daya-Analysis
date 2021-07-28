<template>
  <div id="Sale" style="display: flex; flex-direction: column">
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
        default-active="/sale"
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

        <span style="color: white"> 王小虎 </span>
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
            <span slot="title">填写销售分析信息</span>
          </template>
          <el-menu-item-group>
            <el-select v-model="chooseModel1" placeholder="请选择" @change="sendParameter">
              <el-option
                v-for="item in this.carModels1"
                :key="item.model"
                :label="item.model"
                :value="item.model"
              >
              </el-option>
            </el-select>
          </el-menu-item-group>

          <el-menu-item-group>
            <el-select v-model="chooseModel2" placeholder="请选择" @change="sendParameter">
              <el-option
                v-for="item in this.carModels2"
                :key="item.model"
                :label="item.model"
                :value="item.model"
              >
              </el-option>
            </el-select>
          </el-menu-item-group>

          <el-menu-item-group>
            <template slot="title">选择分析时间区间</template>

            <div class="block">
    <!-- value-format 非绑定更改格式 -->
    <!-- format 绑定更改格式 直接显示到前端 -->
    <el-date-picker
      v-model="value1"
      type="monthrange"
      align="right"
      value-format="yyyy-MM-dd HH:mm:ss"   
      unlink-panels
      range-separator="至"
      start-placeholder="开始月份"
      end-placeholder="结束月份"
      :picker-options="pickerOptions" @change="sendParameter">
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
            <router-link to="/Sale/SaleTime" tag="el-menu-item"
              >销售趋势分析</router-link
            >
            <router-link to="/Sale/SaleNumber" tag="el-menu-item"
              >销量对比</router-link
            >
             <router-link to="/Sale/SalePrice" tag="el-menu-item"
              >价格对比</router-link
            >
             
          </el-menu-item-group>
        </el-submenu>
      </el-menu>
      <!-- </el-aside> -->
      <el-container>
        <router-view> 

        </router-view>
      </el-container>
    </el-container>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "Sale",
  mounted() {
    this.chooseModel1 = "";
    this.chooseModel2 = "";
    axios.get("http://127.0.0.1:5000/Sale/CarModel1.json").then((response) => {
      this.carModels1 = response.data;
    });
    axios.get("http://127.0.0.1:5000/Sale/CarModel2.json").then((response) => {
      this.carModels2 = response.data;
    });
  },
  data() {
   

     return {
       //输出信息
      input: "",
        isCollapse: false,
        pickerOptions: {
          shortcuts: [{
            text: '本月',
            onClick(picker) {
              picker.$emit('pick', [new Date(), new Date()]);
            }
          }, {
            text: '今年至今',
            onClick(picker) {
              const end = new Date();
              const start = new Date(new Date().getFullYear(), 0);
              picker.$emit('pick', [start, end]);
            }
          }, {
            text: '最近六个月',
            onClick(picker) {
              const end = new Date();
              const start = new Date();
              start.setMonth(start.getMonth() - 6);
              picker.$emit('pick', [start, end]);
            }
          }]
        },
        value1: '2015-01-01 00:00:00, 2015-01-01 00:00:00',

        carModels1:[

        ],
        carModels2:[

        ],
        chooseModel1: "",
        chooseModel2: "",
     }
  },

  methods: {
     handleSelect(key, keyPath) {
      console.log(key, keyPath);
    },
    //注销用户
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
    }, destoryUser() {
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
  
    sendParameter() {
    let dataForm = new FormData();
    dataForm.append("chooseModel1", this.chooseModel1);
    dataForm.append("chooseModel2", this.chooseModel2);
    dataForm.append("time", this.value1)
    axios
      .post("http://127.0.0.1:5000/Sale/SendParameter.json", dataForm)
      .then((response) => {
        this.tableData = response.data;
      });
    },

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
/* #Sale {
  
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
} */
#Sale {
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
  padding: 0;;
  height: 100%;
  width: 100%;
}



/* .el-menu.el-menu--horizontal {
  border-bottom: none;
} */
.el-header {
  background-color: transparent;
  color: #ffffff;
  line-height: 60px;
}
.el-aside {
  color: #333;
}

</style>
