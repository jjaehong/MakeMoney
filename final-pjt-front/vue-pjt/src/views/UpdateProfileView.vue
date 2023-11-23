<template>
    <div>
        <div>{{ store.UserDetail.username }}님의 프로필 수정 페이지</div>
        <form @submit.prevent="updateprofile(store.UserDetail)">
            <div class="row" style="width: 500px;">
                <div>
                    <label for="nickname" class="col-3">별명</label>
                    <input type="text" :placeholder=store.UserDetail.nickname class="col-9" id="nickname" v-model="nickname">
                </div>
                <div>
                    <label for="age" class="col-3">나이</label>
                    <input type="text" :placeholder=store.UserDetail.age class="col-9" id="age" v-model="age">
                </div>
                <div>
                    <label for="email" class="col-3">이메일</label>
                    <input type="text" :placeholder=store.UserDetail.email class="col-9" id="email" v-model="email">
                </div>
                <div>
                    <label for="money" class="col-3">현재자산(만원)</label>
                    <input type="text" :placeholder=store.UserDetail.money class="col-9" id="money" v-model="money">
                </div>
                <div>
                    <label for="salary" class="col-3">연봉(만원)</label>
                    <input type="text" :placeholder=store.UserDetail.salary class="col-9" id="salary" v-model="salary">
                </div>
                <div>
                    <label for="consumption" class="col-3">연소비(만원)</label>
                    <input type="text" :placeholder=store.UserDetail.consumption class="col-9" id="consumption" v-model="consumption">
                </div>
                <div>
                    <label for="loan" class="col-3">대출금(만원)</label>
                    <input type="text" :placeholder=store.UserDetail.loan_money class="col-9" id="loan" v-model="loan_money">
                </div>
                <div>
                    <label for="goal_money" class="col-3">목표금액(만원)</label>
                    <input type="text" :placeholder=store.UserDetail.goal_money class="col-9" id="goal_money" v-model="goal_money">
                </div>
                <div>
                    <label for="days" class="col-3">목표개월 수</label>
                    <select name="days" class="col-9" id="days" v-model="goal_period">
                        <option v-for="day in goal_period_str" :value="day">{{ day }}</option>
                    </select>
                </div>
                <button class="btn btn-primary" style="width: 30%;">수정완료</button>
            </div>
        </form>
    </div>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useCounterStore } from '../stores/counter'
import axios from 'axios'
const router = useRouter()
const store = useCounterStore()
const nickname = ref(store.UserDetail.nickname);
const email = ref(store.UserDetail.email);
const age = ref(store.UserDetail.age);
const money = ref(store.UserDetail.money);
const salary = ref(store.UserDetail.salary);
const consumption = ref(store.UserDetail.consumption);
const loan_money = ref(store.UserDetail.loan_money);
const goal_period = ref(store.UserDetail.goal_period);
const goal_money = ref(store.UserDetail.goal_money);
const goal_period_str = ref([6, 12, 24, 36])
const API_URL = 'http://127.0.0.1:8000'

const updateprofile = function(UserDetail) {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/update/${UserDetail.id}/`,
        data: {
            nickname: nickname.value,
            email: email.value,
            age: age.value,
            money: money.value,
            salary: salary.value,
            loan_money: loan_money.value,
            consumption: consumption.value,
            goal_money: goal_money.value,
            goal_period: goal_period.value
        }
      })
      .then((res) => {
        console.log(res.data)
      })
      .catch((err) => {
        console.log(err)
      })
      router.push({name:'profile'})
    }

onMounted(() => {
    store.getUserDetail()
})
</script>

<style scoped>

</style>