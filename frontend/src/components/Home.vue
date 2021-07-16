<template>
  <div class="homepage">
    <div class="left_box">
      <div class="left_box_col"></div>
      <div class="left_box_col"></div>
      <div class="left_box_col">
        <el-carousel indicator-position="outside">
          <el-carousel-item v-for="item in teamMembers" :key="item">
            <h3>{{ item }}</h3>
          </el-carousel-item>
        </el-carousel>
      </div>
    </div>
    <div class="central_box">
      <div class="central_img">
        <!-- <img
          src="../assets/img/waifu.jpeg"
          alt="waifu"
          style="width: 100%"
          object-fit="fill"
        /> -->
      </div>
      <div style="overflow:scroll width:100% height:'30%'">
        <div class="map_title" id="choose_info">信息选择</div>
        <form style="color: white">
          型号
          <li><input type="text" /></li>
          时间
          <li><input type="text" /></li>
        </form>
      </div>
    </div>
    <div class="right_box">
      <div style="overflow:scroll width:100%">
        <form style="color: white">
          <div class="map_title" id="hot_model">热销车型</div>
          <li>show something</li>
          <li>show something</li>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "home",
  data() {
    return {
      teamMembers: ["rjx", "lr", "cdw", "zhj"],
    };
  },
};
</script>
<style scoped>
.map_title#choose_info{
  left: 650px;
  top: -100px;
  position: relative;
  width: 358px;
  background-image: url("../assets/img/first_title.png");
  background-repeat: no-repeat;
  margin: auto;
  height: 28px;
  text-align: center;
  color: white;
  font-size: 14px;
  font-family: "Microsoft YaHei";
  font-weight: bold;
}
.map_title#hot_model{
  left: 70px;
  top: 0px;
  position: relative;
  width: 358px;
  background-image: url("../assets/img/first_title.png");
  background-repeat: no-repeat;
  margin: auto;
  height: 28px;
  text-align: center;
  color: white;
  font-size: 14px;
  font-family: "Microsoft YaHei";
  font-weight: bold;
}
.homepage {
  width: 100%;
  height: 100%;
  background-image: url("../assets/img/home-background.png");
  background-size: 100% 100%;
  position: absolute;
}
.central_box .central_img {
  width: 100%;
  height: 70%;
  border: 2px solid black;
}
.left_box .left_box_col {
  width: 100%;
  height: 33%;
  border: 2px solid black;
}
.left_box {
  top: 8%;
  border: 2px solid black;
  width: 19%;
  height: 92%;
  float: left;
  background-color: transparent;
  display: flex;
  flex-wrap: wrap;
  position: relative;
}
.right_box {
  top: 8%;
  border: 2px solid black;
  width: 19%;
  height: 92%;
  float: left;
  background-color: transparent;
  display: flex;
  flex-wrap: wrap;
  position: relative;
}
.central_box {
  top: 8%;
  border: 2px solid black;
  width: 60%;
  height: 92%;
  float: left;
  background-color: transparent;
  display: flex;
  flex-wrap: wrap;
  position: relative;
}

.el-carousel__item h3 {
  color: #475669;
  font-size: 18px;
  opacity: 0.75;
  line-height: 300px;
  margin: 0;
}

.el-carousel__item:nth-child(2n) {
  background-color: #016ae0;
}

.el-carousel__item:nth-child(2n + 1) {
  background-color: #2c85d2;
}
</style>