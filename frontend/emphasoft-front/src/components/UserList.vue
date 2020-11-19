<template>
    <div class="user-list">
        <ul>
            <li
                    v-for="user in users"
                    :key="user.id"
            >
                {{fullName(user)}}
            </li>
        </ul>
    </div>
</template>

<script>
  export default {
    name: "UserList",
    data() {
      return {
        users: []
      }
    },
    mounted() {
      const accessToken = localStorage.getItem('access_token')
      if (accessToken) {
        this.$axios.get('/users/all',
          {
            headers: {'Authorization': `Bearer ${accessToken}`}
          }).then(response => {
          console.log(response.data)
          this.users = response.data
        })
      }
    },
    methods: {
      fullName: (user)=>{
        return user.last_name + ' ' + user.first_name + ' ' + user.patronymic
      }
    }
  }
</script>

<style scoped lang="scss">
    ul {
        list-style: none;
    }
</style>