import streamlit as st
import pandas as pd

# Title of the app
st.title("JSON to CSV Converter")

# File uploader to allow users to upload a JSON file
uploaded_file = st.file_uploader("Upload JSON File", type=["json"])

if uploaded_file is not None:
    # Read the JSON file into a Pandas DataFrame
    try:
        df = pd.read_json(uploaded_file)
        st.success("File successfully uploaded and read!")

        # Display the dataframe
        st.write("Here's a preview of the data:")
        st.dataframe(df.head())

        # Provide an option to download the DataFrame as a CSV file
        csv = df.to_csv(index=False)
        st.download_button(
            label="Download CSV",
            data=csv,
            file_name="exported_file.csv",
            mime="text/csv",
        )

    except ValueError as e:
        st.error(f"Error reading JSON file: {e}")

else:
    st.info("Please upload a JSON file.")
