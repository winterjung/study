<template>
  <div>
    <todo-list v-bind:child-todos="todos"></todo-list>
    <!-- 이것도 동작함 <TodoList></TodoList> -->
  </div>
</template>

<script>
import TodoList from './components/TodoList';

export default {
  name: 'app',
  components: {
    TodoList,
  },
  data() {
    return {
      todos: [
        {
          title: 'Python 배우기',
          description: `Async를 이용한 비동기 작업 처리, 
          소켓 통신 예제, pipenv를 사용한 프로젝트 구성,
          CI적용, 파이썬 패턴 정리`,
          done: false,
        },
        {
          title: 'Vue 배우기',
          description: 'Vue는 너무 어렵다. vue init만 했는데도 알지 못하는 파일이 무척 많이 생겼다.',
          done: true,
        },
        {
          title: '1년 정리하기',
          description: '나는 1년동안 무엇을 했을까? 상반기엔 학교다니면서 학부연구생을 했다. 프로젝트는 했나?',
          done: false,
        },
        {
          title: '하반기 회고하기',
          description: '소마도하고 발표도하고 블록체인 공부하고...',
          done: false,
        },
      ],
    };
  },
};
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
