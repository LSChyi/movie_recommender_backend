<template>
  <div>
    <login-form v-model="login_info" @resetBtn="$refs.submitBtn.resetBtn()">
      <synchronize-button
        normalText="Submit"
        defaultBtnVariant="primary"
        failText="Login Fail"
        successText="Login success! redirecting..."
        :clickFn="login"
        :enabled="(login_info.email && login_info.password) !== ''"
        ref="submitBtn"
        type="submit"
        ></synchronize-button>
    </login-form>
  </div>
</template>
<script>
import LoginForm from '@/components/loginForm' 
import SynchronizeButton from '@/components/SynchronizeButton'
import axios from 'axios'

const API_BASE = process.env.API_BASE

export default {
  components: {
    LoginForm, SynchronizeButton
  },
  data: function () {
    return {
      login_info: {
        email: '',
        password: ''
      }
    }
  },
  methods: {
    login () {
      return new Promise((resolve, reject) => {
        axios.post(`${API_BASE}/rest-auth/login/`, {
          email: this.login_info.email,
          password: this.login_info.password
        })
          .then((res) => {
            sessionStorage.setItem('token', res.data.key)
            this.$router.push({ name: 'Recommend' })
            resolve()
          })
          .catch((error) => {
            if (error.response) {
              if (error.response.data.non_field_errors) {
                alert('Wrong email or password')
              }
            }
            reject()
          })
      })
    }
  }
}
</script>
