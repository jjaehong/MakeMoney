<template>
    <div>
        <h1 class="profile-info">{{ store.UserDetail.username }} 님의 프로필 페이지 </h1>
        <button class="btn btn-primary" @click="goprofile(store.UserDetail)">프로필 수정</button>
        <div class="d-flex">
            <div v-if="store.UserDetail.nickname">닉네임 : {{ store.UserDetail.nickname }}</div>
            <div v-else>닉네임 : 값을 넣어주세요.</div>
        </div>
        <div class="d-flex">
            <div v-if="store.UserDetail.email">이메일: {{ store.UserDetail.email }}</div>
            <div v-else>이메일 : 값을 넣어주세요.</div>
        </div>
        <div class="d-flex">
            <div v-if="store.UserDetail.age">나이 : {{ store.UserDetail.age }}</div>
            <div v-else>나이 : 값을 넣어주세요.</div>
        </div>
        <div class="d-flex">
            <div v-if="store.UserDetail.money">자산 : {{ store.UserDetail.money }}</div>
            <div v-else>자산 : 값을 넣어주세요.</div>
        </div>
        <div class="d-flex">
            <div v-if="store.UserDetail.salary">연봉 : {{ store.UserDetail.salary }}</div>
            <div v-else>연봉 : 값을 넣어주세요.</div>
        </div>
        <div class="d-flex">
            <div v-if="store.UserDetail.loan_money">대출금 : {{ store.UserDetail.loan_money }}</div>
            <div v-else>대출금 : 값을 넣어주세요.</div>
        </div>
        <div class="d-flex">
            <div v-if="store.UserDetail.consumption">소비 금액(연) : {{ store.UserDetail.consumption }}</div>
            <div v-else>소비 금액(연) : 값을 넣어주세요.</div>
        </div>
        <div class="d-flex">
            <div v-if="store.UserDetail.goal_money">목표 금액 : {{ store.UserDetail.goal_money }}</div>
            <div v-else>목표 금액 : 값을 넣어주세요.</div>
        </div>
        <div class="d-flex">
            <div v-if="store.UserDetail.goal_period">목표 기간 : {{ store.UserDetail.goal_period }}</div>
            <div v-else>목표 기간 : 값을 넣어주세요.</div>
        </div>
        
        <div class="line"></div>
        
        <h2> 1. {{ store.UserDetail.username }} 님이 가입한 상품 목록 </h2>
        <div>
            <div v-if="store.data_str.length > 2" v-for="product in store.total">
                <div v-if="store.data_str.includes(product.fin_prdt_cd)" class="financial-product">
                    <div @click="goDetail(product)">  {{ product.kor_co_nm }} : {{ product.fin_prdt_nm }}</div>
                    <!-- <div @click="goDetail(product)" >상품명 {{ product.fin_prdt_nm }}</div> -->
                    <button @click="del(product.fin_prdt_cd)" class="btn btn-danger">상품 삭제</button>
                </div>
            </div>
            <div v-else class="fw-bold">저장된 금융 상품이 없습니다.</div>
        </div>

        <div class="line"></div>

        <h2> 2. {{ store.UserDetail.username }} 님의 금융상품 추천</h2>
        <div
            v-if="0.2 <= store.UserDetail.consumption / store.UserDetail.salary && store.UserDetail.consumption / store.UserDetail.salary < 0.4">
            {{ store.UserDetail.username }}님은 소비성향이 적습니다. 장기 금리가 높은 상품을 추천합니다.
        </div>
        <div
            v-if="0.4 <= store.UserDetail.consumption / store.UserDetail.salary && store.UserDetail.consumption / store.UserDetail.salary < 0.6">
            {{ store.UserDetail.username }}님은 소비성향이 중간입니다. 중간 기간 금리가 높은 상품을 추천합니다.
        </div>
        <h4 
            v-if="0.6 <= store.UserDetail.consumption / store.UserDetail.salary">
            {{ store.UserDetail.username }}님은 소비성향이 큽니다. 단기 금리가 높은 상품을 추천합니다.
        </h4>
        <br>
        <div>
            <button @click.prevent="toggleRecommendations" style="width: 250px;" class="btn btn-primary">{{ showRecommendations ? '추천 상품 숨기기' : '추천 상품 보기' }}</button>
        </div>
        <div v-if="showRecommendations" class="product-container">
            <h3>추천금융상품 목록</h3>
            <div class="row d-flex align-items-center border border-1px-solid-#ccc m-2 ">
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
            <div v-for="(product, index) in recomment_conf" :key="index" class="border border-1px-solid-#ccc">
                <div class="row d-flex align-items-center m-2"
                    :class="{ 'gray-bg': index % 2 === 0, 'white-bg': index % 2 !== 0 }">
                    <div @click="goDetail(product)" class="col-2 text-center">{{ product.dcls_month }}</div>
                    <div @click="goDetail(product)" class="col-2 text-center">{{ product.kor_co_nm }}</div>
                    <div @click="goDetail(product)" class="col-3 text-center">{{ product.fin_prdt_nm }}</div>
                    <div @click="goDetail(product)" class="col-1 text-center">{{ product.month6 }}</div>
                    <div @click="goDetail(product)" class="col-1 text-center">{{ product.month12 }}</div>
                    <div @click="goDetail(product)" class="col-1 text-center">{{ product.month24 }}</div>
                    <div class="col-1 text-center">{{ product.month36 }}</div>
                    <button @click="goDetail(product)" class="col-1">상세보기</button>
                    </div>
                    <div class="fw-bold m-2" v-if="recomment_day==6 && product.type=='단리'">6개월 예상 수익 : {{ parseFloat((((store.UserDetail.salary-store.UserDetail.consumption)/12*6*(1+product.month6/100)*0.5)).toFixed(2)) }} 만원</div>
                    <div class="fw-bold m-2">
                        <div v-if="recomment_day==6 && product.type=='단리' && store.UserDetail.goal_money+store.UserDetail.loan_money-(store.UserDetail.salary-store.UserDetail.consumption)/12*6*(1+product.month6/100)*0.5 > 0">6개월 후 남은 목표금액(대출금 포함) : {{ parseFloat(((store.UserDetail.goal_money+store.UserDetail.loan_money-(store.UserDetail.salary-store.UserDetail.consumption)/12*6*(1+product.month6/100)*0.5)).toFixed(2)) }}만원</div>
                        <div v-if="recomment_day==6 && product.type=='단리' && store.UserDetail.goal_money+store.UserDetail.loan_money-(store.UserDetail.salary-store.UserDetail.consumption)/12*6*(1+product.month6/100)*0.5 <= 0">목표금액을 달성하였습니다!</div>
                    </div>
                    <div class="fw-bold m-2" v-if="recomment_day==6 && product.type=='복리'">6개월 예상 수익 : {{ parseFloat((((store.UserDetail.salary-store.UserDetail.consumption)/12*6*(((1+product.month6/100/12)^6-1)^6+1))).toFixed(2)) }}만원</div>
                    <div class="fw-bold m-2">
                        <div v-if="recomment_day==6 && product.type=='복리' && store.UserDetail.goal_money+store.UserDetail.loan_money-(store.UserDetail.salary-store.UserDetail.consumption)/12*6*(((1+product.month6/100/12)^6-1)^6+1) > 0">6개월 후 남은 목표금액(대출금 포함) : {{ parseFloat(((store.UserDetail.goal_money+store.UserDetail.loan_money-(store.UserDetail.salary-store.UserDetail.consumption)/12*6*(((1+product.month6/100/12)^6-1)^6+1))).toFixed(2)) }}만원</div>
                        <div v-if="recomment_day==6 && product.type=='복리' && store.UserDetail.goal_money+store.UserDetail.loan_money-(store.UserDetail.salary-store.UserDetail.consumption)/12*6*(((1+product.month6/100/12)^6-1)^6+1) <= 0">목표 금액을 달성하였습니다!</div>
                    </div>

                    <div class="fw-bold m-2" v-if="recomment_day==12 && product.type=='단리'">12개월 예상 수익 : {{ parseFloat((((store.UserDetail.salary-store.UserDetail.consumption)/12*12*(1+product.month12/100))).toFixed(2)) }}만원</div>
                    <div class="fw-bold m-2">
                        <div v-if="recomment_day==12 && product.type=='단리' && store.UserDetail.goal_money+store.UserDetail.loan_money-(store.UserDetail.salary-store.UserDetail.consumption)/12*12*(1+product.month12/100) > 0">12개월 후 남은 목표금액(대출금 포함) : {{ parseFloat(((store.UserDetail.goal_money+store.UserDetail.loan_money-(store.UserDetail.salary-store.UserDetail.consumption)/12*12*(1+product.month12/100))).toFixed(2)) }}만원</div>
                        <div v-if="recomment_day==12 && product.type=='단리' && store.UserDetail.goal_money+store.UserDetail.loan_money-(store.UserDetail.salary-store.UserDetail.consumption)/12*12*(1+product.month12/100) <= 0">목표금액을 달성하였습니다.</div>
                    </div>

                    <div class="fw-bold m-2" v-if="recomment_day==12 && product.type=='복리'">12개월 예상 수익 : {{ parseFloat((((store.UserDetail.salary-store.UserDetail.consumption)/12*12*(((1+product.month12/100/12)^12-1)^12+1))).toFixed(2)) }}만원</div>
                    <div class="fw-bold m-2">
                        <div v-if="recomment_day==12 && product.type=='복리' && store.UserDetail.goal_money+store.UserDetail.loan_money-(store.UserDetail.salary-store.UserDetail.consumption)/12*12*(((1+product.month12/100/12)^12-1)^12+1) > 0">12개월 후 남은 목표금액(대출금 포함) : {{parseFloat((( store.UserDetail.goal_money+store.UserDetail.loan_money-(store.UserDetail.salary-store.UserDetail.consumption)/12*12*(((1+product.month12/100/12)^12-1)^12+1))).toFixed(2)) }}만원</div>
                        <div v-if="recomment_day==12 && product.type=='복리' && store.UserDetail.goal_money+store.UserDetail.loan_money-(store.UserDetail.salary-store.UserDetail.consumption)/12*12*(((1+product.month12/100/12)^12-1)^12+1) <= 0">목표 금액을 달성하였습니다!</div>
                    </div>

                    <div class="fw-bold m-2" v-if="recomment_day==24 && product.type=='단리'">24개월 예상 수익 : {{ parseFloat((((store.UserDetail.salary-store.UserDetail.consumption)/12*12*(1+product.month24/100)*2)).toFixed(2)) }}만원</div>
                    <div class="fw-bold m-2">
                        <div v-if="recomment_day==24 && product.type=='단리' && store.UserDetail.goal_money+store.UserDetail.loan_money-(store.UserDetail.salary-store.UserDetail.consumption)/12*12*(1+product.month24/100)*2 > 0">24개월 후 남은 목표금액(대출금 포함) :  {{ parseFloat(((store.UserDetail.goal_money+store.UserDetail.loan_money-(store.UserDetail.salary-store.UserDetail.consumption)/12*12*(1+product.month24/100)*2)).toFixed(2)) }}만원</div>
                        <div v-if="recomment_day==24 && product.type=='단리' && store.UserDetail.goal_money+store.UserDetail.loan_money-(store.UserDetail.salary-store.UserDetail.consumption)/12*12*(1+product.month24/100)*2 <= 0">목표금액을 달성하였습니다!</div>
                    </div>

                    <div class="fw-bold m-2" v-if="recomment_day==24 && product.type=='복리'">24개월 예상 수익 :  {{ parseFloat((((store.UserDetail.salary-store.UserDetail.consumption)/12*12*(((1+product.month24/100/12)^24-1)^24+1))).toFixed(2)) }} 만원</div>
                    <div class="fw-bold m-2">
                        <div v-if="recomment_day==24 && product.type=='복리' && store.UserDetail.goal_money+store.UserDetail.loan_money-(store.UserDetail.salary-store.UserDetail.consumption)/12*12*(((1+product.month24/100/12)^24-1)^24+1) > 0">24개월 후 남은 목표금액(대출금 포함) :  {{ parseFloat(((store.UserDetail.goal_money+store.UserDetail.loan_money-(store.UserDetail.salary-store.UserDetail.consumption)/12*24*(((1+product.month24/100/12)^24-1)^24+1))).toFixed(2)) }}만원</div>
                        <div v-if="recomment_day==24 && product.type=='복리' && store.UserDetail.goal_money+store.UserDetail.loan_money-(store.UserDetail.salary-store.UserDetail.consumption)/12*12*(((1+product.month24/100/12)^24-1)^24+1) <= 0">목표금액을 달성하였습니다.</div>
                    </div>
            </div>
            </div>

            <button @click.prevent="showgraph" style="width: 250px;" class="btn btn-primary">{{ show ? '그래프 숨기기' : '그래프 보기' }}</button>
            <chart v-if="show" :name="name" :data1="data1" :data2="data2" :day="recomment_day"/>
            <div class="line"></div>
            <h2> 3. {{ store.UserDetail.username }} 님의 목표기간에 따른 금융상품 추천</h2>
            <h3>추천금융상품 목록</h3>
            <div>
                <button @click.prevent="toggleRecommendations1" style="width: 250px;" class="btn btn-primary">{{ showRecommendations1 ? '목표기간 추천 상품 숨기기' : '목표기간 추천 상품 보기' }}</button>
            </div>
            <div v-if="showRecommendations1">
            <div class="row d-flex align-items-center border border-1px-solid-#ccc m-2 ">
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
            <div v-for="(product, index) in best_conf" :key="index" class="border border-1px-solid-#ccc">
                <div class="row d-flex align-items-center m-2"
                    :class="{ 'gray-bg': index % 2 === 0, 'white-bg': index % 2 !== 0 }">
                    <div @click="goDetail(product)" class="col-2 text-center">{{ product.dcls_month }}</div>
                    <div @click="goDetail(product)" class="col-2 text-center">{{ product.kor_co_nm }}</div>
                    <div @click="goDetail(product)" class="col-3 text-center">{{ product.fin_prdt_nm }}</div>
                    <div @click="goDetail(product)" class="col-1 text-center">{{ product.month6 }}</div>
                    <div @click="goDetail(product)" class="col-1 text-center">{{ product.month12 }}</div>
                    <div @click="goDetail(product)" class="col-1 text-center">{{ product.month24 }}</div>
                    <div class="col-1 text-center">{{ product.month36 }}</div>
                    <button @click="goDetail(product)" class="col-1">상세보기</button>
                    </div>
                    <div class="fw-bold m-2" v-if="best_period==6 && product.type=='단리'">6개월 예상 수익 : {{ parseFloat((((store.UserDetail.salary-store.UserDetail.consumption)/12*6*(1+product.month6/100)*0.5)).toFixed(2)) }} 만원</div>
                    <div class="fw-bold m-2">
                        <div v-if="best_period==6 && product.type=='단리' && store.UserDetail.goal_money+store.UserDetail.loan_money-(store.UserDetail.salary-store.UserDetail.consumption)/12*6*(1+product.month6/100)*0.5 > 0">6개월 후 남은 목표금액(대출금 포함) : {{ parseFloat(((store.UserDetail.goal_money+store.UserDetail.loan_money-(store.UserDetail.salary-store.UserDetail.consumption)/12*6*(1+product.month6/100)*0.5)).toFixed(2)) }}만원</div>
                        <div v-if="best_period==6 && product.type=='단리' && store.UserDetail.goal_money+store.UserDetail.loan_money-(store.UserDetail.salary-store.UserDetail.consumption)/12*6*(1+product.month6/100)*0.5 <= 0">목표금액을 달성하였습니다!</div>
                    </div>
                    <div class="fw-bold m-2" v-if="best_period==6 && product.type=='복리'">6개월 예상 수익 : {{ parseFloat((((store.UserDetail.salary-store.UserDetail.consumption)/12*6*(((1+product.month6/100/12)^6-1)^6+1))).toFixed(2)) }}만원</div>
                    <div class="fw-bold m-2">
                        <div v-if="best_period==6 && product.type=='복리' && store.UserDetail.goal_money+store.UserDetail.loan_money-(store.UserDetail.salary-store.UserDetail.consumption)/12*6*(((1+product.month6/100/12)^6-1)^6+1) > 0">6개월 후 남은 목표금액(대출금 포함) : {{ parseFloat(((store.UserDetail.goal_money+store.UserDetail.loan_money-(store.UserDetail.salary-store.UserDetail.consumption)/12*6*(((1+product.month6/100/12)^6-1)^6+1))).toFixed(2)) }}만원</div>
                        <div v-if="best_period==6 && product.type=='복리' && store.UserDetail.goal_money+store.UserDetail.loan_money-(store.UserDetail.salary-store.UserDetail.consumption)/12*6*(((1+product.month6/100/12)^6-1)^6+1) <= 0">목표 금액을 달성하였습니다!</div>
                    </div>

                    <div class="fw-bold m-2" v-if="best_period==12 && product.type=='단리'">12개월 예상 수익 : {{ parseFloat((((store.UserDetail.salary-store.UserDetail.consumption)/12*12*(1+product.month12/100))).toFixed(2)) }}만원</div>
                    <div class="fw-bold m-2">
                        <div v-if="best_period==12 && product.type=='단리' && store.UserDetail.goal_money+store.UserDetail.loan_money-(store.UserDetail.salary-store.UserDetail.consumption)/12*12*(1+product.month12/100) > 0">12개월 후 남은 목표금액(대출금 포함) : {{ parseFloat(((store.UserDetail.goal_money+store.UserDetail.loan_money-(store.UserDetail.salary-store.UserDetail.consumption)/12*12*(1+product.month12/100))).toFixed(2)) }}만원</div>
                        <div v-if="best_period==12 && product.type=='단리' && store.UserDetail.goal_money+store.UserDetail.loan_money-(store.UserDetail.salary-store.UserDetail.consumption)/12*12*(1+product.month12/100) <= 0">목표금액을 달성하였습니다.</div>
                    </div>

                    <div class="fw-bold m-2" v-if="best_period==12 && product.type=='복리'">12개월 예상 수익 : {{ parseFloat((((store.UserDetail.salary-store.UserDetail.consumption)/12*12*(((1+product.month12/100/12)^12-1)^12+1))).toFixed(2)) }}만원</div>
                    <div class="fw-bold m-2">
                        <div v-if="best_period==12 && product.type=='복리' && store.UserDetail.goal_money+store.UserDetail.loan_money-(store.UserDetail.salary-store.UserDetail.consumption)/12*12*(((1+product.month12/100/12)^12-1)^12+1) > 0">12개월 후 남은 목표금액(대출금 포함) : {{parseFloat((( store.UserDetail.goal_money+store.UserDetail.loan_money-(store.UserDetail.salary-store.UserDetail.consumption)/12*12*(((1+product.month12/100/12)^12-1)^12+1))).toFixed(2)) }}만원</div>
                        <div v-if="best_period==12 && product.type=='복리' && store.UserDetail.goal_money+store.UserDetail.loan_money-(store.UserDetail.salary-store.UserDetail.consumption)/12*12*(((1+product.month12/100/12)^12-1)^12+1) <= 0">목표 금액을 달성하였습니다!</div>
                    </div>

                    <div class="fw-bold m-2" v-if="best_period==24 && product.type=='단리'">24개월 예상 수익 : {{ parseFloat((((store.UserDetail.salary-store.UserDetail.consumption)/12*12*(1+product.month24/100)*2)).toFixed(2)) }}만원</div>
                    <div class="fw-bold m-2">
                        <div v-if="best_period==24 && product.type=='단리' && store.UserDetail.goal_money+store.UserDetail.loan_money-(store.UserDetail.salary-store.UserDetail.consumption)/12*12*(1+product.month24/100)*2 > 0">24개월 후 남은 목표금액(대출금 포함) :  {{ parseFloat(((store.UserDetail.goal_money+store.UserDetail.loan_money-(store.UserDetail.salary-store.UserDetail.consumption)/12*12*(1+product.month24/100)*2)).toFixed(2)) }}만원</div>
                        <div v-if="best_period==24 && product.type=='단리' && store.UserDetail.goal_money+store.UserDetail.loan_money-(store.UserDetail.salary-store.UserDetail.consumption)/12*12*(1+product.month24/100)*2 <= 0">목표금액을 달성하였습니다!</div>
                    </div>

                    <div class="fw-bold m-2" v-if="best_period==24 && product.type=='복리'">24개월 예상 수익 :  {{ parseFloat((((store.UserDetail.salary-store.UserDetail.consumption)/12*24*(((1+product.month24/100/12)^24-1)^24+1))).toFixed(2)) }} 만원</div>
                    <div class="fw-bold m-2">
                        <div v-if="best_period==24 && product.type=='복리' && store.UserDetail.goal_money+store.UserDetail.loan_money-(store.UserDetail.salary-store.UserDetail.consumption)/12*24*(((1+product.month24/100/12)^24-1)^24+1) > 0">24개월 후 남은 목표금액(대출금 포함) :  {{ parseFloat(((store.UserDetail.goal_money+store.UserDetail.loan_money-(store.UserDetail.salary-store.UserDetail.consumption)/12*24*(((1+product.month24/100/12)^24-1)^24+1))).toFixed(2)) }}만원</div>
                        <div v-if="best_period==24 && product.type=='복리' && store.UserDetail.goal_money+store.UserDetail.loan_money-(store.UserDetail.salary-store.UserDetail.consumption)/12*24*(((1+product.month24/100/12)^24-1)^24+1) <= 0">목표금액을 달성하였습니다.</div>
                    </div>
                    <div class="fw-bold m-2" v-if="best_period==36 && product.type=='단리'">36개월 예상 수익 : {{ parseFloat((((store.UserDetail.salary-store.UserDetail.consumption)/12*12*(1+product.month36/100)*3)).toFixed(2)) }}만원</div>
                    <div class="fw-bold m-2">
                        <div v-if="best_period==36 && product.type=='단리' && store.UserDetail.goal_money+store.UserDetail.loan_money-(store.UserDetail.salary-store.UserDetail.consumption)/12*12*(1+product.month36/100)*3 > 0">36개월 후 남은 목표금액(대출금 포함) :  {{ parseFloat(((store.UserDetail.goal_money+store.UserDetail.loan_money-(store.UserDetail.salary-store.UserDetail.consumption)/12*12*(1+product.month36/100)*3)).toFixed(2)) }}만원</div>
                        <div v-if="best_period==36 && product.type=='단리' && store.UserDetail.goal_money+store.UserDetail.loan_money-(store.UserDetail.salary-store.UserDetail.consumption)/12*12*(1+product.month36/100)*3 <= 0">목표금액을 달성하였습니다!</div>
                    </div>

                    <div class="fw-bold m-2" v-if="best_period==36 && product.type=='복리'">36개월 예상 수익 :  {{ parseFloat((((store.UserDetail.salary-store.UserDetail.consumption)/12*36*(((1+product.month36/100/12)^36-1)^36+1))/6.6).toFixed(2)) }} 만원</div>
                    <div class="fw-bold m-2">
                        <div v-if="best_period==36 && product.type=='복리' && store.UserDetail.goal_money+store.UserDetail.loan_money-(store.UserDetail.salary-store.UserDetail.consumption)/12*36*(((1+product.month36/100/12)^36-1)^36+1) > 0">36개월 후 남은 목표금액(대출금 포함) :  {{ parseFloat(((store.UserDetail.goal_money+store.UserDetail.loan_money-(store.UserDetail.salary-store.UserDetail.consumption)/12*36*(((1+product.month24/100/12)^36-1)^36+1))/6.6).toFixed(2)) }}만원</div>
                        <div v-if="best_period==36 && product.type=='복리' && store.UserDetail.goal_money+store.UserDetail.loan_money-(store.UserDetail.salary-store.UserDetail.consumption)/12*36*(((1+product.month36/100/12)^36-1)^36+1) <= 0">목표금액을 달성하였습니다.</div>
                    </div>
                </div>
            </div>
                <button @click.prevent="showgraph1" style="width: 250px;" class="btn btn-primary">{{ show1 ? '그래프 숨기기' : '그래프 보기' }}</button>
                <chart1 v-if="show1" :data3="data3" :data4="data4" :name1="name1" :day="best_period"/>
            </div>

