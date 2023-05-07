# Multinomial Logistic Regression

Welcome to the section on Multinomial Logistic Regression! In this section, we will cover the basics of multinomial logistic regression, a popular machine learning algorithm used for classification problems with more than two classes.

## Introduction

Multinomial logistic regression is an extension of binary logistic regression, which is used for binary classification problems. In binary logistic regression, the dependent variable is binary, meaning it can take on only two values (e.g. 0 or 1). In multinomial logistic regression, the dependent variable can take on more than two values, making it suitable for classification problems with multiple classes.

The goal of multinomial logistic regression is to predict the probability of each class given a set of input features. The algorithm works by fitting a set of coefficients to the input features, which are used to calculate the probability of each class. The class with the highest probability is then predicted as the output.

## Example: Iris Dataset

To demonstrate how multinomial logistic regression works, let's use the famous Iris dataset. The Iris dataset contains measurements of the sepal length, sepal width, petal length, and petal width for three different species of iris flowers: setosa, versicolor, and virginica.

First, let's load the dataset and split it into training and testing sets:

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=42)
```

Next, let's fit a multinomial logistic regression model to the training data:

```python
from sklearn.linear_model import LogisticRegression

model = LogisticRegression(multi_class='multinomial', solver='lbfgs')
model.fit(X_train, y_train)
```

We can now use the trained model to make predictions on the test data:

```python
y_pred = model.predict(X_test)
```

Finally, let's evaluate the performance of the model using accuracy as the metric:

```python
from sklearn.metrics import accuracy_score

accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")
```

The output should be something like:

```
Accuracy: 1.0
```

This means that the model correctly predicted the species of all the flowers in the test set.

## Example: Titanic Dataset

Let's try another example using the Titanic dataset, which contains information about passengers on the Titanic and whether they survived or not.

First, let's load the dataset and split it into training and testing sets:

```python
import seaborn as sns
from sklearn.model_selection import train_test_split

titanic = sns.load_dataset('titanic')
titanic = titanic.dropna() # drop rows with missing values
X = titanic[['pclass', 'age', 'fare']]
y = titanic['survived']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```

Next, let's fit a multinomial logistic regression model to the training data:

```python
from sklearn.linear_model import LogisticRegression

model = LogisticRegression(multi_class='multinomial', solver='lbfgs')
model.fit(X_train, y_train)
```

We can now use the trained model to make predictions on the test data:

```python
y_pred = model.predict(X_test)
```

Finally, let's evaluate the performance of the model using accuracy as the metric:

```python
from sklearn.metrics import accuracy_score

accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")
```

The output should be something like:

```
Accuracy: 0.75
```

This means that the model correctly predicted the survival status of 75% of the passengers in the test set.

## Conclusion

In this section, we covered the basics of multinomial logistic regression, a popular machine learning algorithm used for classification problems with more than two classes. We demonstrated how to use multinomial logistic regression on two different datasets, the Iris dataset and the Titanic dataset, using Python and scikit-learn. We hope this section has been helpful in understanding how multinomial logistic regression works and how it can be applied to real-world problems.