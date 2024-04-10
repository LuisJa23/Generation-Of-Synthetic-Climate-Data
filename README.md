Rain Prediction using Random Forest
This project uses Random Forest Classifier to predict whether it will rain tomorrow based on various weather factors. The data used in this project is obtained from a CSV file located at ../resources/weatherAUS_clean.csv.

Requirements
Python (version 3.8 or higher)
joblib
pandas
matplotlib
numpy
scikit-learn
Installation
Make sure you have Python installed. You can download it from python.org.

Install the required dependencies using pip:

Clone or download this repository to your local machine.

Navigate to the project directory.

Run the Python script rain_prediction.py.

Usage
The script rain_prediction.py performs the following steps:

Loads the dataset from the CSV file.
Splits the dataset into features and labels.
Converts categorical variables into dummy variables.
Splits the dataset into training and testing sets.
Normalizes the numerical columns using StandardScaler.
Trains a Random Forest Classifier on the training data.
Makes predictions on the testing data.
Evaluates the performance of the model.
Saves the trained model to a file.
Prints the results and displays a bar chart showing the number of correct predictions for "Yes" and "No" rain tomorrow.
Contribution
If you'd like to contribute to this project, feel free to fork this repository, make your changes, and submit a pull request.

License
This project is licensed under the MIT License.

Contact
For any questions or feedback regarding this project, please contact javierlink22@gmail.com.
