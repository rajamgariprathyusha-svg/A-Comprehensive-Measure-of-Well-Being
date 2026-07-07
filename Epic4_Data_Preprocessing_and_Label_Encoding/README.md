# Epic: Checking and Handling Null Values

## Objective
The objective of this task is to identify missing (null) values in the selected independent variables and handle them before training the machine learning model.

## Dataset
- Dataset Name: Human Development Index Project Dataset
- File: `human-development-index-project-dataset.xlsx`

## Independent Variables (X)
- Life Expectancy
- Schooling
- GNI per Capita
- Internet Users (%)

## Process
1. Load the dataset using Pandas.
2. Select the independent variables.
3. Check for missing values using `isnull().sum()`.
4. Fill missing values with the mean of each column using `fillna(X.mean())`.
5. Verify that all missing values have been handled.

## Technologies Used
- Python
- Pandas

## Output
- Displays the number of null values before handling.
- Replaces missing values with the column mean.
- Displays the updated dataset with no missing values.

## Conclusion
This task ensures that the dataset is free from missing values in the selected input features, making it suitable for training the machine learning model.