import { createRouter, createWebHistory, type RouteRecordRaw } from 'vue-router'
import Home from './Home.vue'
import Settings from './Settings.vue'

const routes: RouteRecordRaw[] = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  
  {
    path: '/settings',
    name: 'Settings',
    component: Settings
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
