<template>
    <div>
        <h1>프로필</h1>
        <button class="btn btn-primary" @click="goprofile(store.UserDetail)">프로필 수정</button>
        <div>ID : {{ store.UserDetail.username }}</div>
        <div class="d-flex">
            <div v-if="store.UserDetail.nickname">NICKNAME : {{ store.UserDetail.nickname }}</div>
            <div v-else>NICKNAME : 값을 넣어주세요.</div>
        </div>
        <div class="d-flex">
            <div v-if="store.UserDetail.email">EMAIL: {{ store.UserDetail.email }}</div>
            <div v-else>EMAIL : 값을 넣어주세요.</div>
        </div>
        <div class="d-flex">
            <div v-if="store.UserDetail.age">AGE : {{ store.UserDetail.age }}</div>
            <div v-else>AGE : 값을 넣어주세요.</div>
        </div>
        <div class="d-flex">
            <div v-if="store.UserDetail.money">MONEY : {{ store.UserDetail.money }}</div>
            <div v-else>MONEY : 값을 넣어주세요.</div>
        </div>
        <div class="d-flex">
            <div v-if="store.UserDetail.salary">SALARY : {{ store.UserDetail.salary }}</div>
            <div v-else>SALARY : 값을 넣어주세요.</div>
        </div>
        <div class="d-flex">
            <div v-if="store.UserDetail.loan_money">LOAN_MONEY : {{ store.UserDetail.loan_money }}</div>
            <div v-else>LOAN_MONEY : 값을 넣어주세요.</div>
        </div>
        <div class="d-flex">
            <div v-if="store.UserDetail.consumption">CONSUMPTION : {{ store.UserDetail.consumption }}</div>
            <div v-else>CONSUMPTION : 값을 넣어주세요.</div>
        </div>
        <div class="d-flex">
            <div v-if="store.UserDetail.goal_money">GOAL_MONEY : {{ store.UserDetail.goal_money }}</div>
            <div v-else>GOAL_MONEY : 값을 넣어주세요.</div>
        </div>
        <div class="d-flex">
            <div v-if="store.UserDetail.goal_period">GOAL_PERIOD : {{ store.UserDetail.goal_period }}</div>
            <div v-else>GOAL_PERIOD : 값을 넣어주세요.</div>
        </div>
            <div v-if="store.data" v-for="product in store.total">
                <div v-if="store.data_str.includes(product.fin_prdt_cd)">
                    Financial_products
                    <div>공시 제출월 {{ product.dcls_month }}</div>
                    <div>금융 회사명 {{ product.kor_co_nm }}</div>
                    <div>상품명 {{ product.fin_prdt_nm }}</div>
                    <div>가입제한 {{ product.join_deny }}</div>
                    <div>가입 방법 {{ product.join_way }}</div>
                    <div>우대조건 {{ product.spcl_cnd }}</div>
                    <button @click="del(product.fin_prdt_cd)" class="btn btn-primary">상품 삭제</button>
                </div>
            </div>
            <div v-else>Financial_products : 저장된 금융 상품이 없습니다.</div>
            <button @click="toggleRecommendations" class="btn btn-primary">추천상품 받기</button>
            <div v-if="showRecommendations">
            <div v-if="0.2 <= store.UserDetail.consumption / store.UserDetail.salary && store.UserDetail.consumption / store.UserDetail.salary < 0.4">소비성향이 적습니다. 장기 금리가 높은 상품을 추천합니다.</div>
            <div v-if="0.4 <= store.UserDetail.consumption / store.UserDetail.salary && store.UserDetail.consumption / store.UserDetail.salary < 0.6">소비성향이 중간입니다. 중간 기간 금리가 높은 상품을 추천합니다.</div>
            <div v-if="0.6 <= store.UserDetail.consumption / store.UserDetail.salary">소비성향이 큽니다. 단기 금리가 높은 상품을 추천합니다.</div>
            <div>
                추천금융상품
                <div class="row d-flex align-items-center">
                    <div class="col-2 text-center">공시 제출월</div>
                    <div class="vr p-0"></div>
                    <div class="col-2 text-center">금융회사명</div>
                    <div class="vr p-0"></div>
                    <div class="col-3 text-center">상품명</div>
                    <div class="vr p-0"></div>
                    <div class="col-1 text-center">6개월</div>
                    <div class="vr p-0"></div>
                    <div class="col-1 text-center">12개월</div>
                    <div class="vr p-0"></div>
                    <div class="col-1 text-center">24개월</div>
                    <div class="vr p-0"></div>
                    <div class="col-1 text-center">36개월</div>
                </div>
                <div v-for="(product, index) in recomment_conf" :key="index">
                    <div class="row d-flex align-items-center" :class="{ 'gray-bg': index % 2 === 0, 'white-bg': index % 2 !== 0 }">
                    <div @click="goDetail(product)" class="col-2 text-center">{{ product.dcls_month }}</div>
                    <div @click="goDetail(product)" class="col-2 text-center">{{ product.kor_co_nm }}</div>
                    <div @click="goDetail(product)" class="col-3 text-center">{{ product.fin_prdt_nm }}</div>
                    <div @click="goDetail(product)" class="col-1 text-center">{{ product.month6 }}</div>
                    <div @click="goDetail(product)" class="col-1 text-center">{{ product.month12 }}</div>
                    <div @click="goDetail(product)" class="col-1 text-center">{{ product.month24 }}</div>
                    <div class="col-1 text-center">{{ product.month36 }}</div>
                    <button @click="goDetail(product)" class="col-1">상세보기</button>
                </div>
                    <div v-if="recomment_day==6 && product.type=='단리'">6개월 예상 수익 : {{ parseFloat((((store.UserDetail.salary-store.UserDetail.consumption)/12*6*(1+product.month6/100)*0.5)).toFixed(2)) }} 만원</div>
                    <div>
                        <div v-if="recomment_day==6 && product.type=='단리' && store.UserDetail.goal_money+store.UserDetail.loan_money-(store.UserDetail.salary-store.UserDetail.consumption)/12*6*(1+product.month6/100)*0.5 > 0">6개월 후 남은 목표금액(대출금 포함) : {{ parseFloat(((store.UserDetail.goal_money+store.UserDetail.loan_money-(store.UserDetail.salary-store.UserDetail.consumption)/12*6*(1+product.month6/100)*0.5)).toFixed(2)) }}만원</div>
                        <div v-if="recomment_day==6 && product.type=='단리' && store.UserDetail.goal_money+store.UserDetail.loan_money-(store.UserDetail.salary-store.UserDetail.consumption)/12*6*(1+product.month6/100)*0.5 <= 0">목표금액을 달성하였습니다!</div>
                    </div>
                    <div v-if="recomment_day==6 && product.type=='복리'">6개월 예상 수익 : {{ parseFloat((((store.UserDetail.salary-store.UserDetail.consumption)/12*6*(((1+product.month6/100/12)^6-1)^6+1))).toFixed(2)) }}만원</div>
                    <div>
                        <div v-if="recomment_day==6 && product.type=='복리' && store.UserDetail.goal_money+store.UserDetail.loan_money-(store.UserDetail.salary-store.UserDetail.consumption)/12*6*(((1+product.month6/100/12)^6-1)^6+1) > 0">6개월 후 남은 목표금액(대출금 포함) : {{ parseFloat(((store.UserDetail.goal_money+store.UserDetail.loan_money-(store.UserDetail.salary-store.UserDetail.consumption)/12*6*(((1+product.month6/100/12)^6-1)^6+1))).toFixed(2)) }}만원</div>
                        <div v-if="recomment_day==6 && product.type=='복리' && store.UserDetail.goal_money+store.UserDetail.loan_money-(store.UserDetail.salary-store.UserDetail.consumption)/12*6*(((1+product.month6/100/12)^6-1)^6+1) <= 0">목표 금액을 달성하였습니다!</div>
                    </div>
                    <div v-if="recomment_day==12 && product.type=='단리'">12개월 예상 수익 : {{ parseFloat((((store.UserDetail.salary-store.UserDetail.consumption)/12*12*(1+product.month12/100))).toFixed(2)) }}만원</div>
                    <div>

                        <div v-if="recomment_day==12 && product.type=='단리' && store.UserDetail.goal_money+store.UserDetail.loan_money-(store.UserDetail.salary-store.UserDetail.consumption)/12*12*(1+product.month12/100) > 0">12개월 후 남은 목표금액(대출금 포함) : {{ parseFloat(((store.UserDetail.goal_money+store.UserDetail.loan_money-(store.UserDetail.salary-store.UserDetail.consumption)/12*12*(1+product.month12/100))).toFixed(2)) }}만원</div>
                        <div v-if="recomment_day==12 && product.type=='단리' && store.UserDetail.goal_money+store.UserDetail.loan_money-(store.UserDetail.salary-store.UserDetail.consumption)/12*12*(1+product.month12/100) <= 0">목표금액을 달성하였습니다.</div>
                    </div>
                    <div v-if="recomment_day==12 && product.type=='복리'">12개월 예상 수익 : {{ parseFloat((((store.UserDetail.salary-store.UserDetail.consumption)/12*12*(((1+product.month12/100/12)^12-1)^12+1))).toFixed(2)) }}만원</div>
                    <div>

                        <div v-if="recomment_day==12 && product.type=='복리' && store.UserDetail.goal_money+store.UserDetail.loan_money-(store.UserDetail.salary-store.UserDetail.consumption)/12*12*(((1+product.month12/100/12)^12-1)^12+1) > 0">12개월 후 남은 목표금액(대출금 포함) : {{parseFloat((( store.UserDetail.goal_money+store.UserDetail.loan_money-(store.UserDetail.salary-store.UserDetail.consumption)/12*12*(((1+product.month12/100/12)^12-1)^12+1))).toFixed(2)) }}만원</div>
                        <div v-if="recomment_day==12 && product.type=='복리' && store.UserDetail.goal_money+store.UserDetail.loan_money-(store.UserDetail.salary-store.UserDetail.consumption)/12*12*(((1+product.month12/100/12)^12-1)^12+1) <= 0">목표 금액을 달성하였습니다!</div>
                    </div>
                    <div v-if="recomment_day==24 && product.type=='단리'">24개월 예상 수익 : {{ parseFloat((((store.UserDetail.salary-store.UserDetail.consumption)/12*12*(1+product.month24/100)*2)).toFixed(2)) }}만원</div>
                    <div>
                        <div v-if="recomment_day==24 && product.type=='단리' && store.UserDetail.goal_money+store.UserDetail.loan_money-(store.UserDetail.salary-store.UserDetail.consumption)/12*12*(1+product.month24/100)*2 > 0">24개월 후 남은 목표금액(대출금 포함) :  {{ parseFloat(((store.UserDetail.goal_money+store.UserDetail.loan_money-(store.UserDetail.salary-store.UserDetail.consumption)/12*12*(1+product.month24/100)*2)).toFixed(2)) }}만원</div>
                        <div v-if="recomment_day==24 && product.type=='단리' && store.UserDetail.goal_money+store.UserDetail.loan_money-(store.UserDetail.salary-store.UserDetail.consumption)/12*12*(1+product.month24/100)*2 <= 0">목표금액을 달성하였습니다!</div>
                    </div>
                    <div v-if="recomment_day==24 && product.type=='복리'">24개월 예상 수익 :  {{ parseFloat((((store.UserDetail.salary-store.UserDetail.consumption)/12*12*(((1+product.month24/100/12)^24-1)^24+1))).toFixed(2)) }} 만원</div>
                    <div>

                        <div v-if="recomment_day==24 && product.type=='복리' && store.UserDetail.goal_money+store.UserDetail.loan_money-(store.UserDetail.salary-store.UserDetail.consumption)/12*12*(((1+product.month24/100/12)^24-1)^24+1) > 0">24개월 후 남은 목표금액(대출금 포함) :  {{ parseFloat(((store.UserDetail.goal_money+store.UserDetail.loan_money-(store.UserDetail.salary-store.UserDetail.consumption)/12*24*(((1+product.month24/100/12)^24-1)^24+1))).toFixed(2)) }}만원</div>
                        <div v-if="recomment_day==24 && product.type=='복리' && store.UserDetail.goal_money+store.UserDetail.loan_money-(store.UserDetail.salary-store.UserDetail.consumption)/12*12*(((1+product.month24/100/12)^24-1)^24+1) <= 0">목표금액을 달성하였습니다.</div>
                    </div>
                </div>
                </div>
            </div>
        </div>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import { useCounterStore } from '../stores/counter'
