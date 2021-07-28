<template>
    <div id="pchart2" style="width: 650px;height:600px;" ref="pc2"></div>
</template>

<script>
import cdw from "../../../../assets/theme/cdw.json";
import * as echarts from 'echarts'
import axios from "axios";
export default {
  name: 'pchart2',
  data() {
        return {
            pChart2: null
        };
    },
  methods:{
	  myEcharts(){
		  // 基于准备好的dom，初始化echarts实例
		  //var myChart = this.$echarts.init(document.getElementById('chart3'));
		  var myChart = echarts.init(this.$refs.pc2);
		  // 指定图表的配置项和数据
		  var option = {
			  title: {
				  text: '动力分析',
                  textStyle: {
                    fontSize: 25,
                    color: '#ffffff'
                  },
			  },
			  tooltip: {},
			  legend: {
				  data:['百分比']
			  },
			  xAxis: {
				  data: ["最大功率(KW)","最大扭矩(N-m)","最大马力(Ps)","最高车速(km/h)","官方0-100km/h加速(s)"],
                  nameTextStyle: {
                      color: "rgba(255, 255, 255, 1)"
                  }
			  },
			  yAxis: {},
			  series: [{
				  name: '百分比',
				  type: 'bar',
				  data: [70,80,90,85,75],
                  showBackground: true,
                  backgroundStyle: {
                    color: 'rgba(180, 180, 180, 0.2)'
                  },
                  color: '#44fdc5'
			  }]
		  };

		  // 使用刚指定的配置项和数据显示图表。
		  myChart.setOption(option);
		  axios.post("http://127.0.0.1:5000/PChart1.json").then((response) => {
                    this.pChart2 = response.data;
                    console.log(this.pChart2)
                    myChart.setOption({
						series: [{  //动画的配置
                            data: this.pChart2 //这里数据是一个数组的形似
                    	}]
					})
                });
		  }
  },
  mounted() {
  	this.myEcharts();
   }
}
</script>

<style>

</style>