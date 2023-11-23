<template>
  <div>
    <br>
    <h1 class="fw-bold">MAKE MONEY</h1>
    <form @submit.prevent="logIn" class="login">
      <div>
        <h3>Login</h3>
        <div class="form-group">
          <label for="username">ID</label>
          <input type="text" v-model.trim="username" id="username" class="form-input">
        </div>
        <div class="form-group">
          <label for="password" >Password</label>
          <input type="password" v-model.trim="password" id="password" class="form-input">
        </div>
        <input type="submit" class="btn-submit" value="로그인">
      </div>
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

.login {
  width: 500px;
  margin: 20px auto;
  padding: 20px;
  background-color: #f4f4f4;
  border: 2px solid #3498db;
  border-radius: 5px;
  text-align: center;
}

.form-group {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  margin-bottom: 15px;
}

label {
  font-weight: bold;
  /* display: block; */
  margin-bottom: 5px;
}

.form-input {
  width: 100%;
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 3px;
  box-sizing: border-box;
}

.btn-submit {
  background-color: #3498db;
  color: white;
  border: none;
  padding: 10px 20px;
  border-radius: 3px;
  cursor: pointer;
}

h1 {
  margin: auto auto;
  text-align: center;
}

</style>