</template>

<script setup>
import { onMounted, ref } from 'vue'
import { useCounterStore } from '../stores/counter'
import { useRouter } from 'vue-router'
import axios from 'axios'
import chart from '../components/chart.vue'
import chart1 from '../components/chart1.vue'
const router = useRouter()
const store = useCounterStore()
const best_period = ref('')
const best_conf = ref('')
const recomment_conf = ref('')
const recomment_day = ref('')
const data1 = ref([])
const data2 = ref([])
const name = ref([])
const data3 = ref([])
const data4 = ref([])
const name1 = ref([])
const show = ref(false)
const show1 = ref(false)
const API_URL = 'http://127.0.0.1:8000'
onMounted(() => {
    store.getUserDetail()
    store.getdeposit()
    console.log(store.data_str.length)
    store.savings.forEach((element) => {
        axios({
            method: 'get',
            url: `${API_URL}/api/v1/products/product-options/${element.fin_prdt_cd}/`
        })
            .then(res => {
                for (let i of res.data) {
                    element['month' + i.save_trm] = i.intr_rate
                    element[i.save_trm] = i.intr_rate
                    element['type'] = i.intr_rate_type_nm
                    element['bestmonth'+i.save_trm] = i.intr_rate2
                }
            })
            .catch((err) => console.log(err))
    })
    best_period.value = store.UserDetail.goal_period
    best_conf.value = store.savings.filter((element) => element.hasOwnProperty(best_period.value))
        .sort((a, b) => b[best_period.value] - a[best_period.value])
        .slice(0, 5)
    if (0.2 <= store.UserDetail.consumption / store.UserDetail.salary && store.UserDetail.consumption / store.UserDetail.salary < 0.4) {
        recomment_day.value = 24
        recomment_conf.value = store.savings.filter((element) => element.hasOwnProperty(24))
            .sort((a, b) => b[24] - a[24])
            .slice(0, 5)
    }
    else if (0.4 <= store.UserDetail.consumption / store.UserDetail.salary && store.UserDetail.consumption / store.UserDetail.salary < 0.6) {
        recomment_day.value = 12
        recomment_conf.value = store.savings.filter((element) => element.hasOwnProperty(12))
            .sort((a, b) => b[12] - a[12])
            .slice(0, 5)
    }
    else if (0.6 <= store.UserDetail.consumption / store.UserDetail.salary) {
        recomment_day.value = 6
        recomment_conf.value = store.savings.filter((element) => element.hasOwnProperty(6))
            .sort((a, b) => b[6] - a[6])
            .slice(0, 5)
    }
})

