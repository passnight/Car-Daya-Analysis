<template>
    <div id="chart5" style="width: 600px;height:400px;" ref="c5"></div>
</template>

<script>
  import * as echarts from 'echarts'
export default {
    name: 'chart5',
    methods:{
      drawPie() {
          var charts = echarts.init(this.$refs.c5);
          var option = {
                    title: {
                        text: "测试结果",
                        link: 'https://www.baidu.com',
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
                                name: '思想道德素质',
                                max: 100
                            },
                            {
                                name: '健康与安全',
                                max: 100
                            },
                            {
                                name: '与人交往',
                                max: 100
                            },
                            {
                                name: '学习与发展',
                                max: 100
                            },
                            {
                                name: '艺术与人文',
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
                        }]
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