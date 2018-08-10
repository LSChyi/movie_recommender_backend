<template>
  <div>
    <b-container>
      <h2>Recommended Movies</h2>
      <div style="margin:12px">
        <b-progress :value="countdown.now" :max="countdown.max" animated></b-progress>
        <div>The recommendation list will be updated in {{ countdown_seconds }} seconds</div>
      </div>
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
      .then(() => this.start_countdown())
  },
  components: {
    Movie
  },
  computed: {
    countdown_seconds () {
      return Math.ceil(this.countdown.now)
    }
  },
  data: function () {
    return {
      movies: [],
      countdown: {
        max: 6,
        now: 6
      }
    }
  },
  methods: {
    get_recommendations () {
      return new Promise((resolve, reject) => {
        axios.get('/movies/recommendations/')
          .then((res) => {
            this.movies = res.data
            resolve()
          })
      })
    },
    start_countdown () {
      this.countdown.now = this.countdown.max
      this.count_minus()
    },
    count_minus () {
      if (this.countdown.now > 0.1) {
        this.countdown.now -= 0.1
        setTimeout(this.count_minus, 100)
      } else {
        this.get_recommendations()
          .then(() => this.start_countdown())
      }
    }
  }
}
</script>
