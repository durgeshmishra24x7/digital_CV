from pathlib import Path
import random
import streamlit as st
from PIL import Image
from io import BytesIO
import base64

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic_path = current_dir / "assets" / "pp.png"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Durgesh Mishra"
PAGE_ICON = "💼"
NAME = "Durgesh Mishra"
DESCRIPTION = """
Manager in Data Analytics & Automation, enabling enterprises to unlock business value 
through AI-driven insights, scalable automation, and data-driven strategy execution. 
Proven success in reducing reporting time by 50%, improving efficiency by 30%, 
and leading award-winning analytics initiatives that drive measurable impact.
"""
EMAIL = "dm24x7@outlook.com"
SOCIAL_MEDIA = {
    "YouTube": "https://www.youtube.com/@machinetalks4128",
    "LinkedIn": "https://www.linkedin.com/in/durgesh-mishra-24x7/",
    "Github": "https://github.com/durgeshmishra24x7",
    "YourQuote": "https://www.yourquote.in/durgesh-mishra-q0if/quotes"
}
PROJECTS = {
    "🏆 EY Analytics - Data Science - Silver (2021)": "https://www.credly.com/badges/3bfe984e-3cfa-4c92-bbf8-d04e667e3447?source=linked_in_profile",
    "🏆 YouTube channel focused on Data Science videos": "https://www.youtube.com/@machinetalks4128",
    "🏆 EY Spot Award for outstanding performance in automation projects": "https://www.linkedin.com/posts/durgesh-mishra-24x7_ive-worked-on-a-number-of-automation-projects-activity-6891341973073068032-6_cB?utm_source=share&utm_medium=member_desktop",
    "🏆 Analytica BI Tool in Python": "https://www.linkedin.com/posts/durgesh-mishra-24x7_python-datascience-visualization-activity-6791795534001688576-35MR?utm_source=share&utm_medium=member_desktop",
    "🏆 Power BI Planetary Dashboard": "https://www.linkedin.com/posts/durgesh-mishra-24x7_datascientist-python-powerbidesktop-activity-6713416344328552448-LMTo?utm_source=share&utm_medium=member_desktop",
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON, layout="wide")

# --- LOAD CSS, PDF & PROFILE PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic_path)

