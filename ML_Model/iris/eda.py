# -*- coding:utf-8 -*-
# 라이브러리 import
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import utils

def run_eda_app():						# run_eda_app() 함수 생성
    st.subheader('탐색적 자료 분석(EDA)')

    iris = pd.read_csv('data/iris.csv')				# 데이터 불러오기
    st.markdown('## IRIS 데이터 확인')
    st.write(iris)						# 데이터 확인하기

    # 메뉴 지정
    # 사이드 바에 하위메뉴 생성
    submenu = st.sidebar.selectbox('하위메뉴', ['기술통계량', '그래프분석', '통계분석'])	
    if submenu == '기술통계량':					# 기술 통계량 메뉴 내용
        st.dataframe(iris)
        with st.expander('데이터 타입'):
            result1 = pd.DataFrame(iris.dtypes)			# 데이터 타입 확인
            st.write(result1)
        with st.expander("기초 통계량"):				# 기초 통계량 확인
            result2 = iris.describe()
            st.write(result2)
        with st.expander("Target 빈도 수 확인"):			# 각 종별 개수 확인
            st.write(iris['Species'].value_counts())
    elif submenu == '그래프분석':				# 그래프 메뉴 내용
        st.title("Title")
        with st.expander('산점도'):			
            fig1 = px.scatter(iris,
                             x = 'SepalWidthCm',
                             y = 'SepalLengthCm',
                             color = 'Species',
                             size = 'PetalWidthCm',
                             hover_data = ['PetalLengthCm'])	# Plotly 산점도 생성
            st.plotly_chart(fig1)				# 산점도 출력

        # layouts 나누기
        col1, col2 = st.columns(2)
        with col1:
            st.title('Seaborn')
            fig, ax=plt.subplots()
            # Seaborn 활용 상자그래프 작성
            ax=sns.boxplot(iris,
                           x = 'SepalWidthCm',
                           y = 'SepalLengthCm',
                           ax=ax)
            st.pyplot(fig)

        with col2:
            st.title('Matplotlib')
            # Matplotlib 활용 히스토그램 작성
            fig, ax=plt.subplots()
            ax.hist(iris['SepalLengthCm'], color='green')
            st.pyplot(fig)

        # Tabs
        # iris의 종별 산점도 그래프 탭 만들기
        # Plotly 사용
        # 종 선택할 때마다 산점도 그래프가 달라지도록 함
        tab1, tab2, tab3, tab4, tab5 = st.tabs(['Select','Setosa', 'Versicolor', 'Virginica', 'Kaggle'])
        with tab1:
            with tab1:
                choice0 = st.selectbox('iris 데이터', iris['Species'].unique())
                result0 = iris[iris['Species'] == choice0]

                st.title('plotly')
                # 그래프 작성
                fig0 = px.scatter(result0
                                  , x='SepalWidthCm'
                                  , y='SepalLengthCm'
                                  , size='SepalWidthCm'
                                  , hover_data=['SepalLengthCm'])
                st.plotly_chart(fig0)
        with tab2:
            st.write('Setosa')
            choice1 = iris['Species'].unique()[0]
            result3 = iris[iris['Species'] == choice1]
            fig2 = px.scatter(result3,
                             x = 'SepalWidthCm',
                             y = 'SepalLengthCm')
            st.plotly_chart(fig2)

        with tab3:
            st.write('Versicolor')
            choice2 = iris['Species'].unique()[1]
            result4 = iris[iris['Species'] == choice2]
            fig3 = px.scatter(result4,
                             x = 'SepalWidthCm',
                             y = 'SepalLengthCm')
            st.plotly_chart(fig3)

        with tab4:
            st.write('Virginica')
            choice3 = iris['Species'].unique()[2]
            result5 = iris[iris['Species'] == choice3]
            fig4 = px.scatter(result5,
                             x = 'SepalWidthCm',
                             y = 'SepalLengthCm')
            st.plotly_chart(fig4)

        with tab5:
            pass

    elif submenu == '통계분석':
        pass
    else:
        st.warning("뭔가 없어요!")