import { createRouter, createWebHistory } from 'vue-router'
import DisciplinasView from '@/views/DisciplinasView.vue'
import CadastroAtividade from '@/views/CadastroAtividade.vue'
import CadastroDesempenho from '@/views/CadastroDesempenho.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'disciplinas',
      component: DisciplinasView,
    },
    {
      path: '/atividades/',
      name: 'atividades',
      component: CadastroAtividade,
    },
    {
      path: '/desempenhos/',
      name: 'desempenhos',
      component: CadastroDesempenho,
    },
  ],
})

export default router
