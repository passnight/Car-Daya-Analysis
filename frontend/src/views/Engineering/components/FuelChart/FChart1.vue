<template>
    <div id="fchart1" style="width: 600px;height:400px;" ref="fc1"></div>
</template>

<script>
import cdw from "../../../../assets/theme/cdw.json";
import * as echarts from 'echarts'
export default {
    name: 'fchart1',
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
                            value: [10.4,12.4,11.5],
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
            }
        },
        mounted() {
            this.drawPie();
        }
}

</script>

<style>

</style>