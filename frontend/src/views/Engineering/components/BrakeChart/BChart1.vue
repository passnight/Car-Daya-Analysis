<template>
    <div id="bchart1" style="width: 650px;height:600px;" ref="bc1"></div>
</template>

<script>
import * as echarts from 'echarts'
import axios from "axios";
export default {
  name: 'bchart1',
  data() {
        return {
            bChart1: null
        };
    },
  methods:{
	  myEcharts(){
		  // 基于准备好的dom，初始化echarts实例
		  //var myChart = this.$echarts.init(document.getElementById('chart3'));
		  var myChart = echarts.init(this.$refs.bc1);
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
				name: '实测100-0km/h制动(m)',
				title: {
					offsetCenter: ['0%', '-55%']
				},
				detail: {
					offsetCenter: ['0%', '-45%'],
				}
			},
			{
				value: 100,
				name: 'ABS防抱死',
				title: {
					offsetCenter: ['0%', '-25%']
				},
				detail: {
					offsetCenter: ['0%', '-15%']
				}
			},
			{
				value: 60,
				name: '制动力分配(EBD/CBC等)',
				title: {
					offsetCenter: ['0%', '5%']
				},
				detail: {
					offsetCenter: ['0%', '15%']
				}
			},
			{
				value: 80,
				name: '主动刹车/主动安全系统',
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
		axios.post("http://127.0.0.1:5000/BChart1.json").then((response) => {
                    this.bChart1 = response.data;
                    console.log(this.bChart1)
                    myCharts.setOption({  //动画的配置
                        series: [{
                            data: [
								{
                                	value: this.bChart1[0]       //这里数据是一个数组的形似
                            	},
								{
                                	value: this.bChart1[0]       //这里数据是一个数组的形似
                            	},
								{
                                	value: this.bChart1[0]       //这里数据是一个数组的形似
                            	},
								{
                                	value: this.bChart1[0]       //这里数据是一个数组的形似
                            	},
							]
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