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
            <div v-if="store.UserDetail.loan">LOAN : {{ store.UserDetail.loan }}</div>
            <div v-else>loan : 값을 넣어주세요.</div>
    
        </div>
            <div v-for="product in store.total">
                <div v-if="data_str.includes(product.fin_prdt_cd)">
                    Financial_products
                    <div>공시 제출월 {{ product.dcls_month }}</div>
                    <div>금융 회사명 {{ product.kor_co_nm }}</div>
                    <div>상품명 {{ product.fin_prdt_nm }}</div>
                    <div>가입제한 {{ product.join_deny }}</div>
                    <div>가입 방법 {{ product.join_way }}</div>
                    <div>우대조건 {{ product.spcl_cnd }}</div>
                    <button @click="del(product)" class="btn btn-primary">상품 삭제</button>
                </div>
            </div>
        </div>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import { useCounterStore } from '../stores/counter'
import { useRouter } from 'vue-router'
import axios from 'axios'

const router = useRouter()
const store = useCounterStore()
const data_str = ref([])
onMounted(() => {
    store.getUserDetail()
    store.getdeposit()
    console.log(store.UserDetail.financial_products)
    console.log(store.UserDetail.financial_products.split(','))

    data_str.value = store.UserDetail.financial_products.split(',')

    console.log(data_str.value)
})

const goprofile = function(UserDetail){
    router.push({name:'updateprofile', params:{username:UserDetail.username}})
}

const del = function(object){
    const financialProducts = store.UserDetail.financial_products || []

    const index = financialProducts.indexOf(object);

    if (index !== -1) {
        financialProducts.splice(index, 1);
    }
    console.log(store.UserDetail.financial_products)
}
</script>

<style scoped>

</style>