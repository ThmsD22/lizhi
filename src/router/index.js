import {createRouter, createWebHistory, createWebHashHistory} from 'vue-router'
import LycheeVarieties from '../views/LycheeVarieties.vue'
import LycheeDetail from '../views/LycheeDetail.vue'

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    server: '127.0.0.1',
    routes: [
        {
            path: '/',
            name: 'home',
            // lazy loading: () => import()
            component: () => import('../views/home/index.vue'),
        },
        {
            path: '/login',
            name: 'login',
            component: () => import('../views/login/index.vue'),
        },
        {
            path: '/register',
            name: 'register',
            component: () => import('../views/register/index.vue')
        },
        {
            path: '/store',
            name: 'store',
            component: () => import('../views/store/index.vue')
        },
        {
            path: '/cart',
            name: 'cart',
            component: () => import('../views/cart/index.vue')
        },{
            path: '/xiangqing',
            name: 'xiangqing',
            component: () => import('../views/xiangqing/index.vue')
        },
        {
            path: '/lychee-varieties',
            name: 'LycheeVarieties',
            component: LycheeVarieties
        },
        {
            path: '/lychee-varieties/:id',
            name: 'LycheeDetail',
            component: LycheeDetail,
            props: true
        }
    ],
})

export default router