const goDetail = function(target){
    router.push({name:'productsdetail', params:{cd:target.fin_prdt_cd}})
}

const goprofile = function (UserDetail) {
    router.push({ name: 'updateprofile', params: { username: UserDetail.username } })
}

const del = function (object) {
    store.data_str = store.data_str.filter((element) => element != object)
    store.data = store.data_str.join(',')
    axios({
        method: 'post',
        url: `${API_URL}/accounts/update/${store.UserDetail.id}/`,
        data: {
            financial_products: store.data
        }
    })
        .then((res) => {
            console.log(res.data)
        })
        .catch((err) => {
            console.log(err)
        })
}


const showRecommendations = ref(false);

const toggleRecommendations = () => {
  showRecommendations.value = !showRecommendations.value;
};

const showRecommendations1 = ref(false)

const toggleRecommendations1 = () => {
    showRecommendations1.value = !showRecommendations1.value
    best_period.value = store.UserDetail.goal_period
    best_conf.value = store.savings.filter((element) => element.hasOwnProperty(best_period.value))
        .sort((a, b) => b[best_period.value] - a[best_period.value])
        .slice(0, 5)
}
const showgraph = () => {
    show.value = !show.value
    name.value = []
    data1.value = []
    data2.value = []
    for(let i of recomment_conf.value){
    
        name.value.push(i.fin_prdt_nm)
        if(0.2 <= store.UserDetail.consumption / store.UserDetail.salary && store.UserDetail.consumption / store.UserDetail.salary < 0.4){
        
            if(i.type=='단리'){
        data1.value.push(parseFloat((((store.UserDetail.salary-store.UserDetail.consumption)/12*12*(1+i.month24/100)*2)).toFixed(2)))
        data2.value.push(parseFloat((((store.UserDetail.salary-store.UserDetail.consumption)/12*12*(1+i.bestmonth24/100)*2)).toFixed(2)))
            }
            else if(i.type=='복리'){
        data1.value.push(parseFloat((((store.UserDetail.salary-store.UserDetail.consumption)/12*12*(((1+i.month24/100/12)^24-1)^24+1))).toFixed(2)))
        data2.value.push(parseFloat((((store.UserDetail.salary-store.UserDetail.consumption)/12*12*(((1+i.bestmonth24/100/12)^24-1)^24+1))).toFixed(2)))
            }
        }
        else if (0.4 <= store.UserDetail.consumption / store.UserDetail.salary && store.UserDetail.consumption / store.UserDetail.salary < 0.6) {
            if(i.type=='단리'){
        data1.value.push(parseFloat((((store.UserDetail.salary-store.UserDetail.consumption)/12*12*(1+i.month12/100))).toFixed(2)))
        data2.value.push(parseFloat((((store.UserDetail.salary-store.UserDetail.consumption)/12*12*(1+i.bestmonth12/100))).toFixed(2)))
            }
            else if(i.type=='복리'){
        data1.value.push(parseFloat((((store.UserDetail.salary-store.UserDetail.consumption)/12*12*(((1+i.month12/100/12)^12-1)^12+1))).toFixed(2)))
        data2.value.push(parseFloat((((store.UserDetail.salary-store.UserDetail.consumption)/12*12*(((1+i.month12/100/12)^12-1)^12+1))).toFixed(2)))
            }
        }
        else if (0.6 <= store.UserDetail.consumption / store.UserDetail.salary) {
            if(i.type=='단리'){
        data1.value.push(parseFloat((((store.UserDetail.salary-store.UserDetail.consumption)/12*6*(1+i.month6/100)*0.5)).toFixed(2)))
        data2.value.push(parseFloat((((store.UserDetail.salary-store.UserDetail.consumption)/12*6*(1+i.bestmonth6/100)*0.5)).toFixed(2)))
            }
            else if(i.type=='복리'){
        data1.value.push(parseFloat((((store.UserDetail.salary-store.UserDetail.consumption)/12*6*(((1+i.month6/100/12)^6-1)^6+1))).toFixed(2)))
        data2.value.push(parseFloat((((store.UserDetail.salary-store.UserDetail.consumption)/12*6*(((1+i.bestmonth6/100/12)^6-1)^6+1))).toFixed(2)))
            }
        }
    }
}

