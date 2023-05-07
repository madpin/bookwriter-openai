# Simple Linear Regression

## Introduction

Linear regression is one of the most commonly used statistical techniques in machine learning. It is a type of regression analysis that is used to model the relationship between a dependent variable and one or more independent variables. Simple linear regression is the most basic form of linear regression, where we have only one independent variable and one dependent variable. In this section, we will cover the basics of simple linear regression.

## Assumptions of Simple Linear Regression

Before we dive into the details of simple linear regression, it is important to understand the assumptions that underlie this technique. These assumptions are:

1. **Linearity:** The relationship between the dependent variable and the independent variable should be linear. This means that the change in the dependent variable is proportional to the change in the independent variable.

2. **Independence:** The observations should be independent of each other. This means that the value of the dependent variable for one observation should not be influenced by the value of the dependent variable for another observation.

3. **Homoscedasticity:** The variance of the errors should be constant across all levels of the independent variable. This means that the spread of the errors should be the same for all values of the independent variable.

4. **Normality:** The errors should be normally distributed. This means that the distribution of the errors should be a normal distribution.

## Simple Linear Regression Equation

The equation for simple linear regression is:

```
y = mx + b
```

where `y` is the dependent variable, `x` is the independent variable, `m` is the slope of the line, and `b` is the y-intercept.

The slope of the line is given by:

```
m = (n * Σ(xy) - Σx * Σy) / (n * Σ(x^2) - (Σx)^2)
```

where `n` is the number of observations, `x` and `y` are the independent and dependent variables respectively, and `Σ` is the sum of the values.

The y-intercept is given by:

```
b = (Σy - m * Σx) / n
```

## Example in Python

In this example, we will use the `Boston` dataset from the `sklearn.datasets` module to demonstrate how to perform simple linear regression.

First, let's load the dataset and split it into independent and dependent variables:

```python
from sklearn.datasets import load_boston
import pandas as pd

boston = load_boston()
df = pd.DataFrame(boston.data, columns=boston.feature_names)
X = df[['RM']]
y = boston.target
```

We have chosen the `RM` variable as our independent variable, which represents the average number of rooms per dwelling. Our dependent variable is the `target` variable, which represents the median value of owner-occupied homes in $1000s.

Next, let's split the data into training and testing sets:

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```

We have split the data into 80% training and 20% testing sets.

Now, let's create a linear regression model and fit it to the training data:

```python
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)
```

We have created a linear regression model and fit it to the training data.

Next, let's make predictions on the testing data and evaluate the model:

```python
from sklearn.metrics import r2_score

y_pred = model.predict(X_test)
r2 = r2_score(y_test, y_pred)
print(f"R-squared: {r2}")
```

We have made predictions on the testing data and calculated the R-squared value, which is a measure of how well the model fits the data. A value of 1 indicates a perfect fit, while a value of 0 indicates no fit at all.

Finally, let's visualize the results:

```python
import matplotlib.pyplot as plt

plt.scatter(X_test, y_test, color='black')
plt.plot(X_test, y_pred, color='blue', linewidth=3)
plt.xlabel('Number of Rooms')
plt.ylabel('Median Value of Homes (in $1000s)')
plt.show()
```

We have plotted the testing data as black dots and the predicted values as a blue line. The x-axis represents the number of rooms, while the y-axis represents the median value of homes.

## Conclusion

Simple linear regression is a powerful technique for modeling the relationship between a dependent variable and one independent variable. By understanding the assumptions of simple linear regression and how to apply it in Python, you can use this technique to gain insights into your data and make accurate predictions.