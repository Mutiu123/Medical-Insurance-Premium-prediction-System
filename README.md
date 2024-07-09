## **Project Description**:

**Introduction:**
The Medical Insurance Premium Prediction System is an advanced analytical tool designed to predict the insurance premium costs for individuals based on various demographic and health-related factors. This system leverages machine learning algorithms to provide accurate estimations that can help users in financial planning and decision-making regarding their health insurance.

**Technical Overview:**
The project utilizes a dataset containing historical insurance data, including age, sex, BMI, number of children, smoking status, region, and charges. The data is preprocessed to convert categorical variables into numerical form for better analysis by the machine learning model.

A **Random Forest Regressor** is employed as the predictive model due to its robustness and ability to handle non-linear relationships within the data. The model is trained on a subset of the data (75%) and tested on the remaining 25% to evaluate its performance. The R-squared score is calculated to measure the accuracy of the predictions against the actual charges.
Absolutely! Here's a problem statement for your project:

## **Problem Statement:**
In the realm of healthcare, accurately predicting medical insurance premiums is a complex challenge due to the multitude of factors that influence insurance costs. Individuals and insurance companies alike struggle to estimate these costs effectively, which can lead to financial uncertainty and difficulty in budgeting for healthcare expenses. The Medical Insurance Premium Prediction System aims to address this challenge by utilizing machine learning algorithms to analyse historical insurance data and provide precise premium cost estimations. This system seeks to empower users with actionable insights, enabling them to make informed decisions regarding their health insurance plans.


## **Methodology:**

**Data Collection:**
The project begins with the collection of a comprehensive dataset from historical medical insurance records. This dataset includes key features such as age, sex, BMI, number of children, smoking status, region, and insurance charges.

**Data Preprocessing:**
Upon acquiring the data, preprocessing steps are undertaken to prepare it for analysis. This includes:
- Replacing categorical string values with numerical codes to facilitate computational processing.
- Splitting the dataset into features (X) and target variable (charges - Y).
- Dividing the data into training and testing sets to evaluate the model's performance on unseen data.

**Exploratory Data Analysis (EDA):**
An exploratory analysis is conducted to understand the distribution and relationships within the data. For instance, a distribution plot for the 'age' feature is generated to visualize the age range of insurance holders.

**Model Selection:**
A Random Forest Regressor is chosen as the predictive model due to its effectiveness in handling complex datasets with multiple features influencing the target variable.

**Model Training:**
The model is trained on the training set, which consists of 75% of the total data. The Random Forest algorithm builds multiple decision trees and merges them together to obtain a more accurate and stable prediction.

**Model Testing and Evaluation:**
The trained model is then tested on the remaining 25% of the data. The R-squared score is computed to assess how well the model's predictions correspond to the actual insurance charges.

**Prediction and Deployment:**
The final step involves deploying the trained model into a Streamlit web application. This application serves as an interactive interface where users can input their personal information and receive a predicted insurance premium cost.

**Model Persistence:**
To ensure that the model can be reused without retraining, it is serialized and saved using pickle. This allows for easy loading of the model for future predictions.

This methodology outlines a systematic approach to solving the problem of predicting medical insurance premiums using machine learning techniques and provides a user-friendly interface for practical application.

**Contributions:**
The contributions to the project were multifaceted. They included sourcing and preprocessing the dataset, conducting exploratory data analysis, developing and training the model, evaluating its performance, designing an interactive web application using Streamlit, deploying the trained model into the application, serializing the model for future use without retraining, enhancing user experience, and documenting the process.

**Deployment Process:**
Deployment was a critical phase in which the serialized model was integrated into a Streamlit web application. The user interface was designed to be intuitive, with interactive elements like sliders and select boxes. The application underwent thorough testing before being hosted on Heroku. The final step was launching the application to the public.

**Impact and Practical Applications:**
The system's impact is far-reaching, aiding in financial planning by allowing individuals to estimate future premiums. It helps insurance companies set premiums accurately and provides policymakers with insights for healthcare policy development. The practical applications are diverse, including personal use for premium estimation, assisting insurance agents and healthcare providers, facilitating research in healthcare economics, and serving as an educational tool.

In conclusion, this system not only effectively uses machine learning to predict medical insurance premiums but also stands as a testament to the practical applications of data science in real-world scenarios.



## **System Demo:**

![The System Demo](https://github.com/Mutiu123/Medical-Insurence-Premium-prediction-System/blob/main/demos/demo1.png)



## **To run the model**
1. **Clone the Repository**:
   - First, clone the repository containing the heart disease prediction system code to your local machine. You can do this using Git or by downloading the ZIP file from the repository.

2. **Install Dependencies**:
   - Open your terminal or command prompt and navigate to the project directory.
   - Install the necessary Python libraries mentioned in the `requirements.txt` file using the following command:
     ```
     pip install -r requirements.txt
     ```

3. **Run the Streamlight App**:
   - In the same terminal or command prompt, execute the following command to run the Streamlight app:
     ```
     streamlet run app.py
     ```
   - This will start the local development server, and you'll see a message indicating that the app is running.
   - Open your web browser and visit `http://localhost:8501` (or the URL provided in the terminal) to access the interactive web app.

4. **Predict Heart Disease**:
   - On the Streamlit app, you'll find a search bar where you can Fill in the relevant information for a patient you want to assess.
   - After entering the patient’s details, click the “Predict” button.

## **Model Deployement**
I Deploy the Streamlight app on Heroku to allow others to access it online Here's an updated step-by-step guide on how to run the app on your device:

1. **Access the Deployed App**:
   - Visit the following link: [Medical-Insurance-Premium-prediction-System](https://mipsys-ba1cc9751f4a.herokuapp.com/).
   - You'll see the web interface where users can input patient information and get predictions.

2. **Interact with the App**:
   - On the web page, you'll find input fields for patient details such as age, gender, bmi, children, smoker and region.
   - Fill in the relevant information for a patient you want to assess.

3. **Click the "Predict" Button**:
   - After entering the patient's details, click the "Predict" button.
   - The app will process the input using the trained logistic regression model.

4. **View the Prediction**:
   - The app will display the prediction result: