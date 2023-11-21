<template>
  <div>
    <h1>Detail</h1>
    <RouterLink :to="{name:'UpdateView', params:{id:article.id}}">
      [게시글 수정]
    </RouterLink>
    <div v-if="article">
      <p>제목 : {{ article.title }}</p>
      <p>내용 : {{ article.content }}</p>
      <p>작성일 : {{ article.created_at }}</p>
      <p>수정일 : {{ article.updated_at }}</p>
      <button @click="delete_article()">삭제</button>
    </div>
  </div>
</template>

<script setup>
import axios from 'axios'
import { onMounted, ref } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { useRoute } from 'vue-router'
import { RouterLink, RouterView } from 'vue-router'

const store = useCounterStore()

// router가 데이터를 다른 url을 보낼 때
// route는 데이터 받은것을 사용할 때
const route = useRoute()
const article = ref(null)

onMounted(() => {
  axios({
    method: 'get',
    url: `${store.API_URL}/api/v1/articles/${route.params.id}/`
  })
    .then((res) => {
      // console.log(res.data)
      article.value = res.data
    })
    .catch((err) => {
      console.log(err)
    })
})


const delete_article = function() {
  axios({
    method:'delete',
    url: `${store.API_URL}/api/v1/articles/${route.params.id}`
  })
  .then((res) => {
    console.log(res)

  })
  .catch((err) => {
    console.log(err)
  })
}



</script>

<style>

</style>
