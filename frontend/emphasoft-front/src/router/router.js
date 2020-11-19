import Vue from 'vue'
import VueRouter from 'vue-router'

import Home from "../components/routes/Home";
import Registration from "../components/routes/Registration";
import UserPage from "../components/routes/UserPage";

Vue.use(VueRouter)

const routes = [
  {
    path:'',
    name:'Home',
    component: Home
  },
  {
    path:'/registration',
    name:'Registration',
    component: Registration
  },
  {
    path:'/user',
    name:'UserPage',
    component: UserPage
  }
]

const router = new VueRouter({
  routes,
  mode: 'history',
})

export default router