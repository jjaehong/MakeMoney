<template>
    <div>
        <h1>프로필</h1>
        <div>{{ store.UserDetail }}</div>
    </div>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import { useCounterStore } from '../stores/counter'
import { useRouter } from 'vue-router'

const store = useCounterStore()
onMounted(() => {
    store.getUserDetail()
})
</script>

<style scoped>

</style>