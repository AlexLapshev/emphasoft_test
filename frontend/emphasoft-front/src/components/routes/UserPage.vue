<template>
    <div class="container">
        <UserList :users="users"></UserList>
    </div>
</template>

<script>
  import UserList from "../UserList";
  export default {
    name: "UserPage",
    components: {UserList},
    data () {
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
      else {
        this.$router.push('/login')
      }
    }
  }
</script>

<style scoped>

</style>