# --- GLOBAL CUSTOM STYLES ---
st.markdown("""
<style>
/* Background overlay for readability */
[data-testid="stAppViewContainer"] > .main {
    background: linear-gradient(rgba(255,255,255,0.9), rgba(255,255,255,0.9)), url("https://source.unsplash.com/nbuYloot8_U");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}

/* Typography */
h1, h2, h3 {
    font-family: 'Segoe UI', sans-serif;
    font-weight: 700;
    color: #1a1a1a;
}
p, li {
    font-family: 'Segoe UI', sans-serif;
    font-size: 16px;
    color: #333333;
    line-height: 1.6;
}

/* Section headers */
.section-header {
    font-size: 22px;
    font-weight: 700;
    color: #0e4d92;
    margin-top: 30px;
    border-bottom: 2px solid #0e4d92;
    padding-bottom: 5px;
}

/* Bullet points with checkmark */
.custom-check-bullet {
    list-style-type: none;
    margin-bottom: 8px;
}
.custom-check-bullet::before {
    content: "✔ ";
    color: #0e8a16;
    font-weight: bold;
    margin-right: 5px;
}

/* Card layout */
.stCard {
    background: white;
    padding: 25px;
    border-radius: 12px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

# --- HERO SECTION (as card with aligned image + text) ---
# --- HERO SECTION (perfectly aligned: image + centered text block) ---
buffer = BytesIO()
profile_pic.resize((240, 240)).save(buffer, format="PNG")  # bigger image
img_b64 = base64.b64encode(buffer.getvalue()).decode()

st.markdown("<div class='stCard'>", unsafe_allow_html=True)
col1, col2 = st.columns([1, 3], gap="large")

with col1:
    st.markdown(
        f"""
        <div style="display:flex; justify-content:center; align-items:center; height:100%; min-height:240px;">
            <img src="data:image/png;base64,{img_b64}" 
                 style="border-radius:18px; width:240px; height:240px; object-fit:cover; box-shadow:0 6px 16px rgba(0,0,0,0.2);">
        </div>
        """,
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        f"""
        <div style="display:flex; flex-direction:column; justify-content:center; height:100%; gap:10px;">
            <h1 style="margin:0;">{NAME}</h1>
            <p style="font-size:18px; text-align:justify; margin:0;">{DESCRIPTION}</p>
            <div style="margin-top:6px;">
                <a href="mailto:{EMAIL}" style="text-decoration:none; font-weight:600; font-size:16px;">📫 {EMAIL}</a>
            </div>
            <div style="display:flex; gap:25px; margin-top:4px;">
    """,
        unsafe_allow_html=True,
    )

    # Resume button directly below description
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )

    # Social Links Inline
     # Social Links Inline with proper spacing
    social_html = """
    <div style='display:flex; gap:25px; margin-top:15px;'>
        <a href='https://youtube.com' target='_blank' style='text-decoration:none; color:#E63946; font-weight:600;'>YouTube</a>
        <a href='https://linkedin.com' target='_blank' style='text-decoration:none; color:#0A66C2; font-weight:600;'>LinkedIn</a>
        <a href='https://github.com' target='_blank' style='text-decoration:none; color:#333; font-weight:600;'>Github</a>
        <a href='https://yourquote.in' target='_blank' style='text-decoration:none; color:#D62828; font-weight:600;'>YourQuote</a>
    </div>
    """
    st.markdown(social_html, unsafe_allow_html=True)


# --- SOCIAL LINKS ---
# cols = st.columns(len(SOCIAL_MEDIA))
# for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
#     cols[index].write(f"[{platform}]({link})")

# --- EXPERIENCE & QUALIFICATIONS ---
st.markdown("<div class='stCard'>", unsafe_allow_html=True)
st.markdown("<h2 class='section-header'>Experience & Qualifications</h2>", unsafe_allow_html=True)
st.markdown("""
<ul>
    <li class='custom-check-bullet'>8+ years of experience delivering actionable insights and automation solutions</li>
    <li class='custom-check-bullet'>Hands-on expertise in Python, SQL, VBA, and Excel for analytics & automation</li>
    <li class='custom-check-bullet'>Proficient in Power BI dashboarding, KPI reporting, and business storytelling</li>
    <li class='custom-check-bullet'>Experience applying NLP and ML techniques to structured & unstructured data</li>
    <li class='custom-check-bullet'>Strong record of leading cross-functional teams in agile project delivery</li>
    <li class='custom-check-bullet'>Recognized with EY awards for analytics innovation and automation excellence</li>
</ul>
""", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# --- SKILLS ---
st.markdown("<div class='stCard'>", unsafe_allow_html=True)
st.markdown("<h2 class='section-header'>Hard Skills</h2>", unsafe_allow_html=True)
st.write(
    """
- 👩‍💻 Programming: Python (Pandas, Scikit-learn, Selenium), SQL, VBA, PowerShell  
- 📊 Data Visualization: Power BI, MS Excel, Matplotlib  
- 📚 Machine Learning: Regression, Decision Trees, NLP, Clustering  
- 🗄️ Databases: PostgreSQL, MySQL  
"""
)
st.markdown("</div>", unsafe_allow_html=True)

# --- WORK HISTORY ---
st.markdown("<div class='stCard'>", unsafe_allow_html=True)
st.markdown("<h2 class='section-header'>Work History</h2>", unsafe_allow_html=True)

st.subheader("🚧 Manager | Ernst & Young (EY)")
st.caption("10/2025 - Present")
st.markdown(
    """
- Headed Automation CoE and managed a high-performing team of 17 analysts and developers, delivering enterprise-scale automation and analytics solutions across global clients.
- Directed automation programs that improved reporting efficiency by 50%, boosted KPI accuracy by 38%, and reduced audit/ITGC cycle times by 30%.
- Designed and governed enterprise-wide Power BI dashboards, enabling CoEs and business leaders to track critical KPIs across multiple geographies.
- Mentored and coached analysts, fostering career growth and building a pipeline of automation and data science talent.  
- Recognized for driving EY’s award-winning analytics initiatives, showcasing measurable business impact and innovation at scale.  
"""
)


st.subheader("🚧 Senior Consultant | Ernst & Young (EY)")
st.caption("05/2020 - Present")
st.markdown(
    """
- Led a team of 4 analysts, delivering automation and data solutions that improved reporting efficiency by **50%** and boosted KPI accuracy by **38%**  
- Designed and deployed Power BI dashboards to monitor key business metrics across global clients  
- Applied NLP for sentiment analysis on customer feedback, enabling actionable insights at scale  
- Automated manual ITGC and audit processes, cutting cycle times by **30%**  
- Mentored junior analysts and contributed to EY’s award-winning analytics initiatives  
"""
)

st.subheader("🚧 Service Management Specialist | Orange Business Services")
st.caption("08/2017 - 04/2020")
st.markdown(
    """
- Automated incident reporting with Python & Selenium, saving 20+ hours per week  
- Developed KPI dashboards in Power BI, enabling proactive SLA management  
- Implemented end-to-end ServiceNow automation, reducing manual effort by **40%**  
- Partnered with stakeholders to identify opportunities for scalable automation  
"""
)

st.subheader("🚧 Website Promoter (Freelance) | The Creation")
st.caption("01/2016 - 11/2017")
st.markdown(
    """
- Executed SEO and digital marketing strategies to boost online visibility  
- Managed content promotion and social media presence for clients  
- Leveraged analytics to track traffic, engagement, and conversion improvements  
"""
)
st.markdown("</div>", unsafe_allow_html=True)

# --- PROJECTS & ACCOMPLISHMENTS ---
st.markdown("<div class='stCard'>", unsafe_allow_html=True)
st.markdown("<h2 class='section-header'>Projects & Accomplishments</h2>", unsafe_allow_html=True)
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
st.markdown("</div>", unsafe_allow_html=True)
