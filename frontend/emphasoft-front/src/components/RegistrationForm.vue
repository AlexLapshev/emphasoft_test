<template>
    <div class="registration-form">
        <form @submit.prevent="registerUser">
            <b-form-group label="Аватар:" label-for="file-small" label-cols-sm="2" label-size="sm">
                <b-form-file id="file-small" size="sm"></b-form-file>
            </b-form-group>
        </form>
    </div>

</template>

<script>
  export default {
    name: "RegistrationForm",
    methods: {
      registerUser () {
        
      }
    }
  }
</script>

<style scoped>

</style>