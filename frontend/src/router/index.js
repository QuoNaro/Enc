import Vue from 'vue';
import Router from 'vue-router';
import UserAuth from '@/components/UserAuth.vue';


Vue.use(Router);

const routes = [
  {
    path: '/auth',
    name: 'UserAuth',
    component: UserAuth,
    children: [
      { path: '#signin'},
      { path: '#signup'}
    ]
  },
];

const router = new Router({
  mode: 'history',
  routes
});

export default router;
