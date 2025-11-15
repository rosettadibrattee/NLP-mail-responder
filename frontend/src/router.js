import { createRouter, createWebHistory } from 'vue-router'
import Home from './Home.vue'
import Settings from './Settings.vue'

const routes = [
  { path: '/', component: Home },
  { path: '/settings', component: Settings }
]

export default createRouter({
  history: createWebHistory(),
  routes
})
