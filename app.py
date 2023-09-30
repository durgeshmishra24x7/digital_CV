from pathlib import Path
import random
import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.jpg"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Durgesh Mishra"
PAGE_ICON = ":wave:"
NAME = "Durgesh Mishra"
DESCRIPTION = """
Senior Consultant in Data Analyst and Automation team, assisting enterprises by supporting data-driven decision-making.
"""
EMAIL = "dm24x7@outlook.com"
SOCIAL_MEDIA = {
    "YouTube": "https://www.youtube.com/@machinetalks4128",
    "LinkedIn": "https://www.linkedin.com/in/durgesh-mishra-24x7/",
    "Github" : "https://github.com/",
    "YourQuote": "https://www.yourquote.in/durgesh-mishra-q0if/quotes"
}
PROJECTS = {
    "🏆 EY Analytics - Data science - Silver (2021)": "https://www.credly.com/badges/3bfe984e-3cfa-4c92-bbf8-d04e667e3447?source=linked_in_profile",
    "🏆 YouTube channel focused on Data Science videos": "https://www.youtube.com/@machinetalks4128",
    "🏆 Earned an EY Spot Award for outstanding performance in automation projects": "https://www.linkedin.com/posts/durgesh-mishra-24x7_ive-worked-on-a-number-of-automation-projects-activity-6891341973073068032-6_cB?utm_source=share&utm_medium=member_desktop",
    "🏆 Analytica BI Tool in Python": "https://www.linkedin.com/posts/durgesh-mishra-24x7_python-datascience-visualization-activity-6791795534001688576-35MR?utm_source=share&utm_medium=member_desktop",
    "🏆 PowerBI Planetary Dashboard": "https://www.linkedin.com/posts/durgesh-mishra-24x7_datascientist-python-powerbidesktop-activity-6713416344328552448-LMTo?utm_source=share&utm_medium=member_desktop",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=300)
#230
with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)
    st.write('\n')
    

# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qualifications")


# Define custom CSS for the bullet style with a check icon
custom_css = """
@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.0/css/all.min.css');

.custom-check-bullet {
    list-style-type: none; /* Remove default bullet */
    padding-left: 0; /* Remove default left padding */
    display: flex;
    align-items: flex-start;
    margin-bottom: 10px; /* Adjust spacing between items */
}

.custom-check-bullet::before {
    font-family: 'Font Awesome 5 Free'; /* Use Font Awesome for icons */
    content: "\u2714"; /* Unicode for a checkmark (✔) */
    margin-right: 10px; /* Adjust the space between the icon and text */
    font-size: 18px; /* Adjust the icon size as needed */
    color: green; /* Adjust the icon color */
    
}
"""

# Use st.markdown to inject the custom CSS into the Streamlit app
st.markdown(f'<style>{custom_css}</style>', unsafe_allow_html=True)


# st.markdown(
#     """

# - ✔️ 7.8 Years expereince extracting actionable insights from data
# - ✔️ Strong hands on experience and knowledge in Python and Excel
# - ✔️ Good understanding of statistical principles and their respective applications
# - ✔️ Developed Power BI Reports and dashboards by blending data from multiple sources
# - ✔️ Utilized Python scripting for advanced data modeling and transformation, incorporating VBA and Python algorithms
# - ✔️ Collaborated with business teams to simplify operations and create scalable automation solutions using Python and VBA, particularly in ITGC and Audit Workplan procedures.
# - ✔️ Leveraged multiple data sets from diverse client systems to build comprehensive analytical models connected to interactive GUIs using Python
# - ✔️ Worked within an agile framework, supporting, planning, and leading projects from inception to development.
# - ✔️ Applied NLP techniques to analyze and extract insights from unstructured text data, enhancing the team's ability to derive valuable information from textual sources.
# - ✔️ Excellent team-player and displaying strong sense of initiative on tasks
# """
# )
# Create bullet points with custom check icons
st.markdown("""
<ul>
    <li class='custom-check-bullet'><p style="text-align: justify;">7.8 Years expereince extracting actionable insights from data</p></li>
    <li class='custom-check-bullet'><p style="text-align: justify;">Strong hands on experience and knowledge in Python and Excel</p></li>
    <li class='custom-check-bullet'><p style="text-align: justify;">Good understanding of statistical principles and their respective applications</p></li>
    <li class='custom-check-bullet'><p style="text-align: justify;">Developed Power BI Reports and dashboards by blending data from multiple sources</p></li>
    <li class='custom-check-bullet'><p style="text-align: justify;">Utilized Python scripting for advanced data modeling and transformation, incorporating VBA and Python algorithms</p></li>
    <li class='custom-check-bullet'><p style="text-align: justify;">Collaborated with business teams to simplify operations and create scalable automation solutions using Python and VBA, particularly in ITGC and Audit Workplan procedures</p></li>
    <li class='custom-check-bullet'><p style="text-align: justify;">Leveraged multiple data sets from diverse client systems to build comprehensive analytical models connected to interactive GUIs using Python</p></li>
    <li class='custom-check-bullet'><p style="text-align: justify;">Worked within an agile framework, supporting, planning, and leading projects from inception to development</p></li>
    <li class='custom-check-bullet'><p style="text-align: justify;">Applied NLP techniques to analyze and extract insights from unstructured text data, enhancing the team's ability to derive valuable information from textual sources</p></li>
    <li class='custom-check-bullet'><p style="text-align: justify;">Excellent team-player and displaying strong sense of initiative on tasks</p></li>
    
</ul>
""", unsafe_allow_html=True)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")


