<template>
    <div style="border: 1px solid lightgrey; margin-bottom: 15px;">
    <div class="d-flex justify-content-between">
      <p> 작성자 : {{ store.UserDetail.username }} </p>
      <p>{{ article.updated_at }}</p>
    </div>
    <!-- <h5 class="article-id">게시물 번호: {{ article.id }}</h5> -->
    <div>
      <h4 class="article-title" >{{ article.title }}</h4>
      <p>{{ article.content }}</p>
    </div>
    <div class="d-flex gap-3" >
      <p>좋아요 {{ article.like_users.length }} </p>
      <p> 댓글 {{ article.comment_count }}</p>
    </div>
    <hr class="separator">
    <RouterLink :to="{ name: 'DetailView', params: { id: article.id }}">
      [Detail]
    </RouterLink>
    
    <hr>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router'
import { useCounterStore } from '../stores/counter';
import { onMounted } from 'vue';

defineProps({
  article: Object
})

const store = useCounterStore()
onMounted(() => {
  store.getUserDetail()
})

</script>


<style scoped>
/* Blue theme styles */
.article-title {
  color: #3498db;
}
.article-content {
  color: #2c3e50; /* Darker text color for better readability */
}

.detail-link {
  color: #3498db; /* Blue color for the link */
  text-decoration: none;
  margin-top: 10px; /* Adjust as needed */
  display: inline-block;
}

.separator {
  border-color: #3498db; /* Blue color for the separator line */
  margin-top: 15px; /* Adjust as needed */
}
</style>