<template>
    <div>
        <div>{{ store.UserDetail.username }}님의 프로필 수정 페이지</div>
        <form @submit.prevent="updateprofile(store.UserDetail)">
            <div class="row" style="width: 500px;">
                <div>
                    <label for="nickname" class="col-3">nickname</label>
                    <input type="text" :placeholder=store.UserDetail.nickname class="col-9" id="nickname" v-model="nickname">
                </div>
                <div>
                    <label for="age" class="col-3">age</label>
                    <input type="text" :placeholder=store.UserDetail.age class="col-9" id="age" v-model="age">
                </div>
                <div>
                    <label for="email" class="col-3">email</label>
                    <input type="text" :placeholder=store.UserDetail.email class="col-9" id="email" v-model="email">
                </div>
                <div>
                    <label for="money" class="col-3">money</label>
                    <input type="text" :placeholder=store.UserDetail.money class="col-9" id="money" v-model="money">
                </div>
                <div>
                    <label for="salary" class="col-3">salary</label>
                    <input type="text" :placeholder=store.UserDetail.salary class="col-9" id="salary" v-model="salary">
                </div>
                <div>
                    <label for="loan" class="col-3">loan_money</label>
                    <input type="text" :placeholder=store.UserDetail.loan_money class="col-9" id="loan" v-model="loan_money">
                </div>
                <select name="" id="">

                </select>
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
const nickname = ref('')
const email = ref('')
const age = ref('')
const money = ref('')
const salary = ref('')
const loan_money = ref('')
const goal_period = ref('')
const goal_money = ref('')
const goal_money_str = ref(['1억원 미만, 1억원 이상 ~ 2억원 미만, 2억원 이상 ~ 3억원 미만, 3억원 이상 ~ 4억원 미만'])
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