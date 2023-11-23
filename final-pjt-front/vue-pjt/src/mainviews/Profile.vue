<template>
    <div>
        <h1>프로필</h1>
        <button class="btn btn-primary" @click="goprofile(store.UserDetail)">프로필 수정</button>
        <div>ID : {{ store.UserDetail.username }}</div>
        <div class="d-flex">
            <div v-if="store.UserDetail.nickname">NICKNAME : {{ store.UserDetail.nickname }}</div>
            <div v-else>NICKNAME : 값을 넣어주세요.</div>

        </div>
        <div class="d-flex">
            <div v-if="store.UserDetail.email">EMAIL: {{ store.UserDetail.email }}</div>
            <div v-else>EMAIL : 값을 넣어주세요.</div>

        </div>
        <div class="d-flex">
            <div v-if="store.UserDetail.age">AGE : {{ store.UserDetail.age }}</div>
            <div v-else>AGE : 값을 넣어주세요.</div>

        </div>
        <div class="d-flex">
            <div v-if="store.UserDetail.money">MONEY : {{ store.UserDetail.money }}</div>
            <div v-else>MONEY : 값을 넣어주세요.</div>

        </div>
        <div class="d-flex">
            <div v-if="store.UserDetail.salary">SALARY : {{ store.UserDetail.salary }}</div>
            <div v-else>SALARY : 값을 넣어주세요.</div>

        </div>
        <div class="d-flex">
            <div v-if="store.UserDetail.loan_money">LOAN_MONEY : {{ store.UserDetail.loan_money }}</div>
            <div v-else>LOAN_MONEY : 값을 넣어주세요.</div>
    
        </div>
            <div v-if="store.data" v-for="product in store.total">
                <div v-if="store.data_str.includes(product.fin_prdt_cd)">
                    Financial_products
                    <div>공시 제출월 {{ product.dcls_month }}</div>
                    <div>금융 회사명 {{ product.kor_co_nm }}</div>
                    <div>상품명 {{ product.fin_prdt_nm }}</div>
                    <div>가입제한 {{ product.join_deny }}</div>
                    <div>가입 방법 {{ product.join_way }}</div>
                    <div>우대조건 {{ product.spcl_cnd }}</div>
                    <button @click="del(product.fin_prdt_cd)" class="btn btn-primary">상품 삭제</button>
                </div>
            </div>
            <div v-else>Financial_products : 저장된 금융 상품이 없습니다.</div>
        </div>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import { useCounterStore } from '../stores/counter'
import { useRouter } from 'vue-router'
import axios from 'axios'
const router = useRouter()
const store = useCounterStore()

const API_URL = 'http://127.0.0.1:8000'
onMounted(() => {
    store.getUserDetail()
    store.getdeposit()
})

const goprofile = function(UserDetail){
    router.push({name:'updateprofile', params:{username:UserDetail.username}})
}

const del = function(object){

    store.data_str = store.data_str.filter((element) => element != object)
    store.data = store.data_str.join(',')
    axios({
        method: 'post',
        url: `${API_URL}/accounts/update/${store.UserDetail.id}/`,
        data: {
            financial_products:store.data
        }
    })
    .then((res) => {
        console.log(res.data)
    })
    .catch((err) => {
        console.log(err)
    })
}
</script>

<style scoped>

</style>