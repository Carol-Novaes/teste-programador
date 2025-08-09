import { createRouter, createWebHistory } from 'vue-router'
import DisciplinasView from '@/views/DisciplinasView.vue'
import AtividadeView from '@/views/AtividadeView.vue'
import DesempenhoView from '@/views/DesempenhoView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'disciplinas',
      component: DisciplinasView,
    },
    {
      path: '/atividades',
      name: 'atividades',
      component: AtividadeView,
    },
    {
      path: '/desempenhos',
      name: 'desempenhos',
      component: DesempenhoView,
    },
  ],
})

export default router
