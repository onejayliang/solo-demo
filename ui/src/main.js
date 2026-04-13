import { createPinia } from 'pinia';
import { route } from 'quasar/wrappers';
import { createRouter, createMemoryHistory, createWebHistory, createWebHashHistory } from 'vue-router';
import { createApp } from 'vue';
import { Quasar, Notify, Dialog, Loading } from 'quasar';
import quasarLang from 'quasar/lang/zh-CN';

import '@quasar/extras/material-icons/material-icons.css';
import '@quasar/extras/mdi-v7/mdi-v7.css';
import 'quasar/src/css/index.sass';

import App from './App.vue';
import routes from './router';

const myApp = createApp(App);

const createHistory = process.env.SERVER
  ? createMemoryHistory
  : (process.env.VUE_ROUTER_MODE === 'history' ? createWebHistory : createWebHashHistory);

const router = createRouter({
  scrollBehavior: () => ({ left: 0, top: 0 }),
  routes,
  history: createHistory(process.env.VUE_ROUTER_BASE)
});

myApp.use(Quasar, {
  plugins: {
    Notify,
    Dialog,
    Loading
  },
  lang: quasarLang
});

myApp.use(createPinia());
myApp.use(router);

myApp.mount('#q-app');
