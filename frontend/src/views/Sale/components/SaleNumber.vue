<template>
<<<<<<< HEAD
<el-contianer>
     <el-container>
      <el-container>
    <el-main>
      <div class="demo-image__placeholder">
        <div id="block" style="display: flex; flex-direction: column">
     
          <el-image
           style="width: 100%; height: 100%"
      :src="src" :fit="fit">
            <div slot="placeholder" class="image-slot">
              加载中<span class="dot">...</span>
            </div>
          </el-image>
        </div>
      </div>
    </el-main>
  </el-container>
   <el-container>
    <el-main>
      <div class="demo-image__placeholder">
       <div id="block" style="display: flex; flex-direction: column">
        
          <el-image
            style="width: 100%; height: 100%"
      :src="src" :fit="fit">
            <div slot="placeholder" class="image-slot">
              加载中<span class="dot">...</span>
            </div>
          </el-image>
        </div>
      </div>
    </el-main>
  </el-container>
 </el-container>


  <el-container>
      <el-container>
    <el-main>
      <div class="demo-image__placeholder">
        <div id="block" style="display: flex; flex-direction: column">

          <el-image 
           style="width: 100%; height: 100%"
      :src="src" :fit="fit">
            <div slot="placeholder" class="image-slot">
              加载中<span class="dot">...</span>
            </div>
          </el-image>
        </div>
      </div>
    </el-main>
  </el-container>
   <el-container>
    <el-main>
      <div class="demo-image__placeholder">
         <div id="block" style="display: flex; flex-direction: column">
          <el-image
            style="width: 100%; height: 100%"
      :src="src" :fit="fit">
            <div slot="placeholder" class="image-slot">
              加载中<span class="dot">...</span>
            </div>
          </el-image>
        </div>
      </div>
    </el-main>
  </el-container>
 </el-container>
</el-contianer>
 
=======
    <div id="柱状图" style="width: 100%; height: 500px;">
    </div>
>>>>>>> 731a7ad7df324c6e85617f6e7a32741e551a3f68
</template>


<script>
<<<<<<< HEAD
export default {
  name: "chapter",
  data() {
    return {
      src: "https://cube.elemecdn.com/6/94/4d3ea53c084bad6931a56d5158a48jpeg.jpeg",
    };
  },
  
};
</script>
<style scoped>

</style>
=======
       import * as echarts from 'echarts'
       import * as axios from 'axios'
        export default {
            data(){
                return {
                    chartColumn: null,
                    mydata:null
                }
            },
            mounted() {
                axios.get("http://127.0.0.1:5000/carSaleNumber.json").then((response) => {
      this.mydata = response.data;
    });
                this.drawLine();
            },
            methods: {
                drawLine(){
                    this.chartDom = echarts.init(document.getElementById('柱状图'));

                    this.chartDom.setOption({
                        tooltip: {
        trigger: 'axis',
        axisPointer: {
            type: 'cross',
            crossStyle: {
                color: '#999'
            }
        }
    },
    toolbox: {
        feature: {
            dataView: {show: true, readOnly: false},
            magicType: {show: true, type: ['line', 'bar']},
            restore: {show: true},
            saveAsImage: {show: true}
        }
    },
    legend: {
        // data: ['甲车', '乙车', '总体趋势'],
        data: ['甲车', '乙车', '总体趋势'],
         textStyle:{
                          
                            color: '#ffffff'//字体颜色
                        },
    },
    xAxis: [
        {
            type: 'category',
           // data: this.mydata.time,
            data: ['1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月'],
            axisPointer: {
                type: 'shadow'
            }
        }
    ],
    yAxis: [
        {
            type: 'value',
            //name:this.mydata.AName,
            name: '甲车',
            min: 0,
            max: 250,
            interval: 50,
            axisLabel: {
                formatter: '{value} 万辆'
            }
        },
        {
            type: 'value',
            //name:this.mydata.BName,
            name: '乙车',
            min: 0,
            max: 25,
            interval: 5,
            axisLabel: {
                formatter: '{value} 万辆'
            }
        }
    ],
        series: [
        {
            name: '甲车',
            //name:this.mydata.AName,
            type: 'bar',
            //data:this.mydata.AData
            data: [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3]
        },
        {
            name: '乙车',
             //name:this.mydata.BName,
            type: 'bar',
            //data:this.mydata.BData
            data: [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3]
        },
        {
            name: '总体趋势',
            type: 'line',
            yAxisIndex: 1,
            //data:this.mydata.CData
            data: [2.0, 2.2, 3.3, 4.5, 6.3, 10.2, 20.3, 23.4, 23.0, 16.5, 12.0, 6.2]
        }
    ]
                });
                }
            }
        }
    </script>
>>>>>>> 731a7ad7df324c6e85617f6e7a32741e551a3f68
