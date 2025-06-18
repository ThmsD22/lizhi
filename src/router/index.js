import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('../views/Home.vue'),
    meta: { title: '首页' }
  },
  {
    path: '/varieties',
    name: 'Varieties',
    component: () => import('../views/Varieties.vue'),
    meta: { title: '品种文化' }
  },
  {
    path: '/map',
    name: 'Map',
    component: () => import('../views/Map.vue'),
    meta: { title: '产区地图' }
  },
  {
    path: '/media',
    name: 'Media',
    component: () => import('../views/Media.vue'),
    meta: { title: '视频图文' }
  },
  {
    path: '/brands',
    name: 'Brands',
    component: () => import('../views/Brands.vue'),
    meta: { title: '品牌农户' }
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router 