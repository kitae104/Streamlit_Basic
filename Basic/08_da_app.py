#################################################
# 국민 연금 가입 정보 분석
#################################################
import os
import warnings
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re
import streamlit as st

# 한글 폰트 설정
plt.rcParams["font.family"] = "NanumGothic"
plt.rcParams["axes.unicode_minus"] = False


class PensionData:
    def __init__(self, filepath):
        self.df = pd.read_csv(os.path.join(filepath), encoding="cp949")
        self.pattern1 = "(\([^)]+\))"  # 괄호와 괄호 사이의 문자열
        self.pattern2 = "(\[[^)]+\])"  # 대괄호와 대괄호 사이의 문자열
        self.pattern3 = "[^A-Za-z0-9가-힣]"  # 영문자, 숫자, 한글이 아닌 문자
        self.preprocess()  # 데이터 전처리

    def preprocess(self):
        # 컬럼명 변경
        self.df.columns = [
            "자료생성년월",
            "사업장명",
            "사업자등록번호",
            "가입상태",
            "우편번호",
            "사업장지번상세주소",
            "주소",
            "고객법정동주소코드",
            "고객행정동주소코드",
            "시도코드",
            "시군구코드",
            "읍면동코드",
            "사업장형태구분코드 1 법인 2 개인",
            "업종코드",
            "업종코드명",
            "적용일자",
            "재등록일자",
            "탈퇴일자",
            "가입자수",
            "금액",
            "신규",
            "상실",
        ]

        # 필요없는 컬럼 제거
        df = self.df.drop(
            [
                "자료생성년월",
                "우편번호",
                "사업장지번상세주소",
                "고객법정동주소코드",
                "고객행정동주소코드",
                "사업장형태구분코드 1 법인 2 개인",
                "적용일자",
                "재등록일자",
            ],
            axis=1,  # axis=1: 열 제거
        )
        df["사업장명"] = df["사업장명"].apply(self.preprocessing)  # 사업장명 전처리
        df["탈퇴일자_연도"] = pd.to_datetime(
            df["탈퇴일자"]
        ).dt.year  # 탈퇴일자_연도 컬럼 추가
        df["탈퇴일자_월"] = pd.to_datetime(
            df["탈퇴일자"]
        ).dt.month  # 탈퇴일자_월 컬럼 추가
        df["시도"] = df["주소"].str.split(" ").str[0]  # 시도 컬럼 추가
        df = (
            df.loc[df["가입상태"] == 1]  # 가입상태가 1인 데이터만 추출
            .drop(["가입상태", "탈퇴일자"], axis=1)  # 가입상태, 탈퇴일자 컬럼 제거
            .reset_index(drop=True)  # 인덱스 초기화
        )
        df["인당금액"] = df["금액"] / df["가입자수"]  # 인당금액 컬럼 추가
        df["월급여추정"] = df["인당금액"] / 9 * 100  # 월급여추정 컬럼 추가
        df["연간급여추정"] = df["월급여추정"] * 12  # 연간급여추정 컬럼 추가
        self.df = df  # 전처리된 데이터프레임 저장

    # 텍스트 데이터 전처리
    def preprocessing(self, x):
        x = re.sub(self.pattern1, "", x)
        x = re.sub(self.pattern2, "", x)
        x = re.sub(self.pattern3, " ", x)
        x = re.sub(" +", " ", x)
        return x

    # 회사명을 포함하는 데이터를 반환
    def find_company(self, company_name):
        return self.df.loc[
            self.df["사업장명"].str.contains(company_name),
            ["사업장명", "월급여추정", "연간급여추정", "업종코드", "가입자수"],
        ].sort_values("가입자수", ascending=False)

    # 회사와 같은 업종의 평균, 최소, 최대 급여 추정 정보를 반환
    def compare_company(self, company_name):
        company = self.find_company(company_name)
        code = company["업종코드"].iloc[0]
        df1 = self.df.loc[
            self.df["업종코드"] == code, ["월급여추정", "연간급여추정"]
        ].agg(["mean", "count", "min", "max"])
        df1.columns = ["업종_월급여추정", "업종_연간급여추정"]
        df1 = df1.T
        df1.columns = ["평균", "개수", "최소", "최대"]
        df1.loc["업종_월급여추정", company_name] = company["월급여추정"].values[0]
        df1.loc["업종_연간급여추정", company_name] = company["연간급여추정"].values[0]
        return df1

    # 검색한 회사의 정보를 반환
    def company_info(self, company_name):
        company = self.find_company(company_name)
        return self.df.loc[company.iloc[0].name]

    # 데이터프레임 반환
    def get_data(self):
        return self.df


