import Vue from 'vue';
import Router from 'vue-router';
import Ping from '../components/Ping.vue';
import Composition from '../components/Composition.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/ping',
      name: 'Ping',
      component: Ping,
    },
    {
      path: '/',
      name: 'Compositions',
      component: Composition,
    },
  ],
});
