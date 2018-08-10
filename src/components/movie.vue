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
    </b-card>
  </div>
</template>

<script>
export default {
  props: [ 'movie' ]
}
</script>
