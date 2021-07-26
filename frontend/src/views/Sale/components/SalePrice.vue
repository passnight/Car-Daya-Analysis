<template>
    <div id="饼状图" style="width: 100%; height: 500px;">
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
    //             var myfun=async function () {
    //        await    
    //         axios.get("http://127.0.0.1:5000/CarSalePrice.json").then((response) => {
    //   this.mydata = response.data;
    // });
    // }
                this.drawLine();
            },
            methods: {
                drawLine(){
                    this.chartDom = echarts.init(
                        document.getElementById('饼状图'));

                    this.chartDom.setOption({
                        title: {
        text: '汽车价格分布图'
    },
     legend: {
        top: 'bottom',
        textStyle:{
                          
                            color: '#ffffff'//字体颜色
                        },
     },

    toolbox: {
        show: true,
        feature: {
            mark: {show: true},
            dataView: {show: true, readOnly: false},
            restore: {show: true},
            saveAsImage: {show: true}
        }
    },
    series: [
        {
            name: '面积模式',
            type: 'pie',
            radius: [25, 200],
            center: ['50%', '50%'],
            roseType: 'area',
            itemStyle: {
                borderRadius: 8
            },
            data: [
                {value: 40, name: '<5万'},
                {value: 38, name: '5~10万'},
                {value: 32, name: '10~15万'},
                {value: 30, name: '15~20万'},
                {value: 28, name: '20~25万'},
                {value: 26, name: '25~50万'},
                {value: 22, name: '50~100万'},
                {value: 18, name: '>100万'}
            ]
        }
    ]
                });
                }
            }
        }
    </script>