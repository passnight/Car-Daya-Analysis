<template>
    <div id="fchart1" style="width: 650px;height:600px;" ref="fc1"></div>
</template>

<script>
import cdw from "../../../../assets/theme/cdw.json";
import * as echarts from 'echarts'
import axios from "axios";
export default {
    name: 'fchart1',
    methods:{
        data() {
        return {
            fChart1: null
        };
    },
      drawPie() {
          var charts = echarts.init(this.$refs.fc1);
          var option = {
                    title: {
                        text: "油耗分析",
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
                                name: 'NEDC综合油耗(L/100km)',
                                max: 20
                            },
                            {
                                name: '实测油耗(L/100km)',
                                max: 20
                            },
                            {
                                name: '标准油耗(L/100km)',
                                max: 20
                            }
                        ],
                    },
                    series: [{
                        name: '油耗分析',
                        type: 'radar',
                        data: [{
                            value: [10.4,12.4,10],
                            name: "油耗分析结果"
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
                axios.post("http://127.0.0.1:5000/FChart1.json").then((response) => {
                    this.fChart1 = response.data;
                    console.log(this.fChart1)
                    charts.setOption({  //动画的配置
                        series: [{
                            data: [{
                                value: this.fChart1 //这里数据是一个数组的形似
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