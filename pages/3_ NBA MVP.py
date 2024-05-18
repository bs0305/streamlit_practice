import streamlit as st
import pandas as pd

# 샘플 데이터 생성
data_mvp = {
    '연도': [2020, 2021, 2022, 2023],
    '선수': ['Giannis Antetokounmpo', 'Nikola Jokic', 'Nikola Jokic', 'Joel Embiid'],
    '팀': ['Milwaukee Bucks', 'Denver Nuggets', 'Denver Nuggets', 'Philadelphia 76ers'],
    '평균 득점': [29.5, 26.4, 27.1, 30.6],
    '평균 어시스트': [5.6, 8.3, 7.9, 4.2],
    '평균 리바운드': [13.6, 10.8, 13.8, 11.7]
}

df_mvp = pd.DataFrame(data_mvp)

# 데이터프레임 표시
st.write("### NBA 역대 MVP 선수들")
st.dataframe(df_mvp)

# 득점, 어시스트, 리바운드 그래프
st.write("### 평균 득점")
st.bar_chart(df_mvp.set_index('연도')['평균 득점'])

st.write("### 평균 어시스트")
st.bar_chart(df_mvp.set_index('연도')['평균 어시스트'])

st.write("### 평균 리바운드")
st.bar_chart(df_mvp.set_index('연도')['평균 리바운드'])

# 선수별 상세 정보 표시
st.write("### 선수별 상세 정보")
selected_year = st.selectbox("연도 선택", df_mvp['연도'])

selected_player = df_mvp[df_mvp['연도'] == selected_year]
if not selected_player.empty:
    player_name = selected_player.iloc[0]['선수']
    player_team = selected_player.iloc[0]['팀']
    player_points = selected_player.iloc[0]['평균 득점']
    player_assists = selected_player.iloc[0]['평균 어시스트']
    player_rebounds = selected_player.iloc[0]['평균 리바운드']

    st.write(f"**선수**: {player_name}")
    st.write(f"**팀**: {player_team}")
    st.write(f"**평균 득점**: {player_points}")
    st.write(f"**평균 어시스트**: {player_assists}")
    st.write(f"**평균 리바운드**: {player_rebounds}")