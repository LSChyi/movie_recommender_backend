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

const API_BASE = process.env.API_BASE

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
      return axios.post(`{API_BASE}/rest-auth/login/`, {
        email: this.login_info.email,
        password: this.login_info.password
      })
    }
  }
}
</script>
