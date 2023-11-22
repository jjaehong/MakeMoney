import { createRouter, createWebHistory } from 'vue-router'
import Home from '@/mainviews/Home.vue'
import Products from '@/mainviews/Products.vue'
import Exchange from '@/mainviews/Exchange.vue'
import Map from '@/mainviews/Map.vue'
import Profile from '@/mainviews/Profile.vue'
import Community from '@/mainviews/Community.vue'
import ProductsDetail from '@/views/ProductsDetail.vue'
import DetailView from '@/views/DetailView.vue'
import CreateView from '@/views/CreateView.vue'
import SignUpView from '@/views/SignUpView.vue'
import LogInView from '@/views/LogInView.vue'
import UpdateProfileView from '@/views/UpdateProfileView.vue'
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
      path: '/articles/:id',
      name: 'DetailView',
      component: DetailView
    },
    {
      path: '/create',
      name: 'CreateView',
      component: CreateView
    },
    {
      path: '/signup',
      name: 'SignUpView',
      component: SignUpView
    },
    {
      path: '/login',
      name: 'LogInView',
      component: LogInView
    },
    {
      path: '/updateprofile/:username',
      name: 'updateprofile',
      component: UpdateProfileView
    }
  ]
})
import { useCounterStore } from '@/stores/counter'

router.beforeEach((to, from) => {
  const store = useCounterStore()
  if ((to.name !== 'home' && to.name !=='LogInView' && to.name !== 'SignUpView')  && !store.isLogin) {
    window.alert('로그인이 필요합니다.')
    return { name: 'LogInView' }
  }
  if ((to.name === 'SignUpView' || to.name === 'LogInView') && (store.isLogin)) {
    window.alert('이미 로그인 했습니다.')
    return { name: 'home' }
  }
})
export default router
