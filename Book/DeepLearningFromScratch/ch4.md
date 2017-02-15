# 챕터 4 : 신경망 학습

`훈련 데이터`와 `시험 데이터`를 나눈다. -> `오버피팅`된 모델을 피하고 `범용 능력`을 제대로 평가하기 위해

## 손실 함수 loss function
비용 함수 cost function 라고도 함

### 평균 제곱 오차 mean squared error, MSE
수식 어떻게 쓰는지 모르겠네  

> [여기서 함](http://latex.codecogs.com/eqneditor/editor.php)  

![오 어떻게 하는지 알았다](img/ch4_식4.1.png)

직관적이당  
한 원소만 1로 그 외는 0 -> `원-핫 인코딩`  

```python
def mean_squared_error(y, t):
    return 0.5 * np.sum((y-t)**2)
```

오차가 더 작은 쪽이 정답에 더 가까울 것이라고 판단 가능

### 교차 엔트로피 오차 cross entropy error, CEE
이걸 더 자주 본 듯

![직관적이지가 않아](img/ch4_식4.2.png)

> 별로 직관적으로 와닿진 않는데 `딥러닝 첫걸음`이라는 책에는 좀 더 친절하게 설명되어 있다.  
그 책의 설명을 가져와 보면 신경망의 출력 y가 0에서 1사이여야 하기 때문에 시그모이드, 소프트맥스 활성함수와 같이 사용되는 경우가 많다.  
직관적으로 이해해 보려면 그냥 오차 d-y(딥러닝 첫걸음에서는 정답이 d이다)가 0일 때는 비용함수의 값이 0이고 y가 0에 가까울수록, 즉 오차가 커질수록 비용함수의 값이 급격하게 커진다. (log니까)

하여튼 수식의 설명은 이렇게 얘는 `MSE`보다 같은 오차에 더 민감하게 반응한다는 점이다.  
그래서 회귀 문제와 같은 경우가 아니면 `CEE`가 좋다고 한다.

```python
def cross_entropy_error(y, t):
    delta = 1e-7
    return -np.sum(t * np.log(y + delta))
```
`delta`가 존재하는 이유는 `np.log()`에 0을 전달하면 `-inf`가 튀어나오기 때문에 그렇다.

### 미니배치 학습
#### 미니배치의 필요성
기계학습은 훈련 데이터에 대한 손실 함수의 값을 구하고, 그 값을 최대한 줄여주는 매개변수를 찾아낸다.  
위에서 본 손실 함수는 훈련 데이터 하나에 대한 것이고, 훈련 데이터가 100개라면 손실 함수로 계산한 100개의 값들을 합해 지표로 삼는다.  
그러려면 그냥 위의 수식에서 앞에 `1/n * sigma` 해주면 된다.  
수식은 만들기 귀찮아서 생략한다. 하여튼 이렇게 `평균 손실 함수`를 구할 수 있다.  

MNIST 데이터셋은 훈련 데이터가 60,000개다. (내가 알기론 5만개 + 테스트용 1만개인데 그게 그거니 넘어가자)  
다른 학습 모델을 위해 훈련시킬 땐 데이터가 수백만 수천만도 넘는다. -> 학습시간 폭발  
그렇기에 훈련 데이터 중 일부를 추려 전체의 `근사치`로 이용한다.  
이렇게 일부만 골라 학습을 수행하는데 그 `일부`를 `미니배치 mini-batch`라고 한다.  
6만장중 100장을 무작위로 뽑아 학습시키는 것

#### 미니배치 코드

```python
import sys, os
sys.path.append(os.pardir) # 이부분은 3장에 설명되어있다.
import numpy as np
from dataset.minist import load_mnist # 이부분도 3장에 설명되어있다.
# 추후에 시간이 있으면 load_mnist에 대해 공부한 내용을 올릴 것이다

(x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, one_hot_label=True)
# normalize가 True면 각 픽셀의 값(여기선 784개의 열 각각)이 0.0과 1.0사이다
# one_hot_label이 True면 t_train(정답)의 값이 [0, 1, 0, ...]식으로 된다.
# False이면 그냥 3, 5, 1, 9 이런식으로 된다.

print(x_train.shape) # (60000, 784)
print(t_train.shape) # (60000, 10)
```
훈련 데이터가 6만개인게 맞구나 하핫  
`ndarray`객체라서 shape프로퍼티가 있다.  
행이 6만개 열이 784개인데 손글씨 이미지가 28x28해상도이다.  
이를 1차원으로 쭉 펼쳐놔서 784인 것이다.  
`t_train`은 열이 10개인데 0부터 9까지 정답인 열이 1의 값을 갖는다.

여기서 무작위로 10장만 빼내려면

```python
train_size = x_train.shape[0] # 60000
batch_size = 10
batch_mask = np.random.choice(train_size, batch_size)
x_batch = x_train[batch_mask]
t_batch = t_train[batch_mask]
```

`np.random.choice(60000, 10)`은 0과 60000사이에서 10개를 뽑아 `ndarray`로 반환한다.
```python
>>> np.random.choice(60000, 10)
array([8013, 23832, ...])
```
그래서 이 mask를 인덱스에 전달하면 해당 인덱스에 해당하는 훈련 데이터만 뽑혀나온다.  
역시 갓갓 numpy!

### 미니배치용 교차 엔트로피 오차
아까랑 구현이 미묘하게 다르다.  
아까꺼가 보기 귀찮아서 여기로 가져왔다.

```python
def cross_entropy_error(y, t):
    delta = 1e-7
    return -np.sum(t * np.log(y + delta))
```
이제 이걸 이렇게 바꿨다.

```python
def cross_entropy_error(y, t):
    if y.ndim == 1:
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)
    
    batch_size = y.shape[0]
    return -np.sum(t * np.log(y)) / batch_size
```
아까 위에서 `x_batch`, `t_batch`를 뽑았는데 한 20개 뽑았다고 해보자.  
그럼 `x_batch.shape`는 `(20, 784)`, `t_batch.shape`는 `(20, 10)`이다.  
그리고 어찌저찌 신경망을 통하고 softmax 활성함수를 통해  
`[0.0, 6.0, 1.0, 0.5, 0.0, 1.0, 0.5, 2.0, 0.0, 0.0]`의 y 하나를 구할 수 있다. 소프트맥스에 관한건 3장에 있다.  
20개를 뽑았으니 y의 shape는 `(20, 10)`이다.  
그럼 if문은 가볍게 무시되고 batch_size는 20이 된다.  
t는 one hot encoding되어있기에 0인 부분의 로그곱도 가볍게 무시되고 t가 1인 부분만 np.log(y)가 실행된다.  
그리고 np.sum을 통해 20개의 행을 다 합해주고 batch_size로 나누어 최종적으로 `평균 CEE`를 구한다.

만약 y.ndim이 1일 때, 즉 batch_size가 1인 경우, 다른 말로 데이터가 하나일 경우에는 reshape로 데이터의 형태를 다듬는다.  
이렇게 해주지 않으면 y.shape[0]이 10(열의 개수)가 되어버려서 의도했던 출력이 나오지 않는다.
