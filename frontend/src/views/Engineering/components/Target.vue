<template>
<div class="tchart">
	<div class="t1">
		<t-chart-1 class="tchart1"/>
		<t-chart-2 class="tchart2"/>
		<t-chart-3 class="tchart3"/>
	</div>
	<div class="t2">
		<t-chart-4 class="tchart4"/>
		<t-chart-5 class="tchart5"/>
		<t-chart-6 class="tchart6"/>
	</div>
	<div class="t3">
		<t-chart-7 class="tchart7"/>
	</div>
</div>
</template>

<script>
import TChart1 from './TargetChart/TChart1'
import TChart2 from './TargetChart/TChart2'
import TChart3 from './TargetChart/TChart3'
import TChart4 from './TargetChart/TChart4'
import TChart5 from './TargetChart/TChart5'
import TChart6 from './TargetChart/TChart6'
import TChart7 from './TargetChart/TChart7'
export default {
	name: 'Target',
  components: {
    TChart1,
	TChart2,
    TChart3,
	TChart4,
	TChart5,
	TChart6,
	TChart7
  }
}
</script>

<style>
.t1{
	float: left;
	width: 270px;
}
.t2{
	float: left;
	width: 270px;
}
.t3{
	float: right;
	width: 600px;
}
</style>

