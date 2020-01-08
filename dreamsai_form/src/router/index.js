import Vue from 'vue'
import Router from 'vue-router'
import Dreams from '@/components/Dreams'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Dreams',
      component: Dreams
    }
  ]
})
