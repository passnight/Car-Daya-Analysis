import Vue from 'vue'
import Router from 'vue-router'
import Element from 'element-ui'
import "element-ui/lib/theme-chalk/index.css"

// import component
import Login from "../components/Login.vue"
import Feedback from "../components/Feedback.vue"


Vue.use(Router)
Vue.use(Element)
Vue.use(Login)
Vue.use(Feedback)

export default new Router({
  routes: [
    {
      path: "/Login",
      name: "Login",
      component: Login
    },
    {
      path: "/Feedback",
      name: "Feedback",
      component: Feedback
    }
  ]
})
