<template>
  <div>
    <p>완료된 작업 수: {{ childTodos.filter(todo => { return todo.done === true }).length }}</p>
    <p>진행중인 작업 수: {{ childTodos.filter(todo => { return todo.done === false }).length }}</p>

    <div v-for="todo in childTodos" :key="todo.title">
      <div>
        <div>
          {{ todo.title }}
        </div>
        <div>
          {{ todo.description }}
        </div>
        <div>
          <span>
            <i></i>
          </span>
        </div>
      </div>
      <div v-show="todo.done">
        완료됨
      </div>
      <div v-show="!todo.done">
        완료
      </div>
    </div>
  </div>
</template>

<script type="text/javascript">
export default {
  props: ['childTodos'],
};
</script>

<style>

</style>
