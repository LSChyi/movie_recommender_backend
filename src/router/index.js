import Vue from 'vue'
import Router from 'vue-router'
import Welcome from '@/components/Welcome'
import SignIn from '@/components/SignIn'
import SignUp from '@/components/SignUp'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Welcome',
      component: Welcome
    }, {
      path: '/sign_in',
      name: 'SignIn',
      component: SignIn
    }, {
      path: '/sign_up',
      name: 'SignUp',
      component: SignUp
    }
  ]
})
