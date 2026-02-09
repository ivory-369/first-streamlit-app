import streamlit as st

st.set_page_config(page_title="メインポータル", layout="wide")  # レイアウトを広く使う
st.title("🌟 Pythonエンジニア ポートフォリオ")

# 1. 自己紹介セクション
st.sidebar.success("メニューからアプリを選択してください")  # サイドバーに案内

col1, col2 = st.columns([1, 2])
with col1:
    st.image("https://via.placeholder.com/150",
             caption="Your Photo")  # 後で自分の写真やアイコンに変更

with col2:
    st.header("自己紹介")
    st.write("Pythonを学習中の[あなたの名前]です。実務に役立つツール開発を目指しています。")

# 2. 自分の強みをアピール
st.header("スキルセット")
st.code("Python, Pandas, Streamlit, Git")

# 3. リンク集
st.header("外部リンク")
st.markdown("[GitHub](https://github.com/あなたのユーザー名)")
st.markdown("[技術ブログ/Qiita](https://qiita.com/)")
