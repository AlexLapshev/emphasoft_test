<template>
    <div class="user-preview" v-if="user">
        <div class="user-preview__avatar">
            <img
                    v-if="avatar"
                    :src="'data:image/jpeg;base64,'+avatar" alt="">
<!--            <img-->
<!--                    v-if="user"-->
<!--                    :src="require('@/assets/avatars/'+user.avatar)"-->
<!--                    alt="Аватар"-->
<!--                    width="200px"-->
<!--                    class="avatar-image"-->
<!--            >-->
        </div>
        <div class="user-preview__username">
            {{fullName()}}
        </div>
    </div>
</template>

<script>
  export default {
    name: "UserPreview",
    data() {
      return {
        avatar: null
      }
    },
    props: {
      user: {}
    },
    methods: {
      fullName: function () {
        return this.user.last_name + ' ' + this.user.first_name + ' ' + this.user.patronymic
      },
    },
    mounted() {
      this.$axios.get('/images', {
        params: {
          user_id: this.user.user_id
        },
        headers: {
          Authorization: 'Bearer ' + localStorage.getItem('access_token')
        }
      }).then(response=>{
        const image = btoa(encodeURIComponent(response.data).replace(/%([0-9A-F]{2})/g,
          function toSolidBytes(match, p1) {
            return String.fromCharCode('0x' + p1);
          }));
        this.avatar = image
      })
    }
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