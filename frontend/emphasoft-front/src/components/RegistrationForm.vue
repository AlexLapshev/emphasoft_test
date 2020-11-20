<template>
    <div class="registration-form">
        <form @submit.prevent="registerUser">
            <vs-input v-model="firstName" class="registration-form__field" placeholder="Имя"/>
            <vs-input v-model="lastName" class="registration-form__field" placeholder="Фамилия"/>
            <vs-input v-model="patronymic" class="registration-form__field" placeholder="Отчество"/>
            <vs-input v-model="password1" class="registration-form__field" type="password" placeholder="Пароль"/>
            <vs-input v-model="password2" class="registration-form__field" type="password"
                      placeholder="Повторите пароль"/>
            <vs-input
                    label="Загрузите аватар"
                    type="file" name="avatar"
                    class="registration-form__file"
                    @change="avatarUpload"

            ></vs-input>
            <vs-button class="btn-submit" gradient type="submit">Зарегистрироваться</vs-button>
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
        firstName: '',
        lastName: '',
        patronymic: '',
        password1: '',
        password2: '',
        avatar: null
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
          formData.append('avatar', this.avatar)
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
          this.password2 === '' ||
          this.avatar === null) {
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
      },
      avatarUpload(event) {
        if (event.target.files[0]) {
          const image = event.target.files[0]
          console.log(image.size, 10 ** 6 * 2)
          if (!['jpg', 'jpeg', 'png'].includes(image.name.split('.').pop())) {
            this.error = 'Некорекктное изображение'
            return
          }
          if (image.size > 10 ** 6 * 2) {
            this.error = 'Размер изображения слишком большой'
            return
          }
          this.error = null
          this.avatar = event.target.files[0]
        }
      }
    }
  }
</script>

<style scoped lang="scss">
    .registration-form {
        form {
            display: inline-block;
            .btn-submit {
                margin: 10px auto 0 auto;
                padding: 0 25px;
            }
        }
        &__field {
            padding-bottom: 8px;
        }

        &__file {
            padding-top: 14px;
        }
    }
</style>