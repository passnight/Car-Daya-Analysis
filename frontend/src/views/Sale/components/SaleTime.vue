<template>
    <div id="折线图" style="width: 100%; height: 500px;">
    </div>
</template>


<script>
       import * as echarts from 'echarts'
        export default {
            data(){
                return {
                    chartColumn: null,
                    mydata:null
                }
            },
            mounted() {
               // axios.get("http://127.0.0.1:5000/CarSaleTime.json").then((response) => {
     // this.mydata = response.data;
    //});
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
        trigger: 'axis',
        axisPointer: {            // 坐标轴指示器，坐标轴触发有效
            type: 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
        }
    },
    legend: {
        data: ['A汽车销售', 'B汽车销售','总体销售'],
        textStyle:{
                          
                            color: '#ffffff'//字体颜色
                        },
    },
    grid: {
        left: '10%',
        right: '10%',
        bottom: '10%',
        top:'10%',
        containLabel: true
    },
    xAxis: [
        {
            type: 'category',
            data: ['一月', '二月', '三月', '四月', '五月', '六月', '七月']
        }
    ],
    yAxis: [
        {
            type: 'value'
        }
    ],
    series: [
        {
            name: 'A汽车销售',
            type: 'bar',
            emphasis: {
                focus: 'series'
            },
            data: [320, 332, 301, 334, 390, 330, 320]
        },
         {
            name: 'B汽车销售',
            type: 'bar',
            emphasis: {
                focus: 'series'
            },
            data: [420, 232, 401, 234, 390, 350, 370]
        },
        {
            name: '总体销售',
            type: 'bar',
            data: [862, 1018, 964, 1026, 1679, 1600, 1570],
            emphasis: {
                focus: 'series'
            },
           
        }
    ]
                });
                }
            }
        }
    </script>