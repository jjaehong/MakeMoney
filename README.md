# final-pjt : 금융 상품 비교 애플리케이션




#### 1. 팀원 정보 및 업무 분담 내역

- 승재홍 : Backend(Django)

- 정구민 : front end(Vue)


#### 2. 서비스 기획 설계 내용

1. 무엇을 개발할 것인가?

    - 서비스 목표 : 고객님의 목표 금액 마련을 도와주는 적금 상품추천 서비스

    - 서비스 내용 :
    
        1. 프로필 페이지
        
        - 회원가입한 유저의 프로필을 보면 유저의 개인정보를 입력하는 폼이 있다. 그 중 연봉(소득), 연 소비 금액, 목표 금액을 입력하면 고객의 소비성향과 저축성향을 알 수 있다. (소득 = 저축 + 소비) (1 = 저축성향(저축/소득) + (소비/소득))

        - 소비자의 저축성향을 바탕으로 분류한다.

            - 높은 저축 성향 : 저축 성향 >= 0.6
            - 평균 저축 성향 : 0.2 <= 저축 성향 <0.6 
            - 낮은 저축 성향 : 저축 성향 < 0.2
        
        - 높은 저축성향을 가진 고객은 24개월 장기 적금 중 가장 높은 금리 5 상품을 추천해준다.
        - 평균 저축성향을 가진 고객은 12개월 중장기 적금 중 가장 높은 금리 5 상품을 추천해준다.
        - 낮은 저축성향을 가진 고객은 6개월 단기 적금 중 가장 높은 금리 5 상품을 추천해준다.
         

2. 왜 개발하는 것인가?

   - (어떤 서비스를 제공해서 고객에게 어떤 편리함을 느끼게 할 것인가? )
   
   - 서비스 목표 : 금융상품(예적금/대출) 비교를 통해서 가장 값싸게 내 집 마련하자(추세선 가능 ?)
   
   - 주요 고객 선정 : **내 집 마련**을 꿈꾸는 사회 초년생 -> **자산 증식**
        24, 12, 6


#### 3. 실제 구현정도



#### 3. 데이터베이스 모델링(ERD)


#### 4. 금융상품 추천 알고리즘에 대한 기술적 설명




#### 5. 서비스 대표 기능에 대한 설명

1. 예적금 상품 정보


2. 환율 정보


3. 지도


4. Community


5. 프로필


6. 네이버 증권

#### 6. 기타(느낀 점, 후기)










#### 0. PJT 기획

1. 무엇을 개발할 것인가?
   
   - 목표 금액 마련에 대한 최적의 설계    

   - 목표금액(내 집 마련, 목돈 마련), 기간(몇 년 안에 모을 건지), 고객의 자산 / 연봉 / 소비 / 저축성향? / 가입된 상품 목록,
   
   - 계산 : 목표금액 - 현재 고객의 자산 =  (연봉 - 연평균소비) * 목표기간 + 대출 금액
   
   - 추천 알고리즘
     
     - 예적금 : (연봉 - 연평균소비) => 예적금 기간에 따른 분류 / 높은 금리
   
     - 대출 : 본인이 가입한 대출상품보다 저금리 상품이 있으면 목록 보여주고 상향 추천하기 -> **대출 갈아타기**


   - user 추가 필드 : 목표금액, 기간, 연평균 소비, 신용등급(개인신용대출)
   
   - if 연봉 < 연평균소비 ==> alert('소비를 줄이셔야 합니다., 이런식으론 집 못삽니다.') 
    


2. 왜 개발하는 것인가?

   - (어떤 서비스를 제공해서 고객에게 어떤 편리함을 느끼게 할 것인가? )
   
   - 서비스 목표 : 금융상품(예적금/대출) 비교를 통해서 가장 값싸게 내 집 마련하자(추세선 가능 ?)
   
   - 주요 고객 선정 : **내 집 마련**을 꿈꾸는 사회 초년생 -> **자산 증식**


3. 어떻게 개발할 것인가?

   - 기술스택 : django, vue, python, javaScript
   


- draw.io : ERD 그리기
- figma : 화면 프로토타입

- 주요 고객 : 은행에 갈 시간이 없어 금융정보를 한 곳에 알 수 있는 웹 애플리케이션


#### 1. 메인 기능

1. 금융 상품 카테고리(금융상품 비교공시 API)
    
    - 예적금 API(몇 주 마다 데이터 갱신) : 금리 높은 것 추천 

    - 대출 상품 API(주담대, 전세자금대출, 개인신용대출) == 사용자 개인의 상황에 따라서 

    - **나에게 맞는 상품 추천 알고리즘**


2. 환율정보(한국수출입은행 환율정보 API)


3. 근처 은행, 근처 부동산 가격 검색(카카오 MAP API)



4. 커뮤니티

   1. 게시판 구현(게시글 CRUD, 댓글 CRUD)

       - 무슨 글 작성? : 칼럼, 
   
   2. 회원 커스터 마이징 :
 
       - 회원 관리(회원가입, 로그인, 로그아웃) 

       - **커스텀 User 구현**
   
   3. profile :


5. 네이버 증권




#### 2. 필수 요구사항


1. 메인페이지

    - 각 팀의 서비스를 소개할 수 있도록 메인 페이지 구성
    
    - 금융상품 / 환율 정보 / 근처 은행(부동산 가능?) / 커뮤니티 / 네이버 증권으로 옮겨가기

        - 프로필
        - 금융 상품 :(예적금 / 대출상품)  
        - 환율 정보 : 환율정보, 환율계산기
        - 지도 : 근처 은행 맵 표시
        - 커뮤니티 : 게시판, 댓글
        - 네이버 증권 이동

2. 회원 커스터마이징

    - 회원관리(회원가입, 로그인, 로그아웃 등 구성)
    - HOME화면



3. 예적금 금리비교

    1. 전체 조회


    2. 상세조회


4. 환율 계산기


5. 근처 은행 검색


6. 커뮤니티(게시판)



7. 프로필 페이지 - 금융상품 추천 알고리즘


8. README


9. 기타