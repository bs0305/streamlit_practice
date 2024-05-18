import streamlit as st
import pandas as pd

# 최신 시즌 데이터 생성 (예시 데이터)
data_mvp = {
    '순위': [1, 2, 3, 4, 5],
    '연도': [2024, 2024, 2024, 2024, 2024],
    '선수': ['Nikola Jokic', 'Joel Embiid', 'Giannis Antetokounmpo', 'Luka Doncic', 'Kevin Durant'],
    '팀': ['Denver Nuggets', 'Philadelphia 76ers', 'Milwaukee Bucks', 'Dallas Mavericks', 'Phoenix Suns'],
    '평균 득점': [28.0, 30.6, 29.5, 27.4, 26.7],
    '평균 어시스트': [8.1, 4.2, 5.6, 8.8, 5.4],
    '평균 리바운드': [12.3, 11.7, 13.6, 9.5, 7.3]
}

df_mvp = pd.DataFrame(data_mvp)

# 득점, 어시스트, 리바운드 그래프
st.write("### 평균 득점")
st.line_chart(df_mvp.set_index('선수')['평균 득점'])

st.write("### 평균 어시스트")
st.line_chart(df_mvp.set_index('선수')['평균 어시스트'])

st.write("### 평균 리바운드")
st.line_chart(df_mvp.set_index('선수')['평균 리바운드'])

# 선수별 상세 정보 표시
st.write("### 선수별 상세 정보")
selected_player = st.selectbox("선수 선택", df_mvp['선수'])

selected_data = df_mvp[df_mvp['선수'] == selected_player]
if not selected_data.empty:
    player_name = selected_data.iloc[0]['선수']
    player_team = selected_data.iloc[0]['팀']
    player_points = selected_data.iloc[0]['평균 득점']
    player_assists = selected_data.iloc[0]['평균 어시스트']
    player_rebounds = selected_data.iloc[0]['평균 리바운드']

    st.write(f"**선수**: {player_name}")
    st.write(f"**팀**: {player_team}")
    st.write(f"**평균 득점**: {player_points}")
    st.write(f"**평균 어시스트**: {player_assists}")
    st.write(f"**평균 리바운드**: {player_rebounds}")
