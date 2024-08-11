import streamlit as st

# 로그인 상태 초기화
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

# 로그인 실패 상태 초기화
if 'login_failed' not in st.session_state:
    st.session_state['login_failed'] = False

# 페이지 상태 초기화
if 'page' not in st.session_state:
    st.session_state['page'] = None


# 로그인 검증 함수
def validate_login(username, password):
    if username == "admin" and password == "admin1818":
        return True
    elif username.startswith("SJ"):
        digit_sum = sum(int(d) for d in password)
        if digit_sum % 10 == 0:
            return True
    elif username.startswith("HW"):
        digit_sum = sum(int(d) for d in password)
        if digit_sum % 10 == 1:
            return True
    elif username.startswith("SH"):
        digit_sum = sum(int(d) for d in password)
        if digit_sum % 10 == 2:
            return True
    return False


# 로그인 폼
def login():
    st.sidebar.title("로그인")
    username = st.sidebar.text_input("사용자 이름")
    password = st.sidebar.text_input("비밀번호", type="password")

    if st.sidebar.button("로그인"):
        if validate_login(username, password):
            st.session_state['logged_in'] = True
            st.session_state['login_failed'] = False
        else:
            st.session_state['login_failed'] = True

    if st.session_state['login_failed']:
        st.sidebar.error("로그인 실패! 사용자 이름이나 비밀번호를 확인하세요.")


# 메인 페이지 (로그인 후 메인 화면)
def main_page():
    st.sidebar.title('선택하세요')

    # 4개의 행으로 구성된 버튼 생성
    if st.sidebar.button('부산일과학고 방문면담 수학기출'):
        st.session_state['page'] = '부산일과학고 방문면담 수학기출'
    if st.sidebar.button('부산일과학고 방문면담 과학기출'):
        st.session_state['page'] = '부산일과학고 방문면담 과학기출'
    if st.sidebar.button('부산과학고 방문면담 수학기출'):
        st.session_state['page'] = '부산과학고 방문면담 수학기출'
    if st.sidebar.button('부산과학고 방문면담 과학기출'):
        st.session_state['page'] = '부산과학고 방문면담 과학기출'

    # 선택된 페이지에 따라 메인 화면에 내용을 표시
    if st.session_state['page'] == '부산일과학고 방문면담 수학기출':
        import BS1S_M
        BS1S_M.main()  # BS1S_M.py의 main() 함수 실행

    elif st.session_state['page'] == '부산일과학고 방문면담 과학기출':
        import BS1S_S
        BS1S_S.main()  # BS1S_S.py의 main() 함수 실행

    elif st.session_state['page'] == '부산과학고 방문면담 수학기출':
        import BSS_M
        BSS_M.main()  # BSS_M.py의 main() 함수 실행

    elif st.session_state['page'] == '부산과학고 방문면담 과학기출':
        import BSS_S
        BSS_S.main()  # BSS_S.py의 main() 함수 실행


# 화면 전환 로직
if st.session_state['logged_in']:
    main_page()
else:
    st.write("### 당신의 과학고 방문면담을 도와드립니다.^^")
    login()
