<template>
    <div id="fchart1" style="width: 600px;height:400px;" ref="fc1"></div>
</template>

<script>
import cdw from "../../../../assets/theme/cdw.json";
import * as echarts from 'echarts'
import axios from "axios";
export default {
    name: 'fchart1',
    data() {
        return {
        fChart1: null
        };
    },
    methods:{
      drawPie() {
          var charts = echarts.init(this.$refs.fc1,'cdw');
          var option = {
                    title: {
                        text: "油耗分析",
                        target: "blank",
                        textAlign: 'left',
 
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
                                name: '认证车主平均油耗',
                                max: 30
                            },
                            {
                                name: 'NEDC综合油耗',
                                max: 30
                            },
                            {
                                name: '实测油耗',
                                max: 30
                            }
                        ],
                    },
                    series: [{
                        name: '油耗分析',
                        type: 'radar',
                        data: [{
                            value: [],
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
                    myChart.setOption({  //动画的配置
                        series: [{
                        data: this.fChart1 //这里数据是一个数组的形似
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