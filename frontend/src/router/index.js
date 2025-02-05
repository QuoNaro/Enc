import Vue from 'vue';
import Router from 'vue-router';
import UserRegister from '../components/UserRegister.vue';
import UserLogin from '../components/UserLogin.vue';
import UserAuth from '@/components/UserAuth.vue';


Vue.use(Router);

const routes = [
  {
    path: '/register',
    name: 'UserRegister',
    component: UserRegister
  },
  {
    path: '/login',
    name: 'UserLogin',
    component: UserLogin
  },

  {
    path: '/auth',
    name: 'UserAuth',
    component: UserAuth,
    children: [
      { path: '#signin', component: UserLogin },
      { path: '#signup', component: UserRegister }
    ]
  },
];

const router = new Router({
  mode: 'history',
  routes
});

export default router;
