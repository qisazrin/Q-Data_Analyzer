import streamlit as st
import pickle
import numpy as np
import warnings
warnings.filterwarnings('ignore')

st.set_page_config(page_title='MCadotor',page_icon='🥑')

st.title(' 🥑 Student Marks Predictor')
st.write('Enter The Number Of Hours Studied (1-10) and **Click Predict** To See The Predict Marks.')

def load_model(path:str='SLR.pkl'):        # use this code to open/load pickle 
    with open (path,'rb') as h:
        model = pickle.load(h)
    return model

# Load model
try: 
    model = load_model('SLR.pkl')
except FileNotFoundError:
    st.error("SLR.pkl not found. Please Place Your Pickle file named 'SLR.pkl' in the same folder as st.py")
    st.stop()
except Exception as e:
    st.error(f'Failed To Load Model:{e}')
    st.stop()

# input: int/float hours from 1 to 10

hours= st.number_input(label='Hours_Studied',
                       min_value = 1.0,
                       max_value = 10.0,
                       step = 0.1, 
                       value= 1.0,
                       format = '%.1f')
if st.button('predict'):
    try:
        x = np.array([[hours]],dtype=float)
        prediction = model.predict(x)
        predicted_marks = prediction[0]

        # show result
        st.success(f'Predicted Marks : {predicted_marks : 1f}')
        st.write('Note: This Is Model Prediction')

    except Exception as e:
        st.error(f'Failed:{e}')
    