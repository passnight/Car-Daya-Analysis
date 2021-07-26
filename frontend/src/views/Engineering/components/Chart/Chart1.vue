<template>
<<<<<<< HEAD:frontend/src/views/Engineering/components/Chart/Chart1.vue
  <!--为echarts准备一个具备大小的容器dom-->
  <div id="chart1" style="width: 600px; height: 400px;" ref="c1"></div>
=======
  <div class="Echarts">
    <div id="main" style="width: 600px;height:400px;"></div>
  </div>
  <!-- <div class="Echarts">
    <div id="main2" style="width: 600px;height:400px;"></div>
  </div> -->
>>>>>>> 34fa00471fb686dcb4d9c0533d2152354662654f:frontend/src/components/Engineering/Target.vue
</template>

<script>
<<<<<<< HEAD:frontend/src/views/Engineering/components/Chart/Chart1.vue
  import * as echarts from 'echarts'
    export default {
        name: 'chart1',
        data () {
            return {
                charts: '',
                opinion:['直接访问','邮件营销','联盟广告','视频广告','搜索引擎'],
                opinionData:[
                  {value:335, name:'直接访问'},
                  {value:310, name:'邮件营销'},
                  {value:234, name:'联盟广告'},
                  {value:135, name:'视频广告'},
                  {value:1548, name:'搜索引擎'}
                ]
            }
        },
        methods:{
            drawPie(id){
               //this.charts = echarts.init(document.getElementById(id))
               this.charts = echarts.init(this.$refs.c1)
               this.charts.setOption({
                 tooltip: {
                   trigger: 'item',
                   formatter: '{a}<br/>{b}:{c} ({d}%)'
                 },
                 legend: {
                   orient: 'vertical',
                   x: 'left',
                   data:this.opinion
                 },
                 series: [
                   {
                     name:'访问来源',
                     type:'pie',
                     radius:['50%','70%'],
                     avoidLabelOverlap: false,
                     label: {
                       normal: {
                         show: false,
                         position: 'center'
                       },
                       emphasis: {
                         show: true,
                         textStyle: {
                           fontSize: '30',
                           fontWeight: 'blod'
                         }
                       }
                     },
                     labelLine: {
                       normal: {
                         show: false
                       }
                     },
                     data:this.opinionData
                   }
                 ]
               })
            }
        },
      //调用
        mounted(){
            this.$nextTick(function() {
                this.drawPie('main')
            })
        }
    }
=======
export default {
  name: 'Echarts',
  methods:{
	  myEcharts(){
		  // 基于准备好的dom，初始化echarts实例
		  var myChart = this.$echarts.init(document.getElementById('main'));

		  // 指定图表的配置项和数据
		  var option = {
			  title: {
				  text: 'ECharts 入门示例'
			  },
			  tooltip: {},
			  legend: {
				  data:['销量']
			  },
			  xAxis: {
				  data: ["衬衫","羊毛衫","雪纺衫","裤子","高跟鞋","袜子"]
			  },
			  yAxis: {},
			  series: [{
				  name: '销量',
				  type: 'bar',
				  data: [5, 20, 36, 10, 10, 20]
			  }]
		  };

		  // 使用刚指定的配置项和数据显示图表。
		  myChart.setOption(option);
		  }
  },
  mounted() {
  	this.myEcharts();
   }
//   methods2:{
// 	  myEcharts2(){
// 		  // 基于准备好的dom，初始化echarts实例
// 		  var myChart2 = this.$echarts.init(document.getElementById('main2'));

// 		  // 指定图表的配置项和数据
// 		  var option2 = {
// 			  title: {
// 				  text: 'ECharts 入门示例'
// 			  },
// 			  tooltip: {},
// 			  legend: {
// 				  data:['销量']
// 			  },
// 			  xAxis: {
// 				  data: ["衬衫","羊毛衫","雪纺衫","裤子","高跟鞋","袜子"]
// 			  },
// 			  yAxis: {},
// 			  series: [{
// 				  name: '销量',
// 				  type: 'bar',
// 				  data: [5, 20, 36, 10, 10, 20]
// 			  }]
// 		  };

// 		  // 使用刚指定的配置项和数据显示图表。
// 		  myChart2.setOption(option2);
// 		  }
//   },
//   mounted2() {
//   	this.myEcharts2();
//   }
}
>>>>>>> 34fa00471fb686dcb4d9c0533d2152354662654f:frontend/src/components/Engineering/Target.vue
</script>

<style>

</style>

