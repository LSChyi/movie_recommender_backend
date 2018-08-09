<template>
  <div>
    <b-container>
      <b-row class="justify-content-md-center">
        <b-col sm></b-col>
        <b-col sm>
          <b-form>
            <b-form-group label="Email" :state="email.state">
              <b-form-input :state="email.state" type="email" v-model="email.email" @input="changeInput(email)"></b-form-input>
            </b-form-group>
            <b-form-group label="Password" :state="password.state">
              <b-form-input :state="password.state" type="password" v-model="password.password" @input="changeInput(password)"></b-form-input>
            </b-form-group>
            <slot></slot>
          </b-form>
        </b-col>
        <b-col sm></b-col>
      </b-row>
    </b-container>
  </div>
</template>
<script>
export default {
  props: [ 'value' ],
  data: function () {
    return {
      email: {
        state: null,
        email: ''
      },
      password: {
        state: null,
        password: ''
      }
    }
  },
  methods: {
    changeInput (obj) {
      obj.state = null
      var re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
      if (re.test(this.email.email)) {
        this.email.state = null
        this.$emit('input', {
          email: this.email.email,
          password: this.password.password
        })
      } else {
        this.email.state = false
        this.$emit('input', {
          email: '',
          password: this.password.password
        })
      }
      this.$emit('resetBtn')
    }
  }
}
</script>
<style scoped>
</style>
