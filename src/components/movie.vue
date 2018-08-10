<template>
  <div>
    <b-card
      :title="movie.name"
      :img-src="'https://image.tmdb.org/t/p/w780' + movie.poster_partial_url"
      img-alt="Image"
      img-top
      class="mb-2"
      bg-variant="dark"
      border-variant="white"
      style="max-width: 20rem;"
      >
      <b-button @click="open_modal">Trialers and Rate It!</b-button>
    </b-card>
    <b-modal
      :ref="'modal_' + movie.id"
      :title="movie.name"
      header-text-variant="dark"
      body-text-variant="dark"
      @hidden="hide_modal"
      hide-footer
      >
      <div class="d-block text-center">
        <b-embed
          type="iframe"
          :src="'https://www.youtube.com/embed/' + trailer.youtube_id"
          allowfullscreen
          v-for="trailer in trailers"
          :key="trailer.youtube_id"
          ></b-embed>
      </div>
    </b-modal>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  props: [ 'movie' ],
  data: function () {
    return {
      trailers: []
    }
  },
  methods: {
    open_modal () {
      this.$emit('changeModal')
      axios.get(`/movies/${this.movie.id}/trailers/`)
        .then((res) => {
          this.trailers = res.data
        })
      this.$refs[`modal_${this.movie.id}`].show()
    },
    hide_modal () {
      this.$emit('changeModal')
    }
  }
}
</script>