st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas, Request), SQL, VBA, Powershell
- 📊 Data Visulization: PowerBi, MS Excel, Matplotlib
- 📚 Modeling: Linear regression, Logistic regression, Decision trees, NLP
- 🗄️ Databases: Postgres and MySQL

"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Senior Consulatant | Ernst and Young**")
st.write("09/2023 - Present")

st.markdown(
    """
Responsibilities:

Data Analysis and Automation Team:

<ul>
<li class='custom-check-bullet'><p style="text-align: justify;">Find and interpret rich data sources, manage large amounts of data, merge data sources, ensure consistency of data-sets, and create visualizations to aid in understanding data</p></li>
<li class='custom-check-bullet'><p style="text-align: justify;">Work with internal teams to understand deeply the critical execution activities. Analyze complex data, determine compelling opportunities to influence execution, and translate those requirements into technical solutions</p></li>
<li class='custom-check-bullet'><p style="text-align: justify;">Leveraging data science techniques, optimize processes and deliver innovation as part of the SDE strategy for execution excellence</p></li>
<li class='custom-check-bullet'><p style="text-align: justify;">Ensure operational and business metric health by monitoring production data points</p></li>
<li class='custom-check-bullet'><p style="text-align: justify;">Collaborate with clients to understand their business requirements and provide data-driven solutions</p></li>
<li class='custom-check-bullet'><p style="text-align: justify;">Practical experience with and theoretical understanding of algorithms for classification, regression, clustering, and anomaly detection</p></li>
<li class='custom-check-bullet'><p style="text-align: justify;">Advanced expertise in statistical coding languages (e.g., Python) with a proven track record of hands-on application and meeting deadlines</p></li>
<li class='custom-check-bullet'><p style="text-align: justify;">Extraordinary data analytical skills, including the ability to model, interpret, and visualize data</p></li>
<li class='custom-check-bullet'><p style="text-align: justify;">Ability to extract meaningful business insights from data and identify the stories behind the patterns</p></li>
<li class='custom-check-bullet'><p style="text-align: justify;">Utilize Python and Power BI for in-depth data analysis and visualization</p></li>
<li class='custom-check-bullet'><p style="text-align: justify;">Create and maintain automated Excel reports for accurate and timely data delivery</p></li>
<li class='custom-check-bullet'><p style="text-align: justify;">Used PowerBI and SQL to redefine and track KPIs surrounding automation initiatives and supplied recommendations to boost landing page conversion rate by 38%</p></li>
<li class='custom-check-bullet'><p style="text-align: justify;">Led a team of 4 analysts to brainstorm potential marketing and sales improvements and implemented A/B tests to generate 15% more client leads</p></li>
<li class='custom-check-bullet'><p style="text-align: justify;">Develop tailored Python scripts and applications to address client-specific needs and optimize data processes</p></li>
<li class='custom-check-bullet'><p style="text-align: justify;">Apply NLP techniques to extract insights from textual data sources and led a team to perform sentiment analysis, such as audio customer feedback</p></li>
<li class='custom-check-bullet'><p style="text-align: justify;">Design interactive Power BI dashboards for monitoring key performance indicators</p></li>
<li class='custom-check-bullet'><p style="text-align: justify;">Identify and resolve data-related issues, offering ongoing client support</p></li>
<li class='custom-check-bullet'><p style="text-align: justify;">Mentor junior team members in relevant skills</p></li>
</ul>
    """, unsafe_allow_html=True
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Service Management Specialist | Orange Business Services**")
st.write("08/2017 - 04/2020")
st.write(
    """
Responsibilities:

Service Management and Automation Team:
<ul>
<li class='custom-check-bullet'><p style="text-align: justify;"><p style="text-align: justify;">Specializing in dashboard analysis for KPI/SLA Metrics and incident data insights,</p></li>
<li class='custom-check-bullet'><p style="text-align: justify;"><p style="text-align: justify;">Analyzed customer network operations and reported on Quality of Service</p></li>
<li class='custom-check-bullet'><p style="text-align: justify;"><p style="text-align: justify;">Automated report downloads from web MSS portal using Selenium and Python</p></li>
<li class='custom-check-bullet'><p style="text-align: justify;"><p style="text-align: justify;">Created interactive Power BI dashboards for customer interactions</p></li>
<li class='custom-check-bullet'><p style="text-align: justify;"><p style="text-align: justify;">Developed comprehensive analytical models by working with diverse data sets from multiple client systems, integrated with Python-based interactive GUIs</p></li>
<li class='custom-check-bullet'><p style="text-align: justify;"><p style="text-align: justify;">Worked in an agile framework, supporting, planning, and leading projects from planning to development</p></li>
<li class='custom-check-bullet'><p style="text-align: justify;"><p style="text-align: justify;">Designed automation solutions for complex business challenges, including end-to-end testing process automation and email automation using Python scripting</p></li>
<li class='custom-check-bullet'><p style="text-align: justify;"><p style="text-align: justify;">Produced Power BI Reports and dashboards by blending data from multiple sources</p></li>
<li class='custom-check-bullet'><p style="text-align: justify;"><p style="text-align: justify;">Implemented end-to-end process automation for the Service Now ticketing tool using Beautiful Soup and Selenium</p></li>
<li class='custom-check-bullet'><p style="text-align: justify;"><p style="text-align: justify;">Developed a GUI to fetch live data from websites using Python and Beautiful Soup and interconnected it with the GUI</p></li>
</ul>
""", unsafe_allow_html=True
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**Website Promoter - Freelancer | The Creation**")
st.write("01/2016 - 11/2017")
st.write(
    """

Responsibilities:

Digital Marketing Team:
<ul>
<li class='custom-check-bullet'><p style="text-align: justify;"><p style="text-align: justify;">Develop and execute content promotion strategies to increase website visibility</p></li>
<li class='custom-check-bullet'><p style="text-align: justify;">Continuously monitor and improve website SEO to enhance search engine rankings</p></li>
<li class='custom-check-bullet'><p style="text-align: justify;">Manage and curate social media profiles to maintain an active online presence</p></li>
<li class='custom-check-bullet'><p style="text-align: justify;">Create and send email campaigns to subscribers, promoting website content and offerings</p></li>
<li class='custom-check-bullet'><p style="text-align: justify;">Use web analytics tools to track website performance and generate reports on traffic, user behavior, and conversions</p></li>
<li class='custom-check-bullet'><p style="text-align: justify;">Build and manage quality backlinks to improve website authority and search rankings</p></li>
<li class='custom-check-bullet'><p style="text-align: justify;">Produce engaging and relevant content, optimizing it for readers and search engines</p></li>
<li class='custom-check-bullet'><p style="text-align: justify;">Plan and execute online advertising campaigns to drive targeted traffic and adjust strategies based on performance</p></li>
<li class='custom-check-bullet'><p style="text-align: justify;">Analyze competitor websites and strategies to identify opportunities for improvement</p></li>
<li class='custom-check-bullet'><p style="text-align: justify;">Participate in relevant online communities and forums to promote the website and build relationships with influencers</p></li>
</ul>
""", unsafe_allow_html=True
)

bck_img_urls = ["https://source.unsplash.com/AJXKxuRrUcg","https://source.unsplash.com/nbuYloot8_U","https://source.unsplash.com/JbGXFmkTj1Q"]

random_value = random.choice(bck_img_urls)    
print("random_value: ",random_value)
size = 500
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url({random_value});
background-size: {size}%;
background-position: top left;
background-repeat: no-repeat;
background-attachment: local;
}}

"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
    

