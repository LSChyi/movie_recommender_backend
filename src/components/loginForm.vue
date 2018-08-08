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
        email: null
      },
      password: {
        state: null,
        password: null
      }
    }
  },
  methods: {
    changeInput (obj) {
      obj.state = null
      this.$emit('input', {
        email: this.email.email,
        password: this.password.password
      })
    }
  }
}
</script>
<style scoped>
</style>
