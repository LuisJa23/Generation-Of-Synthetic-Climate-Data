Description
This code generates synthetic weather data using a Random Forest model. The real data is loaded from a CSV file and split into independent variables (X) and target variable (y). Then, it is split into training and test sets. A RandomForestClassifier model is defined with 100 trees and a maximum depth of 10. The model is fitted to the training set and used to generate synthetic data for 24924 examples. The synthetic data is saved in a CSV file.

Requirements
Python 3.7 or higher
Pandas
Scikit-learn
Running
Install dependencies:
pip install pandas scikit-learn
Run the script:
python generate_synthetic_data.py
Files
generate_synthetic_data.py: The script that generates the synthetic data.
../../sources/weatherAUS_balanced_and_clean.csv: The CSV file with the real data.
../../sources/synthetic_data_random_forest.csv: The CSV file with the generated synthetic data.
Note
This code is an example and can be modified to adapt it to your needs.
It is recommended to adjust the parameters of the RandomForestClassifier model to obtain better results.
Resources
Scikit-learn documentation: https://scikit-learn.org/0.21/documentation.html
Random Forest tutorial: https://www.analyticsvidhya.com/blog/2021/06/understanding-random-forest/
Keywords
Synthetic data generation
Random Forest
Scikit-learn
Python
