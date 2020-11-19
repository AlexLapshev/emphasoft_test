import Vue from 'vue'
import VueRouter from 'vue-router'

import Home from "../components/routes/Login";
import Registration from "../components/routes/Registration";
import UserPage from "../components/routes/UserPage";

Vue.use(VueRouter)

const routes = [
  {
    path:'/login',
    name:'Home',
    component: Home
  },
  {
    path:'/registration',
    name:'Registration',
    component: Registration
  },
  {
    path:'',
    name:'UserPage',
    component: UserPage
  }
]

const router = new VueRouter({
  routes,
  mode: 'history',
})

export default router