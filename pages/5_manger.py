import streamlit as st
import pandas as pd
import tempfile

# 관리자 아이디와 비밀번호
admin_username = "1234"
admin_password = "1234"

# 랭킹 데이터
ranking_data = {
    '연도': [2020, 2021, 2022, 2023],
    '선수': ['Giannis Antetokounmpo', 'Nikola Jokic', 'Nikola Jokic', 'Joel Embiid'],
    '팀': ['Milwaukee Bucks', 'Denver Nuggets', 'Denver Nuggets', 'Philadelphia 76ers'],
    '평균 득점': [29.5, 26.4, 27.1, 30.6],
    '평균 어시스트': [5.6, 8.3, 7.9, 4.2],
    '평균 리바운드': [13.6, 10.8, 13.8, 11.7]
}
df_ranking = pd.DataFrame(ranking_data)

# 로그인 함수
def login(username, password):
    if username == admin_username and password == admin_password:
        return True
    else:
        return False

# 메인 함수
def main():
    st.title("랭킹 페이지 다운로드")
    
    # 로그인 폼
    username = st.sidebar.text_input("아이디")
    password = st.sidebar.text_input("비밀번호", type="password")
    login_button = st.sidebar.button("로그인")

    if login_button:
        if login(username, password):
            st.success("로그인 성공!")
            st.write("랭킹 페이지 다운로드:")
            st.write(df_ranking)
            
            # Excel 파일을 임시로 저장
            with tempfile.NamedTemporaryFile(delete=False, suffix='.xlsx') as temp:
                df_ranking.to_excel(temp.name, index=False)
                with open(temp.name, 'rb') as f:
                    data = f.read()
                st.download_button(
                    label="엑셀로 다운로드",
                    data=data,
                    file_name='ranking.xlsx',
                    mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
                )
        else:
            st.error("아이디 또는 비밀번호가 잘못되었습니다.")

if __name__ == '__main__':
    main()
