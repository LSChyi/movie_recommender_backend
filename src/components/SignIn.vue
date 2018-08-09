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
      return this.$http.post('http://localhost:8000/rest-auth/login/')
    }
  }
}
</script>
