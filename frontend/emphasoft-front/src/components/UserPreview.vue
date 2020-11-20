<template>
    <div class="user-preview" v-if="user">
        <div class="user-preview__avatar">
            <img :src="'data:image/jpeg;base64,'+user.avatar" alt="avatar">
        </div>
        <div class="user-preview__username">
            {{fullName()}}
        </div>
    </div>
</template>

<script>
  export default {
    name: "UserPreview",
    props: {
      user: {}
    },
    methods: {
      fullName: function () {
        return this.user.last_name + ' ' + this.user.first_name + ' ' + this.user.patronymic
      },
    },
  }
</script>

<style scoped lang="scss">
    .user-preview {
        margin-right: 10px;

        &__username {
            width: 100px;
        }

        &__avatar {
            img {
                width: 80px;
                height: 80px;
                border-radius: 50%;
            }
        }
    }
</style>