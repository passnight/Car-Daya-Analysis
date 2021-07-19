<template>
  <el-container class="homepage">
    <el-header>
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
    </el-header>

    <el-container>
      <el-aside id="left_box" width="400px">
        <div>
          <el-row :gutter="200">
            <el-col :span="1">
              <img src="../../assets/img/car1.jpg" alt="car1" width="190"
            /></el-col>
            <el-col :span="1"
              ><img src="../../assets/img/car2.jpg" alt="car2" width="190"
            /></el-col>
          </el-row>
          <el-row :gutter="200">
            <el-col :span="1"
              ><img src="../../assets/img/car3.jpg" alt="car3" width="190"
            /></el-col>
            <el-col :span="1"
              ><img src="../../assets/img/car4.jpg" alt="car4" width="190"
            /></el-col>
          </el-row>
        </div>

        <div>
          <el-carousel :interval="5000" arrow="always" height="300">
            <el-carousel-item v-for="item in teamMembers" :key="item">
              <h3>{{ item }}</h3>
            </el-carousel-item>
          </el-carousel>
        </div>
      </el-aside>

      <el-main id="main_table">
        <div></div>
        <!-- <img src="../../assets/img/car1.jpg" alt="car" width="60%" /> -->
        <sale-map style="background-color: transparent"></sale-map>
        <p></p>

        <el-select v-model="value" placeholder="请选择汽车型号">
          <el-option
            v-for="item in carModels"
            :key="item.value"
            :label="item.model"
            :value="item.model"
          >
          </el-option>
        </el-select>

        <div class="block">
          <p style="color: white">请选择分析时间：{{ value }}</p>
          <el-date-picker
            v-model="value"
            type="daterange"
            start-placeholder="开始日期"
            end-placeholder="结束日期"
            :default-time="['00:00:00', '23:59:59']"
          >
          </el-date-picker>
        </div>
      </el-main>
    </el-container>
  </el-container>
</template>

<script>
import * as echarts from "echarts";
import axios from "axios";
export default {
  name: "home",
  methods: {
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
            min: 800,
            max: 50000,
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
  },
  data() {
    const item = {
      carType: "兰博基尼",
      userComment: "不错，挺好",
    };
    return {
      mapChart: null,
      showLabel: false,
      datas: [{ name: "北京市", value: 40000 }],
      value: null,
      teamMembers: ["rjx", "lr", "cdw", "zhj"],
      carModels: [
        {
          model: "特斯拉",
        },
      ],
    };
  },
  mounted() {
    axios.get("http://127.0.0.1:5000/CarModel.json").then((response) => {
      this.carModels = response.data;
    });
    axios.post("http://127.0.0.1:5000/SellingData.json").then((response) => {
      this.datas = response.data;
      console.log(this.datas)
    });
    // axios.get("../../../static/data/SellingData.json").then((response) => {
    //   this.datas = response.data;
    // });
    this.$nextTick(function () {
      this.drawMap();
    });
  },
};
</script>
<style scoped>
#main_table {
  height: auto;
}
#left_box {
  border: 2px solid white;
}
#selLayer {
  width: 200px;
  display: block;
  height: 26px;
  background-color: transparent;
  color: #0b7ff3;
  border: #0b7ff3 2px solid;
  position: absolute;
  right: 2px;
  border-radius: 5px;
  margin-top: 2px;
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
.dataAllBorder01 {
  width: 100%;
  height: 100%;
  border-radius: 10px;
  border: 1px #0174f5 solid;
  padding: 1px;
  box-sizing: border-box;
}
.cage_cl {
  background-color: rgba(2, 8, 23, 0.1);
}
.dataAllBorder02 {
  width: 100%;
  height: 100%;
  box-sizing: border-box;
  border: 2px solid #016ae0;
  border-radius: 10px;
}
.homepage {
  /* width: 100%;
  height: 100%;
  background-image: url("../../assets/img/home-background.png");
  background-size: 100% 100%;
  position: absolute; */

  background: url("../../assets/img/home-background.png") no-repeat;
  background-position: center;
  height: 100%;
  width: 100%;
  background-size: cover;
  background-position: top;
}
.message_scroll {
  border: rgba(12, 122, 200, 0.5) 1px solid;
  background-color: rgba(20, 66, 125, 0.12);
  height: 90px;
  cursor: pointer;
  margin-bottom: 6px;
}
.scroll_top {
  height: 25px;
}
.scroll_title {
  float: left;
  background-image: url("../../assets/img/pushmessage_class.png");
  background-repeat: no-repeat;
  width: 150px;
  line-height: 25px;
  color: white;
  font-size: 14px;
  text-align: center;
}
.msg_cage {
  padding-left: 10px;
  padding-right: 6px;
  height: 18px;
  overflow: hidden;
  margin-top: 8px;
}
.localize_title {
  color: #2c85d2;
}
.el-carousel__item h3 {
  color: #475669;
  font-size: 18px;
  opacity: 0.75;
  line-height: 300px;
  margin: 0;
}

.el-carousel__item:nth-child(2n) {
  background-color: #99a9bf;
}

.el-carousel__item:nth-child(2n + 1) {
  background-color: #d3dce6;
}

.el-row {
  margin-bottom: 20px;
}
.el-col {
  border-radius: 4px;
}
.bg-purple-dark {
  background: #99a9bf;
}
.bg-purple {
  background: #d3dce6;
}
.bg-purple-light {
  background: #e5e9f2;
}
.grid-content {
  border-radius: 4px;
  min-height: 36px;
}
.row-bg {
  padding: 10px 0;
  background-color: #f9fafc;
}
</style>