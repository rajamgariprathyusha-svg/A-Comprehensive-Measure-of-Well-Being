HDI Prediction Project Workflow - Beginner Guide
This document explains each epic and story in simple step-by-step form.

Epic 1: Environment Setup
1.	Install Python.
2.	Open VS Code.
3.	Open Terminal.
4.	Run: python -m pip install numpy pandas matplotlib seaborn scikit-learn flask
5.	Create folders: dataset, model, templates, static.
Epic 2: Import Libraries
6.	Create train_model.py.
7.	Import numpy, pandas, matplotlib, seaborn, sklearn, pickle and flask.
Epic 3: Dataset
8.	Download dataset from Kaggle.
9.	Place it in dataset folder.
10.	Load using pandas.
11.	Use head(), info(), describe().
12.	Create basic visualizations.
Epic 4: Data Preprocessing
13.	Select X and Y.
14.	Check missing values.
15.	Handle null values.
16.	Encode categorical columns if needed.
17.	Prepare cleaned dataset.
Epic 5: Train-Test Split
18.	Use train_test_split().
19.	Keep 80% training and 20% testing.
Epic 6: Train Model
20.	Create LinearRegression model.
21.	Fit using training data.
22.	Predict on test data.
23.	Evaluate using R2 score.
Epic 7: Save Model
24.	Save model using pickle.dump().
25.	Verify HDI.pkl is created.
Epic 8: Flask Web Application
26.	Create app.py.
27.	Load HDI.pkl.
28.	Create '/' and '/predict' routes.
29.	Create templates/home.html and indexnew.html.
30.	Create static/style.css.
31.	Run python app.py.
32.	Open http://127.0.0.1:5000.
33.	Test prediction and verify output.
