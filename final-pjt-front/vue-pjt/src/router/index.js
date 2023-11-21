import { createRouter, createWebHistory } from 'vue-router'
import Home from '@/mainviews/Home.vue'
import Products from '@/mainviews/Products.vue'
import Exchange from '@/mainviews/Exchange.vue'
import Map from '@/mainviews/Map.vue'
import Profile from '@/mainviews/Profile.vue'
import Community from '@/mainviews/Community.vue'
import ProductsDetail from '@/views/ProductsDetail.vue'
import test from '@/mainviews/test.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home,
    },
    {
      path: '/products',
      name: 'products',
      component: Products,
    },
    {
      path: '/exchange',
      name: 'exchange',
      component: Exchange,
    },
    {
      path: '/map',
      name: 'map',
      component: Map,
    },
    {
      path: '/community',
      name: 'community',
      component: Community,
    },
    {
      path: '/profile',
      name: 'profile',
      component: Profile,
    },
    {
      path: '/products/:cd',
      name: 'productsdetail',
      component: ProductsDetail
    },
    {
      path: '/test',
      name: 'test',
      component: test
    },

  ]
})

export default router
