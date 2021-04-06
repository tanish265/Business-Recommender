import streamlit as st

# from IPython.display import HTML

# HTML('<iframe src=plot_data.html width=700 height=450></iframe>')

import streamlit.components.v1 as components

# >>> import plotly.express as px
# >>> fig = px.box(range(10))
# >>> fig.write_html('test.html')
st.title("")
html_temp = """
<div style="background-color:tomato;padding:10px">
<h2 style="color:white;text-align:center;">Business Recommender ML App </h2>
</div>
"""
st.markdown(html_temp,unsafe_allow_html=True)
# st.header("test html import")
st.markdown('')

st.write("Map of Ahmedabad-India city with markers depicting different regions.")

st.write("Click on marker to see details like neighbourhood name, "
         "business score and label. Same label markers are coloured same and these labels are generated using KMeans Algorithm.")

st.write("Label 0-- Green")
st.write("Label 1-- Red")
st.write("Label 2-- Orange")
st.markdown('')
HtmlFile = open("plot_data.html", 'r', encoding='utf-8')
source_code = HtmlFile.read()
# print(source_code)
components.html(source_code, height = 450,width=700)
# st.write("")
st.markdown('#')

st.write("### Other Visualizations--")
st.write("Hover over the icon at top-right corner of the map to see the menu to change theme or other details.")

st.write("1. An all-in-one map showing medical data(hospitals, doctors, pharmacies, etc) of Ahmedabad.")

HtmlFile2 = open("medical_data.html", 'r', encoding='utf-8')
source_code2 = HtmlFile2.read()
# print(source_code2)
components.html(source_code2, height = 450,width=700)
st.markdown('#')
st.write("2. Similar map showing education related data(schools, universities, etc) of Ahmedabad.")

HtmlFile3 = open("education_data.html", 'r', encoding='utf-8')
source_code3 = HtmlFile3.read()
# print(source_code2)
components.html(source_code3, height = 450,width=700)
st.markdown('#')
st.write("3. Finally a map showing food related data(restaurants,supermarkets, etc) of Ahmedabad.")

HtmlFile4 = open("food_data.html", 'r', encoding='utf-8')
source_code4 = HtmlFile4.read()
# print(source_code2)
components.html(source_code4, height = 450,width=700)

st.markdown('#####')
st.markdown('#### Made by -- Tanish Gupta')
