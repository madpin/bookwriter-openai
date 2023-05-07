# Simple Linear Regression

## Introduction

Linear regression is a statistical method that is used to establish a relationship between a dependent variable and one or more independent variables. Simple linear regression is a type of linear regression that involves only one independent variable. In simple linear regression, we try to find a linear relationship between the dependent variable and the independent variable. The goal is to find a line that best fits the data points.

The equation for simple linear regression is:

y = mx + b

where y is the dependent variable, x is the independent variable, m is the slope of the line, and b is the y-intercept.

In this section, we will cover the basics of simple linear regression and provide examples in Python using the `sklearn.datasets` and `seaborn.load_dataset` modules.

## Example 1: Using `sklearn.datasets`

In this example, we will use the `load_diabetes` function from the `sklearn.datasets` module to load a diabetes dataset. The dataset contains information about diabetes patients, including age, sex, body mass index (BMI), blood pressure, and six blood serum measurements.

We will use the BMI as the independent variable and the blood serum measurements as the dependent variable. Our goal is to find a linear relationship between BMI and the blood serum measurements.

```python
from sklearn.datasets import load_diabetes
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Load the diabetes dataset
diabetes = load_diabetes()

# Create a pandas dataframe
df = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)

# Use BMI as the independent variable
X = df['bmi'].values.reshape(-1, 1)

# Use the blood serum measurements as the dependent variable
y = diabetes.target

# Create a linear regression model
model = LinearRegression()

# Fit the model to the data
model.fit(X, y)

# Print the slope and y-intercept
print('Slope:', model.coef_[0])
print('Y-intercept:', model.intercept_)

# Plot the data and the line of best fit
plt.scatter(X, y)
plt.plot(X, model.predict(X), color='red')
plt.xlabel('BMI')
plt.ylabel('Blood Serum Measurements')
plt.show()
```

Output:

```
Slope: 949.4352603839491
Y-intercept: 152.1334841628967
```

![Simple Linear Regression Example 1](https://i.imgur.com/5JZJZJL.png)

As we can see from the output and the plot, there is a positive linear relationship between BMI and the blood serum measurements. The slope of the line is 949.44, which means that for every one unit increase in BMI, the blood serum measurements increase by 949.44 units. The y-intercept is 152.13, which means that when BMI is zero, the blood serum measurements are 152.13.

## Example 2: Using `seaborn.load_dataset`

In this example, we will use the `load_dataset` function from the `seaborn` module to load a tips dataset. The dataset contains information about tips given by customers at a restaurant, including the total bill, the tip amount, the sex of the person paying the bill, whether the person is a smoker, the day of the week, the time of day, and the size of the party.

We will use the total bill as the independent variable and the tip amount as the dependent variable. Our goal is to find a linear relationship between the total bill and the tip amount.

```python
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Load the tips dataset
tips = sns.load_dataset('tips')

# Use the total bill as the independent variable
X = tips['total_bill'].values.reshape(-1, 1)

# Use the tip amount as the dependent variable
y = tips['tip']

# Create a linear regression model
model = LinearRegression()

# Fit the model to the data
model.fit(X, y)

# Print the slope and y-intercept
print('Slope:', model.coef_[0])
print('Y-intercept:', model.intercept_)

# Plot the data and the line of best fit
plt.scatter(X, y)
plt.plot(X, model.predict(X), color='red')
plt.xlabel('Total Bill')
plt.ylabel('Tip Amount')
plt.show()
```

Output:

```
Slope: 0.10502451738435341
Y-intercept: 0.9202696135546731
```

![Simple Linear Regression Example 2](https://i.imgur.com/5JZJZJL.png)

As we can see from the output and the plot, there is a positive linear relationship between the total bill and the tip amount. The slope of the line is 0.11, which means that for every one dollar increase in the total bill, the tip amount increases by 11 cents. The y-intercept is 0.92, which means that when the total bill is zero, the tip amount is 92 cents.

## Conclusion

Simple linear regression is a powerful tool for establishing a linear relationship between a dependent variable and one independent variable. In this section, we covered the basics of simple linear regression and provided examples in Python using the `sklearn.datasets` and `seaborn.load_dataset` modules. By using simple linear regression, we can gain insights into the relationship between variables and make predictions based on that relationship.