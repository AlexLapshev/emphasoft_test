<template>
    <div class="container">
        <GoogleSignIn></GoogleSignIn>
    </div>
</template>

<script>
    import GoogleSignIn from "../GoogleSignIn";
  export default {
    name: "Home",
    components: {
      GoogleSignIn
    },
  }
</script>

<style scoped>

</style>