<template>
<div class="com-container">
    <div id="pchart1" style="width: 600px;height:400px;" ref="pc1"></div>
</div>
</template>

<script>
import cdw from "../../../../assets/theme/cdw.json";
import * as echarts from 'echarts'
export default {
    name: 'pchart1',
    methods:{
      drawPie() {
          var charts = echarts.init(this.$refs.pc1,'cdw');
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
                                max: 100
                            },
                            {
                                name: '最大扭矩(N-m)',
                                max: 100
                            },
                            {
                                name: '最高车速(km/h)',
                                max: 100
                            },
                            {
                                name: '官方0-100km/h加速(s)',
                                max: 100
                            },
                            {
                                name: '最大马力(Ps)',
                                max: 100
                            }
                        ],
                    },
                    series: [{
                        name: '动力分析',
                        type: 'radar',
                        data: [{
                            value: [70,80,90,85,75],
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