<template>
  <div
    class="flex items-center gap-1"
    :class="props.direction === 'row' ? 'flex-row' : 'flex-col'"
  >
    <div
      class="flex flex-row items-center bg-gray-100 border border-gray-100 shadow-sm rounded-full pr-2"
    >
      <button
        @click="upvote"
        class="group size-6 rounded-full hover:bg-red-100"
        :class="upvoteIcon === icons.ups ? 'bg-red-100' : 'text-gray-100'"
      >
        <Icon
          :name="upvoteIcon"
          class="w-4 h-4 group-hover:text-red-500 group-hover:font-bold"
          :class="upvoteIcon === icons.ups ? 'text-red-600' : 'text-gray-600'"
        />
      </button>
      <p class="text-sm text-gray-600">{{ props.votes.upvotes }}</p>
    </div>
    <div
      class="flex flex-row items-center bg-gray-100 border border-gray-100 shadow-sm rounded-full pr-2"
    >
      <button
        @click="downvote"
        class="group size-6 rounded-full hover:bg-red-100"
        :class="downvoteIcon === icons.downs ? 'bg-red-100' : 'text-gray-100'"
      >
        <Icon
          :name="downvoteIcon"
          class="w-4 h-4 group-hover:text-red-500 group-hover:font-bold"
          :class="
            downvoteIcon === icons.downs ? 'text-red-600' : 'text-gray-600'
          "
        />
      </button>
      <p class="text-sm text-gray-600">{{ props.votes.downvotes }}</p>
    </div>
    <div>{{ rowLayout }}</div>
  </div>
</template>

<script setup>
import { useAuth } from "#imports";

const auth = useAuth();

const icons = {
  up: "i-bx-upvote",
  ups: "i-bx-bxs-upvote",
  down: "i-bx-downvote",
  downs: "i-bx-bxs-downvote",
};

const upvoteIcon = ref(icons.up);
const downvoteIcon = ref(icons.down);

const props = defineProps({
  votes: {
    type: Object,
    required: true,
  },
  object_id: {
    type: Number,
    required: true,
  },
  is_voted: {
    type: Object,
  },
  contentType: {
    type: String,
    required: true,
  },
  direction: {
    type: String,
    required: true,
  },
});

if (props.is_voted.id) {
  if (props.is_voted.type === 1) upvoteIcon.value = icons.ups;
  else downvoteIcon.value = icons.downs;
}

const setVote = async (endPoint, method, body = {}) => {
  try {
    console.log("body: ", body);
    const res = await $fetch(`http://127.0.0.1:8000/api/votes/${endPoint}`, {
      method: method,
      headers: {
        Authorization: `Bearer ${auth.accessToken}`,
      },
      body: body,
    });
    console.log("res: ", res);
    if (res.id) {
      props.is_voted.id = res.id;
      props.is_voted.type = res.type;
      // props.is_voted = new Proxy(res, {});
      // set(props, "is_voted", res);
      // props.is_voted = { ...res };
      // props.is_voted = res;
      console.log("res is_voted: ", props.is_voted);
    } else props.is_voted = null;
  } catch (error) {
    throw new Error("setVote error: ", error);
  }
};

const upvote = async () => {
  if (auth.user) {
    // undo upvoted
    if (upvoteIcon.value === icons.ups) {
      //NOTE:
      console.log(props.is_voted);
      if (props.is_voted) {
        try {
          await setVote(`vote/delete/${props.is_voted.id}`, "delete");
          upvoteIcon.value = icons.up;
          props.votes.upvotes--;
        } catch (err) {
          console.error("undo upvoted error: ", err);
        }
      }
    } else {
      // update downvote to upvote
      if (downvoteIcon.value === icons.downs) {
        if (props.is_voted) {
          try {
            await setVote(`vote/update/${props.is_voted.id}`, "put", {
              content_type: props.contentType,
              object_id: props.object_id,
              type: 1,
            });
            props.votes.downvotes--;
            upvoteIcon.value = icons.ups;
            props.votes.upvotes++;
          } catch (err) {
            console.error("update vote from downvote to upvote error: ", err);
          }
        }
        // create new vote of type upvote
      } else {
        try {
          await setVote("vote/", "post", {
            content_type: props.contentType,
            object_id: props.object_id,
            type: 1,
          });
          upvoteIcon.value = icons.ups;
          props.votes.upvotes++;
        } catch (err) {
          console.error("create new vote of type upvote error: ", err);
        }
      }
    }
    downvoteIcon.value = icons.down;
  } else navigateTo("/auth/login");
};

const downvote = async () => {
  if (auth.user) {
    // undo downvote
    if (downvoteIcon.value === icons.downs) {
      if (props.is_voted) {
        try {
          await setVote(`vote/delete/${props.is_voted.id}`, "delete");
          downvoteIcon.value = icons.down;
          props.votes.downvotes--;
        } catch (err) {
          console.error("undo downvoted error: ", err);
        }
      }
    } else {
      // update upvote to downvote
      if (upvoteIcon.value === icons.ups) {
        if (props.is_voted) {
          try {
            await setVote(`vote/update/${props.is_voted.id}`, "put", {
              content_type: props.contentType,
              object_id: props.object_id,
              type: -1,
            });
            props.votes.upvotes--;
            downvoteIcon.value = icons.downs;
            props.votes.downvotes++;
          } catch (err) {
            console.error("update vote from upvote to downvote error: ", err);
          }
        }
        // create new vote of type downvote
      } else {
        try {
          await setVote("vote/", "post", {
            content_type: props.contentType,
            object_id: props.object_id,
            type: -1,
          });
          downvoteIcon.value = icons.downs;
          props.votes.downvotes++;
        } catch (err) {
          console.error("create new vote of type downvote error: ", err);
        }
      }
    }
    upvoteIcon.value = icons.up;
  } else navigateTo("/auth/login");
};
</script>
