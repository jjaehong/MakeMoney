import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useCounterStore = defineStore('counter', () => {
  const deposit = ref([])
  const bank = ref(['전체'])
  const total = ref([])
  const savings = ref([])
  const country = ref([])
  const exchange = ref([])
  const cost = ref('')
  // const period = ref('')
  const API_URL = 'http://127.0.0.1:8000'

  const getdeposit = function () {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/products/product-list/`
    })
    .then(res => {
      total.value = res.data
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

  return { deposit, API_URL, getdeposit, bank, savings, total, getexchange, country, exchange }
})
