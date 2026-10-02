import streamlit as st
import pandas as pd
import pickle

# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Placement Prediction",
    page_icon="🎓",
    layout="centered"
)

# =========================================================
# LOAD TRAINED MODELS
# =========================================================

@st.cache_resource
def load_model():
    with open("logistic_regression_model.pkl", "rb") as f:
        model_1 = pickle.load(f)

    with open("decision_tree_model.pkl", "rb") as f:
        model_2 = pickle.load(f)

    with open("random_forest_model.pkl","rb") as f:
        model_3=pickle.load(f)

    return model_1, model_2, model_3

model_1, model_2 ,model_3 = load_model()

# =========================================================
# TITLE
# =========================================================

st.title("🎓 Student Placement Prediction")

st.write(
    "Enter the student's academic and skill details "
    "to predict their placement status."
)

# =========================================================
# INPUT FEATURES
# =========================================================

st.subheader("Enter Student Details")

CGPA = st.number_input(
    "CGPA",
    min_value=0.0,
    max_value=10.0,
    value=7.0,
    step=0.1
)

Internships = st.number_input(
    "Number of Internships",
    min_value=0.0,
    max_value=20.0,
    value=1.0,
    step=1.0
)

Projects = st.number_input(
    "Number of Projects",
    min_value=0.0,
    max_value=20.0,
    value=2.0,
    step=1.0
)

Workshops = st.number_input(
    "Number of Workshops",
    min_value=0.0,
    max_value=20.0,
    value=2.0,
    step=1.0
)

AptitudeTestScore = st.number_input(
    "Aptitude Test Score",
    min_value=0.0,
    max_value=100.0,
    value=70.0,
    step=1.0
)

SoftSkillsRating = st.number_input(
    "Soft Skills Rating",
    min_value=0.0,
    max_value=4.0,
    value=2.5,
    step=0.1
)

SSC_Marks = st.number_input(
    "SSC Marks",
    min_value=0.0,
    max_value=100.0,
    value=75.0,
    step=1.0
)

HSC_Marks = st.number_input(
    "HSC Marks",
    min_value=0.0,
    max_value=100.0,
    value=75.0,
    step=1.0
)


# =========================================================
# PREDICTION BUTTON
# =========================================================

if st.button("🔮 Predict Placement", use_container_width=True):

    # -----------------------------------------------------
    # Create DataFrame
    # -----------------------------------------------------

    user_input = pd.DataFrame([{
        "CGPA": CGPA,
        "Internships": Internships,
        "Projects": Projects,
        "Workshops": Workshops,
        "AptitudeTestScore": AptitudeTestScore,
        "SoftSkillsRating": SoftSkillsRating,
        "SSC_Marks": SSC_Marks,
        "HSC_Marks": HSC_Marks
    }])


    # -----------------------------------------------------
    # Prediction
    # -----------------------------------------------------

    # model_1
    # -------------------------------
    prediction_1 = model_1.predict(user_input)[0]
    
    probability_1 = model_1.predict_proba(user_input)[0][1]

    # model_2
    # --------------------------------------
    prediction_2 = model_2.predict(user_input)[0]
 
    probability_2 = model_2.predict_proba(user_input)[0][1]

    # model_3
    # ---------------------------------------
    prediction_3 = model_3.predict(user_input)[0]

    probability_3 = model_3.predict_proba(user_input)[0][1]
    
    # -----------------------------------------------------
    # Display Results
    # -----------------------------------------------------

    st.subheader("📊 Prediction Result")

    # model_1
    # --------------------------------------
    st.write("Logistic Regression:")

    st.metric("Placement Probability",f"{probability_1 * 100:.2f}%")

    if prediction_1 == 1:
        st.success("✅ Prediction: Student is likely to be Placed")
    else:
        st.error("❌ Prediction: Student is likely to be Not Placed")

    # -----------------------------------------------------
    # Progress Bar
    # -----------------------------------------------------

    st.write("Placement Probability")

    st.progress(float(probability_1))

    # model_2
    # --------------------------------------

    st.write("Decision Tree:")

    st.metric("Placement Probability",f"{probability_2*100:.2f}%")

    if prediction_2 == 1:
        st.success("✅ Prediction: Student is likely to be Placed")
    else:
        st.error("❌ Prediction: Student is likely to be Not Placed")

    # -----------------------------------------------------
    # Progress Bar
    # -----------------------------------------------------

    st.write("Placement Probability")

    st.progress(float(probability_2))

    # model_3
    # --------------------------------------

    st.write("Random Forest:")
    
    st.metric("Placement Probability",f"{probability_3*100:.2f}%")
    
    if prediction_3 == 1:
        st.success("✅ Prediction: Student is likely to be Placed")
    else:
        st.error("❌ Prediction: Student is likely to be Not Placed")

    # -----------------------------------------------------
    # Progress Bar
    # -----------------------------------------------------

    st.write("Placement Probability")

    st.progress(float(probability_3))

    # -----------------------------------------------------
    # Show Entered Data
    # -----------------------------------------------------

    with st.expander("View Input Details"):

        st.dataframe(
            user_input,
            use_container_width=True
        )
