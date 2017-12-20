<template>
  <div>
    <p>완료된 작업 수: {{ childTodos.filter(todo => { return todo.done === true }).length }}</p>
    <p>진행중인 작업 수: {{ childTodos.filter(todo => { return todo.done === false }).length }}</p>

    <my-todo v-on:delete-child-todo="deleteMyTodo" v-for="todo in childTodos" v-bind:todo="todo" :key="todo.title"></my-todo>
  </div>
</template>

<script type="text/javascript">
import myTodo from './Todo';

export default {
  props: ['childTodos'],
  components: {
    myTodo,
  },
  methods: {
    deleteMyTodo(todo) {
      const todoIndex = this.childTodos.indexOf(todo);
      this.childTodos.splice(todoIndex, 1);
    },
  },
};
</script>

<style>

</style>
