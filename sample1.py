import streamlit as st

# タイトルの表示
st.title("私の初めてのStreamlitアプリ")
st.title("私の初めてのStreamlitアプリ")


# テキスト入力
name = st.text_input("お名前を教えてください")
name2 = st.text_input("お名前を教えてください")

# ボタンと反応
if st.button("挨拶する"):
    st.success(f"こんにちは、{name}さん！これはPythonで動いています。")