<template id = "car-big-data-home">
  <div id="home" style="display: flex; flex-direction: column">
    <el-row style="flex: none; display: flex; height: 60px">
      <div
        style="
          display: flex;
          align-items: center;
          margin-left: 10px;
          flex: none;
        "
      ></div>
      <el-menu
        class="el-menu-demo"
        mode="horizontal"
        router
        default-active="/home"
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
            <el-button @click="changePassword">修改密码</el-button>
            <el-button @click="destroyUser">注销用户</el-button>
          </el-dropdown-menu>
        </el-dropdown>

        <span style="color: white"> {{ userName }} </span>
      </div>
    </el-row>

    <el-container style="border: 1px solid #eee; display: flex; flex: auto">
      <section class="screen-left">
        <div id="left-top">
          <el-row :gutter="100">
            <el-col :span="1"
              ><img
                class="car001"
                src="../../assets/img/car2.jpg"
                width="269px"
            /></el-col>
          </el-row>
          <el-row :gutter="100">
            <el-col :span="1"
              ><img class="car002" src="../../assets/img/car4.jpg"
            /></el-col>
          </el-row>
        </div>
        <div id="left-bottom">
          <el-card class="box-card">
            <div slot="header" class="clearfix">
              <span>小组成员介绍</span>
            </div>
            <div class="text item">
              <span>71119113 李锐 </span>
            </div>
            <div class="text item">
              <span>71119201 饶杰熙 </span>
            </div>
            <div class="text item">
              <span>71119117 陈铎文 </span>
            </div>
            <div class="text item">
              <span>71119221 张惠杰 </span>
            </div>
          </el-card>
        </div>
      </section>
      <section class="screen-middle">
        <div id="middle-top">
          <sale-map
            style="background-color: transparent; width: 500px; height: 450px"
          ></sale-map>
        </div>
        <div id="middle-bottom">
          <el-select
            v-model="selectedCarModel"
            placeholder="请选择汽车型号"
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
          <div class="block">
            <p style="color: white">请选择分析时间</p>
            <el-date-picker
              @change="sendParameter"
              v-model="selectedTime"
              type="daterange"
              start-placeholder="开始日期"
              end-placeholder="结束日期"
              :default-time="['00:00:00', '23:59:59']"
            >
            </el-date-picker>
          </div>
        </div>
      </section>
      <section class="screen-right">
        >
        <span style="color: white">汽车销量排行榜</span>
        <div class="scollbox" style="margin-top: 10px">
          <vue-seamless-scroll
            :data="List"
            class="seamless-warp"
            :class-option="classOption"
          >
            <ul>
              <li
                class="DataList_top"
                v-for="(item, index) in List"
                :key="index"
              >
                <div class="DataList_left one">{{ index + 1 }}</div>
                <div class="DataList_left two">{{ item.name }}</div>
                <div class="DataList_left three">{{ item.sale }}</div>
              </li>
            </ul>
          </vue-seamless-scroll>
        </div>
      </section>
    </el-container>
  </div>
</template>

