<template>
    <div class="registration-form">
        <form @submit.prevent="registerUser">
            <vs-input v-model="firstName" class="registration-form__field" placeholder="Имя"/>
            <vs-input v-model="lastName" class="registration-form__field" placeholder="Фамилия"/>
            <vs-input v-model="patronymic" class="registration-form__field" placeholder="Отчество"/>
            <vs-input v-model="password1" class="registration-form__field" type="password" placeholder="Пароль"/>
            <vs-input v-model="password2" class="registration-form__field" type="password"
                      placeholder="Повторите пароль"/>
            <vs-button gradient type="submit">Зарегистрироваться</vs-button>
            <Error
                    :error="error"
            ></Error>
        </form>
    </div>
</template>

<script>
  import Error from "./Error";

  export default {
    name: "RegistrationForm",
    components: {Error},
    data() {
      return {
        error: null,
        firstName: 'Алексей',
        lastName: 'Лапшев',
        patronymic: 'Николаевич',
        password1: '123456789',
        password2: '123456789'
      }
    },
    methods: {
      registerUser() {
        this.error = null
        if (this.validateEmpty() && this.validatePasswords() && this.validateData()) {
          const formData = new FormData()
          formData.append('email_token', localStorage.getItem('google_token'))
          formData.append('first_name', this.firstName)
          formData.append('last_name', this.lastName)
          formData.append('patronymic', this.patronymic)
          formData.append('password', this.password1)
          this.$axios.post('/security/register', formData, {
            headers: {
              'Content-Type': 'multipart/form-data'
            }
          }).then(response => {
            console.log(response.data)
            localStorage.clear()
            localStorage.setItem('access_token', response.data.access_token)
            this.$router.push('/')
          })
        }
      },
      validateEmpty() {
        if (
          this.firstName === '' ||
          this.lastName === '' ||
          this.patronymic === '' ||
          this.password1 === '' ||
          this.password2 === '') {
          this.error = 'Все поля должны быть заполнены'
          return false
        }
        return true
      },
      validatePasswords() {
        if (this.password1 !== this.password2) {
          this.error = 'Пароли не совпадают'
          return false
        } else if (this.password1.length < 6) {
          this.error = 'Пароль слишком короткий'
          return false
        }

        return true
      },
      validateData() {
        const reg = /[^а-яА-ЯЁё]/
        if (reg.test(this.firstName) || reg.test(this.lastName) || reg.test(this.patronymic)) {
          this.error = 'Недопустимые символы в имени/фамилии/отчестве'
          return false
        }
        if (this.firstName.length < 2) {
          this.error = 'Имя слишком короткое'
          return false
        }
        if (this.lastName.length < 2) {
          this.error = 'Фамилия слишком короткая'
          return false
        }
        if (this.patronymic.length < 2) {
          this.error = 'Отчество слишком короткое'
          return false
        }
        return true
      }

    }
  }
</script>

<style scoped lang="scss">
    .registration-form {
        margin: 0 auto;

        &__field {
            padding-bottom: 8px;
        }
    }
</style>