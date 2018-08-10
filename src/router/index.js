import Vue from 'vue'
import Router from 'vue-router'
import Welcome from '@/components/Welcome'
import SignIn from '@/components/SignIn'
import SignUp from '@/components/SignUp'
import Recommend from '@/components/Recommend'

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
    }, {
      path: '/recommend',
      name: 'Recommend',
      component: Recommend,
      beforeEnter: (to, from, next) => {
        if (!sessionStorage.getItem('token')) {
          console.log('here')
          next({ name: 'SignIn' })
        } else {
          next()
        }
      }
    }
  ]
})
