import streamlit as st
import pandas as pd
import altair as alt

# 100m 달리기 데이터
data_100m = {
    '연도': [2000, 2004, 2008, 2012, 2016, 2020],
    '선수': ['Maurice Greene', 'Justin Gatlin', 'Usain Bolt', 'Usain Bolt', 'Usain Bolt', 'Lamont Marcell Jacobs'],
    '기록(초)': [9.87, 9.85, 9.69, 9.63, 9.81, 9.80]
}
df_100m = pd.DataFrame(data_100m)

# 마라톤 데이터
data_marathon = {
    '연도': [2000, 2004, 2008, 2012, 2016, 2020],
    '선수': ['Gezahegne Abera', 'Stefano Baldini', 'Samuel Wanjiru', 'Stephen Kiprotich', 'Eliud Kipchoge', 'Eliud Kipchoge'],
    '기록(분)': [130, 130, 126, 128, 128, 128]
}
df_marathon = pd.DataFrame(data_marathon)

# 수영 100m 자유형 데이터
data_swimming = {
    '연도': [2000, 2004, 2008, 2012, 2016, 2020],
    '선수': ['Pieter van den Hoogenband', 'Pieter van den Hoogenband', 'Alain Bernard', 'Nathan Adrian', 'Kyle Chalmers', 'Caeleb Dressel'],
    '기록(초)': [48.30, 48.17, 47.21, 47.52, 47.58, 47.02]
}
df_swimming = pd.DataFrame(data_swimming)

# 높이뛰기 데이터
data_high_jump = {
    '연도': [2000, 2004, 2008, 2012, 2016, 2020],
    '선수': ['Sergey Klyugin', 'Stefan Holm', 'Andrey Silnov', 'Ivan Ukhov', 'Derek Drouin', 'Gianmarco Tamberi/Mutaz Essa Barshim'],
    '기록(미터)': [2.35, 2.36, 2.36, 2.38, 2.38, 2.37]
}
df_high_jump = pd.DataFrame(data_high_jump)

# 각 종목의 데이터프레임과 차트를 Streamlit에 표시
st.write("### 올림픽 100m 달리기 남자 결승 역대 금메달리스트 기록")
st.dataframe(df_100m)
st.altair_chart(alt.Chart(df_100m).mark_line().encode(
    x='연도',
    y=alt.Y('기록(초)', scale=alt.Scale(domain=[9, 10])), # y축 범위 및 간격 조정
    tooltip=['선수', '연도', '기록(초)']
).properties(width=600, height=300))

st.write("### 올림픽 마라톤 남자 결승 역대 금메달리스트 기록")
st.dataframe(df_marathon)
st.altair_chart(alt.Chart(df_marathon).mark_line().encode(
    x='연도',
    y=alt.Y('기록(분)', scale=alt.Scale(domain=[120, 140])), # y축 범위 및 간격 조정
    tooltip=['선수', '연도', '기록(분)']
).properties(width=600, height=300))

st.write("### 올림픽 수영 100m 자유형 남자 결승 역대 금메달리스트 기록")
st.dataframe(df_swimming)
st.altair_chart(alt.Chart(df_swimming).mark_line().encode(
    x='연도',
    y=alt.Y('기록(초)', scale=alt.Scale(domain=[46, 50])), # y축 범위 및 간격 조정
    tooltip=['선수', '연도', '기록(초)']
).properties(width=600, height=300))

st.write("### 올림픽 높이뛰기 남자 결승 역대 금메달리스트 기록")
st.dataframe(df_high_jump)
st.altair_chart(alt.Chart(df_high_jump).mark_line().encode(
    x='연도',
    y=alt.Y('기록(미터)', scale=alt.Scale(domain=[2.3, 2.4])), # y축 범위 및 간격 조정
    tooltip=['선수', '연도', '기록(미터)']
).properties(width=600, height=300))
