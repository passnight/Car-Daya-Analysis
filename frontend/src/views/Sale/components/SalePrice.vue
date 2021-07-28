<template>
    <div id="折线图" style="width: 100%; height: 500px;">
    </div>
</template>


<script>
       import * as echarts from 'echarts'
       import axios from "axios";
        export default {
            data(){
                return {
                    chartColumn: null,
                    mydata:null,
                    salePrice: null
                }
            },
            mounted() {
                var myfun=async function () {
           await     axios.get("http://127.0.0.1:5000/CarSalePrice.json").then((response) => {
      this.mydata = response.data;
    });
    }
                this.drawLine();
            },
            methods: {
                drawLine(){
                    this.chartColumn = echarts.init(
                        document.getElementById('折线图'));

                    this.chartColumn.setOption({
                    
                title: {
                    text: '汽车价格对比阶梯折线图',
                    textStyle: {
                    fontSize: 25,
                    color: '#ffffff'}
                },
                tooltip: {
                    trigger: 'axis'
                },
                legend: {
                    data: [],
                    textStyle:{
                            color: '#ffffff'//字体颜色
                        },
                },
                grid: {
                    left: '3%',
                    right: '4%',
                    bottom: '3%',
                    containLabel: true
                },
                toolbox: {
                    feature: {
                        saveAsImage: {}
                    }
                },
                xAxis: {
                    type: 'category',
                    data: []
                },
                yAxis: {
                    type: 'value'
                },
                series: [
                    {
                        name: '',
                        type: 'line',
                        step: 'start',
                        data: []
                    },
                    {
                        name: '',
                        type: 'line',
                        step: 'middle',
                        data: []
                    }
                ]
            });
            axios.post("http://127.0.0.1:5000/carSalePrice.json").then((response) => {
                    this.salePrice = response.data;
                    //this.saleTime2 = response.data2;
                    console.log(this.salePrice)
                    this.chartColumn.setOption( //动画的配置
                        this.salePrice
                    )
                });
                }
            }
        }
    </script>