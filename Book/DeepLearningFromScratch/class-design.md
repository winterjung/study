#  CustomNetwork
## 특징
- 각 layer의 output distribution 시각화
- distribution과 weight의 realtime plotting
- 가중치 초깃값 지정
- 배치정규화 레이어
- 드룹아웃 레이어
- 인풋, 아웃풋 사이즈 설정
- 히든 레이어 개수, 노드 개수 설정
- 컨볼루션, 풀링 layer도 추가가능하게


## 변수
## 메서드

# Trainer
## 특징
- optimizer 설정
- loss, accuracy를 클래스에서 관리
- epoch, 미니배치 사이즈
- validatoin, test관리

## 변수
### 전달되는 변수
- `network`
- `verbose` : step마다 train loss, epoch마다 acc 출력
- `x_train`, `t_train`, `x_test`, `t_test` : 트레인, 테스트 데이터셋
- `epoch` : 횟수지정
- `batch_size`
- `evaluate_sample_num_per_epoch` : 데포크마다 샘플 수만큼 평가
- `optimizer` : `SGD`, `Momentum`, `Nesterov`, `AdaGrad`, `RMSprop`, `Adam`

### 내부에서 만드는 변수
- `train_size`
- `iter_per_epoch` : 1 epoch당 iter횟수
- `max_iter`
- `current_iter`, `current_epoch`
- `train_loss_list`, `train_acc_list`, `test_acc_list`

## 메서드
- `__init__`
- `train_step` : batch_mask -> network.gradient -> optimizer.update -> network.loss
  중간중간 epoch에 따라 test진행, 중간결과 출력
- `train` : `train_step`실행, 최종 test_acc구하고 `verbose`에 따라 최종 테스트 정확도 출력