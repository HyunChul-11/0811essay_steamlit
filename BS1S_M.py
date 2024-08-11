import streamlit as st
import random

# 문제 데이터 로드
def load_questions(file_path='BS1S_M.txt'):
    questions = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()  # 문자열의 앞뒤 공백 제거
            if '|' in line:
                question, explanation = line.split('|', 1)
                questions.append({"question": question.strip(), "explanation": explanation.strip()})
    return questions

# 문제 선택 함수
def get_random_question(questions):
    return random.choice(questions)

# Streamlit 애플리케이션
def main():
    st.title('부산일과학고 방문면담 수학기출')

    # 문제 데이터 로드
    questions = load_questions()

    if not questions:
        st.error("No questions found. Please check your BS1S_M.txt file.")
        return

    # 상태 변수 초기화
    if 'show_explanation' not in st.session_state:
        st.session_state.show_explanation = False

    # 페이지에 처음 들어올 때마다 또는 "다른 문제를 보여주세요"를 누를 때 새로운 문제를 로드
    if 'first_load' not in st.session_state or st.session_state['first_load']:
        st.session_state.current_question = get_random_question(questions)
        st.session_state.show_explanation = False
        st.session_state.first_load = False

    # "다른 문제를 보여주세요" 버튼이 눌리면 새로운 문제 로드
    if st.button('다른 문제를 보여주세요'):
        st.session_state.current_question = get_random_question(questions)
        st.session_state.show_explanation = False

    # 현재 선택된 문제
    selected_question = st.session_state.current_question

    st.subheader('기출문제:')
    st.markdown(selected_question['question'])

    # 해설 요청 버튼
    if st.button('해설을 보여주세요'):
        st.session_state.show_explanation = True

    # 해설이 요청되었으면 해설을 표시
    if st.session_state.show_explanation:
        st.markdown("**해설:**")
        st.markdown(selected_question['explanation'])

if __name__ == "__main__":
    # 페이지에 처음 로드되었음을 기록
    if 'first_load' not in st.session_state:
        st.session_state.first_load = True

    main()
