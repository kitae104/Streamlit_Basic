# 예제 2 이미 Trace가 있는Figure에Trace 추가하여 겹쳐 그리기
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

def main():
    st.title("Streamlit with Plotly2")
    # 데이터 불러오기
    df = px.data.iris()

    # express를 활용한 scatter plot 생성
    fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species",
                    title="Plotly Express를 이용한 그래프")

    # 그래프에 선 추가하기(이미 생성된 trace의 type, 색, 스타일, 템플릿 등 추가 편집이 가능)
    fig.add_trace(
        go.Scatter(
            x=[2, 4],
            y=[4, 8],
            mode="lines",
            line=go.scatter.Line(color="gray"),
            showlegend=False)
    )

    # 변경하기 
    # fig.update_traces(marker=dict(color="RoyalBlue"),
    #               selector=dict(type="trace"))

    # 타이틀 추가하기
    fig.update_layout(title_text="타이틀 변경하기",title_font_size=30)

    # 축 타이틀 추가하기
    fig.update_xaxes(title_text='너비($)')
    fig.update_yaxes(title_text='길이($)')

    st.plotly_chart(fig, use_container_width=True)

if __name__ == "__main__":
    main()