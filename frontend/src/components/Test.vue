<template id="temp">
	<div>
    	<h1>这是第三种创建组件的方式</h1>
    </div>
</template>

<script>
import Vue from 'vue'
Vue.component('mycom3',{
  // template:"#tmp1"
  template: "#temp"
})
    
    export default{
      name: "mycom3"
    }
</script>
