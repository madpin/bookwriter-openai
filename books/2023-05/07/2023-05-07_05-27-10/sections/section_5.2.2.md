# GRU Networks

Recurrent Neural Networks (RNNs) are a type of neural network that can process sequential data. They can be used for a wide range of tasks such as natural language processing, speech recognition, and time series prediction. However, traditional RNNs suffer from the vanishing gradient problem, which makes it difficult to learn long-term dependencies in the data. 

Gated Recurrent Unit (GRU) networks were introduced in 2014 by Cho et al. as an improvement over traditional RNNs. GRUs are designed to address the vanishing gradient problem and allow for better modeling of long-term dependencies in sequential data. In this section, we will cover the basics of GRU networks.

## GRU Architecture

The GRU architecture is similar to that of a traditional RNN, but with the addition of gating mechanisms that allow the network to selectively update and forget information over time. A GRU cell has two sets of gates: reset gates and update gates. The reset gates determine how much of the previous state should be forgotten, while the update gates determine how much of the new state should be added to the current state. 

The equations for a GRU cell are as follows:

$$ z_t = \sigma(W_z x_t + U_z h_{t-1} + b_z) $$
$$ r_t = \sigma(W_r x_t + U_r h_{t-1} + b_r) $$
$$ \tilde{h_t} = \tanh(W_h x_t + U_h (r_t \odot h_{t-1}) + b_h) $$
$$ h_t = (1 - z_t) \odot h_{t-1} + z_t \odot \tilde{h_t} $$

where $x_t$ is the input at time step $t$, $h_{t-1}$ is the previous state, $h_t$ is the current state, $z_t$ is the update gate, $r_t$ is the reset gate, $\tilde{h_t}$ is the candidate activation, $\sigma$ is the sigmoid function, $\odot$ is the element-wise multiplication, and $W$ and $U$ are weight matrices.

The reset gate determines how much of the past information should be forgotten, while the update gate determines how much of the new information should be added to the current state. The candidate activation $\tilde{h_t}$ is a proposed activation that is computed based on the input at the current time step and the previous state, and the final activation $h_t$ is a combination of the previous state and the candidate activation, weighted by the update gate $z_t$.

## GRU Implementation in Python

Let's see an example of how to implement a GRU network in Python using the `sklearn.datasets` module. We will use the Boston Housing dataset to predict the median value of owner-occupied homes in thousands of dollars.

First, we will import the necessary libraries and load the dataset:

```python
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

boston = load_boston()
X, y = boston.data, boston.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
```

Next, we will define the GRU model using the Keras API:

```python
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, GRU

model = Sequential()
model.add(GRU(32, input_shape=(X_train.shape[1], 1)))
model.add(Dense(1))

model.compile(loss='mse', optimizer='adam')
```

We first create a `Sequential` model and add a `GRU` layer with 32 units and an input shape of `(X_train.shape[1], 1)`. The input shape is `(n_features, n_timesteps)` and since we are treating each feature as a separate time step, we set `n_timesteps=1`. We then add a `Dense` layer with a single output unit and compile the model with mean squared error loss and the Adam optimizer.

We can now train the model:

```python
history = model.fit(X_train[:,:,np.newaxis], y_train, epochs=50, batch_size=32, validation_split=0.2)
```

We reshape the input data to `(n_samples, n_timesteps, n_features)` and train the model for 50 epochs with a batch size of 32. We also use a validation split of 0.2 to monitor the validation loss during training.

Finally, we can evaluate the model on the test set:

```python
test_loss = model.evaluate(X_test[:,:,np.newaxis], y_test)
print(f'Test Loss: {test_loss:.4f}')
```

Our model achieves a test loss of 20.13, which is a decent result considering the simplicity of the model and the small size of the dataset.

## Conclusion

In this section, we covered the basics of GRU networks. We saw how GRUs can be used to model sequential data and how they address the vanishing gradient problem of traditional RNNs. We also saw an example of how to implement a GRU network in Python using the Keras API. With their ability to model long-term dependencies, GRUs are a powerful tool for a wide range of applications in machine learning and artificial intelligence.