<template>
    <div class="container">
        <h1>РЕГИСТРАЦИЯ</h1>
        <RegistrationForm></RegistrationForm>
    </div>
</template>

<script>
  import RegistrationForm from "../RegistrationForm";
  export default {
    name: "Registration",
    components: {RegistrationForm},
    mounted() {
      if (localStorage.getItem('access_token')) {
        this.$router.push('/')
      }
      else if (!localStorage.getItem('google_token')) {
        this.$router.push('/')
      }
    }
  }
</script>

<style scoped lang="scss">
    h1 {
        text-align: left;
    }

</style>