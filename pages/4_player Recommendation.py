import streamlit as st
import pandas as pd
import random

# 선수 데이터
player_data = {
    '이름': ['이강인', '손흥민', '메시', '호날두', '케인', '쿠바니'],
    '팀': ['헤르타 베를린', '토트넘', '파리 생제르망', '맨체스터 유나이티드', '토트넘', '레알 마드리드'],
    '포지션': ['미드필더', '공격수', '공격수', '공격수', '공격수', '미드필더'],
    '나이': [21, 29, 34, 36, 28, 29],
    '경기 수': [105, 318, 778, 798, 380, 436],
    '골 수': [13, 116, 676, 679, 221, 64],
}

player_df = pd.DataFrame(player_data)

# 랜덤 선수 선택 함수
def select_random_player():
    return random.choice(player_df['이름'])

# 랜덤 선수 정보 표시 함수
def show_random_player_info():
    selected_player = select_random_player()
    player_info = player_df[player_df['이름'] == selected_player]
    st.write(f"## {selected_player} 선수 정보")
    st.write(f"**팀**: {player_info['팀'].values[0]}")
    st.write(f"**포지션**: {player_info['포지션'].values[0]}")
    st.write(f"**나이**: {player_info['나이'].values[0]}")
    st.write(f"**경기 수**: {player_info['경기 수'].values[0]}")
    st.write(f"**골 수**: {player_info['골 수'].values[0]}")

# Streamlit 애플리케이션 구성
st.title("랜덤 선수 정보")
st.write("아래 버튼을 누르면 랜덤한 선수의 정보를 확인할 수 있습니다.")
if st.button("랜덤 선수 선택"):
    show_random_player_info()