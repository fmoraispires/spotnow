import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home.vue'
import Login from '@/components/auth/Login.vue'
import Registo from '@/components/auth/Registo.vue'
import Booking from '@/components/user_menu/Booking.vue'
import Historic from '@/components/user_menu/Historic.vue'
import AddGarage from '@/components/user_menu/AddGarage.vue'
import Payment from '@/components/user_menu/Payment.vue'
import Settings from '@/components/user_menu/Settings.vue'
import About from '@/components/staff/About.vue'
import Team from '@/components/staff/Team.vue'
import Contact from '@/components/staff/Contact.vue'
import Faq from '@/components/staff/Faq.vue'
import Door from '@/components/user_menu/Door.vue'





Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'SpotNow',
      component: Home
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/registo',
      name: 'Registo',
      component: Registo
    },
    {
      path: '/reserva',
      name: 'Reservar Garagem',
      component: Booking
    },
    {  
      path: '/historico',
      name: 'Histórico',
      component: Historic
    },
    {
      path: '/addgaragem',
      name: 'Adicionar Garagem',
      component: AddGarage
    },
    {
      path: '/payment',
      name: 'Métodos de Pagamento',
      component: Payment
    },
    {
      path: '/settings',
      name: 'Dados da Conta',
      component: Settings
    },
    {
      path: '/about',
      name: 'A Nossa História',
      component: About
    },
    {
      path: '/team',
      name: 'A Equipa',
      component: Team,
    },
    {
      path: '/contact',
      name: ' Contacte Nós',
      component: Contact

    },
    {
      path: '/faq',
      name: 'FAQ',
      component: Faq
    },
    {
      path: '/door',
      name: 'Door',
      component: Door
    },
    {
      path: 'https://www.facebook.com/SpotNow-110913667105487/',
      name:'facebook'
    }


  ]
})