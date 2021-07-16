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
import Home from "../components/Home/Home.vue"
import HotSale from "../components/Home/HotSale.vue"
import SuggestProduction from "../components/Home/SuggestProduction.vue"
import Engineering from "../components/Engineering/Engineering.vue"
import Brake from "../components/Engineering/Brake.vue"
import Fuel from "../components/Engineering/Fuel.vue"
import Power from "../components/Engineering/Power.vue"
import Target from "../components/Engineering/Target.vue"
import Test from "../components/Test.vue"


Vue.use(Router)
Vue.use(Element)
Vue.use(Login)
Vue.use(Feedback)
Vue.use(Sale)
Vue.use(Home)
Vue.use(HotSale)
Vue.use(SuggestProduction)
Vue.use(FeedbackComment)
Vue.use(FeedbackTarget)
Vue.use(Engineering)
Vue.use(Brake)
Vue.use(Fuel)
Vue.use(Power)
Vue.use(Target)
Vue.use(Test)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: "/login",
      name: "Login",
      component: Login
    },
    {
      path: "/feedback",
      name: "Feedback",
      component: Feedback,
      children: [
        {
          path: "feedbackComment",
          name: "FeedbackComment",
          component: FeedbackComment
        },
        {
          path: "feedbackTarget",
          name: "FeedbackTarget",
          component: FeedbackTarget
        }
      ]
    },
    {
      path: "/sale",
      name: "Sale",
      component: Sale
    },
    {
      path: "/manager",
      name: "Manager",
      component: Manager
    },
    {
      path: "/home",
      name: "Home",
      component: Home,
      children: [
        {
          path: "HotSale",
          name: "HotSale",
          component: HotSale
        },
        {
          path: "SuggestProduction",
          name: "SuggestProduction",
          component: SuggestProduction
        }
      ]
    },
    {
      path: "/engineering",
      name: "Engineering",
      component: Engineering,
      children: [
        {
          path: "brake",
          name: "Brake",
          component: Brake
        },
        {
          path: "fuel",
          name: "Fuel",
          component:Fuel
        },
        {
          path: "power",
          name: "Power",
          component:Power
        },
        {
          path: "target",
          name: "Target",
          component:Target
        }
      ]
    },
    {
      path: "/Test",
      name: "Test",
      component: Test
    }
  ]
})