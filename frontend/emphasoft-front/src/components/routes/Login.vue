<template>
    <div class="container">
        <GoogleSignIn></GoogleSignIn>
    </div>
</template>

<script>
  import GoogleSignIn from "../GoogleSignIn";

  export default {
    name: "Login",
    components: {
      GoogleSignIn
    },
    mounted() {
      if (localStorage.getItem('access_token')) {
        this.$router.push('/')
      }
    }
  }
</script>

<style scoped>

</style>