import streamlit as st
from PIL import Image
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Ritam Mallick - Portfolio",
    page_icon="📊",
    layout="wide"
)


# Create sidebar for navigation
def sidebar_menu():
    with st.sidebar:
        st.title("Navigation")
        page = st.radio("Go to", ["Home", "Projects", "Skills", "Experience", "Education", "Contact"])

        st.divider()

        st.write("## Connect With Me")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.button("📧")
        with col2:
            st.button("👔")
        with col3:
            st.button("🐙")

    return page


# Home page content
def home():
    col1, col2 = st.columns([1, 2], gap="large")

    with col1:
        # Replace with your own image
        st.image(r"C:\Users\dell\Desktop\portfolio\pic.jpg", width=300)

    with col2:
        st.title("RITAM MALLICK")
        st.subheader("Analytics & Data Enthusiast")
        st.write("""
        ## About Me

        Welcome to my portfolio! I am a passionate Computer Science graduate engineer 
        currently pursuing MBA in Business Analytics and Data Science. With expertise in 
        advanced Excel, Python, SQL, Power BI, data visualization, and statistical modeling.

        I'm highly motivated and results-oriented, eager to leverage my skills to drive 
        data-informed business decisions and contribute to organizational success.

        ### Quick Bio
        - 🔭 I'm currently working on my MBA in Business Analytics & Data Science
        - 🌱 I'm currently learning Machine Learning techniques and Prompt Engineering
        - 👯 I'm looking to collaborate on data analytics and machine learning projects
        - 💬 Ask me about Python, SQL, Power BI, and data visualization
        """)

    st.divider()

    st.header("Featured Projects")
    featured_col1, featured_col2 = st.columns(2)

    with featured_col1:
        st.subheader("Movie Recommendation System")
        st.image("https://via.placeholder.com/600x300", use_column_width=True)
        st.write(
            "Recommendation system using Apriori Algorithm and Association Rule Learning Algorithm for predicting relative movies according to genre, directors, and casts.")
        st.button("Learn More", key="project1")

    with featured_col2:
        st.subheader("Heart Health Monitoring System")
        st.image("https://via.placeholder.com/600x300", use_column_width=True)
        st.write(
            "Health monitoring system using multiple Machine Learning algorithms including Naïve Bayes, Logistic Regression, KNN, Random Forest, Decision Tree & XG Boost.")
        st.button("Learn More", key="project2")


# Projects page content
def projects():
    st.title("My Projects")
    st.write("Here are some of the projects I've worked on:")

    # Project 1
    with st.expander("Movie Recommendation System using Machine Learning"):
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image("https://via.placeholder.com/400x300")
        with col2:
            st.subheader("Movie Recommendation System using Machine Learning")
            st.write(
                "Developed a recommendation system using Apriori Algorithm and Association Rule Learning Algorithm. The system predicts related movies based on genre, directors, and casts, enhancing user experience by providing personalized recommendations.")
            st.write("**Technologies used:** Python, Machine Learning, Apriori Algorithm, Association Rule Learning")
            st.write("**GitHub:** [Link to repository](https://github.com)")
            st.write("**Year:** 2023")

    # Project 2
    with st.expander("Heart Health Monitoring System using Machine Learning Algorithms"):
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image("https://via.placeholder.com/400x300")
        with col2:
            st.subheader("Heart Health Monitoring System")
            st.write(
                "Created a comprehensive health monitoring system using multiple Machine Learning algorithms including Naïve Bayes, Logistic Regression, KNN, Random Forest, Decision Tree & XG Boost. The system analyzes health data to predict potential heart-related issues.")
            st.write(
                "**Technologies used:** Python, Naïve Bayes, Logistic Regression, KNN, Random Forest, Decision Tree, XG Boost")
            st.write("**GitHub:** [Link to repository](https://github.com)")
            st.write("**Year:** 2023")

    # Project 3
    with st.expander("Web Applications"):
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image("https://via.placeholder.com/400x300")
        with col2:
            st.subheader("Web Applications")
            st.write(
                "Designed and developed several web applications during leisure time, showcasing front-end and back-end development skills. These projects demonstrate creativity, problem-solving abilities, and technical proficiency.")
            st.write("**Technologies used:** HTML, CSS, JavaScript, various web frameworks")
            st.write("**GitHub:** [Link to repository](https://github.com)")
            st.write("**Year:** 2021")


