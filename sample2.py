import streamlit as st

# タイトルを表示
st.title("Streamlit デモアプリ")
# テキストを表示
st.write("こんにちは！これは最初のステップです。")
st.write("計算もできる。3×2=")
st.write(3*2)

# タイトルを表示
st.title("入力の取得")

# テキスト入力
name = st.text_input("お名前を教えてください")
# 数値入力（スライダー）
age = st.slider("年齢を選択", 0, 100, 25)

if name:
    st.write(f"{name}さん（{age}歳）、ようこそ！")


st.title("ボタンの利用")

if st.button("おみくじを引く"):
    # ボタンが押されたときだけ実行
    st.balloons() # お祝いのアニメーション
    st.success("大吉です！")


st.title("選択UI:選択肢（セレクトボックス・ラジオボタン）")
# セレクトボックス
option = st.selectbox(
    "好きなフルーツは？",
    ["りんご", "バナナ", "メロン"]
)

# ラジオボタン
size = st.radio("サイズを選択", ["S", "M", "L"])

st.write(f"選んだのは: {option} の {size} サイズです。")

import pandas as pd

st.title("データの表示")

df = pd.DataFrame({
    '名前': ['田中', '佐藤', '鈴木'],
    '得点': [85, 92, 78]
})

# インタラクティブなテーブル
st.dataframe(df)
# 静的なテーブル
st.table(df)

# サイドバーにタイトル
st.sidebar.title("設定メニュー")

# サイドバーに入力項目を追加
user_id = st.sidebar.text_input("ID入力")
mode = st.sidebar.selectbox("モード", ["閲覧", "編集"])

st.write(f"メイン画面：現在のモードは {mode} です。")



st.title("レイアウト分割")
# 2つのカラムを作成
col1, col2 = st.columns(2)

with col1:
    st.header("左側")
    st.write("ここには画像や説明を入れます。")

with col2:
    st.header("右側")
    st.button("右側のボタン")


st.title("ファイルアップロード")
uploaded_file = st.file_uploader("CSVファイルを選択してください", type='csv')

if uploaded_file is not None:
    # アップロードされたファイルを読み込む
    df = pd.read_csv(uploaded_file)
    st.write("プレビュー:")
    st.dataframe(df.head())


st.title("カウンター（状態保持）")
# セッション状態を初期化
if 'count' not in st.session_state:
    st.session_state.count = 0

increment = st.button('カウントアップ')
if increment:
    st.session_state.count += 1

st.write(f"現在のカウント: {st.session_state.count}")