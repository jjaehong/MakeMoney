<template>
  <div>


    <h5>{{ article.id }}</h5>
    <div class="d-flex flex-column border border-secondary">

      <div class="d-flex justify-content-between">
        <div>작성자 : </div>
        <div>{{ article.updated_at }}</div>
      </div>
      <div>
        <h4>{{ article.title }}</h4>
        <p>{{ article.content }}</p>
      </div>
      <div class="d-flex ">
        <p>좋아요 갯수</p>
        <p> 댓글 {{ article.comment_count }}</p>
      </div>
      <RouterLink :to="{ name: 'DetailView', params: { id: article.id } }">
        [Detail]
      </RouterLink>
    </div>

    <hr>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router'

defineProps({
  article: Object
})
</script>
