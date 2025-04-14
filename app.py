import streamlit as st
import openai
import os

st.set_page_config(page_title="AI 冷知識卡", page_icon="💡")

openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("今天的冷知識卡 💡")

product = st.selectbox(
    "請選擇一項商品或主題：",
    ["雞胸肉", "瑜伽墊", "鮭魚", "高蛋白粉", "彈力帶"]
)

if st.button("產生冷知識"):
    prompt = f"請針對「{product}」生成一段有趣的冷知識，約 30 字內。內容要生活化、有趣，讓人願意分享。"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    output = response.choices[0].message.content.strip()
    st.success(f"你知道嗎？\n\n{output}")
