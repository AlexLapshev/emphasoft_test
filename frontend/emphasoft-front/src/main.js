import Vue from 'vue'

import Axios from "axios";
import LoadScript from 'vue-plugin-load-script';
import Vuesax from 'vuesax'
import UploadImage from 'vue-upload-image';


import App from './App.vue'
import router from "./router/router";
import store from './store'


import 'vuesax/dist/vuesax.css' //Vuesax styles



Vue.config.productionTip = false
Vue.prototype.$axios = Axios.create({baseURL: process.env.VUE_APP_BASE_URL})
Vue.use(LoadScript)
Vue.use(Vuesax)
Vue.component('upload-image', UploadImage)

new Vue({
  store,
  router,
  render: h => h(App)
}).$mount('#app')
