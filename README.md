# Project Title : Cardiovascular Risk Prediction

## Description

we started our project by importing data and then we handeled missing values and duplicates.further we went to analysis During the time of our analysis, we initially did EDA on all the features of our datset.. We first analysed our dependent variable, 'TenYearCHD'. Next we analysed categorical variable and dropped the variable who were not co-related, we also analysed numerical variable, found out the correlation, distribution and their relationship with the dependent variable. We also removed some numerical features and hot encoded the categorical variables.
Next we implemented 3 machine learning algorithms Kneighbour clasiifier, Random Forest and Logistic regression. We did hyperparameter tuning to improve our model performance
we created our flask app and deployed it with on- Heroku 


## Table of Content
* Dataset Information
* Tools and Libraries Used
* Files
* Results
* Screenshots
* Deployment
* Feedback

## Dataset Information
The dataset is from an ongoing cardiovascular study on residents of the town of Framingham,Massachusetts. The classification goal is to predict whether the patient has a 10-year risk offuture coronary heart disease (CHD). The dataset provides the patients’ information. It includes over 4,000 records and 15 attributes.

Dataset Link:-https://raw.githubusercontent.com/samarthgangurde01/Cardiovascular-Risk-Prediction/main/data_cardiovascular_risk.csv


## Tools and Libraries Used
* Pandas
* numpy
* Matplotlib
* Seaborn
* plotly
* sklearn
* imblearn
* pickle


## Files
* This repository contain files as mentioned below

* capston_cardiovascular_risk PREDICTION.ipynb: Google colab contains all the python code, documentation and visualization

* data_cardiovascular_risk.csv: Our dataset 

* Data.csv: Our processed dataset file

* app.py:contains whole structure of app

* requirements.txt:contains required libraries 


## Results

Model	                       Accuracy

KNeighbors classifier	            0.87

Random Forests      	            0.89

Logistic Regression 	            0.70


## Screenshots
![image](https://user-images.githubusercontent.com/93859458/152776902-3650f9bf-455b-454d-a8f0-4185b0159d91.png)
![image](https://user-images.githubusercontent.com/93859458/152777045-bd5211c9-b7d3-4846-ab60-729bbef7d6c4.png)
![image](https://user-images.githubusercontent.com/93859458/152777153-d7e4f1ed-db54-495f-a830-33f3ee6429cf.png)
![image](https://user-images.githubusercontent.com/93859458/152777289-a605ac71-554a-4f8a-a9f1-60bc70a953b3.png)



## Run Locally

Clone the project

```bash
  git clone https://github.com/samarthgangurde01/Cardiovascular-Risk-Prediction
```

Go to the project directory

```bash
  cd my-project
```

Install all the libraries mentioned in the requirements.txt file with the command pip install -r requirements.txt

```bash
   pip install -r requirements.tx
```

Open your terminal/command prompt from your project directory and run the file main.py by executing the command 

```bash
  python3 app.py
```
Go to your browser and type in the address bar.

```bash
  http://127.0.0.1:5000/ 
```

## Deployment

we deployed our app on Heroku
Heroku is a cloud platform as a service (PaaS) supporting several programming languages. One of the first cloud platforms, Heroku has been in development since June 2007, when it supported only the Ruby programming language, but now supports Java, Scala, Python.

1. Signing Up..First, visit Heroku.com and sign up for a new account.

2. Creating Your App,Once you have your account, click the 'New' menu in the upper right corner and select 'Create New App'

3. Now, simply name your new app

4. Connect your github account to the Heroku 

5. Select repository name ,choose branch as main and click on Deploy Branch..Here you gooo!

screenshort of Heroku ploatform
![image](https://user-images.githubusercontent.com/93859458/153572083-e0818742-8166-4e35-91e2-e7b14bed6cf2.png)




## Deployed App
![image](https://user-images.githubusercontent.com/93859458/153576834-35da14bb-d700-48dc-b1f0-e35d993a7760.png)

App Link:-https://cardiovascular-risk-prediction.herokuapp.com

## Trial Dataset
age :- 36
sex :- male
is_smoking :- NO
cigsPerDay :- 0.0
BPMeds :- NO
prevalentHyp:- YES
diabetes :- YES
totChol :- 212
sysBP :-168
BMI :-29.77
heartRat :-72
glucose :-75

## Feedback

If you have any feedback, please reach out to us at samarthgangurde01@gmail.com

