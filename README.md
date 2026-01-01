# ATS Advisor – Resume Evaluation & Optimization System

ATS Advisor is a Streamlit-based application that simulates the behavior of a real-world Applicant Tracking System (ATS) combined with a senior technical recruiter.  
It helps candidates evaluate, optimize, and score their resumes against a target job description using Large Language Models (LLMs).

The system is designed to be **ATS-realistic**, **fact-preserving**, and **recruiter-friendly**, focusing on keyword relevance, skill alignment, and clarity.

---

## Key Features

1. Resume Evaluation (Recruiter View)
- Analyzes resume against a given job description
- Identifies strengths aligned with the role
- Highlights gaps and missing requirements
- Provides a clear hiring verdict (Shortlist / Hold / Reject)

2. ATS-Optimized Resume Improvement
- Rewrites the resume using ATS-friendly formatting
- Improves keyword relevance without adding fake information
- Converts responsibilities into impact-focused bullet points
- Groups skills logically for ATS parsing

3. ATS Match Percentage Scoring
- Calculates resume-to-job-description compatibility
- Identifies strong matching areas
- Lists missing or weak keywords
- Outputs an objective ATS-style verdict

---

## Why This Project Is Realistic

- Uses **text-based resume parsing**, not image-based OCR (aligned with real ATS systems)
- Enforces **strict factual integrity** (no hallucinated experience)
- Output formatting mirrors actual ATS + recruiter review reports
- Optimized for **free-tier LLM usage** with low token consumption

---

## Technology Stack

Frontend:
- Streamlit

Backend / AI:
- Google Gemini API (gemini-flash-latest)

Utilities:
- python-dotenv (environment variable management)
- PDF text extraction libraries (text-based parsing)

Language:
- Python

---

## Application Workflow

1. User uploads resume (PDF)
2. User provides job description
3. User selects one of the actions:
   - Resume evaluation
   - Resume optimization
   - ATS percentage match
4. System processes inputs using Gemini LLM
5. Structured ATS-style output is displayed in the UI

---

## Project Structure

ATS_PROJECT/
│── app.py              # Main Streamlit application
│── requirements.txt    # Project dependencies
│── .env                # API key configuration
│── README.md           # Project documentation

---

## Setup Instructions

1. Clone the repository
   git clone <repository-url>
   cd ATS_PROJECT

2. Create and activate a virtual environment
   python -m venv venv
   source venv/bin/activate   (Linux/Mac)
   venv\Scripts\activate      (Windows)

3. Install dependencies
   pip install -r requirements.txt

4. Configure environment variables
   Create a .env file in the project root and add:
   GEMINI_API_KEY=your_api_key_here

5. Run the application
   streamlit run app.py

---

## Model Selection Notes

This project intentionally uses:
- models/gemini-flash-latest

Reasons:
- Free-tier compatible
- Low latency and cost-efficient
- Sufficient reasoning for ATS-style analysis
- Avoids quota exhaustion issues

---

## Limitations

- Resume parsing is text-based; scanned image-only PDFs may not parse correctly
- Free-tier API limits apply
- Results depend on resume content quality and job description clarity

---

## Future Enhancements

- Resume section-wise scoring
- Skill gap recommendations with learning resources
- Downloadable ATS report (PDF)
- Multi-job comparison
- Role-specific weighting (Frontend / Backend / Data / AI)

---

## Disclaimer

This tool is designed for **educational and career preparation purposes**.  
It does not guarantee job selection and should be used as a resume improvement aid.

---

## Author

Developed by an aspiring AI / Software Engineer focused on building practical, real-world LLM-powered applications for recruitment and career analytics.
