<template>
    <div class="error">
        {{error}}
    </div>
</template>

<script>
  export default {
    name: "error",
    props: {
      error: {}
    }
  }
</script>

<style scoped>
    .error {
        color: #ec6b6b;
        text-align: left;
    }
</style>