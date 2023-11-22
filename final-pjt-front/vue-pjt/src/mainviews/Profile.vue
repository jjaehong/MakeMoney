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
            <div v-if="store.UserDetail.financial_products" v-for="product in store.UserDetail.financial_products" class="d-flex">Financial_products : {{ product }}</div>
            <div v-else>Financial_products : 등록된 상품이 없습니다.</div>
    </div>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import { useCounterStore } from '../stores/counter'
import { useRouter } from 'vue-router'

const router = useRouter()
const store = useCounterStore()

onMounted(() => {
    store.getUserDetail()
})

const goprofile = function(UserDetail){
    router.push({name:'updateprofile', params:{username:UserDetail.username}})
}
</script>

<style scoped>

</style>