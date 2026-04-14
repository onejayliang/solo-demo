import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    component: () => import('../pages/IndexPage.vue')
  },
  {
    path: '/xungen',
    component: () => import('../pages/XunGenPage.vue')
  },
  {
    path: '/zupu',
    component: () => import('../pages/ZuPuPage.vue')
  },
  {
    path: '/zongqin',
    component: () => import('../pages/ZongQinPage.vue')
  },
  {
    path: '/profile',
    component: () => import('../pages/ProfilePage.vue')
  },
  {
    path: '/login',
    component: () => import('../pages/LoginPage.vue')
  },
  {
    path: '/:pathMatch(.*)*',
    component: () => import('../pages/ErrorNotFound.vue')
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router