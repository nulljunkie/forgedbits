<script setup>
import { Cropper } from "vue-advanced-cropper";
// import "vue-advanced-cropper/dist/style.css";

const cropperRef = ref(null);

const emit = defineEmits(["sendBlob", "cancelCrop"]);

const props = defineProps({
  imageUrl: {
    type: String,
    required: true,
  },
  cropWidth: {
    type: Number,
    required: true,
  },
  cropHeigth: {
    type: Number,
    required: true,
  },
});

const cropImage = () => {
  const { canvas } = cropperRef.value.getResult();
  if (canvas) {
    canvas.toBlob((blob) => {
      emit("sendBlob", blob);
      emit("cancelCrop");
    }, "image/jpeg");
  }
};
</script>

<template>
  <div
    class="fixed inset-0 z-50 border-4 border-green-500 flex items-center justify-center dark:bg-gray-900 bg-gray-900 bg-opacity-50 dark:bg-opacity-50"
  >
    <!-- class="fixed inset-0 z-50 flex items-center justify-center dark:bg-gray-900 bg-gray-900 bg-opacity-50 dark:bg-opacity-50" -->
    <div
      class="relative border-2 border-red-500 max-w-[480px] max-h-[480px] rounded-md overflow-hidden"
    >
      <Cropper
        ref="cropperRef"
        :src="props.imageUrl"
        :stencil-props="{
          handlers: {},
          movable: false,
          resizable: false,
        }"
        :stencil-size="{
          width: props.cropWidth,
          height: props.cropHeigth,
        }"
        image-restriction="stencil"
        class="h-[480px] w-[480px] border-2 border-pink-500"
      />

      <div class="absolute top-0 right-0 border-2 border-cyan-500">
        <button
          @click="emit('cancelCrop')"
          class="text-gray-800 px-1.5 py-1 rounded-md bg-gray-100 hover:bg-gray-200 m-1"
        >
          cancel
        </button>
        <button
          @click="cropImage"
          class="text-white rounded-md px-1.5 py-1 bg-gray-800 hover:bg-gray-900 m-1"
        >
          save
        </button>
      </div>
    </div>
  </div>
</template>
