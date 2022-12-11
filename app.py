# -*- coding: utf-8 -*-

import streamlit as st
import numpy as np
import pandas as pd

st.title("Web Application")
data = {
    'lat': np.random.randn(200) / 100 + 35.68,
    'lon': np.random.randn(200) / 100 + 139.75,
}
map_data = pd.DataFrame(data)
# 地図に散布図を描く
st.map(map_data)