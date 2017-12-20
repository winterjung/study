<template>
  <div>
    <p>완료된 작업 수: {{ childTodos.filter(todo => { return todo.done === true }).length }}</p>
    <p>진행중인 작업 수: {{ childTodos.filter(todo => { return todo.done === false }).length }}</p>

    <div class="ui centered card" v-for="todo in childTodos" :key="todo.title">
      <div class="content">
        <div class="header">
          {{ todo.title }}
        </div>
        <div class="description">
          {{ todo.description }}
        </div>
        <div class="extra content">
          <span class="right floated edit icon">
            <i class="edit icon"></i>
          </span>
        </div>
      </div>
      <div class="ui bottom attached green basic button" v-show="todo.done">
        완료됨
      </div>
      <div class="ui bottom attached red basic button" v-show="!todo.done">
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
