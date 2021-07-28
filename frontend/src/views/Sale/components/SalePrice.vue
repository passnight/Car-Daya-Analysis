<template>
<<<<<<< HEAD
<el-contianer>
     <el-container>
      <el-container>
    <el-main>
      <div class="demo-image__placeholder">
        <div id="block" style="display: flex; flex-direction: column">
     
          <el-image :src="src" :fit="scale - down">
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
        
          <el-image :src="src" :fit="scale - down">
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

          <el-image :src="src" :fit="scale - down">
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
          <el-image :src="src" :fit="scale - down">
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
    <div id="折线图" style="width: 100%; height: 500px;">
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
=======
       import * as echarts from 'echarts'
        export default {
            data(){
                return {
                    chartColumn: null,
                    mydata:null
                }
            },
            mounted() {
                var myfun=async function () {
           await     axios.get("http://127.0.0.1:5000/CarSalePrice.json").then((response) => {
      this.mydata = response.data;
    });
    }
                this.drawLine();
            },
            methods: {
                drawLine(){
                    this.chartColumn = echarts.init(
                        document.getElementById('折线图'));

                    this.chartColumn.setOption({
                       title: {
        text: '汽车价格对比折线图'
    },
    tooltip: {
        trigger: 'axis'
    },
    legend: {
        //data:this.mydata.AName
        //data:this.mydata.BName
        data: ['甲车型', '乙车型']
        ,
         textStyle:{
                          
                            color: '#ffffff'//字体颜色
                        },
    },
    grid: {
        left: '3%',
        right: '4%',
        bottom: '3%',
        top:'15%',
        containLabel: true
    },
    toolbox: {
        feature: {
            saveAsImage: {}
        }
    },
    xAxis: {
        type: 'category',
        boundaryGap: false,
        //data:this.mydata.time
         data: ['一月', '二月', '三月', '四月', '五月', '六月']
    },
    yAxis: {
        type: 'value'
    },
    series: [
        {
            //name:this.mydata.AName
            name: '甲车型',
            type: 'line',
            stack: '售价',
            //data:this.mydata.Adata
            data: [120, 132, 101, 134, 90, 230, 210]
        },
        {
               //name:this.mydata.BName
            name: '乙车型',
            type: 'line',
            stack: '售价',
              //data:this.mydata.Bdata
            data: [220, 182, 191, 234, 290, 330, 310]
        }
    ]
                });
                }
            }
        }
    </script>
>>>>>>> 731a7ad7df324c6e85617f6e7a32741e551a3f68
