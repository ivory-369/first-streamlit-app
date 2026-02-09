import streamlit as st  # 各ファイルで必ずインポートが必要

st.set_page_config(page_title="BMI計算ツール")  # ページごとにタイトル設定可能
st.title("⚖️ BMI計算ツール")

st.write("数値を入力するだけで、即座に健康状態を判定します。")

# 入力欄の作成
col1, col2 = st.columns(2)
with col1:
    weight = st.number_input("体重 (kg)", min_value=1.0, value=60.0, step=0.1)
with col2:
    height = st.number_input("身長 (cm)", min_value=1.0, value=170.0, step=0.1)

if st.button("判定する"):
    # BMI計算
    height_m = height / 100
    bmi = weight / (height_m ** 2)

    st.divider()  # 区切り線
    st.metric(label="あなたのBMI", value=f"{bmi:.2f}")

    if bmi < 18.5:
        st.warning("判定：低体重（痩せ型）")
    elif bmi < 25:
        st.success("判定：普通体重")
    else:
        st.error("判定：肥満")
