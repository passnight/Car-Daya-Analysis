<template>
    <div id="chart3" style="width: 600px;height:400px;" ref="c3"></div>
</template>

<script>
  import * as echarts from 'echarts'
export default {
    name: 'chart3',
    methods:{
      drawPie() {
          var charts = echarts.init(this.$refs.c3);
          var option = {
                    title: {
                        text: "动力分析",
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
                        name: '测试标题名字',
                        type: 'radar',
                        data: [{
                            value: [70,80,90,85,75],
                            name: "测试结果"
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