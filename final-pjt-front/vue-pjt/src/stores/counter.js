import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'
import axios from 'axios'

export const useCounterStore = defineStore('counter', () => {
  const router = useRouter()
  const articles = ref([])
  const comments = ref([])
  const token = ref(null)
  const deposit = ref([])
  const bank = ref(['전체'])
  const total = ref([])
  const savings = ref([])
  const country = ref([])
  const exchange = ref([])
  const UserDetail = ref([])
  const getuser = ref([])
  // const cost = ref('')
  // const period = ref('')
  const isLogin = computed(() => {
    if (token.value === null) {
      return false
    } else {
      return true
    }
  })
  const API_URL = 'http://127.0.0.1:8000'

  const getdeposit = function () {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/products/product-list/`
    })
    .then(res => {
      total.value = res.data
      if(deposit.value.length == 0){
      res.data.forEach((element) => {
        if (!bank.value.includes(element.kor_co_nm)){
          bank.value.push(element.kor_co_nm)
        }
        if (element.fin_prdt_nm.includes('예금')){
          deposit.value.push(element)
        }
        else{
          savings.value.push(element)
        }
      })
    }
    })
  
    .catch(err => console.log(err))
  }

  const getexchange = function(){
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/exchanges/`
    })
    .then(res => {
      exchange.value = res.data
      res.data.forEach((element) =>{
      country.value.push(element.cur_nm)
    })
    })
    .catch(err => console.log(err))
  }

  // DRF에 article 조회 요청을 보내는 action
  const getArticles = function () {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/articles/`,
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
      .then((res) =>{
        // console.log(res)
        articles.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const getComments = function () {
    axios({
      method:'get',
      url:`${API_URL}/api/v1/articles/comments/`,
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
      .then((res) => {
        console.log(res)
        comments.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const signUp = function (payload) {
    const { username, password1, password2 } = payload

    axios({
      method: 'post',
      url: `${API_URL}/accounts/signup/`,
      data: {
        username, password1, password2
      }
    })
      .then((res) => {
        console.log(res)
        const password = password1
        logIn({ username, password })
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const logIn = function (payload) {
    const { username, password } = payload

    axios({
      method: 'post',
      url: `${API_URL}/accounts/login/`,
      data: {
        username, password
      }
    })
      .then((res) => {
        console.log(res.data)
        token.value = res.data.key
        router.push({ name: 'home' })
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const logOut = function () {
    axios({
      method: 'post',
      url: `${API_URL}/accounts/logout/`,
    })
      .then((res) => {
        token.value = null
        router.push({ name: 'home' })
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const getUserDetail = function() {
    axios({
      method: 'get',
      url: `${API_URL}/accounts/user/`, 
      headers: {
        Authorization: `Token ${token.value}`
      } 
    })
    .then((res) =>{
      UserDetail.value = res.data
    })
    .catch((err) => {
      console.log(err)
    })

  }


  return { deposit, API_URL, getdeposit, bank, savings, total, getexchange, country, exchange, 
    articles, getArticles, signUp, logIn, token, isLogin, logOut, getUserDetail, UserDetail, getComments, comments }
}, { persist: true})
