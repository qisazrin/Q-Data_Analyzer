import streamlit as st
import pandas as pd
import numpy as np
import io 
import matplotlib.pyplot as mb

# set page (title and text)
st.set_page_config(page_title='Analyze Data',layout='wide',page_icon='🐦‍🔥')
st.title('🐦‍🔥 Analyze Data')
st.write('Upload a CSV files and explore data interactively!')

# for uploading data
upload_file=st.file_uploader('📂 Upload CSV file',type=['csv'])

if upload_file is not None:
    try:
        df=pd.read_csv(upload_file)
        # converting bool column as str
        bool_col=df.select_dtypes(include=['bool']).columns
        df[bool_col]=df[bool_col].astype(str)
    except Exception as e:
        st.error('Could Not Read The Csv.Please Check The File Format')
        st.exception(e)
        st.stop()
    st.success('📩 File Uploaded Successfully!')
    st.write('### 📃 Preview of Data')
    st.dataframe(df.head())

    st.write('### ℹ️ Data Overview')
    st.write('Number of Rows :',df.shape[0])
    st.write('Number of Columns :',df.shape[1])
    st.write('Number of Missing Values :',int(df.isnull().sum().sum()))   # the sum of sum missing values
    st.write('Number of Duplicate Records :',df.duplicated().sum())
    st.write('Number of Object :',df.select_dtypes(include=['object']).shape[1])

    st.subheader('ℹ️ Complete Summary of Dataset')
    buffer = io.StringIO()
    df.info(buf=buffer)
    s = buffer.getvalue()
    st.text(s)
     
    #statistical summary
    st.write('### 📈 Statistical Summary')
    st.dataframe(df.describe())

    # Non-numerical summary
    st.write('### 📈 Non-Numerical Statistical Summary')
    object_cols = df.select_dtypes(include=['object'])
    if not object_cols.empty:
        st.dataframe(object_cols.describe())
    else:
        st.info("No object (string/categorical) columns found in this dataset.")

    st.subheader('Select The Desired Columns For Analysis ')
    # multiselect box
    columns=st.multiselect('Choose Colums',df.columns.tolist())

    st.subheader('Preview')
    if columns:   # if user selected one or ore column
        st.dataframe(df[columns].head(10))
    else:
        st.info('No Columns Selected.')
    
    # data filter
    st.subheader("🔍 Simple Filtering")
    st.write("You can filter your dataset by choosing a column and a value.")

    filter_col = st.selectbox("Select a column to filter by", options=df.columns.tolist())
    unique_vals = df[filter_col].dropna().unique().tolist()

    if len(unique_vals) < 50:  # only show filter options if not too many
        selected_val = st.selectbox("Select value", options=unique_vals)
        filtered_df = df[df[filter_col] == selected_val]
        st.write(f"### Filtered Results (where **{filter_col} = {selected_val}**)")
        st.dataframe(filtered_df.head(10))
    else:
        st.info("Column has too many unique values — skipping filter menu.")

    # Data Visualization
        st.subheader("📊 Data Visualization")

    cols = df.select_dtypes(include=[np.number,'bool']).columns.tolist()
    colss = df.columns.tolist()
    if len(cols) >= 1:
        col1, col2 = st.columns(2)
    with col1:
        x_axis = st.selectbox("Select X-axis", options=colss)
    with col2:
        y_axis = st.selectbox("Select Y-axis", options=cols)

    st.write("---")
    col3, col4, col5 = st.columns(3)

    with col3:  # line graph
        if st.button("📈 Show Line Graph"):
            fig, ax = mb.subplots()
            ax.plot(df[x_axis], df[y_axis], color='skyblue', marker='o')
            ax.set_xlabel(x_axis)
            ax.set_ylabel(y_axis)
            ax.set_title(f'Line Graph: {y_axis} vs {x_axis}')
            st.pyplot(fig)

    with col4:   # Bar graph
        if st.button("📊 Show Bar Chart"):
            fig, ax = mb.subplots()
            # convert x-axis to string to avoid issues with bools or mixed types
            ax.bar(df[x_axis].astype(str), df[y_axis], color='lightgreen')
            ax.set_xlabel(x_axis)
            ax.set_ylabel(y_axis)
            ax.set_title(f'Bar Chart: {y_axis} vs {x_axis}')
            mb.xticks(rotation=45)
            st.pyplot(fig)

    with col5:    # pie chart
        if st.button("🥧 Show Pie Chart"):
            # Pie chart works best for categorical or boolean columns
            # Count occurrences of each category in the selected x-axis
            pie_data = df[x_axis].value_counts()
            fig, ax = mb.subplots()
            ax.pie(
                pie_data.values,
                labels=pie_data.index.astype(str),
                autopct='%1.1f%%',
                startangle=90,
                colors=mb.cm.Paired.colors
            )
            ax.set_title(f'Pie Chart of {x_axis}')
            st.pyplot(fig)
else:
    st.info('Please Upload a CSV File To Get Started')
    st.info('No Column Selected.')