import { useRouter } from 'vue-router'
import axios from 'axios'
const router = useRouter()
const store = useCounterStore()
const best_period = ref('')
const best_conf = ref('')
const recomment_conf = ref('')
const recomment_day = ref('')
const API_URL = 'http://127.0.0.1:8000'
onMounted(() => {
    store.getUserDetail()
    store.getdeposit()
    store.savings.forEach((element) => {
        axios({
            method: 'get',
            url: `${API_URL}/api/v1/products/product-options/${element.fin_prdt_cd}/`
        })
        .then(res => {
            for(let i of res.data){
                element['month'+i.save_trm] = i.intr_rate
                element[i.save_trm] = i.intr_rate
                element['type'] = i.intr_rate_type_nm
            }
        })
        .catch((err) => console.log(err))
    })
    best_period.value = store.UserDetail.goal_period
    console.log(store.UserDetail.consumption/store.UserDetail.salary)
    best_conf.value = store.savings.filter((element) => element.hasOwnProperty(best_period.value))
    .sort((a, b) => b[best_period.value] - a[best_period.value])
    .slice(0, 5)
    if(0.2 <= store.UserDetail.consumption / store.UserDetail.salary && store.UserDetail.consumption / store.UserDetail.salary < 0.4){
        recomment_day.value = 24
        recomment_conf.value = store.savings.filter((element) => element.hasOwnProperty(24))
    .sort((a, b) => b[24] - a[24])
    .slice(0, 5)
    }
    else if(0.4 <= store.UserDetail.consumption / store.UserDetail.salary && store.UserDetail.consumption / store.UserDetail.salary < 0.6){
        recomment_day.value = 12
        recomment_conf.value = store.savings.filter((element) => element.hasOwnProperty(12))
    .sort((a, b) => b[12] - a[12])
    .slice(0, 5)
    }
    else if(0.6 <= store.UserDetail.consumption / store.UserDetail.salary){
        recomment_day.value = 6
        recomment_conf.value = store.savings.filter((element) => element.hasOwnProperty(6))
    .sort((a, b) => b[6] - a[6])
    .slice(0, 5)
    }
    console.log(recomment_conf.value)

})

const goprofile = function(UserDetail){
    router.push({name:'updateprofile', params:{username:UserDetail.username}})
}

const del = function(object){
    store.data_str = store.data_str.filter((element) => element != object)
    store.data = store.data_str.join(',')
    axios({
        method: 'post',
        url: `${API_URL}/accounts/update/${store.UserDetail.id}/`,
        data: {
            financial_products:store.data
        }
    })
    .then((res) => {
        console.log(res.data)
    })
    .catch((err) => {
        console.log(err)
    })
}

const goDetail = function(target){
    router.push({name:'productsdetail', params:{cd:target.fin_prdt_cd}})
}

const showRecommendations = ref(false);

const toggleRecommendations = () => {
  showRecommendations.value = !showRecommendations.value;
};
</script>

<style scoped>
.gray-bg {
    background-color: #ccc; /* Gray background color */
}

.white-bg {
    background-color: #ccc; /* White background color */
}
</style>