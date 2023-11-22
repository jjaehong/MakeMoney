<template>
  <div>
    <h1>Detail</h1>
    <RouterLink :to="{name:'UpdateView', params:{id:$route.params.id}}">
      [게시글 수정]
    </RouterLink>
    <div v-if="article">
      <p>제목 : {{ article.title }}</p>
      <p>내용 : {{ article.content }}</p>
      <p>작성일 : {{ article.created_at }}</p>
      <p>수정일 : {{ article.updated_at }}</p>
      <button @click="deleteArticle()">삭제</button>
    </div>
    <hr>
    <h4>댓글 작성란</h4>
    <form @submit="createComment">
      <input type="text" v-model="content">
      <input type="submit" value="댓글 작성">
    </form>


    <!-- <div v-if="comment">
    
    
    </div> -->

  </div>
</template>

<script setup>
import axios from 'axios'
import { onMounted, ref } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { useRoute,useRouter } from 'vue-router'
import { RouterLink, RouterView } from 'vue-router'


const store = useCounterStore()

// router가 데이터를 다른 url을 보낼 때
// route는 이 페이지에서 데이터 받은 것을 사용할 때
const route = useRoute()
const router = useRouter()
const article = ref(null)
const content = ref(null)
console.log(route.params)
onMounted(() => {
  axios({
    method: 'get',
    url: `${store.API_URL}/api/v1/articles/${route.params.id}/`
  })
    .then((res) => {
      // console.log(res.data)
      article.value = res.data
      // console.log(route)
    })
    .catch((err) => {
      console.log(err)
    })
})



const deleteArticle = function() {
  axios({
    method:'delete',
    url: `${store.API_URL}/api/v1/articles/${route.params.id}`
  })
  .then((res) => {
    console.log(res)
    router.push({name: 'community'})
  })
  .catch((err) => {
    console.log(err)
  })
}

const createComment = function(event) {
  event.preventDefault()
  axios({
    method:'post',
    url:`${store.API_URL}/api/v1/articles/${route.params.id}/comments/`,
    data:{
      content:content.value
    },
    headers: {
      Authorization: `Token ${store.token}`
    },
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
