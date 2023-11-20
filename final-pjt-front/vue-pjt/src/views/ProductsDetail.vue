<template>
    <div v-for="test in info"> 
        <div>공시 제출월 {{ test.dcls_month }}</div>
        <div>금융 회사명 {{ test.kor_co_nm }}</div>
        <div>상품명 {{ test.fin_prdt_nm }}</div>
        <div>가입제한 {{ test.join_deny }}</div>
        <div>가입 방법 {{ test.join_way }}</div>
        <div>우대조건 {{ test.spcl_cnd }}</div>
        
</div>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import { useCounterStore } from '../stores/counter'
import { useRoute } from 'vue-router'
const store = useCounterStore()
const route = useRoute()
const info = store.total.filter((element) => element.fin_prdt_cd == route.params.cd)
onMounted(() => { 
    store.getdeposit()
 })
</script>

<style scoped>

</style>