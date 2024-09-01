import streamlit as st
import plotly.express as px

'''
그래프 탬플릿 종류
- Basics: scatter, line, area, bar, funnel, timeline
- Part-of-Whole: pie, sunburst, treemap, icicle, funnel_area
- 1D Distributions: histogram, box, violin, strip, ecdf
- 2D Distributions: density_heatmap, density_contour
- Matrix or Image Input: imshow
- 3-Dimensional: scatter_3d, line_3d
- Multidimensional: scatter_matrix, parallel_coordinates, parallel_categories
- Tile Maps: scatter_mapbox, line_mapbox, choropleth_mapbox, density_mapbox
- Outline Maps: scatter_geo, line_geo, choropleth
- Polar Charts: scatter_polar, line_polar, bar_polar
- Ternary Charts: scatter_ternary, line_ternary
'''

def main():
    st.title("Streamlit with Plotly2")
    
    # px.bar() 함수를 활용해서 bar chart 생성과 동시에 Data, Layout 값 입력
    fig = px.bar(x=["a", "b", "c"], y=[1, 3, 2],title="express를 이용한 그래프")

    # Display visualization
    st.plotly_chart(fig, use_container_width=True)

if __name__ == "__main__":
    main()