<template>
    <div class="user-list">
        <UserPreview
                v-for="user in users"
                :key="user.id"
                :user="user"
        ></UserPreview>
    </div>
</template>

<script>
  import UserPreview from "./UserPreview";

  export default {
    name: "UserList",
    components: {
      UserPreview
    },
    props: {
      users: {}
    },
    mounted() {
    },
  }
</script>

<style scoped lang="scss">
    .user-list {
        display: flex;
        justify-content: center;
    }
</style>