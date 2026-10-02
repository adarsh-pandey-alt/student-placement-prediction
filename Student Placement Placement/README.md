🎓 Student Placement Prediction
📌 Project Overview

This project is a Machine Learning-based Student Placement Prediction System that predicts whether a student is likely to be Placed or Not Placed based on academic performance, internships, projects, aptitude test scores, soft skills, and other student-related factors.

The project implements three Machine Learning classification algorithms and provides an interactive Streamlit web application for making predictions.

🎯 Objective

The main objective of this project is to build and compare Machine Learning classification models that can predict student placement status using student-related features.

This project demonstrates the complete Machine Learning workflow, including:

Data exploration

Data preprocessing

Feature selection

Model training

Model evaluation

Cross-validation

Feature importance analysis

Model saving

Streamlit application development

📊 Features Used

The following features are used for prediction:

CGPA

Internships

Projects

Workshops

Aptitude Test Score

Soft Skills Rating

SSC Marks

HSC Marks

🤖 Machine Learning Models

Three classification models are implemented:

1. Logistic Regression

Logistic Regression is implemented using a pipeline with StandardScaler for feature scaling.

2. Decision Tree Classifier

A Decision Tree Classifier is used with a maximum depth of 5.

3. Random Forest Classifier

A Random Forest Classifier is used as an ensemble learning model.

⚙️ Technologies Used

Python

Pandas

Scikit-learn

Matplotlib

Seaborn

Streamlit

Pickle

🔄 Project Workflow
Dataset
   ↓
Data Exploration
   ↓
Data Preprocessing
   ↓
Feature and Target Selection
   ↓
Train-Test Split
   ↓
Model Training
   ↓
Model Evaluation
   ↓
Cross-Validation
   ↓
Feature Importance Analysis
   ↓
Save Trained Models
   ↓
Streamlit Application
   ↓
Student Input
   ↓
Placement Prediction

📈 Model Evaluation

The models are evaluated using the following metrics:

Accuracy

Precision

Recall

F1-score

Confusion Matrix

5-Fold Cross-Validation

Confusion matrices are visualized using Seaborn.

Feature importance is also analyzed for:

Decision Tree

Random Forest

💻 Streamlit Application

The project includes an interactive Streamlit web application.

Users can enter student details through the web interface, including:

CGPA

Number of Internships

Number of Projects

Number of Workshops

Aptitude Test Score

Soft Skills Rating

SSC Marks

HSC Marks

The application provides predictions and placement probabilities from all three Machine Learning models.

📁 Project Structure
student-placement-prediction/
│
├── app.py
├── training.py
├── placementdata.csv
├── README.md
├── requirements.txt
└── .gitignore

File Description
File	Description
app.py	Streamlit application for student placement prediction
training.py	Trains and evaluates the Machine Learning models
placementdata.csv	Dataset used for model training
README.md	Project documentation
requirements.txt	Required Python libraries
.gitignore	Files excluded from GitHub
Generated Model Files

The trained model files are not included in the GitHub repository because the Random Forest model file is larger than GitHub's browser upload limit.

Running training.py will automatically generate:

logistic_regression_model.pkl
decision_tree_model.pkl
random_forest_model.pkl


These files are used by app.py for making predictions.

🚀 How to Run the Project
1. Clone the Repository
git clone https://github.com/adarsh-pandey-alt/student-placement-prediction.git
cd student-placement-prediction


Replace https://github.com/adarsh-pandey-alt/student-placement-prediction.git with the URL of your GitHub repository.

2. Install the Required Libraries

You can install all required libraries using:

pip install -r requirements.txt

3. Train the Machine Learning Models

Run:

python training.py


This will:

Load the dataset

Preprocess the data

Train the three Machine Learning models

Evaluate the models

Perform cross-validation

Generate feature importance analysis

Save the trained models as .pkl files

4. Run the Streamlit Application

After training the models, run:

streamlit run app.py


The Streamlit application will open in your web browser.

📊 Prediction Output

The Streamlit application provides predictions from:

Logistic Regression

Decision Tree

Random Forest

For each model, the application displays:

Placement prediction

Placement probability

The entered student information can also be viewed within the application.

🔮 Future Improvements

Possible improvements for this project include:

Hyperparameter tuning

ROC-AUC evaluation

Feature engineering

Testing additional Machine Learning algorithms

Using a larger and more diverse dataset

Improved user interface

Model performance comparison visualization

Deployment to a cloud platform

⚠️ Disclaimer

This project provides a Machine Learning-based prediction and does not guarantee actual student placement.

The predictions depend on the quality and characteristics of the dataset used to train the models. The results are intended for educational and demonstration purposes.

👨‍💻 Project Level

This project is designed as a beginner-to-intermediate Machine Learning project for learning and demonstrating:

Classification algorithms

Data preprocessing

Model evaluation

Cross-validation

Feature importance

Machine Learning model deployment using Streamlit