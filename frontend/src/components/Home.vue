<template>
  <div class="homepage">
    <div id="left_box">

      <div
        class="dataAllBorder01 cage_cl"
        style="margin-top: 1.5% !important; height: 33%; width: 100%"
      >
        <div class="dataAllBorder02 video_cage">
          <img class="video_around" src="../assets/img/car1.jpg" style="width:50%">
          <img class="video_around" src="../assets/img/car2.jpg" style="width:50%"/>
          <img class="video_around" src="../assets/img/car3.jpg" style="width:50%"/>
          <img class="video_around" src="../assets/img/car4.jpg" style="width:50%"/>
        </div>
      </div>

      <!-- 滚动栏 -->
      <div class="dataAllBorder02" style="padding: 1.2%; overflow: hidden height:33% width:33%">
        <!-- will be import scroll message -->
        <div class="message_scroll_box">
          <div class="message_scroll">
            <div class="scroll_top">
              <span class="scroll_title">71119201 饶杰熙 }</span>
            </div>
            <div class="msg_cage">
              <a class="localize_title">${scrollMessage[i].topSaleCarMod}</a>
            </div>
            <div class="msg_cage">
              <a class="localize_msg">${scrollMessage[i].topSaleCarSeller}</a>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- 大地图 -->
    <div id="central_box">
      <div class="map_title_box" style="height: 6%">
        <div class="map_title_innerbox">
          <div class="map_title">销售热点区域</div>
        </div>
      </div>
      <div class="map" id="map" style="width: 60%; height: 100%">
        <img src="../assets/img/waifu.jpeg" />
      </div>

      <div class="map_title_box">
        <div class="map_title_innerbox">
          <div
            class="map_title"
            style="background-image: url(img/second_title.png)"
          >
            数据筛选
          </div>
        </div>
        <div>
          <select id="selLayer" style="width: 100px">
            <option value="">利润排名</option>
            <option value="">前景排名</option>
          </select>
        </div>
        <form>
          <li>型号 <input type="text" name="型号" /></li>
          <li>时间 <input type="text" name="时间" /></li>
        </form>
      </div>
    </div>
    <div id="right_box">
      <div
        class="dataAllBorder01 cage_cl"
        style="margin-top: 9% !important; height: 24%"
      >
        <!-- 推荐生产的车型 -->
        <form>
          <li>model1</li>
          <li>model2</li>
          <li>model3</li>
          <li>model4</li>
        </form>
      </div>
    </div>
    推荐生产
  </div>
</template>

<script>
export default {
  name: "home",
};
</script>
<style scoped>
#left_box {
  width: 20%;
  float: left;
  display: flex;
  background-color:aliceblue
}
#central_box {
  width: 60%;
  display: flex;
}
#right_box {
  width: 20%;
  float: right;
  background-color:bisque
}
.homepage {
  width: 100%;
  height: 100%;
  background-image: url("../assets/img/home-background.png");
  background-size: 100% 100%;
  position: absolute;
}
/* #selLayer {
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
  background-image: url("../assets/img/pushmessage_class.png");
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
} */
.localize_title {
  color: #2c85d2;
}
</style>