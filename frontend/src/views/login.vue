<template>
  <body id="poster">
    <h2 class="login-header" style="text-align: center; color: #ffffff">
      汽车大数据分析系统
    </h2>
    <el-form class="login-container" label-position="left" label-width="10px">
      <h2 class="login_title">登录</h2>
      <el-form-item>
        <el-input type="text" placeholder="账号" v-model="username"></el-input>
      </el-form-item>
      <el-form-item>
        <el-input
          type="password"
          placeholder="密码"
          v-model="password"
        ></el-input>
      </el-form-item>
      <el-form-item style="width: 100%">
        <el-button
          type="primary"
          style="width: 100%; background: #bae2f8; border: none"
          v-on:click="login"
          >登录</el-button
        >
      </el-form-item>
    </el-form>
    <el-footer class="login-footer" style="height: 30px">
      <h3 class="login_copyright">版权所有</h3>
    </el-footer>
  </body>
</template>

<script>
import axios from "axios";
export default {
  name: "Login",
  methods: {
    login: function () {
      var data = new FormData();
      data.append("username", this.username);
      data.append("password", this.password);
      axios.post("http://127.0.0.1:5000/user.json", data).then((response) => {
        console.log(response.data);
        let result = response.data;
        if (result==="success") {
          alert("login succeed");
          this.$router.push("/home");
        } else {
          alert("you stupid");
        }
      });
    },
  },
  data() {
    return{
      username: "rjx",
      password: "123456"
    }
  }
};
</script>
<style scoped>
#poster {
  background: url("../assets/img/02.jpeg") no-repeat;
  background-position: center;
  height: 100%;
  width: 100%;
  background-size: cover;
  position: fixed;
}
body {
  margin: 0px;
}
.login-container {
  border-radius: 15px;
  background-clip: padding-box;
  margin: 90px auto;
  width: 350px;
  padding: 35px 35px 15px 35px;
  background: Transparent;
  border: 1px solid #eaeaea;
  box-shadow: 0 0 25px #cac6c6;
}
.login_title {
  margin: 0px auto 30px auto;
  text-align: center;
  color: #ffffff;
}
.login_copyright {
  text-align: center;
  color: #def7fc;
}
</style>