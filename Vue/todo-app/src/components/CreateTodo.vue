<template>
  <div class='ui basic content center aligned segment'>
    <button class='ui basic button icon' v-on:click="openForm" v-show="!isCreating">
      <i class='plus icon'></i>
    </button>
    <div class='ui centered card' v-show="isCreating">
      <div class='content'>
        <div class='ui form'>
          <div class='field'>
            <label>제목</label>
            <input v-model="titleText" type='text' ref='title' defaultValue="">
          </div>
          <div class='field'>
            <label>설명</label>
            <input v-model="descriptionText" type='text' ref='description' defaultValue="">
          </div>
          <div class='ui two button attached buttons'>
            <button class='ui basic blue button' v-on:click="sendForm()">
              만들기
            </button>
            <button class='ui basic red button' v-on:click="closeForm">
              취소
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      titleText: '',
      descriptionText: '',
      isCreating: false,
    };
  },
  methods: {
    openForm() {
      this.isCreating = true;
    },
    closeForm() {
      this.isCreating = false;
    },
    sendForm() {
      if (this.titleText.length > 0 && this.descriptionText.length > 0) {
        this.$emit('hey-please-create-todo', {
          title: this.titleText,
          description: this.descriptionText,
          done: false,
        });
        this.clearnForm();
      }
      this.isCreating = false;
    },
    clearnForm() {
      this.titleText = '';
      this.descriptionText = '';
    },
  },
};
</script>

<style>

</style>
