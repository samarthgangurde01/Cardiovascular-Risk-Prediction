import numpy as np
import pandas as pd
from flask import Flask, request, render_template

app = Flask(__name__)


df=pd.read_csv("dataset.csv")
df.drop(columns=['Unnamed: 0'],inplace=True)
y = df['TenYearCHD']
X = df.drop(['TenYearCHD'],axis = 1)

from imblearn.combine import SMOTETomek
from imblearn.under_sampling import NearMiss
smk = SMOTETomek(random_state=42)
X,y=smk.fit_resample(X,y)

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X = scaler.fit_transform(X)

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=.20,random_state=5)

from sklearn.linear_model import LogisticRegression
Lr=LogisticRegression()
from sklearn.model_selection import GridSearchCV
param_grid = {'C': [0.001, 0.01, 0.1, 1, 10, 100, 1000] }
Lr_clf = GridSearchCV(LogisticRegression(penalty='l2'), param_grid)
Lr_clf.fit(X_train,y_train)



@app.route('/')
def home():
    return render_template('rap.html')


@app.route('/predict', methods=['POST'])
def predict():
    input_features = [float(x) for x in request.form.values()]
    features_value = [np.array(input_features)]

    features_name = ['age', 'sex', 'is_smoking', 'cigsPerDay', 'BPMeds', 'prevalentHyp','diabetes', 'totChol', 'sysBP', 'BMI', 'heartRate','glucose_median']

    df = pd.DataFrame(features_value, columns=features_name)

    output = Lr_clf.predict(df)

    if output == 1:
        res_val = "Shows Cardiovascular Risk "
    else:
        res_val = " Person is safe from Cardiovascular"

    return render_template('rap.html', prediction_text=format(res_val))


if __name__ == "__main__":
    app.run(debug=True)
