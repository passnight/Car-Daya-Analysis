<template>
    <div id="折线图" style="width: 100%; height: 500px;">
    </div>
</template>


<script>
       import * as echarts from 'echarts'
        export default {
            data(){
                return {
                    chartColumn: null
                }
            },
            mounted() {
                this.drawLine();
            },
            methods: {
                drawLine(){
                    this.chartColumn = echarts.init(document.getElementById('折线图'));

                    this.chartColumn.setOption({
                       title: {
        text: '汽车销售趋势对比折线图'
    },
    tooltip: {
        trigger: 'axis'
    },
    legend: {
        data: ['甲车型', '乙车型'],
         textStyle:{
                          
                            color: '#ffffff'//字体颜色
                        },
    },
    grid: {
        left: '3%',
        right: '4%',
        bottom: '3%',
        top:'15%',
        containLabel: true
    },
    toolbox: {
        feature: {
            saveAsImage: {}
        }
    },
    xAxis: {
        type: 'category',
        boundaryGap: false,
        data: ['一月', '二月', '三月', '四月', '五月', '六月']
    },
    yAxis: {
        type: 'value'
    },
    series: [
        {
            name: '甲车型',
            type: 'line',
            stack: '销售占比',
            data: [50, 40, 45, 60, 90, 75, 55]
        },
        {
            name: '乙车型',
            type: 'line',
            stack: '销售占比',
            data: [32, 23, 54, 45, 32, 67, 43]
        }
    ]
                });
                }
            }
        }
    </script>