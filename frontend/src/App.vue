<template>
<div style="height: 100%">
  <router-link to="/feedback">feedback page</router-link>
  <router-link to="/login">login page</router-link>
  <router-link to="/sale">Sale</router-link>
  <router-link to="/home">Home</router-link>
  <router-link to="/manager">Manager</router-link>
  <router-link to="/engineering">Engineering</router-link>
  <router-link to="/test">Test</router-link>
  <router-view></router-view>
</div> 

</template>

<script>
export default {
  name: "App"
};
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
#app {
  margin: 0;
  padding: 0;
}
</style>
