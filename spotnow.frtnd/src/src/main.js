import Vue from 'vue'
import App from './App.vue'
import BootstrapVue from 'bootstrap-vue'
import Vuex from 'vuex'
import router from './router'
import axios from 'axios'
import VueAxios from 'vue-axios'
import * as VueGoogleMaps from "vue2-google-maps";

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import vuetify from './plugins/vuetify';

Vue.prototype.$http = axios;
Vue.config.productionTip = false

Vue.use(BootstrapVue)
Vue.use(VueAxios, axios)
Vue.use(Vuex)

Vue.use(VueGoogleMaps, {
  load: {
    key: "AIzaSyBy7Iufw9KF1JjF0pO7rJUJqquIBm-g0qw",
    libraries: "places", // necessary for places input
  }
});

new Vue({
  router,
  axios,
  vuetify,
  // mounted: function(){
        

   render: h => h(App)
}).$mount('#app')
