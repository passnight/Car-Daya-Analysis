<template>
    <div id="chart4" style="width: 600px;height:400px;" ref="c4"></div>
</template>

<script>
  import * as echarts from 'echarts'
export default {
  name: 'chart4',
  methods:{
	  myEcharts(){
		  // 基于准备好的dom，初始化echarts实例
		  //var myChart = this.$echarts.init(document.getElementById('chart3'));
		  var myChart = echarts.init(this.$refs.c4);
		  // 指定图表的配置项和数据
		  var option = {
			  title: {
				  text: 'ECharts 入门示例'
			  },
			  tooltip: {},
			  legend: {
				  data:['销量']
			  },
			  xAxis: {
				  data: ["衬衫","羊毛衫","雪纺衫","裤子","高跟鞋","袜子"]
			  },
			  yAxis: {},
			  series: [{
				  name: '销量',
				  type: 'bar',
				  data: [5, 20, 36, 10, 10, 20]
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