# Binary Logistic Regression

Welcome to the world of binary logistic regression! In this section, we will cover the basics of binary logistic regression, which is a statistical method used to analyze and model the relationship between a binary dependent variable and one or more independent variables.

## Introduction

Binary logistic regression is a type of regression analysis used to model the probability of a certain event occurring. The dependent variable in binary logistic regression is binary, meaning it can only take on two values, typically 0 or 1. The independent variables can be continuous, categorical, or a combination of both.

The goal of binary logistic regression is to find the best fitting model that can predict the probability of the dependent variable being 1, given the values of the independent variables. The output of binary logistic regression is a probability score between 0 and 1, which can be interpreted as the likelihood of the event occurring.

## Example

Let's take a look at a simple example to illustrate the concept of binary logistic regression. Suppose we want to predict whether a student will pass or fail an exam based on their study hours. We have a dataset of 100 students, where the dependent variable "pass" is binary (1 for pass, 0 for fail) and the independent variable "study hours" is continuous.

We can use binary logistic regression to model the relationship between study hours and the probability of passing the exam. The logistic regression equation can be written as:

```
logit(p) = β0 + β1 * study_hours
```

where p is the probability of passing the exam, β0 is the intercept, β1 is the coefficient for study hours, and logit() is the logit function that maps the probability score to the log odds.

We can estimate the coefficients β0 and β1 using maximum likelihood estimation, which is a method for finding the values of the coefficients that maximize the likelihood of the observed data. Once we have the coefficients, we can use the logistic regression equation to predict the probability of passing the exam for any given value of study hours.

## Assumptions

Before we dive deeper into binary logistic regression, it's important to understand the assumptions that underlie this method. Like any statistical method, binary logistic regression has certain assumptions that must be met in order for the results to be valid.

The first assumption is that the dependent variable is binary. This means that the dependent variable can only take on two values, typically 0 or 1. If the dependent variable is continuous, then binary logistic regression is not appropriate.

The second assumption is that the observations are independent. This means that the value of the dependent variable for one observation does not depend on the value of the dependent variable for any other observation. If the observations are not independent, then the results of binary logistic regression may be biased.

The third assumption is that there is no multicollinearity among the independent variables. This means that the independent variables are not highly correlated with each other. If there is multicollinearity, then the coefficients of the independent variables may be unstable and difficult to interpret.

## Model Evaluation

Once we have estimated the coefficients of the logistic regression equation, we need to evaluate the performance of the model. There are several metrics that can be used to evaluate the performance of a binary logistic regression model, including accuracy, precision, recall, and F1 score.

Accuracy measures the proportion of correct predictions out of all predictions. Precision measures the proportion of true positives (correctly predicted positives) out of all predicted positives. Recall measures the proportion of true positives out of all actual positives. The F1 score is the harmonic mean of precision and recall.

## Conclusion

Binary logistic regression is a powerful statistical method for modeling the relationship between a binary dependent variable and one or more independent variables. By estimating the coefficients of the logistic regression equation, we can predict the probability of the dependent variable being 1, given the values of the independent variables. However, it's important to understand the assumptions and limitations of binary logistic regression, and to evaluate the performance of the model using appropriate metrics.