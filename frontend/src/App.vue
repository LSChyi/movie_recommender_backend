<template>
  <div id="app">
    <b-navbar toggleable="md" type="light" variant="light">
      <b-navbar-toggle target="nav_text_collapse"></b-navbar-toggle>
      <b-navbar-brand :to="{ name: 'Welcome' }">Movie Recommender</b-navbar-brand>
      <b-collapse is-nav id="nav_collapse">
        <b-navbar-nav class="ml-auto">
          <b-nav-item v-if="!token">
            <router-link :to="{ name: 'SignIn' }">Sign in</router-link> or <router-link :to="{ name: 'SignUp' }">Sign up</router-link>
          </b-nav-item>
          <b-nav-item @click="logout" v-else>Logout</b-nav-item>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
    <br />
    <router-view/>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'App',
  data: function () {
    return {
      get token () {
        return localStorage.getItem('token')
      }
    }
  },
  created: function () {
    if (localStorage.getItem('token')) {
      axios.defaults.headers.common['Authorization'] = `Token ${localStorage.getItem('token')}`
      this.$router.push({ name: 'Recommend' })
    }
  },
  methods: {
    logout () {
      localStorage.removeItem('token')
      this.$router.push({ name: 'Welcome' })
      delete axios.defaults.headers.common['Authorization']
      console.log(axios.defaults.headers.common['Authorization'])
    }
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
}
</style>
