<template>
    <div>
        <h1>환율 계산기</h1>
        <div class="text-center" style="width: 80%;">
        <div class="input-group">
        <span class="currency1">
            <select name="country" v-model="country1" @change="ec" id="currency-one" class="form-select input-group-prepend">
                <option v-for="country in store.country" name="country" :value=country>{{ country }}</option>
            </select>
        </span>
            <input type="text" v-model=exchange1 @input="ec" id="amount-one" class="form-control">
        </div>
        <div class="input-group">
        <span class="currency2">
            <select name="country" v-model="country2" @change="ec" id="currency-two" class="form-select input-group-prepend">
                <option v-for="country in store.country" name="country" :value=country>{{ country }}</option>
            </select>
        </span>
            <input type="text" v-model=exchange2 @input="ec" id="amount-two" class="form-control">
        </div>
        <div>*엔화, 인도네시아 루피아는 100 단위, 나머지는 모두 1단위</div>

    </div>
</div>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import { useCounterStore } from '../stores/counter'
const store = useCounterStore()
const country1 = ref('한국 원')
const country2 = ref('한국 원')
const exchange1 = ref(1)
const exchange2 = ref(1)
const ex = ref(false)
onMounted(() => { 
    store.getexchange()
})

const ec = function(){
    if(ex.value==false){
        store.exchange.filter((element) => element.cur_nm =='일본 옌')[0].deal_bas_r /= 100
        store.exchange.filter((element) => element.cur_nm =='인도네시아 루피아')[0].deal_bas_r /= 100
        store.exchange.filter((element) => element.cur_nm =='일본 옌')[0].deal_bas_r = store.exchange.filter((element) => element.cur_nm =='일본 옌')[0].deal_bas_r.toString()
        store.exchange.filter((element) => element.cur_nm =='인도네시아 루피아')[0].deal_bas_r = store.exchange.filter((element) => element.cur_nm =='인도네시아 루피아')[0].deal_bas_r.toString()
        ex.value = true
    }
    exchange2.value = parseFloat((exchange1.value * store.exchange.filter((element) => element.cur_nm==country1.value)[0].deal_bas_r.replace(',', '') / store.exchange.filter((element) => element.cur_nm==country2.value)[0].deal_bas_r.replace(',', '')).toFixed(3))
}


</script>

<style scoped>
</style>