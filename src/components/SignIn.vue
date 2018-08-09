<template>
  <div>
    <login-form v-model="login_info">
      <synchronize-button
        normalText="Submit"
        defaultBtnVariant="primary"
        failText="Login Fail"
        :clickFn="login"
        ></synchronize-button>
    </login-form>
  </div>
</template>
<script>
import LoginForm from '@/components/loginForm' 
import SynchronizeButton from '@/components/SynchronizeButton'
import axios from 'axios'

export default {
  components: {
    LoginForm, SynchronizeButton
  },
  data: function () {
    return {
      login_info: {}
    }
  },
  methods: {
    login () {
      return axios.post('http://localhost:8000/rest-auth/login/', {
        email: this.login_info.email,
        password: this.login_info.password
      })
    }
  }
}
</script>
