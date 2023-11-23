import numpy as np

class Perception:
    """ Perceptron classifier.

    Parameters
    ----------------------
    eta : float
        learning rate. (between 0.0 and 1.0)
    n_iter : int
        Passes over the training dataset.
    random_state : int
        Random number generator seed for random weight initialization.

    Attributes
    ----------------------
    w_ : 1d_array
        Weights after fitting.
    b_ : Scalar
        Bias unit after fitting.

    errors : list
        Number of misclassfications (updates) in each epoch.

    """
    def __init__(self, eta=0.01, n_iter=50, random_state = 1):  #eta:lr
        self.eta = eta
        self.n_iter = n_iter
        self.random_state = random_state

    def fit(self, X, y):
        """ Fit training data.

        Parameters
        ----------------------
        X : {array-like}, shape = [n_examples, n_features]
            Training vectors, when n_examples is the number of examples
            ans n_features is the number of features.
        Y : array-like, shape = [n_examples]
            Target values.

        Returns
        ----------------------
        self : object

        """
        regn = np.random.RandomState(self.random_state)
        self.w_ = regn.normal(loc=0.0, scale=0.01, size=X.shape[1])
        # 上述语句为初始化权重向量,  均值为0(以y轴为中心的正态分布)，标准差为0.01的正态分布的随机数

        self.b_ = np.float_(0.)
        self.errors_ = []

        for _ in range(self.n_iter):
            errors = 0
            for xi, target in zip(X,y):
                update = self.eta * (target - self.predict(xi))
                self.w_ += update * xi
                self.b_ += update
                errors += int(update != 0.0)
            self.errors_.append(errors)
        return self

    def net_input(self, X):
        """Calculate net input"""
        return np.dot(X, self.w_) + self.b_

    def predict(self, X):
        """return class label after unit step"""
        return np.where(self.net_input(X) >= 0.0, 1, 0)