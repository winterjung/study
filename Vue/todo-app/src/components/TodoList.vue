<template>
  <div>
    <p>완료된 작업 수: {{ childTodos.filter(todo => { return todo.done === true }).length }}</p>
    <p>진행중인 작업 수: {{ childTodos.filter(todo => { return todo.done === false }).length }}</p>

    <my-todo 
      v-on:delete-child-todo="deleteMyTodo"
      v-on:complete-child-todo="completeSomeTodo"
      v-on:undoTodo="undoTodo"
      v-for="todo in childTodos"
      v-bind:todo="todo"
      :key="todo.title">
    </my-todo>
  </div>
</template>

<script type="text/javascript">
import sweetalert from 'sweetalert';
import myTodo from './Todo';

export default {
  props: ['childTodos'],
  components: {
    myTodo,
  },
  methods: {
    deleteMyTodo(todo) {
      sweetalert({
        title: '정말 지우시겠습니까?',
        text: '할 일은 다 하시고 지우시는 거겠죠?',
        icon: 'warning',
        dangerMode: true,
        buttons: ['취소', '네! 지워주세요!'],
        closeModal: true,
      }).then(
      (willDelete) => {
        if (willDelete) {
          const todoIndex = this.childTodos.indexOf(todo);
          this.childTodos.splice(todoIndex, 1);
          sweetalert('지워짐!', '해야할 일이 지워졌습니다.', 'success');
        }
      });
    },
    completeSomeTodo(todo) {
      const todoIndex = this.childTodos.indexOf(todo);
      this.childTodos[todoIndex].done = true;
      sweetalert('완료!', '고생하셨습니다.', 'success');
    },
    undoTodo(todo) {
      const todoIndex = this.childTodos.indexOf(todo);
      this.childTodos[todoIndex].done = false;
    },
  },
};
</script>

<style>

</style>
