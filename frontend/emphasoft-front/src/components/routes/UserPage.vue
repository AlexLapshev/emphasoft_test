<template>
    <div class="container">
        <h3>
            Привет, {{me.first_name}}
        </h3>
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
        me: {},
        users: []
      }
    },
    mounted() {
      const accessToken = localStorage.getItem('access_token')
      if (accessToken) {
        const config = {headers: {'Authorization': `Bearer ${accessToken}`}}
        this.$axios.get('/users/me', config).then(response=>{
          this.me = response.data
        })
        this.$axios.get('/users/all', config).then(response => {
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