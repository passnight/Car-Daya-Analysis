import Vue from 'vue'
import Router from 'vue-router'
import Element from 'element-ui'
import "element-ui/lib/theme-chalk/index.css"

// import component
import Content from "../components/content.vue"
import Main from '../components/Main.vue'
import Shit from "../components/Shit.vue"
import Login from "../components/Login.vue"


Vue.use(Router)
Vue.use(Element)
Vue.use(Login)

export default new Router({
  routes: [
    {
      path: '/content',
      name: 'content',
      component: Content
    },
    {
      path: '/Main',
      name: 'Main',
      component: Main
    },
    {
      path: "/Shit",
      name: "Shit",
      component: Shit
    },
    {
      path: "/Login",
      name: "Login",
      component: Login
    }
  ]
})
