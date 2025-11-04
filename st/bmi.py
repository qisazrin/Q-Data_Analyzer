import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(page_title='BMI Calculator',layout='centered')

st.title('🐻 BMI Calculator')
st.write("Let's calculate you Body Mass Index(BMI)")
st.header('🐾 Enter you Details ')

# create for h&w input
height=st.number_input('Enter you Height( in cm)',min_value=100,max_value=250,value=160)
weight= st.number_input('Enter you weight( in kg)',min_value=30,max_value=200,value=50)

st.write('🦒 Your Height :',height,'cm')
st.write('🐘 Your Weight :',weight,'kg')

if st.button('calculate BMI'):
    h_m = height/100     # convert cm to meter
    bmi = weight/(h_m**2)
    st.success(f'Your BMI is **{bmi:.2f}**')

# BMI category
    if bmi <18.5:
       category ='Underweight'  
       color= '#F54927'

    elif 18.5 <= bmi <25:
       category = 'Normal'
       color ='#56FC5F'

    elif 25<= bmi <30:
        category = 'Overweight'
        color ='#E3FC56'

    else:
        category = 'Obese'
        color ='#FB5C5C'

    st.markdown(
        f"""
        <div style='background-color:{color};padding:15px;border-radius:10px;text-align:center'>
        <h3> Your BMI Category : {category}</h3>
        </div>
        """,
        unsafe_allow_html=True
        )
    
    st.header("📊 BMI Range Chart")
 
# Data
bmi_data = pd.DataFrame({
    "Category": ["Underweight", "Normal", "Overweight", "Obese"],
    "Range": [18.5, 24.9, 29.9, 40]
})
 
# Define custom colors for each category
color_scale = alt.Scale(
    domain=["Underweight", "Normal", "Overweight", "Obese"],
    range=['#F54927', '#56FC5F', '#E3FC56', '#FB5C5C']
)
 
# Create chart
chart = (
    alt.Chart(bmi_data)
    .mark_bar()
    .encode(
        x=alt.X("Category:N", title="BMI Category"),
        y=alt.Y("Range:Q", title="BMI Range"),
        color=alt.Color("Category:N", scale=color_scale, legend=None)
    )
    .properties(width=600, height=400)
)
 
st.altair_chart(chart, use_container_width=True)