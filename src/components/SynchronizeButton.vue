<template>
  <b-button :disabled="!isEable" :variant="variantType" @click="execClick" ref="button" :type="type">
    <span v-if="btnStatus === 'loading'">
      <spinner></spinner>
      {{ loadingText }}
    </span>
    {{ displayText }}
  </b-button>
</template>

<script>
import Spinner from '@/components/Spinner'

export default {
  props: {
    enabled: {
      default: true,
      type: Boolean
    },
    normalText: {
      type: String
    },
    successText: {
      type: String
    },
    failText: {
      type: String
    },
    defaultBtnVariant: {
      default: '',
      type: String
    },
    loadingText: {
      default: '',
      type: String
    },
    clickFn: {
      type: Function
    },
    type: {
      type: String,
      default: "button"
    }
  },
  data () {
    return {
      btnStatus: ''
    }
  },
  components: {
    Spinner
  },
  computed: {
    isEable () {
      return this.enabled && (this.btnStatus !== 'loading')
    },
    displayText () {
      if (this.btnStatus === 'success') {
        return this.successText
      } else if (this.btnStatus === 'fail') {
        return this.failText
      } else if (this.btnStatus === 'loading') {
        return ''
      } else {
        return this.normalText
      }
    },
    variantType () {
      if (this.btnStatus === 'success') {
        return 'success'
      } else if (this.btnStatus === 'fail') {
        return 'danger'
      } else if (this.btnStatus === 'loading') {
        return ''
      } else {
        return this.defaultBtnVariant
      }
    }
  },
  methods: {
    execClick () {
      this.btnStatus = 'loading'
      this.clickFn()
        .then((res) => {
          this.$emit('execSuccess', res)
          this.btnStatus = 'success'
        })
        .catch((err) => {
          this.$emit('execFail', err)
          this.btnStatus = 'fail'
        })
    },
    resetBtn () {
      this.btnStatus = ''
    },
    click () {
      this.$refs.button.onclick()
    }
  }
}
</script>
