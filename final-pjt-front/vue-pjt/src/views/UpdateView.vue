<template>
    <div>
        <h1>게시글 수정 페이지</h1>
        <form @submit.prevent="putArticle()">
            <div>
                <label for="title">제목:</label>
                <input type="text" id="title" v-model.trim="title" >
            </div>
            <div>
                <label for="content">내용:</label>
                <textarea id="content" v-model.trim="content" cols="30" rows="10"></textarea>
            </div>
            <input type="submit" value="수정">

        </form>
    </div>
</template>

<script setup>

import {useCounterStore} from '@/stores/counter' 
import axios from 'axios'
import { useRoute, useRouter } from 'vue-router';
import {onMounted, ref} from 'vue'

const store = useCounterStore()
const route = useRoute()
const router = useRouter()

const title = ref(null)
const content = ref(null)


onMounted(() =>{
    axios({
        method:'get',
        url: `${store.API_URL}/api/v1/articles/${route.params.id}/`,
        })

        .then((res) => {
            // console.log(res.data.content)
            title.value = res.data.title
            content.value = res.data.content
          })
        .catch((err) => {
            console.log(err)
        })
})


const putArticle = function () {
    axios({
        method:'put',
        url: `${store.API_URL}/api/v1/articles/${route.params.id}/`,
        data: {
            title:title.value,
            content:content.value,
        }
    })
        .then((res) => {
            console.log(res)
            router.push({name:'DetailView', params: { id: route.params.id} })
        })
        .catch((err) => {
            console.log(err)
        })
}

</script>

<style scoped>

</style>