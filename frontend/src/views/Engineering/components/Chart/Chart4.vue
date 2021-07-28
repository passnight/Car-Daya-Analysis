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
		series: [{
			type: 'gauge',
			startAngle: 90,
			endAngle: -270,
			pointer: {
				show: false
			},
			progress: {
				show: true,
				overlap: false,
				roundCap: true,
				clip: false,
				itemStyle: {
					borderWidth: 1,
					borderColor: '#464646'
				}
			},
			axisLine: {

				lineStyle: {
					width: 40
				}
			},
			splitLine: {
				show: false,
				distance: 0,
				length: 10
			},
			axisTick: {
				show: false
			},
			axisLabel: {
				show: false,
				distance: 50
			},
			data: [{
				value: 20,
				name: 'Perfect',
				title: {
					offsetCenter: ['0%', '-55%']
				},
				detail: {
					offsetCenter: ['0%', '-45%']
				}
			},
			{
				value: 40,
				name: 'Good',
				title: {
					offsetCenter: ['0%', '-25%']
				},
				detail: {
					offsetCenter: ['0%', '-15%']
				}
			},
			{
				value: 60,
				name: 'Commonly',
				title: {
					offsetCenter: ['0%', '5%']
				},
				detail: {
					offsetCenter: ['0%', '15%']
				}
			},
			{
				value: 60,
				name: '233',
				title: {
					offsetCenter: ['0%', '35%']
				},
				detail: {
					offsetCenter: ['0%', '45%']
				}
			}
			],
			title: {
				fontSize: 14
			},
			detail: {
				width: 50,
				height: 14,
				fontSize: 14,
				color: 'auto',
				borderColor: 'auto',
				borderRadius: 20,
				borderWidth: 1,
				formatter: '{value}%'
			}
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