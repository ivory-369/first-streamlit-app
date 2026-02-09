import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="データ分析サンプル")
st.title("📈 データ分析サンプル")
st.write("ランダムなデータを生成して、グラフをリアルタイム表示します。")

# サンプルデータの作成
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['商品A', '商品B', '商品C']
)

# 折れ線グラフの表示
st.line_chart(chart_data)

st.write("このように、Pandasと連携して簡単に可視化が可能です。")
