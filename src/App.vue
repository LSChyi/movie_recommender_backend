<template>
  <div id="app">
    <b-navbar toggleable="md" type="light" variant="light">
      <b-navbar-toggle target="nav_text_collapse"></b-navbar-toggle>
      <b-navbar-brand href="#">Movie Recommender</b-navbar-brand>
      <b-collapse is-nav id="nav_collapse">
        <b-navbar-nav class="ml-auto">
          <b-nav-item>
            <a href="#">Sign in</a> or <a href="#">Sign up</a>
          </b-nav-item>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
    <br />
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App'
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
