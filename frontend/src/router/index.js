import Vue from 'vue'
import Router from 'vue-router'
import Element from 'element-ui'
import "element-ui/lib/theme-chalk/index.css"

// import component
import Login from "../components/Login.vue"
import Feedback from "../components/Feedback/Feedback.vue"
import FeedbackComment from "../components/Feedback/feedbackComment.vue"
import FeedbackTarget from "../components/Feedback/FeedbackTarget.vue"
import Sale from "../components/Sale.vue"
import Manager from "../components/Manager.vue"
import Home from "../components/Home.vue"
import Engineering from "../components/Engineering/Engineering.vue"
import Brake from "../components/Engineering/Brake.vue"
import Fuel from "../components/Engineering/Fuel.vue"
import Power from "../components/Engineering/Power.vue"
import Target from "../components/Engineering/Target.vue"


Vue.use(Router)
Vue.use(Element)
Vue.use(Login)
Vue.use(Feedback)
Vue.use(Sale)
Vue.use(Home)
Vue.use(FeedbackComment)
Vue.use(FeedbackTarget)
Vue.use(Engineering)
Vue.use(Brake)
Vue.use(Fuel)
Vue.use(Power)
Vue.use(Target)


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
      component: Feedback,
      children: [
        {
          path: "FeedbackComment",
          name: "FeedbackComment",
          component: FeedbackComment
        },
        {
          path: "FeedbackTarget",
          name: "FeedbackTarget",
          component: FeedbackTarget
        }
      ]
    },
    {
      path: "/Sale",
      name: "Sale",
      component: Sale
    },
    {
      path: "/Manager",
      name: "Manager",
      component: Manager
    },
    {
      path: "/Home",
      name: "Home",
      component: Home
    },
    {
      path: "/Engineering",
      name: "Engineering",
      component: Engineering,
      children: [
        {
          path: "Brake",
          name: "Brake",
          component: Brake
        },
        {
          path: "Fuel",
          name: "Fuel",
          component:Fuel
        },
        {
          path: "Power",
          name: "Power",
          component:Power
        },
        {
          path: "Target",
          name: "Target",
          component:Target
        }
      ]
    }
  ]
})