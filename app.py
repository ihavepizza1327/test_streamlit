import streamlit as st 

st.title("Конверт валют")

col1, col2 = st.columns(2)
x = col1.number_input("", min_value=0.0, value=1.0, step=1.0)
# rate = 88.67
rates = {"USD": 88.67, "KZT": 0.18}
# st.write(f'{x * rate} RUB')
currency = col2.selectbox("Валюта", list(rates))
# st.success(f'{x * rate} RUB')# warning error меняется цвет\
st.success(f"{x * rates[currency]: .2f} RUB")