# Skills page content
def skills():
    st.title("Skills & Expertise")

    # Technical Skills
    st.header("Technical Skills")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Programming & Tools")
        languages = {
            "Python": 90,
            "SQL": 85,
            "Advanced Excel": 90,
            "Core Java": 75,
            "JavaScript": 70
        }

        for lang, proficiency in languages.items():
            st.write(f"{lang}")
            st.progress(proficiency / 100)

    with col2:
        st.subheader("Data Visualization & Analytics")
        frameworks = {
            "Power BI": 85,
            "Tableau": 80,
            "Machine Learning": 75,
            "Statistical Modeling": 80,
            "Android Studio": 70
        }

        for framework, proficiency in frameworks.items():
            st.write(f"{framework}")
            st.progress(proficiency / 100)

    # Soft Skills
    st.header("Soft Skills")
    soft_skills = ["Good Communication", "Analytical Thinking", "Creative and Problem Solving", "Quick Learner",
                   "Project Management", "Team Coordination"]

    col1, col2 = st.columns(2)

    for i, skill in enumerate(soft_skills):
        if i % 2 == 0:
            with col1:
                st.write(f"- {skill}")
        else:
            with col2:
                st.write(f"- {skill}")


# Experience page content
def experience():
    st.title("Work Experience")

    # Experience 1
    st.subheader("Project Associate")
    st.write("STEM LEARNING | May 2024 - Aug 2024")
    st.write("""
    - Coordinated and managed the execution of multiple STEM learning projects simultaneously
    - Ensured on-time and within-budget delivery of projects
    - Handled databases to maintain project timelines, budgets, and resource allocation plans
    - Collaborated with cross-functional teams to achieve project goals
    """)

    st.divider()

    # Experience 2
    st.subheader("Software Testing Engineer (Intern)")
    st.write("ERTL(E), STQC, MCIT, DIT, Govt of India | Aug 2023 - Apr 2024")
    st.write("""
    - Conducted functional testing of e-District Chattisgarh, a government web portal for citizens
    - Performed surveillance of Integrated eProcurement System for the government of Chattisgarh
    - Collaborated with IBM on web portal testing and improvement
    - Documented test cases and reported issues to development teams
    """)

    st.divider()

    # Experience 3
    st.subheader("Project Management Intern")
    st.write("Foruppo | Jun 2023 - Aug 2023")
    st.write("""
    - Conducted virtual meetings with potential collaborators and prospects
    - Coordinated with team members to ensure project progress
    - Recruited new team members for various projects
    - Coached and supported project team members with their assigned tasks
    """)


# Education page content
def education():
    st.title("Education")

    # Degree 1
    st.subheader("MBA-PGP (Business Analytics & Data Science)")
    st.write("Bengal Institute of Business Studies | Aug 2024 - Present")

    st.divider()

    # Degree 2
    st.subheader("Bachelor of Technology (Computer Science Engineering)")
    st.write("Haldia Institute of Technology | Jul 2019 - Aug 2023")

    st.divider()

    # Certifications
    st.header("Certifications")
    certifications = [
        {"name": "Data Analytics Job Simulation", "issuer": "", "date": "February 2025", "link": "#"},
        {"name": "Prompt Engineering", "issuer": "", "date": "December 2024", "link": "#"},
        {"name": "Machine Learning with Python", "issuer": "", "date": "September - October 2024", "link": "#"},
        {"name": "Wipro Talent Next Program", "issuer": "Wipro", "date": "May - September 2022", "link": "#"}
    ]

    for cert in certifications:
        st.write(f"**{cert['name']}** - {cert['issuer']} ({cert['date']})")
        st.write(f"[View Certificate]({cert['link']})")


# Contact page content
def contact():
    st.title("Contact Me")

    st.write("Feel free to reach out to me through any of the following channels:")

    col1, col2 = st.columns(2)

    with col1:
        st.write("### Direct Contact")
        st.write("📧 Email: rk.rit7@gmail.com")
        st.write("📱 Phone: +91-7098199401")
        st.write("📍 Location: Kolkata, India")

    with col2:
        st.write("### Social Media")
        st.write("👔 [LinkedIn](https://linkedin.com/in/ritam-mallick)")
        st.write("🐙 [GitHub](https://github.com/ritammallick)")
        # Assuming GitHub username - update as needed

    st.write("### Send a Message")
    with st.form("contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")

        submitted = st.form_submit_button("Send Message")
        if submitted:
            st.success("Thanks for your message! I'll get back to you soon.")


# Main app
def main():
    # Apply custom CSS
    st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    h1, h2, h3 {
        color: #1e3d59;
    }
    .stButton>button {
        background-color: #ff6e40;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

    # Display page based on selection
    page = sidebar_menu()

    if page == "Home":
        home()
    elif page == "Projects":
        projects()
    elif page == "Skills":
        skills()
    elif page == "Experience":
        experience()
    elif page == "Education":
        education()
    elif page == "Contact":
        contact()


if __name__ == "__main__":
    main()