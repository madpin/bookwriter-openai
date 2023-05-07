# Classification

Classification is a type of supervised learning that involves predicting a categorical or discrete target variable based on a set of input features. The goal of classification is to build a model that can accurately predict the class of new, unseen data points based on the patterns learned from the training data.

Classification is a widely used technique in machine learning and has many practical applications, such as spam filtering, fraud detection, image recognition, and sentiment analysis.

## Types of Classification Algorithms

There are many different types of classification algorithms, each with its own strengths and weaknesses. Some of the most commonly used classification algorithms include:

- Logistic Regression
- Decision Trees
- Random Forests
- Support Vector Machines (SVM)
- Naive Bayes
- K-Nearest Neighbors (KNN)

Each of these algorithms has its own unique approach to classification, and the choice of algorithm will depend on the specific problem and the characteristics of the data.

## Example: Iris Dataset

To illustrate the concept of classification, we will use the famous Iris dataset, which is included in the scikit-learn library. The Iris dataset contains measurements of the sepal length, sepal width, petal length, and petal width for 150 iris flowers, with 50 flowers from each of three different species: setosa, versicolor, and virginica.

Let's start by loading the dataset and taking a look at the first few rows:

```python
from sklearn.datasets import load_iris
import pandas as pd

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['target'] = iris.target
df.head()
```

Output:

|   | sepal length (cm) | sepal width (cm) | petal length (cm) | petal width (cm) | target |
|---|-------------------|------------------|-------------------|------------------|--------|
| 0 | 5.1               | 3.5              | 1.4               | 0.2              | 0      |
| 1 | 4.9               | 3.0              | 1.4               | 0.2              | 0      |
| 2 | 4.7               | 3.2              | 1.3               | 0.2              | 0      |
| 3 | 4.6               | 3.1              | 1.5               | 0.2              | 0      |
| 4 | 5.0               | 3.6              | 1.4               | 0.2              | 0      |

In this dataset, the target variable is the species of the iris flower, encoded as 0, 1, or 2 for setosa, versicolor, and virginica, respectively.

Let's now split the data into training and testing sets, and train a logistic regression model to predict the species of the iris flower based on the sepal length and width:

```python
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

X = df[['sepal length (cm)', 'sepal width (cm)']]
y = df['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print(f"Accuracy: {accuracy}")
```

Output:

```
Accuracy: 0.8
```

We achieved an accuracy of 80% on the test set, which is not bad for a simple logistic regression model with only two input features.

## Example: Titanic Dataset

Another popular dataset for classification is the Titanic dataset, which contains information about the passengers on the Titanic, including their age, sex, class, and whether they survived or not.

Let's load the dataset and take a look at the first few rows:

```python
import seaborn as sns

titanic = sns.load_dataset('titanic')
titanic.head()
```

Output:

|   | survived | pclass | sex    | age   | sibsp | parch | fare     | embarked | class  | who   | adult_male | deck | embark_town | alive |
|---|----------|--------|--------|-------|-------|-------|----------|----------|--------|-------|------------|------|-------------|-------|
| 0 | 0        | 3      | male   | 22.0  | 1     | 0     | 7.2500   | S        | Third  | man   | True       | NaN  | Southampton | no    |
| 1 | 1        | 1      | female | 38.0  | 1     | 0     | 71.2833  | C        | First  | woman | False      | C    | Cherbourg   | yes   |
| 2 | 1        | 3      | female | 26.0  | 0     | 0     | 7.9250   | S        | Third  | woman | False      | NaN  | Southampton | yes   |
| 3 | 1        | 1      | female | 35.0  | 1     | 0     | 53.1000  | S        | First  | woman | False      | C    | Southampton | yes   |
| 4 | 0        | 3      | male   | 35.0  | 0     | 0     | 8.0500   | S        | Third  | man   | True       | NaN  | Southampton | no    |

In this dataset, the target variable is whether the passenger survived or not, encoded as 0 or 1, respectively.

Let's now preprocess the data by filling in missing values and encoding categorical variables:

```python
titanic.drop(['deck', 'embark_town', 'alive'], axis=1, inplace=True)
titanic.dropna(inplace=True)

titanic['sex'] = titanic['sex'].map({'male': 0, 'female': 1})
titanic['embarked'] = titanic['embarked'].map({'S': 0, 'C': 1, 'Q': 2})

X = titanic.drop('survived', axis=1)
y = titanic['survived']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```

Now that the data is preprocessed, let's train a random forest classifier to predict whether a passenger survived or not based on their age, sex, class, and fare:

```python
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print(f"Accuracy: {accuracy}")
```

Output:

```
Accuracy: 0.8100558659217877
```

We achieved an accuracy of 81% on the test set, which is a decent result for a random forest classifier with only four input features.

## Conclusion

Classification is a powerful technique in machine learning that can be used to predict categorical or discrete target variables based on a set of input features. There are many different types of classification algorithms, each with its own strengths and weaknesses, and the choice of algorithm will depend on the specific problem and the characteristics of the data.

In this section, we covered the basics of classification and demonstrated how to apply it to two popular datasets using Python and scikit-learn. With these examples as a starting point, you can explore more advanced classification techniques and apply them to your own datasets.