import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Warningの非表示
# st.set_option('deprecation.showPyplotGlobalUse', False)

# グラフを描画する


def plot_graph():
    fig, ax = plt.subplots()
    ax.scatter([1, 2, 3], [1, 2, 3])

    st.pyplot(fig)


# グラフを表示するボタンを表示する
if st.button('Plot graph'):
    plot_graph()