const showgraph1 = function() {
    best_period.value = store.UserDetail.goal_period
    best_conf.value = store.savings.filter((element) => element.hasOwnProperty(best_period.value))
        .sort((a, b) => b[best_period.value] - a[best_period.value])
        .slice(0, 5)
    show1.value = !show1.value
    name1.value = []
    data3.value = []
    data4.value = []
    for(let i of best_conf.value){
        console.log(i)
    name1.value.push(i.fin_prdt_nm)
    if(best_period.value==6){
    
        if(i.type=='단리'){
    data3.value.push(parseFloat((((store.UserDetail.salary-store.UserDetail.consumption)/12*6*(1+i.month6/100)*0.5)).toFixed(2)))
    if(parseFloat(((store.UserDetail.goal_money+store.UserDetail.loan_money-(store.UserDetail.salary-store.UserDetail.consumption)/12*6*(1+i.month6/100)*0.5)).toFixed(2)) > 0){
    data4.value.push(parseFloat(((store.UserDetail.goal_money+store.UserDetail.loan_money-(store.UserDetail.salary-store.UserDetail.consumption)/12*6*(1+i.month6/100)*0.5)).toFixed(2)))
    }
    else if(parseFloat(((store.UserDetail.goal_money+store.UserDetail.loan_money-(store.UserDetail.salary-store.UserDetail.consumption)/12*6*(1+i.month6/100)*0.5)).toFixed(2)) <= 0){
        data4.value.push(0)
    }
        }
        else if(i.type=='복리'){
    data3.value.push(parseFloat((((store.UserDetail.salary-store.UserDetail.consumption)/12*6*(((1+i.month6/100/12)^6-1)^6+1))).toFixed(2)))
    if(parseFloat(((store.UserDetail.goal_money+store.UserDetail.loan_money-(store.UserDetail.salary-store.UserDetail.consumption)/12*6*(((1+i.month6/100/12)^6-1)^6+1))).toFixed(2)) > 0){
    data4.value.push(parseFloat(((store.UserDetail.goal_money+store.UserDetail.loan_money-(store.UserDetail.salary-store.UserDetail.consumption)/12*6*(((1+i.month6/100/12)^6-1)^6+1))).toFixed(2)))
    }
    else if(parseFloat(((store.UserDetail.goal_money+store.UserDetail.loan_money-(store.UserDetail.salary-store.UserDetail.consumption)/12*6*(((1+i.month6/100/12)^6-1)^6+1))).toFixed(2)) <= 0){
        data4.value.push(0)
    }
        }
        }

    else if (best_period.value==12) {
        if(i.type=='단리'){
    data3.value.push(parseFloat((((store.UserDetail.salary-store.UserDetail.consumption)/12*12*(1+i.month12/100))).toFixed(2)))
    if(parseFloat(((store.UserDetail.goal_money+store.UserDetail.loan_money-(store.UserDetail.salary-store.UserDetail.consumption)/12*12*(1+i.month12/100))).toFixed(2)) > 0){
    data4.value.push(parseFloat((((store.UserDetail.salary-store.UserDetail.consumption)/12*12*(1+i.bestmonth12/100))).toFixed(2)))
        }
    else if(parseFloat(((store.UserDetail.goal_money+store.UserDetail.loan_money-(store.UserDetail.salary-store.UserDetail.consumption)/12*12*(1+i.month12/100))).toFixed(2)) <= 0){
        data4.value.push(0)
    }
}
        else if(i.type=='복리'){
    data3.value.push(parseFloat((((store.UserDetail.salary-store.UserDetail.consumption)/12*12*(((1+i.month12/100/12)^12-1)^12+1))).toFixed(2)))
    if(parseFloat((( store.UserDetail.goal_money+store.UserDetail.loan_money-(store.UserDetail.salary-store.UserDetail.consumption)/12*12*(((1+i.month12/100/12)^12-1)^12+1))).toFixed(2)) > 0){
        data4.value.push(parseFloat((( store.UserDetail.goal_money+store.UserDetail.loan_money-(store.UserDetail.salary-store.UserDetail.consumption)/12*12*(((1+i.month12/100/12)^12-1)^12+1))).toFixed(2)))
    }
    else if(parseFloat((( store.UserDetail.goal_money+store.UserDetail.loan_money-(store.UserDetail.salary-store.UserDetail.consumption)/12*12*(((1+i.month12/100/12)^12-1)^12+1))).toFixed(2)) <=0){
        data4.value.push(0)
    }
    
    }
    }

    else if (best_period.value==24) {
        if(i.type=='단리'){
    data3.value.push(parseFloat((((store.UserDetail.salary-store.UserDetail.consumption)/12*12*(1+i.month24/100)*2)).toFixed(2)))
    if(parseFloat(((store.UserDetail.goal_money+store.UserDetail.loan_money-(store.UserDetail.salary-store.UserDetail.consumption)/12*12*(1+i.month24/100)*2)).toFixed(2)) > 0){
    data4.value.push(parseFloat(((store.UserDetail.goal_money+store.UserDetail.loan_money-(store.UserDetail.salary-store.UserDetail.consumption)/12*12*(1+i.month24/100)*2)).toFixed(2)))
    }
    else if(parseFloat(((store.UserDetail.goal_money+store.UserDetail.loan_money-(store.UserDetail.salary-store.UserDetail.consumption)/12*12*(1+i.month24/100)*2)).toFixed(2)) <= 0){
        data4.value.push(0)
    }
        }
        else if(i.type=='복리'){
    data3.value.push(parseFloat((((store.UserDetail.salary-store.UserDetail.consumption)/12*24*(((1+i.month24/100/12)^24-1)^24+1))).toFixed(2)))
    if(parseFloat(((store.UserDetail.goal_money+store.UserDetail.loan_money-(store.UserDetail.salary-store.UserDetail.consumption)/12*24*(((1+i.month24/100/12)^24-1)^24+1))).toFixed(2)) > 0){
    data4.value.push(parseFloat(((store.UserDetail.goal_money+store.UserDetail.loan_money-(store.UserDetail.salary-store.UserDetail.consumption)/12*24*(((1+i.month24/100/12)^24-1)^24+1))).toFixed(2)))
    }
    else if(parseFloat(((store.UserDetail.goal_money+store.UserDetail.loan_money-(store.UserDetail.salary-store.UserDetail.consumption)/12*24*(((1+i.month24/100/12)^24-1)^24+1))).toFixed(2)) <= 0){
        data4.value.push(0)
    }
        }
    }


    else if (best_period.value==36){
        if(i.type=='단리'){
    data3.value.push(parseFloat((((store.UserDetail.salary-store.UserDetail.consumption)/12*12*(1+i.month36/100)*3)).toFixed(2)))
    if(parseFloat(((store.UserDetail.goal_money+store.UserDetail.loan_money-(store.UserDetail.salary-store.UserDetail.consumption)/12*12*(1+i.month36/100)*3)).toFixed(2)) > 0){
    data4.value.push(parseFloat(((store.UserDetail.goal_money+store.UserDetail.loan_money-(store.UserDetail.salary-store.UserDetail.consumption)/12*12*(1+i.month36/100)*3)).toFixed(2)))
    }
    else if(parseFloat(((store.UserDetail.goal_money+store.UserDetail.loan_money-(store.UserDetail.salary-store.UserDetail.consumption)/12*12*(1+i.month36/100)*3)).toFixed(2)) <= 0){
        data4.value.push(0)
    }
        }
        else if(i.type=='복리'){
    data3.value.push(parseFloat((((store.UserDetail.salary-store.UserDetail.consumption)/12*36*(((1+i.month36/100/12)^36-1)^36+1))/6.6).toFixed(2)))
    if(parseFloat(((store.UserDetail.goal_money+store.UserDetail.loan_money-(store.UserDetail.salary-store.UserDetail.consumption)/12*36*(((1+i.month36/100/12)^36-1)^36+1))).toFixed(2)) > 0){
    data4.value.push(parseFloat(((store.UserDetail.goal_money+store.UserDetail.loan_money-(store.UserDetail.salary-store.UserDetail.consumption)/12*36*(((1+i.month36/100/12)^36-1)^36+1)/10)).toFixed(2)))
    }
    else if(parseFloat(((store.UserDetail.goal_money+store.UserDetail.loan_money-(store.UserDetail.salary-store.UserDetail.consumption)/12*36*(((1+i.month24/100/12)^36-1)^36+1))).toFixed(2)) <= 0){
        data4.value.push(0)
    }
        }

    }
    console.log(data4.value)
}
}
</script>

<style scoped>

.product-container {
  padding: 20px;
  border-radius: 10px;
  border: 1px solid #ccc;
}

.profile-title {
    text-align: center;
    font-size: 24px;
    margin-top: 10px;
    margin-bottom: 20px;
}

.btn-primary {
    margin-bottom: 20px;
    margin-left: 20px;
}

.btn-danger {

}

.profile-info {
    margin-top: 20px;
    margin-bottom: 20px;
}

.d-flex {
    margin-left: 20px;
    margin-top: 10px;
    align-items: flex-start;
}


/* 추가한 스타일 */
.financial-product {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-top: 20px;
    font-weight: bold;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
}

.gray-bg {
    background-color: #ccc;
    /* Gray background color */
}

.white-bg {
    background-color: #ccc;
    /* White background color */
}

.line {
    border: 1px solid #3498db;
    margin: 20px auto;
}

</style>

<style>
h1{
    font-weight: bold;
}

h2{
    font-weight: bold;
}
</style>