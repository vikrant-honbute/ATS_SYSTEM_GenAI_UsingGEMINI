from dotenv import load_dotenv
load_dotenv()

import base64
import streamlit as st
import os
import io

import fitz  # PyMuPDF
import google.generativeai as genai


genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def get_gemini_response(input_prompt, pdf_content, job_description):
    model = genai.GenerativeModel("models/gemini-flash-latest")
    response = model.generate_content(
        [input_prompt, pdf_content[0], job_description]
    )
    return response.text


def input_pdf_setup(uploaded_file):
    if uploaded_file is None:
        raise FileNotFoundError("No file uploaded")

    pdf_bytes = uploaded_file.read()

    
    pdf_doc = fitz.open(stream=pdf_bytes, filetype="pdf")


    page = pdf_doc.load_page(0)
    pix = page.get_pixmap(matrix=fitz.Matrix(2, 2)) 
    img_bytes = pix.tobytes("jpeg")

    pdf_parts = [
        {
            "mime_type": "image/jpeg",
            "data": base64.b64encode(img_bytes).decode()
        }
    ]

    return pdf_parts


# -------------------- Streamlit UI --------------------
st.set_page_config(page_title="ATS Advisor")
st.header("ATS Helping System")

input_text = st.text_area("Job Description:", key="input")
uploaded_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])

if uploaded_file:
    st.success("PDF Uploaded Successfully")

submit1 = st.button("Tell Me About the Resume")
submit2 = st.button("How Can I Improvise my Skills")
submit3 = st.button("Percentage Match")

input_prompt1 = """
You are an experienced Technical Human Resource Manager with hiring experience in software and data roles.

Your task is to evaluate the provided resume against the given job description from a recruiter’s perspective.

RULES:
- Do not rewrite the resume
- Do not add assumptions or fake experience
- Base your evaluation strictly on the given resume content

EVALUATION TASKS:
1. Assess overall alignment with the job role
2. Identify key strengths relevant to the job description
3. Identify weaknesses or missing requirements
4. Comment on role suitability (Junior / Entry / Mid-level fit)

OUTPUT FORMAT (MANDATORY):

=== OVERALL FIT ===
Brief verdict on whether the candidate fits the role (Yes / Partial / No) with 2–3 lines of reasoning.

=== STRENGTHS ===
List 4–6 bullet points highlighting strong matches with the job requirements.

=== WEAKNESSES / GAPS ===
List 3–5 bullet points of missing or weak areas compared to the job description.

=== HIRING MANAGER NOTE ===
1–2 lines on whether you would shortlist this resume and why.

IMPORTANT:
- Keep language professional and recruiter-like
- No emojis
- No markdown

"""

input_prompt2 = """
You are acting as a professional Applicant Tracking System (ATS) and a senior technical recruiter.

Your task is to analyze, improve, and optimize the provided resume so it performs exceptionally well in ATS screening and recruiter review.

STRICT RULES:
1. Do NOT add fake experience, fake projects, or false claims.
2. Do NOT exaggerate responsibilities beyond what is reasonable.
3. Do NOT use buzzwords without evidence.
4. Preserve factual accuracy at all times.

OBJECTIVES:
- Maximize ATS keyword match for the target role
- Improve clarity, technical precision, and impact
- Ensure recruiter readability in under 30 seconds
- Use concise, achievement-oriented bullet points

INPUTS YOU WILL RECEIVE:
- Resume text
- Target job role
- Job description (if provided)

TASKS TO PERFORM:
1. Rewrite the resume using ATS-optimized formatting:
   - Clear section headings
   - Bullet points only (no paragraphs)
   - Simple, standard fonts assumed
2. Optimize keywords naturally based on the job role.
3. Convert responsibilities into measurable achievements where possible.
4. Remove filler words, weak verbs, and redundancy.
5. Ensure skills are grouped logically (Languages, Frameworks, Tools, Databases, Cloud, etc.).
6. Maintain professional tone suitable for large tech companies.

OUTPUT FORMAT (MANDATORY):

=== ATS SCORE ESTIMATE ===
Provide a percentage estimate of ATS compatibility and briefly justify it.

=== OPTIMIZED RESUME ===
Provide the fully rewritten resume in clean, copy-paste-ready format.

=== KEYWORD MATCH ANALYSIS ===
- Matched Keywords:
- Missing / Weak Keywords:
- Suggested Additions (only if truthful):

=== RECRUITER FEEDBACK ===
Give 5–7 concise bullet points of feedback as a senior recruiter reviewing this resume.

IMPORTANT:
- Do NOT include explanations inside the resume.
- Do NOT include emojis.
- Do NOT include markdown.
- Output must look like a real ATS-processed resume.

"""

input_prompt3 = """
You are an advanced Applicant Tracking System (ATS) scanner designed to evaluate resume-to-job-description compatibility.

Your task is to calculate how well the provided resume matches the given job description.

RULES:
- Base scoring strictly on skills, experience, tools, and keywords
- Do not infer skills that are not explicitly mentioned
- Do not rewrite the resume
- Be objective and ATS-like, not conversational

SCORING CRITERIA:
- Skill match (primary and secondary)
- Tool and technology match
- Role relevance
- Experience alignment
- Keyword presence

OUTPUT FORMAT (MANDATORY):

MATCH PERCENTAGE: XX%

MISSING / WEAK KEYWORDS:
- List 5–10 important missing or weak keywords

STRONG MATCHING AREAS:
- List 4–6 strong matching skills or areas

FINAL ATS VERDICT:
1–2 lines explaining why the resume received this score and whether it would pass an initial ATS filter.

IMPORTANT:
- Output the percentage first
- No emojis
- No markdown
- Keep language concise and system-like

"""

if submit1:
    if uploaded_file:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt1, pdf_content, input_text)
        st.subheader("Response")
        st.write(response)
    else:
        st.warning("Please upload a resume")

if submit2:
    if uploaded_file:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt2, pdf_content, input_text)
        st.subheader("Response")
        st.write(response)
    else:
        st.warning("Please upload a resume")

if submit3:
    if uploaded_file:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt3, pdf_content, input_text)
        st.subheader("Response")
        st.write(response)
    else:
        st.warning("Please upload a resume")



   




