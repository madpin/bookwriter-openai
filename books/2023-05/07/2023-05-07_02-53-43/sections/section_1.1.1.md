# Supervised Learning

Supervised learning is a type of machine learning where the algorithm learns from labeled data. In supervised learning, the algorithm is trained on a labeled dataset, where the input data is paired with the correct output. The algorithm then uses this labeled data to make predictions on new, unseen data.

Supervised learning is used in a variety of applications, including image recognition, speech recognition, and natural language processing. In this section, we will cover the basics of supervised learning and its use cases.

## Types of Supervised Learning

There are two main types of supervised learning: regression and classification.

### Regression

Regression is used when the output variable is a continuous value. The goal of regression is to predict a numerical value based on input data. For example, predicting the price of a house based on its size and location.

### Classification

Classification is used when the output variable is a categorical value. The goal of classification is to predict which category an input data point belongs to. For example, predicting whether an email is spam or not.

## Use Cases

Supervised learning is used in a variety of applications, including:

- Predicting customer churn
- Fraud detection
- Sentiment analysis
- Image recognition
- Speech recognition
- Natural language processing

## Example: Iris Dataset

The Iris dataset is a classic dataset used in machine learning. It contains measurements of the sepal length, sepal width, petal length, and petal width of three different species of iris flowers: setosa, versicolor, and virginica.

We will use the Iris dataset to demonstrate how to perform classification using the k-nearest neighbors algorithm.

```python
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

# Load the Iris dataset
iris = load_iris()

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2)

# Create a k-nearest neighbors classifier with k=3
knn = KNeighborsClassifier(n_neighbors=3)

# Train the classifier on the training data
knn.fit(X_train, y_train)

# Make predictions on the testing data
predictions = knn.predict(X_test)

# Print the accuracy of the classifier
print("Accuracy:", knn.score(X_test, y_test))
```

In this example, we first load the Iris dataset using the `load_iris` function from the `sklearn.datasets` module. We then split the dataset into training and testing sets using the `train_test_split` function from the `sklearn.model_selection` module.

Next, we create a k-nearest neighbors classifier with k=3 using the `KNeighborsClassifier` class from the `sklearn.neighbors` module. We train the classifier on the training data using the `fit` method.

Finally, we make predictions on the testing data using the `predict` method and print the accuracy of the classifier using the `score` method.

## Example: Titanic Dataset

The Titanic dataset contains information about the passengers on the Titanic, including their age, sex, and class, as well as whether they survived or not.

We will use the Titanic dataset to demonstrate how to perform binary classification using logistic regression.

```python
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# Load the Titanic dataset
titanic = pd.read_csv("titanic.csv")

# Drop columns that are not useful for prediction
titanic = titanic.drop(["PassengerId", "Name", "Ticket", "Cabin", "Embarked"], axis=1)

# Convert categorical variables to numerical variables
titanic = pd.get_dummies(titanic, columns=["Sex"])

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(titanic.drop("Survived", axis=1), titanic["Survived"], test_size=0.2)

# Create a logistic regression classifier
lr = LogisticRegression()

# Train the classifier on the training data
lr.fit(X_train, y_train)

# Make predictions on the testing data
predictions = lr.predict(X_test)

# Print the accuracy of the classifier
print("Accuracy:", lr.score(X_test, y_test))
```

In this example, we first load the Titanic dataset using the `read_csv` function from the `pandas` module. We then drop columns that are not useful for prediction using the `drop` method and convert categorical variables to numerical variables using the `get_dummies` function.

Next, we split the dataset into training and testing sets using the `train_test_split` function from the `sklearn.model_selection` module. We create a logistic regression classifier using the `LogisticRegression` class from the `sklearn.linear_model` module and train the classifier on the training data using the `fit` method.

Finally, we make predictions on the testing data using the `predict` method and print the accuracy of the classifier using the `score` method.

## Conclusion

Supervised learning is a powerful tool for making predictions based on labeled data. In this section, we covered the basics of supervised learning and its use cases. We also demonstrated how to perform classification using the k-nearest neighbors algorithm and binary classification using logistic regression.