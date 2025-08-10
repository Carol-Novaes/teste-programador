<template>
  <div class="disciplinas-container">
    <h1>Disciplinas</h1>   

    <div v-if="!loading && !error">
      <table class="disciplinas-table">
      <thead>
        <tr>
          <th>Disciplina</th>
          <th>Curso</th>
          <th>CH</th>
          <th>Ano</th>
          <th>Professor</th>
          <th>Ação</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="d in disciplinas" :key="d.codigo">
          <td>{{ d.nome }}</td>
          <td>{{ d.curso_nome }}</td>
          <td>{{ d.carga_horaria }} h</td>
          <td>{{ d.ano }}</td>
          <td>{{ d.professor }}</td>
          <td> 
            <router-link :to="{name: 'atividades', query: { disciplina_id: d.codigo, disciplina_nome: d.nome }}" class="btn-atividade">
                Cadastrar Atividade
            </router-link>
          </td>             
        </tr>
      </tbody>   
    </table>
    </div>

    <div v-if="loading" class="loading-message">
      <p>Carregando disciplinas...</p>
    </div>
    
    <div v-if="error" class="error-message">
      <p>Erro ao carregar disciplinas: {{ error }}</p>
      <button @click="fetchDisciplinas">Tentar novamente</button>
    </div>
 </div> 
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { getAPI } from '@/axios-api'

const disciplinas = ref([])
const error = ref(null) 
const loading = ref(false)

const fetchDisciplinas = async () => {  // Função extraída para reuso (opcional)
  loading.value = true
  error.value = null
  try {
    const response = await getAPI.get('/disciplinas/')
    disciplinas.value = response.data
  } catch (err) {
    error.value = 'Erro ao carregar disciplinas: ' + err.message
    console.error(err)
  } finally {
    loading.value = false
  }
}

onMounted(() => {
  fetchDisciplinas()
})
</script>

<style scoped>
.disciplinas-container {
  padding: 20px;
  max-width: 85%;
  margin: 0 auto;
}

.disciplinas-table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 20px;
}

.disciplinas-table th,
.disciplinas-table td {
  border: 1px solid #ddd;
  padding: 12px;
  text-align: left;
}

.disciplinas-table th {
  background-color: #f5f5f5;
  font-weight: bold;
}

.disciplinas-table tr:nth-child(even) {
  background-color: #f9f9f9;
}

.disciplinas-table tr:hover {
  background-color: #f0f0f0;
}

.loading-message {
  text-align: center;
  padding: 20px;
  color: #666;
}

.error-message {
  text-align: center;
  padding: 20px;
  color: #d32f2f;
}

.error-message button {
  margin-top: 10px;
  padding: 8px 16px;
  background-color: #d32f2f;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.error-message button:hover {
  background-color: #b71c1c;
}

.disciplinas-table td:last-child {
  text-align: center;
}

.btn-atividade {
  display: inline-block;
  padding: 6px 12px;
  background-color: #257ee4;
  color: white;
  text-decoration: none;
  border-radius: 4px;
  transition: background-color 0.3s;
}

.btn-atividade:hover {
  background-color: #89b7eb;
}
</style>