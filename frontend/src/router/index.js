import Vue from 'vue'
import Router from 'vue-router'
import Element from 'element-ui'
import "element-ui/lib/theme-chalk/index.css"

// import component
import Login from "../views/Login.vue"
import Feedback from "../views/Feedback/Feedback.vue"
import FeedbackComment from "../views/Feedback/components/feedbackComment.vue"
import FeedbackTarget from "../views/Feedback/components/FeedbackTarget.vue"
//更改ZHJ
import Sale from "../views/Sale/Sale.vue"
import SaleNumber from "../views/Sale/components/SaleNumber.vue"
import SalePrice from "../views/Sale/components/SalePrice.vue"
import SaleTime from "../views/Sale/components/SaleTime.vue"
import SalePlace from "../views/Sale/components/SalePlace.vue"
//
//import Sale from "../views/Sale.vue"
import Manager from "../views/Manager.vue"
import Home from "../views/Home/Home.vue"
import SaleMap from '../views/Home/components/SellMap.vue'

import Engineering from "../views/Engineering/Engineering.vue"
import Brake from "../views/Engineering/components/Brake.vue"
import Fuel from "../views/Engineering/components/Fuel.vue"
import Power from "../views/Engineering/components/Power.vue"
import Target from "../views/Engineering/components/Target.vue"
import Test from "../views/Test.vue"

//component
// import mycom3 from '../views/Test.vue';

// Vue.use(mycom3)



Vue.use(Router)
Vue.use(Element)
Vue.use(Login)
Vue.use(Feedback)
Vue.use(Sale)
//ZHJ
Vue.use(SaleNumber)
Vue.use(SaleTime)
Vue.use(SalePrice)
Vue.use(SalePlace)

//
Vue.use(Home)
Vue.use(SaleMap)
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
      path: "/",
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
      component: Sale,
      //ZHJ
     children:[
        {
          path:"SaleTime",
          name:"SaleTime",
         component:SaleTime,
        } ,
        {
          path:"SalePrice",
          name:"SalePrice",
         component:SalePrice,
        },
        {
          path:"SaleNumber",
          name:"SaleNumber",
         component:SaleNumber,
        }
        ,
        {
          path:"SalePlace",
          name:"SalePlace",
         component: SalePlace,
        }
      ]
      //
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
          path:"SaleMap",
          name:"SaleMap",
          component: SaleMap
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
  ],
  components: {
    // mycom3
    SaleMap
  }
})