import streamlit as st
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

st.title("AI Resume Screening System")

job_description = st.text_area("Enter Job Description")
resume = st.text_area("Paste Resume Content")

if st.button("Analyze Match"):
    job_embedding = model.encode(job_description, convert_to_tensor=True)
    resume_embedding = model.encode(resume, convert_to_tensor=True)

    similarity = util.cos_sim(job_embedding, resume_embedding)
    score = float(similarity[0][0]) * 100

    st.subheader(f"Match Score: {score:.2f}%")

    if score > 70:
        st.success("Strong Match")
    elif score > 50:
        st.warning("Moderate Match")
    else:
        st.error("Low Match")