@st.cache_data
def read_pensiondata():
    data = PensionData("국민연금공단_국민연금 가입 사업장 내역_20240924.csv")
    return data


data = read_pensiondata()
company_name = st.text_input("회사명을 입력해 주세요", placeholder="검색할 회사명 입력")

if data and company_name:
    output = data.find_company(company_name=company_name)
    if len(output) > 0:
        st.subheader(output.iloc[0]["사업장명"])
        info = data.company_info(company_name=company_name)
        st.markdown(
            f"""
            - `{info['주소']}`
            - 업종코드명 `{info['업종코드명']}`
            - 총 근무자 `{int(info['가입자수']):,}` 명
            - 신규 입사자 `{info['신규']:,}` 명
            - 퇴사자 `{info['상실']:,}` 명
            """
        )
        col1, col2, col3 = st.columns(3)
        col1.text("월급여 추정")
        col1.markdown(f"`{int(output.iloc[0]['월급여추정']):,}` 원")

        col2.text("연봉 추정")
        col2.markdown(f"`{int(output.iloc[0]['연간급여추정']):,}` 원")

        col3.text("가입자수 추정")
        col3.markdown(f"`{int(output.iloc[0]['가입자수']):,}` 명")

        st.dataframe(output.round(0), use_container_width=True)

        comp_output = data.compare_company(company_name=company_name)
        st.dataframe(comp_output.round(0), use_container_width=True)

        st.markdown(f"### 업종 평균 VS {company_name} 비교")

        percent_value = info["월급여추정"] / comp_output.iloc[0, 0] * 100 - 100
        diff_month = abs(comp_output.iloc[0, 0] - info["월급여추정"])
        diff_year = abs(comp_output.iloc[1, 0] - info["연간급여추정"])
        upordown = "높은" if percent_value > 0 else "낮은"

        st.markdown(
            f"""
        - 업종 **평균 월급여**는 `{int(comp_output.iloc[0, 0]):,}` 원, **평균 연봉**은 `{int(comp_output.iloc[1, 0]):,}` 원 입니다.
        - `{company_name}`는 평균 보다 `{int(diff_month):,}` 원, :red[약 {percent_value:.2f} %] `{upordown}` `{int(info['월급여추정']):,}` 원을 **월 평균 급여**를 받는 것으로 추정합니다.
        - `{company_name}`는 평균 보다 `{int(diff_year):,}` 원 `{upordown}` `{int(info['연간급여추정']):,}` 원을 **연봉**을 받는 것으로 추정합니다.
        """
        )

        fig, ax = plt.subplots(1, 2)

        p1 = ax[0].bar(
            x=["Average", "Your Company"],
            height=(comp_output.iloc[0, 0], info["월급여추정"]),
            width=0.7,
        )
        ax[0].bar_label(p1, fmt="%d")
        p1[0].set_color("black")
        p1[1].set_color("red")
        ax[0].set_title("Monthly Salary")

        p2 = ax[1].bar(
            x=["Average", "Your Company"],
            height=(comp_output.iloc[1, 0], info["연간급여추정"]),
            width=0.7,
        )
        p2[0].set_color("black")
        p2[1].set_color("red")
        ax[1].bar_label(p2, fmt="%d")
        ax[1].set_title("Yearly Salary")

        ax[0].tick_params(axis="both", which="major", labelsize=8, rotation=0)
        ax[0].tick_params(axis="both", which="minor", labelsize=6)
        ax[1].tick_params(axis="both", which="major", labelsize=8)
        ax[1].tick_params(axis="both", which="minor", labelsize=6)

        st.pyplot(fig)

        st.markdown("### 동종업계")
        df = data.get_data()
        st.dataframe(
            df.loc[
                df["업종코드"] == info["업종코드"],
                ["사업장명", "월급여추정", "연간급여추정", "가입자수"],
            ]
            .sort_values("연간급여추정", ascending=False)
            .head(10)
            .round(0),
            use_container_width=True,
        )

    else:
        st.subheader("검색결과가 없습니다")
