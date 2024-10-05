<template>
  <div class="bg-gray-100">
    <div class="max-w-[500px] mx-auto">
      <div class="flex flex-col items-stretch pt-28 min-h-screen">
        <form
          v-on:submit.prevent="addTask"
          class="flex gap-2 justify-center mb-8"
        >
          <UInput color="blue" v-model="todo.newTask" />
          <UButton color="blue" @click="addTask" label="add task" />
        </form>

        <TransitionGroup name="list" tag="ul">
          <li
            v-for="task in todo.tasks"
            :key="task"
            class="flex justify-between items-center p-2 m-2 text-gray-700 font-semibold bg-white rounded-lg shadow-sm w-full"
          >
            <div>{{ task.id }}: {{ task.name }}</div>
            <UButton
              @click="deleteTask(task)"
              icon="material-symbols-delete-outline-rounded"
              size="sm"
              color="red"
              square
              variant="ghost"
            />
          </li>
        </TransitionGroup>
      </div>
    </div>
  </div>
</template>

<script setup>
const show = ref(false);

const todo = reactive({
  newTask: "",
  count: 0,
  tasks: [],
});

const addTask = () => {
  const task = todo.newTask.trim(" ");
  if (task) {
    todo.tasks.unshift({ id: todo.count++, name: task });
    todo.newTask = "";
  }
};

const deleteTask = (task) => {
  console.log("task: ", task);
  const index = todo.tasks.indexOf(task);
  todo.tasks.splice(index, 1);
};
</script>

<style scoped>
.list-enter-active {
  animation: bounce-in 0.5s;
}
.list-leave-active {
  animation: bounce-in 0.5s reverse;
}
@keyframes bounce-in {
  0% {
    transform: scale(0);
  }
  50% {
    transform: scale(1.05);
  }
  100% {
    transform: scale(1);
  }
}
</style>
