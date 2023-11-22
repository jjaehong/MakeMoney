<template>
    <h1>금융 상품 이력</h1>
    <div class="container">
        <div class="row">
            <div class="col-3 gx-5">
                <form @submit.prevent="check">
                    <select name="bank">
                        <option v-for="bank in store.bank" name="bank" :value=bank>{{ bank }}</option>
                    </select>
                    <hr>
                    <select name="days">
                        <option v-for="day in days" :value=day name="days">{{ day }}</option>
                    </select>
                    <button>확인</button>
                </form>
            </div>
            <div class="col" style="margin-left: 5px;">
                <button @click="dep">정기예금</button>
                <button @click="sav">정기적금</button>
                <div v-if="bank_name=='전체' && select==true" v-for="deposit in store.deposit" style="display: block;">
                    <div @click="goDetail(deposit)">{{ deposit.dcls_month }}  {{ deposit.kor_co_nm }}  {{ deposit.fin_prdt_nm }} {{ deposit.month6 }} {{ deposit.month12 }} {{ deposit.month24 }} {{ deposit.month36 }}</div>
                    <button class="btn btn-primary" @click="save(deposit)" v-if="!data_str.includes(deposit.fin_prdt_cd)">저장</button>
                    <button class="btn btn-primary" @click="del(deposit)" v-else>삭제</button>
                </div>
                <div v-if="bank_name=='전체' && select==false" v-for="savings in store.savings" style="display: block;">
                    <div @click="goDetail(savings)">{{ savings.dcls_month }}  {{ savings.kor_co_nm }}  {{ savings.fin_prdt_nm }} {{ savings.month6 }} {{ savings.month12 }} {{ savings.month24 }} {{ savings.month36 }}</div>
                    <button class="btn btn-primary" @click="save(savings)" v-if="!data_str.includes(savings.fin_prdt_cd)">저장</button>
                    <button class="btn btn-primary" @click="del(savings)" v-else>삭제</button>

                </div>
                <div v-if="bank_name!='전체' && select==true" v-for="deposit in store.deposit">
                    <div v-if="deposit.kor_co_nm==bank_name" @click="goDetail(deposit)">{{ deposit.dcls_month }}  {{ deposit.kor_co_nm }}  {{ deposit.fin_prdt_nm }} 
                        <div v-if="day==6">{{ deposit.month6 }}</div>
                        <div v-if="day==12">{{ deposit.month6 }} {{ deposit.month12 }}</div>
                        <div v-if="day==24">{{ deposit.month6 }} {{ deposit.month12 }} {{ deposit.month24 }}</div>
                        <div v-if="day==36">{{ deposit.month6 }} {{ deposit.month12 }} {{ deposit.month24 }} {{ deposit.month36 }}</div>
                        <button class="btn btn-primary" @click="save(deposit)" v-if="!data_str.includes(deposit.fin_prdt_cd)">저장</button>
                        <button class="btn btn-primary" @click="del(deposit)" v-else>삭제</button>
                    </div>
                </div>
                <div v-if="bank_name!='전체' && select==false" v-for="savings in store.savings">
                    <div v-if="savings.kor_co_nm==bank_name" @click="goDetail(savings)">{{ savings.dcls_month }}  {{ savings.kor_co_nm }}  {{ savings.fin_prdt_nm }}
                        <div v-if="day==6">{{ savings.month6 }}</div>
                        <div v-if="day==12">{{ savings.month6 }} {{ savings.month12 }}</div>
                        <div v-if="day==24">{{ savings.month6 }} {{ savings.month12 }} {{ savings.month24 }}</div>
                        <div v-if="day==36">{{ savings.month6 }} {{ savings.month12 }} {{ savings.month24 }} {{ savings.month36 }}</div>
                        <button class="btn btn-primary" @click="save(savings)" v-if="!data_str.includes(savings.fin_prdt_cd)">저장</button>
                    <button class="btn btn-primary" @click="del(savings)" v-else>삭제</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import { useCounterStore } from '../stores/counter'
import { useRouter } from 'vue-router'
import axios from 'axios'
const bank_name = ref('전체')
const store = useCounterStore()
const select = ref(false)
const router = useRouter()
const days = ref(['전체', 6, 12, 24, 36])
const day = ref('')
const data = ref([])
const data_str = ref([])
const API_URL = 'http://127.0.0.1:8000'
onMounted(() => { 
    store.getdeposit()
    store.getUserDetail()
    store.deposit.forEach((element) =>{
        axios({
            method: 'get',
            url: `${API_URL}/api/v1/products/product-options/${element.fin_prdt_cd}/`
        })
        .then(res => {
            for(let i of res.data){
            element['month'+i.save_trm] = i.intr_rate
            }
        })
        .catch((err) => console.log(err))
    })
    store.savings.forEach((element) => {
        axios({
            method: 'get',
            url: `${API_URL}/api/v1/products/product-options/${element.fin_prdt_cd}/`
        })
        .then(res => {
            for(let i of res.data){
                element['month'+i.save_trm] = i.intr_rate
            }
        })
        .catch((err) => console.log(err))
    })
    data.value = store.UserDetail.financial_products
    data_str.value = data.value.split(',')
 })
const dep = function() {
    select.value = true
}

const sav = function(){
    select.value = false
}
const check = function(event){
    bank_name.value = event.target[0].value
    day.value = event.target[1].value
}

const goDetail = function(target){
    router.push({name:'productsdetail', params:{cd:target.fin_prdt_cd}})
}

const save = function(object) {
    data.value += object.fin_prdt_cd+','
    data_str.value = data.value.split(',') 
    axios({
        method: 'post',
        url: `${API_URL}/accounts/update/${store.UserDetail.id}/`,
        data: {
            financial_products:data.value
        }
    })
    .then((res) => {
        console.log(res.data)
    })
    .catch((err) => {
        console.log(err)
    })
    console.log(data_str.value)
}


const del = function(object){
    data_str.value = data_str.value.filter((element) => element != object.fin_prdt_cd)
    data.value = data_str.value.join(',')
    
    axios({
        method: 'post',
        url: `${API_URL}/accounts/update/${store.UserDetail.id}/`,
        data: {
            financial_products:data.value
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