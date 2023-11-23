<template>
    <br>
    <div v-for="test in info" class="container">
        <h2 class="fw-bold">상품명 : {{ test.fin_prdt_nm }}</h2>
        <div class="fw-bold">금융 회사명 : {{ test.kor_co_nm }}</div>
        <div>가입제한 : {{ JoinWayToString(test.join_deny) }}</div>
        <div>가입대상 : {{ test.join_member }} </div>
        <div>가입 방법 : {{ test.join_way }}</div>
        <div>공시 제출월 : {{ test.dcls_month }}</div>
        <!-- <div> 상품 설명 : {{ test.etc_note }} </div> -->
        <table>
            <tr>
                <th>상품 설명</th>
                <td> 
                    {{ test.etc_note }}
                </td>
            </tr>
        </table>
        <table>
            <tr>
                <th>우대 조건</th>
                <td> 
                    <ul>
                        <li v-for="condition in parseConditions(test.spcl_cnd)" :key="condition" >
                            {{ condition }}
                        </li>
                    </ul>
                </td>
            </tr>
        </table>

    </div>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import { useCounterStore } from '../stores/counter'
import { useRoute } from 'vue-router'
const store = useCounterStore()
const route = useRoute()
const info = store.total.filter((element) => element.fin_prdt_cd == route.params.cd)

const parseConditions = (spcl_cnd) => {
    // 'p'를 기준으로 우대조건을 나누고 빈 문자열은 필터링합니다.
    return spcl_cnd.split('p').filter(condition => condition.trim() !== '');
};


const JoinWayToString = (joinWay) => {
    console.log('joinway', joinWay)
  switch (joinWay.toString()) {
    case '1':
      return '제한 없음';
    case '2':
      return '서민 전용';
    case '3':
      return '일부 제한';
    default:
      return '';
  }
};

onMounted(() => {
    store.getdeposit()
})

</script>





<style scoped>
.container {
    display: grid;
    gap: 20px;
    flex-wrap: wrap;
    /* border: 1px solid #ddd; */
}

table {
    width: 100%;
    border-collapse: collapse;
}

th,
td {
    border: 1px solid #ddd;
    padding: 8px;
    text-align: left;
}
</style>