import streamlit as st
import os
from markitdown import MarkItDown

st.set_page_config(page_title="MarkItDown Web", layout="wide")

st.title("MarkItDown Web Converter")

# Initialize MarkItDown without the enable_plugins parameter
md = MarkItDown()

# File upload section
uploaded_files = st.file_uploader("Select the files to convert", accept_multiple_files=True)

if uploaded_files:
    for uploaded_file in uploaded_files:
        st.subheader(f"Processing of documents: {uploaded_file.name}")
        
        # Save uploaded files to a temporary directory
        temp_path = f"temp_{uploaded_file.name}"
        with open(temp_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        try:
            # Converted documents
            result = md.convert(temp_path)
            
            # Displaying conversion results
            st.text_area("Conversion results", result.text_content, height=300)
            
            # Provide download button
            st.download_button(
                label="Download Markdown file",
                data=result.text_content,
                file_name=f"{os.path.splitext(uploaded_file.name)[0]}.md",
                mime="text/markdown"
            )
            
        except Exception as e:
            st.error(f"Conversion failure: {str(e)}")
        finally:
            # Cleaning up temporary files
            if os.path.exists(temp_path):
                os.remove(temp_path)

st.sidebar.markdown("""
## Instructions for use
1. Click on "Select Files to Convert" to upload one or more files.
2. The system automatically converts the file to Markdown format
3. Conversion results can be previewed
4. Click on "Download Markdown file" to save the result.

## Supported file formats
- PDF
- Word
- PowerPoint
- Excel
- Picture Files
- audio file (computer)
- HTML
- CSV, JSON, XML
- ZIP file
""")
