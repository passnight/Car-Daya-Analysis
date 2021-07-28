<template>
    <div id="bchart2" style="width: 650px;height:600px;" ref="bc2"></div>
</template>

<script>
import cdw from "../../../../assets/theme/cdw.json";
import * as echarts from 'echarts'
import axios from "axios";
export default {
    name: 'bchart2',
    data() {
        return {
            bChart2: null
        };
    },
    methods:{
      drawPie() {
          var charts = echarts.init(this.$refs.bc2);
          var option = {
                    title: {
                        text: "制动分析",
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
                                name: '实测100-0km/h制动(m)',
                                max: 50
                            },
                            {
                                name: 'ABS防抱死',
                                max: 1
                            },
                            {
                                name: '制动力分配(EBD/CBC等)',
                                max: 1
                            },
                            {
                                name: '主动刹车/主动安全系统',
                                max: 1
                            }
                        ],
                    },
                    series: [{
                        name: '制动分析',
                        type: 'radar',
                        data: [{
                            value: [],
                            name: "制动分析结果"
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
                axios.post("http://127.0.0.1:5000/BChart1.json").then((response) => {
                    this.bChart2 = response.data;
                    console.log(this.bChart2)
                    charts.setOption({  //动画的配置
                        series: [{
                            data: [{
                                value: this.bChart2 //这里数据是一个数组的形似
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

</style>