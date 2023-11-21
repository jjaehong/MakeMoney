<template>
  <div>
    <h1>Login</h1>
    <form @submit.prevent="logIn">
      <div>
        <label for="username">Username </label>
        <input type="text" v-model.trim="username" id="username">
      </div>
      <div>
        <label for="password">Password </label>
        <input type="password" v-model.trim="password" id="password">
      </div>
      <input type="submit">
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { RouterLink, useRouter } from 'vue-router'
const store = useCounterStore()
const username = ref(null)
const password = ref(null)
const router = useRouter()
const logIn = function () {
  const payload = {
    username: username.value,
    password: password.value
  }
  store.logIn(payload)
}
</script>

<style>

</style>
