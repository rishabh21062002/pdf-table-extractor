import time
from unstract.llmwhisperer import LLMWhispererClientV2
import streamlit as st
from new_test3 import extract_tables_from_text
from test6 import extract_structured_table

# Initialize the client with the correct API URL and API key
client = LLMWhispererClientV2(
    base_url="https://llmwhisperer-api.us-central.unstract.com/api/v2",
    api_key="DCt8PJPe9djki8SrObHuNS1WD2ORAEQWMQWvMdSDeHo"  # Replace with your actual API key
)

st.title("PDF Text Extractor 📝")

# File uploader
uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file is not None:
    st.write("Processing file... Please wait ⏳")

    # Save the uploaded file
    file_path = "uploaded.pdf"
    with open(file_path, "wb") as f:
        f.write(uploaded_file.read())

    # Start processing
    with st.spinner("Extracting text..."):
        result = client.whisper(file_path=file_path)

        # Polling loop to check processing status
        while True:
            status = client.whisper_status(whisper_hash=result["whisper_hash"])

            if status["status"] == "processed":
                resultx = client.whisper_retrieve(
                    whisper_hash=result["whisper_hash"]
                )
                break  # Exit loop once processing is done

            time.sleep(5)  # Wait 5 seconds before checking again

    extracted_text = resultx["extraction"]["result_text"]

    # Save extracted text
    output_file = "extracted_text.txt"
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(extracted_text)

    st.success("✅ Extraction Complete!")
    st.download_button(
        label="📄 Download Extracted Text",
        data=extracted_text,
        file_name="extracted_text.txt",
        mime="text/plain"
    )

    # Show extracted text preview
    with st.expander("📜 View Extracted Text"):
        st.text_area("Extracted Text", extracted_text, height=300)

    # Buttons to extract tables
    st.write("### Choose Table Extraction Method:")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Extract **Structured** Table 📊"):
            structured_output = "structured_output.xlsx"
            extract_structured_table("extracted_text.txt", structured_output)
            st.success(f"Structured table saved as `{structured_output}`")

    with col2:
        if st.button("Extract **Unstructured** Table 🔄"):
            unstructured_output = "unstructured_output.xlsx"
            extract_tables_from_text("extracted_text.txt", unstructured_output)
            st.success(f"Unstructured table saved as `{unstructured_output}`")

