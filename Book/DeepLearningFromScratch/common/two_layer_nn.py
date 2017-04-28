import numpy as np
from collections import OrderedDict
from layers import SoftmaxWithLoss, Affine, Relu

class TwoLayerNet:
    def __init__(self, input_size, hidden_size, output_size, weight_init_std=0.01):
        self.params = None
        self.layers = None
        self.last_layer = None
        
        self.init_params(input_size, hidden_size, output_size, weight_init_std)
        self.init_layers()
        
    def init_params(self, input_size, hidden_size, output_size, weight_init_std):
        self.params = {}
        self.params["W1"] = np.random.randn(input_size, hidden_size) * weight_init_std
        self.params["b1"] = np.zeros(hidden_size)
        self.params["W2"] = np.random.randn(hidden_size, output_size) * weight_init_std
        self.params["b2"] = np.zeros(output_size)
        
    def init_layers(self):
        self.layers = OrderedDict()
        self.layers["Affine1"] = Affine(self.params["W1"], self.params["b1"])
        self.layers["Relu"] = Relu()
        self.layers["Affine2"] = Affine(self.params["W2"], self.params["b2"])
        self.last_layer = SoftmaxWithLoss()
    
    def predict(self, x):
        for layer in self.layers.values():
            x = layer.forward(x)
        return x
    
    def loss(self, x, t):
        y = self.predict(x)
        loss = self.last_layer.forward(y, t)
        return loss
    
    def accuracy(self, x, t):
        y = self.predict(x)
        y = np.argmax(y, axis=1)  # 열을 하나로 축소
        if t.ndim != 1:  # one-hot-encoding == True
            t = np.argmax(t, axis=1)
        
        acc = np.sum(y == t) / x.shape[0]
        return acc
    
    def gradient(self, x, t):
        # 순전파
        self.loss(x, t)
        
        # 역전파
        dout = 1
        dout = self.last_layer.backward(dout)
        
        layers = list(self.layers.values())
        layers.reverse()
        for layer in layers:
            dout = layer.backward(dout)
            
        # 결과 저장
        grads = {}
        grads["W1"] = self.layers["Affine1"].dW
        grads["b1"] = self.layers["Affine1"].db
        grads["W2"] = self.layers["Affine2"].dW
        grads["b2"] = self.layers["Affine2"].db
        return grads
