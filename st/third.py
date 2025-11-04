#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
# page setup
st.set_page_config(page_title = 'Colors and Layout')       # use sat-page-config as a title of the product not the same as title.

st.title('COlors,Layout & Charts')
st.write('Now show your Creativity')

st.markdown('''
<div style = 'background-color:#637EF8'>
<h3 style = 'color:#E5F59A'> HTML style using markdown</h3>
<p>This is HTML Paragraph Tag</p>
</div> ''',unsafe_allow_html=True)

#markdown
st.markdown('\n')
# display text in bold and italic
st.markdown('**Streamlit** is  a python library for creating interactive *web apps*')
#links
st.markdown('Visit for More Info:(https://streamlit.io/) *To Learn* **streamlit**')

# code ()
code1 = '''def hello():
   print('H1 i am a python function')'''

st.code(code1,language='python')

#latex()
st.latex('''(a+b)^2 - a^2 + b^2 + 2*a*b''')

st.markdown('/n')
st.markdown('**Sigmoid Function**')
st.latex(r''' \frac {1}{1+e^-score}''')  # use this method to use mathematical (use curly bracket utk pecahan atas dn bwh)

#Layouts

col1, col2=st.columns(2)

with col1:
    st.header('Left Side')
    name = st.text_input('Enter Your Name?')
    st.write('Hello User!', name if name else 'Guest')

with col2:
    st.header('Right Side')
    age = st.slider('Pick a Number', 1, 100,22)
    st.write(f'Next year you will become (age+1) year old')

# a sidebar is like a mini control panel on the left side

with st.sidebar:
    st.header('control panel')
    user_color = st.color_picker('Pick Your Favorite Color','#000000')
    st.write('you have selected :', user_color)
    
    


# In[ ]:




