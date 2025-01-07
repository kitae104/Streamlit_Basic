import streamlit as st
from sklearn.datasets import make_regression
import numpy as np
import plotly.graph_objects as go

class LogisticRegression():
    """
    Logistic Regression model.
    """
    def __init__(self, n_epochs=100, lr=1e-3):
        self.weights = None
        self.bias = 0.0
        self.n_epochs = n_epochs
        self.lr = lr

    def _sigmoid(self, Z):
        """
        Implements the stable version of the sigmoid function.
        """
        return np.array([1 / (1 + np.exp(-z)) if z >= 0 else np.exp(z) / (1 + np.exp(z)) for z in Z])
    
    def _loss(self, y_true, y_pred, eps=1e-9):
        """
        Implements the stable version of the binary cross-entropy loss function. Debug only.
        """
        return -1.0 * np.mean(y_true * np.log(y_pred + eps) + (1 - y_true) * np.log(1 - y_pred + eps))
    
    def _update(self, X, y_true, y_pred):
        """
        Computes the gradient of the loss function and updates the model.
        """
        dLdw = np.matmul((y_pred - y_true), X)
        dLdb = np.sum((y_pred - y_true))
        self.weights = self.weights - self.lr * dLdw
        self.bias = self.bias - self.lr * dLdb

    def fit(self, X, y):
        """
        Fits the model to the data.
        """
        self.weights = np.zeros((X.shape[1]))
        for _ in range(self.n_epochs):
            z = np.matmul(self.weights, X.transpose()) + self.bias
            y_pred = self._sigmoid(z)
            self._update(X, y, y_pred)

    def predict(self, X):
        """
        Predicts classes for X.
        """
        z = np.matmul(self.weights, X.transpose()) + self.bias
        y_pred = self._sigmoid(z)
        return [1 if p > 0.5 else 0 for p in y_pred]
    
class LinearRegression():
    """
    Linear Regression model.
    """
    def __init__(self, n_epochs=2000, lr=1e-3):
        self.m = 0.0
        self.c = 0.0
        self.n_epochs = n_epochs
        self.lr = lr

    def _update(self, X, y, y_pred):
        """
        Computes the gradient of the loss function and updates the model.
        """
        dLdm = (-2 / len(X)) * np.sum(X * (y - y_pred))
        dLdc = (-2 / len(X)) * np.sum(y - y_pred)
        self.m = self.m - self.lr * dLdm
        self.c = self.c - self.lr * dLdc

    def fit(self, X, y):
        """
        Fits the model to the data.
        """
        for _ in range(self.n_epochs):
            y_pred = self.m * X + self.c
            self._update(X, y, y_pred)

    def predict(self, X):
        """
        Predicts y values for X.
        """
        return self.m * X + self.c


## data 
def train_test_split(X, y, train_size=None, test_size=None):
    """
    Splits X and y into training and test portions.
    """
    n = len(X)
    p = np.random.permutation(n)
    X_shuffled, y_shuffled = X[p], y[p]
    if train_size != None:
        n_train = int(train_size * n)
    elif test_size != None:
        n_train = int(n - test_size * n)
    return X_shuffled[:n_train], X_shuffled[n_train:], y_shuffled[:n_train], y_shuffled[n_train:]

def normalize_data(X):
    """
    Normalizes the data.
    """
    for i in range(X.shape[-1]):
        col = X[:, i]
        X[:, i] = (col - col.min()) / (col.max() - col.min())

def make_sin(n_samples=100, noise=0.0):
    """
    Produces a sinusoidal regression problem.
    """
    x = np.linspace(-5, 5, num=n_samples)
    y = np.sin(x) + np.random.normal(scale=noise, size=n_samples)
    return x.reshape((len(x), 1)), y

## metrics
def confusion_matrix(y_true, y_pred):
    """
    Computes the confusion matrix.
    """
    classes = np.unique(y_true)
    cm = np.zeros((len(classes), len(classes)))
    for i in range(len(classes)):
        for j in range(len(classes)):
           cm[i, j] = np.sum((y_true == classes[i]) & (y_pred == classes[j]))
    return cm

def accuracy_score(y_true, y_pred):
    """
    Computes the accuracy score.
    """
    cm = confusion_matrix(y_true, y_pred)
    return np.sum(np.diag(cm)) / np.sum(cm)

def precision_score(y_true, y_pred):
    """
    Computes the precision score.
    """
    cm = confusion_matrix(y_true, y_pred)
    return np.mean(np.diag(cm) / np.sum(cm, axis=0))

def recall_score(y_true, y_pred):
    """
    Computes the recall score.
    """
    cm = confusion_matrix(y_true, y_pred)
    return np.mean(np.diag(cm) / np.sum(cm, axis=1))

def entropy(y):
    """
    Computes entropy.
    """
    _, counts = np.unique(y, return_counts=True)
    p = counts / len(y)
    return -np.sum(p * np.log2(p))

def gini_impurity(y):
    """
    Computes Gini impurity.
    """
    _, counts = np.unique(y, return_counts=True)
    p = counts / len(y)
    return 1 - np.sum(p**2)

def variance(y):
    """
    Computes variance.
    """
    return np.var(y)

def information_gain(y_parent, y_left, y_right, criterion='gini'):
    """
    Computes information gain.
    """
    if criterion == 'gini':
        f = gini_impurity
    elif criterion == 'entropy':
        f = entropy
    elif criterion == 'variance':
        f = variance
    f = gini_impurity if criterion == 'gini' else entropy
    return f(y_parent) - (len(y_left) / len(y_parent)) * f(y_left) - (len(y_right) / len(y_parent)) * f(y_right)

def mean_squared_error(y_true, y_pred):
    """
    Mean squared error.
    """
    return np.mean(np.square(y_true - y_pred))

def _create_scatter_plot(x, y, color, marker_symbol=None):
    """
    Creates a Scatter object.
    """
    return go.Scatter(
        x=x,
        y=y,
        mode='markers',
        marker_symbol=marker_symbol,
        marker=dict(
            color=color,
            colorscale=['rgb(0, 0, 255)', 'rgb(255, 0, 0)'],
            line=dict(width=1),
        ),
        showlegend=False
    )

def create_plot():
    """
    Creates a plot.
    """
    fig = go.Figure()
    fig.update_xaxes(showgrid=True)
    fig.update_yaxes(showgrid=True)
    return fig

def add_data_to_plot(fig, X, y, marker_symbol='circle', problem_type='classification'):
    """
    Adds data to a plot.
    """
    if problem_type == 'classification':
        scatter = _create_scatter_plot(X[:, 0], X[:, 1], y, marker_symbol=marker_symbol)
    elif problem_type == 'regression':
        scatter = _create_scatter_plot(X, y, 'rgb(0, 0, 255)', marker_symbol=marker_symbol)
    fig.add_trace(scatter)

def add_decision_boundary(fig_train, fig_test, X, model):
    """
    Adds a classification decision boundary to the plots.
    """
    h = 0.01
    min1, max1 = X[:, 0].min() - 0.1, X[:, 0].max() + 0.1
    min2, max2 = X[:, 1].min() - 0.1, X[:, 1].max() + 0.1
    x1_grid = np.arange(min1, max1, h)
    x2_grid = np.arange(min2, max2, h)
    xx, yy = np.meshgrid(x1_grid, x2_grid)
    r1, r2 = xx.flatten(), yy.flatten()
    r1, r2 = r1.reshape((len(r1), 1)), r2.reshape((len(r2), 1))
    grid = np.hstack((r1, r2))
    y_pred = np.array(model.predict(grid))
    zz = y_pred.reshape(xx.shape)
    boundary = go.Heatmap(
        x=xx[0], 
        y=x2_grid, 
        z=zz, 
        colorscale=['rgb(128, 128, 255)', 'rgb(255, 128, 128)'], 
        showscale=False
    )
    fig_train.add_trace(boundary)
    fig_test.add_trace(boundary)

def add_regression_line(fig, X, model):
    """
    Adds a regression line to the plot.
    """
    h = 0.01
    min, max = X.min() - 0.1, X.max() + 0.1
    x_grid = np.arange(min, max, h)
    y_pred = np.array(model.predict(x_grid))
    line = go.Scatter(
        x=x_grid, 
        y=y_pred,
        mode='lines',
        marker=dict(
            color='rgb(255, 0, 0)',
            line=dict(width=1),
        ),
        showlegend=False,
    )
    fig.add_trace(line)

def add_clustering_scheme(fig, x, y, labels, marker_symbol='circle'):
    """
    Adds a clustering scheme to the plot.
    """
    scatter = _create_scatter_plot(x, y, labels, marker_symbol=marker_symbol)
    fig.add_trace(scatter)


st.set_page_config(page_title='Regression', layout='centered')
st.title('Regression :chart_with_upwards_trend:')

st.markdown(
    """
    This page showcases the implementation of the regression Tool. 
    With this tool, you have the flexibility to choose from two default 
    datasets, select different models, and visualize the predicted outcomes. 
    Additionally, you can tailor the data parameters and fine-tune the 
    model hyperparameters to study the behavior of the chosen regressor.
    """
)

REGRESSION = 'Linear'
SINE = 'Sine'
LINEAR = 'Linear regression'
REGRESSION_TREE = 'Regression tree'
KNN = 'K-nearest neighbors'

st.header('Data')

data_option = st.selectbox(
    'Select a dataset',
    (REGRESSION, SINE),
)

n_samples = st.slider('Select the number of samples', 0, 1000, 500, step=10)
if data_option == REGRESSION:
    noise = st.slider('Select the amount of noise', 0.0, 50.0, 25.0)
    X, y = make_regression(n_samples=n_samples, n_features=1, noise=noise)
elif data_option == SINE:
    noise = st.slider('Select the amount of noise', 0.0, 1.0, 0.3)
    X, y = make_sin(n_samples=n_samples, noise=noise)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)

st.header('Model')
    
model_option = st.selectbox(
    'Select a model',
    (LINEAR, REGRESSION_TREE, KNN),
)

if model_option == LINEAR:
    n_epochs = st.slider('Select the number of training iterations', 1000, 3000, 2000)
    lr = st.slider('Select the learning rate value', min_value=0.0001, step=0.001, max_value=0.005, value=0.001, format='%f')
    model = LinearRegression(n_epochs=n_epochs, lr=lr)
elif model_option == REGRESSION_TREE:
    max_depth = st.slider('Select the maximum depth', 0, 10, 5)
    min_samples_split = st.slider('Select the minimum number of samples required to split a node', 0, 5, 2)
    model = DecisionTreeRegressor(max_depth=max_depth, min_samples_split=min_samples_split)
elif model_option == KNN:
    n_neighbors = st.slider('Select the number of neighbors', 1, 10, 5)
    model = KNeighborsRegressor(n_neighbors=n_neighbors)

X_train = X_train[:, 0]
model.fit(X_train, y_train)

st.header('Results')

fig = create_plot()
add_data_to_plot(fig, X_train, y_train, marker_symbol='circle', problem_type='regression')
add_regression_line(fig, X, model)
st.plotly_chart(fig, use_container_width=True)

