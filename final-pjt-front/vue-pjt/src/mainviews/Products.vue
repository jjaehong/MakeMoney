<template>
    <h1>금융 상품 이력</h1>
    <div class="container">
        <div class="row">

            <div class="col-3 gx-5">
                <form @submit.prevent="check">
                    <select name="bank">
                        <option v-for="bank in store.bank" name="bank" :value=bank>{{ bank }}</option>
                    </select>
                    <button>확인</button>
                </form>
            </div>
            <div class="col" style="margin-left: 5px;">
                <button @click="dep">정기예금</button>
                <button @click="sav">정기적금</button>
                <div v-if="bank_name=='전체' && select==true" v-for="deposit in store.deposit" style="display: block;">
                    <div @click="goDetail(deposit)">{{ deposit.dcls_month }}  {{ deposit.kor_co_nm }}  {{ deposit.fin_prdt_nm }}</div>
                </div>
                <div v-if="bank_name=='전체' && select==false" v-for="savings in store.savings" style="display: block;">
                    <div @click="goDetail(savings)">{{ savings.dcls_month }}  {{ savings.kor_co_nm }}  {{ savings.fin_prdt_nm }}</div>
                </div>
                <div v-if="bank_name!='전체' && select==true" v-for="deposit in store.deposit">
                    <div v-if="deposit.kor_co_nm==bank_name" @click="goDetail(deposit)">{{ deposit.dcls_month }}  {{ deposit.kor_co_nm }}  {{ deposit.fin_prdt_nm }}</div>
                </div>
                <div v-if="bank_name!='전체' && select==false" v-for="savings in store.savings">
                    <div v-if="savings.kor_co_nm==bank_name" @click="goDetail(savings)">{{ savings.dcls_month }}  {{ savings.kor_co_nm }}  {{ savings.fin_prdt_nm }}</div>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import { useCounterStore } from '../stores/counter'
import { useRouter } from 'vue-router'
const bank_name = ref('전체')
const store = useCounterStore()
const select = ref(false)
const router = useRouter()

onMounted(() => { 
    store.getdeposit()
 })
const dep = function() {
    select.value = true
}

const sav = function(){
    select.value = false
}
const check = function(event){
    bank_name.value = event.target[0].value
}

const goDetail = function(target){
    router.push({name:'productsdetail', params:{cd:target.fin_prdt_cd}})
}
</script>

<style scoped>

</style>