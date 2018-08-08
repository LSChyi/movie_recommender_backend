<template>
  <div>
    <b-container>
      <b-row class="justify-content-md-center">
        <b-col sm></b-col>
        <b-col sm>
          <b-form>
            <b-form-group label="Email" :state="emailState">
              <b-form-input :state="emailState" type="email"></b-form-input>
            </b-form-group>
            <b-form-group label="Password" :state="passwordState">
              <b-form-input :state="passwordState" type="password"></b-form-input>
            </b-form-group>
            <slot></slot>
            <b-button type="submit" variant="primary">Submit</b-button>
          </b-form>
        </b-col>
        <b-col sm></b-col>
      </b-row>
    </b-container>
  </div>
</template>
<script>
export default {
  props: [ 'value' ]
}
</script>
<style scoped>
</style>
