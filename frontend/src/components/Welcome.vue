<template>
  <div>
    <h1>Movie Recommender System</h1>
    <h2>Based on 10M Movielens Dataset</h2>
    <ul>
      <li>
        <router-link :to="{ name: 'SignIn' }">Sign in</router-link>
      </li>
      <li>
        <router-link :to="{ name: 'SignUp' }">Sign up</router-link>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
}
</script>

<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
