<template>
<div class="com-container">
    <div id="pchart2" style="width: 600px;height:400px;" ref="pc2"></div>
</div>
</template>

<script>
import cdw from "../../../../assets/theme/cdw.json";
import * as echarts from 'echarts'
export default {
  name: 'pchart2',
  methods:{
	  myEcharts(){
		  // 基于准备好的dom，初始化echarts实例
		  //var myChart = this.$echarts.init(document.getElementById('chart3'));
		  var myChart = echarts.init(this.$refs.pc2,'cdw');
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
				  data: ["最大功率(KW)","最大扭矩(N-m)","最高车速(km/h)","官方0-100km/h加速(s)","最大马力(Ps)"],
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
		  }
  },
  mounted() {
  	this.myEcharts();
   }
}
</script>

<style>

</style>