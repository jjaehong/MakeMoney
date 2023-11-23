<template>
  <div>
    <h1>Detail</h1>
    <RouterLink :to="{ name: 'UpdateView', params: { id: $route.params.id } }">
      [게시글 수정]
    </RouterLink>
    <div v-if="article">
      <h4>제목 : {{ article.title }}</h4>
      <p>내용 : {{ article.content }}</p>
      <p>작성일 : {{ article.created_at }}</p>
      <p>수정일 : {{ article.updated_at }}</p>
      <div class="d-flex justify-content-between">
        <span class="bi bi-arrow-through-heart-fill h1 " :class="{ 'heart': islike }" @click="likes(store.UserDetail.username)">
        </span>
        <button @click="deleteArticle()">삭제</button>
      </div>
    </div>
    <hr>
    <h4>댓글 작성란</h4>
    <form @submit="createComment">
      <input type="text" v-model="content">
      <input type="submit" value="댓글 작성">
    </form>
    <hr>
    <h3>댓글 목록</h3>
    <div v-for="comment in store.comments" :key="comment.id">
      <div v-if="comment.article.id == route.params.id">
        <div class="d-flex flex-column border border-secondary">
          <div class="d-flex justify-content-between border border-secondary">
            <div> 작성자 : {{ comment.user.username }} </div>
            <div> {{ comment.updated_at }} </div>
          </div>
          <h4> {{ comment.content }} </h4>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import axios from 'axios'
import { onMounted, onUpdated, ref, computed, watch } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { useRoute, useRouter } from 'vue-router'
import { RouterLink, RouterView } from 'vue-router'



const store = useCounterStore()
// router가 데이터를 다른 url을 보낼 때
// route는 이 페이지에서 데이터 받은 것을 사용할 때
const route = useRoute()
const router = useRouter()
const article = ref(null)
const content = ref(null)


// watch(dfdf, (new, old) => {
//   if (new !==old ) {
//     dsaf
//   }
// })
const islike = computed(() => {
  console.log(store.UserDetail.id)
  console.log(article.value.like_users)
  return article.value.like_users.includes(store.UserDetail.id)

})
// console.log(route.params)
onMounted(() => {
  store.getUserDetail()
  store.getComments()
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


const deleteArticle = function () {
  axios({
    method: 'delete',
    url: `${store.API_URL}/api/v1/articles/${route.params.id}`
  })
    .then((res) => {
      // console.log(res)
      router.push({ name: 'community' })
    })
    .catch((err) => {
      console.log(err)
    })
}

const createComment = function (event) {
  event.preventDefault()
  axios({
    method: 'post',
    url: `${store.API_URL}/api/v1/articles/${route.params.id}/comments/`,
    data: {
      content: content.value
    },
    headers: {
      Authorization: `Token ${store.token}`
    },
  })
    .then((res) => {
      // console.log(res.data)
      content.value = ''

    })
    .catch((err) => {
      console.log(err)
    })
}

const likes = function () {
  axios({
    method: 'post',
    url: `${store.API_URL}/api/v1/articles/${route.params.id}/likes/`,
    data: {
      article: article.id,
      // user:username,
    },
    headers: {
      Authorization: `Token ${store.token}`
    },
  })
    .then((res) => {
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
    .catch((err) => {
      console.log(err)
    })

}


</script>

<style scoped>
.heart {
  color: red;
  /* background-color: red; */
}
</style>