<script>
import vueSeamless from "vue-seamless-scroll";
import * as echarts from "echarts";
import axios from "axios";
export default {
  components: {
    //组件
    vueSeamless,
  },
  computed: {
    classOption() {
      return {
        step: 1, // 数值越大速度滚动越快
        limitMoveNum: 4, // 开始无缝滚动的数据量 this.dataList.length
        hoverStop: true, // 是否开启鼠标悬停stop
        direction: 1, // 0向下 1向上 2向左 3向右
        openWatch: true, // 开启数据实时监控刷新dom
        singleHeight: 0, // 单步运动停止的高度(默认值0是无缝不停止的滚动) direction => 0/1
        singleWidth: 0, // 单步运动停止的宽度(默认值0是无缝不停止的滚动) direction => 2/3
        waitTime: 1000, // 单步运动停止的时间(默认值1000ms)
        autoPlay: true,
      };
    },
  },

  methods: {
    sendParameter() {
      let form = new FormData();
      form.append("selectedCarModel", this.selectedCarModel);
      let d = new Date(this.selectedTime[0]);
      let startDate = d.getFullYear() + "-" + (d.getMonth() + 1) + "-1";
      d = new Date(this.selectedTime[1]);
      let endDate = d.getFullYear() + "-" + (d.getMonth() + 1) + "-1";
      form.append("startDate", startDate);
      form.append("endDate", endDate);
      console.log(endDate);
      axios
        .post("http://127.0.0.1:5000/Main/SellingData.json", form)
        .then((response) => {
          let result = response.data;
          this.datas = result;
          let option = {
            title: {
              text: "车辆销售区域分布图",
              x: "center",
              textStyle: {
                color: "#9c0505",
              },
            },

            series: [
              {
                type: "map",
                map: "china",
                label: {
                  show: this.showLabel,
                  color: "black",
                  fontSize: 10,
                },
                // 地图大小倍数
                zoom: 1.2,
                data: this.datas,
              },
            ],
            visualMap: {
              min: 0,
              max: 200,
              text: ["High", "Low"],
              realtime: false,
              calculable: true,
              inRange: {
                color: ["lightskyblue", "yellow", "orangered"],
              },
            },
          };
          console.log(this.datas);
          this.mapChart.setOption(option);
        });
    },
    handleSelect(key, keyPath) {
      console.log(key, keyPath);
    },
    drawMap() {
      axios.get("../../../static/json/ChinaMap.json").then((response) => {
        echarts.registerMap("china", response.data);
        this.mapChart = echarts.init(
          document.getElementById("chinese_selling_map")
        );
        let option = {
          title: {
            text: "车辆销售区域分布图",
            x: "center",
            textStyle: {
              color: "#9c0505",
            },
          },

          series: [
            {
              type: "map",
              map: "china",
              label: {
                show: this.showLabel,
                color: "black",
                fontSize: 10,
              },
              // 地图大小倍数
              zoom: 1.2,
              data: this.datas,
            },
          ],
          visualMap: {
            min: 0,
            max: 200,
            text: ["High", "Low"],
            realtime: false,
            calculable: true,
            inRange: {
              color: ["lightskyblue", "yellow", "orangered"],
            },
          },
        };
        this.mapChart.setOption(option);
      });
    },
    //修改密码
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

  data() {
    const item = {
      carType: "兰博基尼",
      userComment: "不错，挺好",
    };
    return {
      selectedCarModel: "卡罗拉",
      selectedTime: [
        Date("Wed Jul 15 2019 13:48:55 GMT+0800 (GMT+08:00)"),
        Date("Wed Jul 28 2021 13:48:55 GMT+0800 (GMT+08:00)"),
      ],
      userName: "1111",
      mapChart: null,
      showLabel: false,
      datas: [{ name: "北京市", value: 50 }],
      value: null,
      teamMembers: ["rjx", "lr", "cdw", "zhj"],
      carModels: [
        {
          model: "特斯拉",
        },
        {
          model: "兰博基尼",
        },
      ],
      List: [
        {
          name: "特斯拉",
          sale: "100000",
        },
      ],
    };
  },
  mounted() {
    axios.get("http://127.0.0.1:5000/UserName").then((response) => {
      this.userName = response.data;
      console.log("user anme:" + this.userName);
    });
    this.drawMap();
    // this.chooseModel = "无限制";
    // this.priceLevel = "无限制";
    axios.get("http://127.0.0.1:5000/Main/CarModel.json").then((response) => {
      this.carModels = response.data;
    });
    axios.get("http://127.0.0.1:5000/Main/TopSale").then((response) => {
      this.List = response.data;
    });
  },
};
</script>
<style scoped>
#home {
  background: url("../../assets/img/home-background.png") no-repeat;
  background-position: center;
  height: 100%;
  width: 100%;
  margin-left: 0;
  margin-top: 0;
  background-size: cover;
  background-position: top;
}
.resize {
  position: absolute;
  right: 20px;
  top: 20px;
  cursor: pointer;
}
#car001 {
  width: 100%;
  height: 100%;
}
.screen-left {
  overflow: hidden;
  /* display: flex; */
  height: 100%;
  width: 27.6%;
}

#left-top {
  height: 53%;
  position: relative;
}
#left-bottom {
  height: 31%;
  margin-top: 10%;
  position: relative;
}

.screen-middle {
  height: 100%;
  width: 41.5%;
  margin-left: 1.6%;
  margin-right: 1.6%;
}

#middle-top {
  width: 100%;
  height: 56%;
  position: relative;
}
#middle-bottom {
  margin-top: 25px;
  width: 100%;
  height: 28%;
  position: relative;
}

.screen-right {
  height: 100%;
  width: 27.6%;
}
#right-top {
  height: 46%;
  position: relative;
}
#right-bottom {
  height: 38%;
  margin-top: 25px;
  position: relative;
}
.text {
  font-size: 14px;
}

.item {
  margin-bottom: 18px;
}

.clearfix:before,
.clearfix:after {
  display: table;
  content: "";
}
.clearfix:after {
  clear: both;
}

.box-card {
  width: 100%;
  background-color: #134094;
  color: white;
}
.map {
  width: 100%;
  height: 95%;
  background-repeat: no-repeat;
  background-position-x: -300px;
  background-position-y: -200px;
  border-radius: 0px 0px 8px 8px;
  position: relative;
  overflow: hidden;
  cursor: move;
}
.map_title {
  width: 358px;
  background-image: url("../../assets/img/first_title.png");
  background-repeat: no-repeat;
  margin: auto;
  height: 28px;
  text-align: center;
  color: white;
  font-size: 14px;
  font-family: "Microsoft YaHei";
  font-weight: bold;
}
.map_title_innerbox {
  position: absolute;
  top: -4px;
  width: 100%;
}
.map_title_box {
  height: 11%;
  width: 100%;
  top: 0px;
  left: 0px;
  background-color: rgba(17, 25, 69, 0.1);
  border-radius: 11px 11px 0px 0px;
  position: relative;
}
.seamless-warp {
  width: 100%;
  height: 90%;
  overflow: hidden;
}
ul {
  padding: 0;
}
.DataList_top {
  list-style: none;
  width: 100%;
  height: 100%;
  background-color: #4383c1;
  margin-top: 0.5rem;
  color: white;
  font-size: 1rem;
  display: flex;
  align-items: center;
}
.DataList_left {
  float: left;
  text-align: center;
}
.one {
  width: 9%;
}
.two {
  width: 60%;
  color: rgb(9, 255, 0);
  margin-left: 1%;
}
.three {
  width: 29%;
  margin-left: 1%;
}
html,
body {
  margin: 0;
  height: 100%;
  width: 100%;
}
</style>
