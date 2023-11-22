<template>
    <div>
        <div>{{ store.UserDetail.username }}님의 프로필 수정 페이지</div>
        <form @submit.prevent="updateprofile(store.UserDetail)">
            <div class="row" style="width: 500px;">
                <div>
                    <label for="nickname" class="col-2">nickname</label>
                    <input type="text" :placeholder=store.UserDetail.nickname class="col-9" id="nickname" v-model="nickname">
                </div>
                <div>
                    <label for="age" class="col-2">age</label>
                    <input type="text" :placeholder=store.UserDetail.age class="col-9" id="age" v-model="age">
                </div>
                <div>
                    <label for="email" class="col-2">email</label>
                    <input type="text" :placeholder=store.UserDetail.email class="col-9" id="email" v-model="email">
                </div>
                <div>
                    <label for="money" class="col-2">money</label>
                    <input type="text" :placeholder=store.UserDetail.money class="col-9" id="money" v-model="money">
                </div>
                <div>
                    <label for="salary" class="col-2">salary</label>
                    <input type="text" :placeholder=store.UserDetail.age class="col-9" id="salary" v-model="salary">
                </div>
                <div>
                    <label for="loan" class="col-2">loan</label>
                    <input type="text" :placeholder=store.UserDetail.age class="col-9" id="loan" v-model="loan">
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
const route = useRoute()
const store = useCounterStore()
const nickname = ref('')
const email = ref('')
const age = ref('')
const money = ref('')
const salary = ref('')
const loan = ref('')
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
            loan: loan.value
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