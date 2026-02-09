import streamlit as st
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import datetime

# --- 1. データベース設定 ---
def init_db():
    # SQLiteデータベースに接続（ファイルがなければ作成される）
    conn = sqlite3.connect('health_data.db')
    c = conn.cursor()
    # テーブル作成（日付と体重）
    c.execute('''
        CREATE TABLE IF NOT EXISTS weight_logs (
            date TEXT PRIMARY KEY,
            weight REAL
        )
    ''')
    conn.commit()
    conn.close()

# データの挿入・更新用関数
def save_data(date, weight):
    conn = sqlite3.connect('health_data.db')
    c = conn.cursor()
    # 日付が重複していれば更新、なければ挿入
    c.execute('INSERT OR REPLACE INTO weight_logs (date, weight) VALUES (?, ?)', (date, weight))
    conn.commit()
    conn.close()

# データの読み込み用関数
def load_data():
    conn = sqlite3.connect('health_data.db')
    # SQLの結果をそのままPandas DataFrameとして読み込む
    df = pd.read_sql_query("SELECT * FROM weight_logs ORDER BY date ASC", conn)
    conn.close()
    return df

# --- 2. メインアプリ処理 ---
def main():
    st.title("🏃 体重管理ダッシュボード")
    init_db()

    # サイドバー：データ入力
    st.sidebar.header("データ入力")
    input_date = st.sidebar.date_input("日付を選択", datetime.date.today())
    input_weight = st.sidebar.number_input("体重 (kg)", min_value=30.0, max_value=150.0, value=65.0, step=0.1)
    
    if st.sidebar.button("記録を保存"):
        save_data(str(input_date), input_weight)
        st.sidebar.success("保存しました！")
        # 画面をリロードしてグラフを更新
        st.rerun()

    # メイン画面：データ表示とグラフ
    df = load_data()

    if not df.empty:
        # カラムを分けて表示
        col1, col2 = st.columns([1, 2])

        with col1:
            st.subheader("履歴データ")
            # 表を表示（インデックスを非表示に）
            st.dataframe(df, hide_index=True)

        with col2:
            st.subheader("推移グラフ")
            # --- Matplotlibによる描画 ---
            fig, ax = plt.subplots()
            ax.plot(df['date'], df['weight'], marker='o', linestyle='-', color='royalblue')
            ax.set_xlabel("日付")
            ax.set_ylabel("体重 (kg)")
            plt.xticks(rotation=45) # 日付が見えやすいように斜めにする
            
            # Streamlit上でMatplotlibの図を表示
            st.pyplot(fig)
    else:
        st.info("サイドバーからデータを入力してください。")

if __name__ == "__main__":
    main()