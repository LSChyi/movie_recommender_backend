<template>
  <div>
    <login-form v-model="login_info" @resetBtn="$refs.submitBtn.resetBtn()">
      <b-form-group label="Confirm Password" :state="confirmPassword">
        <b-form-input :state="confirmPassword" type="password" v-model="password_confirm"></b-form-input>
      </b-form-group>
      <synchronize-button
        normalText="Submit"
        defaultBtnVariant="primary"
        failText="Create Fail"
        successText="Account created, redirecting..."
        :clickFn="register"
        :enabled="(login_info.email && login_info.password && password_confirm) !== '' && confirmPassword"
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

export default {
  components: {
    LoginForm, SynchronizeButton
  },
  computed: {
    confirmPassword () {
      if (this.password_confirm) {
        return this.password_confirm === this.login_info.password
      } else {
        return null
      }
    }
  },
  data: function () {
    return {
      login_info: {
        email: '',
        password: ''
      },
      password_confirm: ''
    }
  },
  methods: {
    register () {
      return new Promise((resolve, reject) => {
        axios.post('/users/register/', {
          email: this.login_info.email,
          password: this.login_info.password
        })
          .then((res) => {
            resolve()
            alert('Register success! Now you can sign in the system')
            this.$router.push({ name: 'SignIn' })
          })
          .catch((error) => {
            console.log(error)
            if (error.response) {
              if (error.response.data.email) {
                alert('The email is already used')
              }
            }
            reject()
          })
      })
    }
  }
}
</script>
