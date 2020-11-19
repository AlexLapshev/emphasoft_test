<template>
    <GoogleLogin
            :params="params"
            :onSuccess="onSuccess"
            :onFailure="onFailure"
            class="google-btn"
    ></GoogleLogin>
</template>

<script>
  import GoogleLogin from 'vue-google-login';

  export default {
    name: "Home",
    components: {
      GoogleLogin
    },
    data() {
      return {
        params: {
          client_id: process.env.VUE_APP_GOOGLE_CLINENT_ID
        },

      }
    },
    methods: {
      onSuccess(googleUser) {
        const idToken = googleUser.getAuthResponse().id_token
        this.$axios.post('/security/google-auth', {access_token: idToken}).then(response=>{
          if (response.status === 200) {
            console.log(response.data)
            localStorage.setItem('access_token', response.data.access_token)
            this.$router.push('/')
          }
        }).catch(error=>{
          if (error.response.status === 403) {
            localStorage.setItem('google_token', idToken)
            this.$router.push('registration')
          }
        })
      },
      onFailure(error) {
        console.log(error)
      }
    }
  }
</script>

<style scoped lang="scss">
    .google-btn {
        height: 50px;
        width: 50px;
        border: 1px solid white;
        background: url("../assets/google_btn.svg") no-repeat center;
        background-size: cover;
        cursor:pointer;
        outline:none;
        &:hover{
            border: 1px solid #828683;
            border-radius: 5px;
        }
    }
</style>