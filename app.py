import streamlit as st
import openai
from datetime import date

st.set_page_config(page_title="나의 사주 운세", page_icon="🔮")

st.title("🔮 나의 사주 운세 테스트 앱")

api_key = st.text_input("🔑 OpenAI API 키를 입력하세요", type="password")
if not api_key:
    st.stop()

openai.api_key = api_key

st.subheader("회원 정보 입력")

email = st.text_input("이메일")

# 날짜 범위 설정: 1900년 ~ 오늘
birth_date = st.date_input(
    "생년월일",
    min_value=date(1900, 1, 1),
    max_value=date.today()
)

birth_time = st.time_input("출생 시각")
birth_place = st.text_input("출생 지역 (예: 서울특별시)")

if st.button("오늘의 사주 운세 보기"):
    prompt = f"""
    당신은 사주 명리학 전문가입니다.
    사용자의 생년월일은 {birth_date}, 출생 시각은 {birth_time}, 출생지는 {birth_place}입니다.
    오늘의 기운을 사주 명리학적으로 해석하여 약 200자 내외로 현실적인 조언 중심으로 써 주세요.
    """

    with st.spinner("운세를 계산 중입니다..."):
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )

    st.success("✨ 오늘의 운세 ✨")
    st.write(response.choices[0].message["content"])
