<template>
  <div class="ui centered card">
    <div class="content" v-show="!isEditing">
      <div class="header">
        {{ todo.title }}
      </div>
      <div class="description">
        {{ todo.description }}
      </div>
      <div class="extra content">
        <span class="right floated edit icon" v-on:click="showForm">
          <i class="edit icon"></i>
        </span>
        <span class="right floated trash icon" v-on:click="deleteTodo(todo)">
          <i class="trash icon"></i>
        </span>
      </div>
    </div>
    <!-- 수정 모드에서 보이게 될 컨텐츠 -->
    <div class="content" v-show="isEditing">
      <div class="ui form">
        <div class="field">
          <label>제목</label>
          <input type="text" v-model="todo.title">
        </div>
        <div class="field">
          <label>설명</label>
          <input type="text" v-model="todo.description">
        </div>
        <div class="ui two button attached buttons">
          <button class="ui blue basic button" v-on:click="hideForm">
            닫기
          </button>
        </div>
      </div>
    </div>
    <div class="ui bottom attached green basic button" v-on:click="undoTodo(todo)" v-show="!isEditing && todo.done">
      완료됨
    </div>
    <div class="ui bottom attached red basic button" v-on:click="completeMyTodo(todo)" v-show="!isEditing && !todo.done">
      진행중
    </div>
  </div>
</template>

<script type="text/javascript">
export default {
  props: ['todo'],
  data() {
    return {
      isEditing: false,
    };
  },
  methods: {
    showForm() {
      this.isEditing = true;
    },
    hideForm() {
      this.isEditing = false;
    },
    deleteTodo(todo) {
      this.$emit('delete-child-todo', todo);
    },
    completeMyTodo(todo) {
      this.$emit('complete-child-todo', todo);
    },
    undoTodo(todo) {
      this.$emit('undoTodo', todo);
    },
  },
};
</script>
