<template>
    <div id="pchart1" style="width: 650px;height:600px;" ref="pc1"></div>
</template>

<script>
import cdw from "../../../../assets/theme/cdw.json";
import * as echarts from 'echarts'
import axios from "axios";
export default {
    name: 'pchart1',
    data() {
        return {
            pChart1: null
        };
    },
    methods:{
      drawPie() {
          var charts = echarts.init(this.$refs.pc1);
          var option = {
                    title: {
                        text: "动力分析",
                        target: "blank",
                        textAlign: 'left',
                        textStyle: {
                        fontSize: 25,
                        color: '#ffffff'
                    },
                    },
                    tooltip: {},//提示层
                    legend: {
                        data: ['name1']
                    },
                    radar: {
                        name: {
                            textStyle: {
                                color: '#fff', //字体颜色
                                backgroundColor: '#999', //背景色
                                borderRadius: 3, //圆角
                                padding: [3, 5] //padding
                            }
                        },
                        center: ['50%', '50%'],
                        radius: '60%',
                        startAngle: 270,
                        indicator: [{
                                name: '最大功率(KW)',
                                max: 500
                            },
                            {
                                name: '最大扭矩(N-m)',
                                max: 800
                            },
                            {
                                name: '最大马力(Ps)',
                                max: 800
                            },
                            {
                                name: '最高车速(km/h)',
                                max: 350
                            },
                            {
                                name: '官方0-100km/h加速(s)',
                                max: 20
                            }
                        ],
                    },
                    series: [{
                        name: '动力分析',
                        type: 'radar',
                        data: [{
                            value: [],
                            name: "动力分析结果"
                        }],
                        itemStyle: {
                    	normal: {
                        color: '#44fdc5',
                        lineStyle: {
                            color: '#44fdc5',
                        },
                    },
                },
                    }]
                };
                charts.setOption(option);
                axios.post("http://127.0.0.1:5000/PChart1.json").then((response) => {
                    this.pChart1 = response.data;
                    console.log(this.pChart1)
                    charts.setOption({  //动画的配置
                        series: [{
                            data: [{
                                value: this.pChart1 //这里数据是一个数组的形似
                            }]
                        }]
                    })
                });
            }
        },
        mounted() {
            this.drawPie();
        }
}

</script>

<style>
.com-container {
    z-index: 999;
    position: absolute;
    transform: translateY(-50%);
    top: 50%;
    cursor: pointer;
}
</style>