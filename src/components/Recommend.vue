<template>
  <div>
    <b-container>
      <h2>Recommended Movies</h2>
      <b-card-group deck>
        <movie v-for="movie in movies" :key="movie.id" :movie="movie"></movie>
      </b-card-group>
    </b-container>
  </div>
</template>

<script>
import axios from 'axios'
import Movie from '@/components/movie'

export default {
  created: function () {
    this.get_recommendations()
  },
  components: {
    Movie
  },
  data: function () {
    return {
      movies: []
    }
  },
  methods: {
    get_recommendations () {
      axios.get('/movies/recommendations/')
        .then((res) => {
          this.movies = res.data
        })
    }
  }
}
</script>
