<template>
  <div class="desempenhos-container">
    <h1>Cadastro de Desempenho</h1>   

    <div v-if="!loading && !error">
      <form @submit.prevent="cadastrarDesempenho" class="desempenho-form">
        <div class="form-group">
          <label for="aluno">Aluno:</label>
          <select id="aluno" v-model="novoDesempenho.aluno" required>
            <option value="" disabled selected>Selecione um aluno</option>
            <option v-for="aluno in alunos" :key="aluno.id" :value="aluno.id">
              {{ aluno.nome }}
            </option>
          </select>

          <label for="atividade">Atividade:</label>
          <select id="atividade" v-model="novoDesempenho.atividade" required>
            <option value="" disabled selected>Selecione uma atividade</option>
            <option v-for="atividade in atividades" :key="atividade.id" :value="atividade.id">
              {{ atividade.nome }} (Valor: {{ atividade.valor }} pts)
            </option>
          </select>

          <label for="nota">Nota:</label>
          <input type="number" id="nota" v-model="novoDesempenho.nota" step="0.1" min="0" required>
        </div>
        
        <button type="submit" class="btn-submit">Cadastrar Desempenho</button>

        <router-link :to="{ name: 'disciplinas' }" class="btn-cancel">
          Cancelar
        </router-link>
      </form>
      
      <div v-if="successMessage" class="success-message">
        {{ successMessage }}
      </div>
    </div>

    <div v-if="loading" class="loading-message">
      <p v-if="!isSubmitting">Carregando dados...</p>
      <p v-if="isSubmitting">Enviando dados...</p>
    </div>
    
    <div v-if="error" class="error-message">
      <p>Erro: {{ error }}</p>
      <button @click="carregarDados">Tentar novamente</button>
    </div>
 </div> 
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { getAPI } from '@/axios-api'

const alunos = ref([])
const atividades = ref([])

const novoDesempenho = ref({
  aluno: '',
  atividade: '',
  nota: null
})

const loading = ref(false)
const isSubmitting = ref(false)
const error = ref(null)
const successMessage = ref(null)

const carregarAlunos = async () => {
  try {
    const response = await getAPI.get('/alunos/')
    alunos.value = response.data
  } catch (err) {
    throw new Error('Erro ao carregar alunos: ' + err.message)
  }
}

const carregarAtividades = async () => {
  try {
    const response = await getAPI.get('/atividades/')
    atividades.value = response.data
  } catch (err) {
    throw new Error('Erro ao carregar atividades: ' + err.message)
  }
}

const carregarDados = async () => {
  error.value = null
  loading.value = true
  try {
    await Promise.all([carregarAlunos(), carregarAtividades()])
  } catch (err) {
    error.value = err.message
  } finally {
    loading.value = false
  }
}

const cadastrarDesempenho = async () => {
  error.value = null
  successMessage.value = null
  isSubmitting.value = true
  
  try {
    const payload = {
      ...novoDesempenho.value,
      nota: parseFloat(novoDesempenho.value.nota)
    }
    
    const response = await getAPI.post('/desempenhos/', payload)
    
    if (response.status === 201) {
      successMessage.value = 'Desempenho cadastrado com sucesso!'
    }
  } catch (err) {
    error.value = 'Erro ao cadastrar desempenho: ' + (err.response?.data?.message || err.message)
    console.error(err)
  } finally {
    isSubmitting.value = false
  }
}

onMounted(() => {
  carregarDados()
})
</script>

<style scoped>
.desempenhos-container {
  padding: 20px;
  max-width: 600px;
  margin: 0 auto;
}

.desempenho-form {
  background-color: #f9f9f9;
  padding: 20px;
  border-radius: 8px;
  margin-top: 20px;
}

.form-group {
  margin-bottom: 15px;
}

.form-group label {
  display: block;
  margin-bottom: 5px;
  margin-top: 5px;
  font-weight: bold;
}

.form-group input,
.form-group select {
  width: 100%;
  padding: 8px;
  border: 1px solid #ddd;
  border-radius: 4px;
  box-sizing: border-box;
}

.btn-submit {
  display: inline-block;  
  padding: 10px 15px;
  background-color: #257ee4;;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  margin-right: 10px;
}

.btn-submit:hover {
  background-color: #89b7eb;
}

.btn-cancel {
  display: inline-block;
  padding: 9px 15px;
  background-color: #f44336;
  color: white;
  text-decoration: none;
  border-radius: 4px;
}

.btn-cancel:hover {
  background-color: #eb8982;
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

.success-message {
  text-align: center;
  padding: 15px;
  margin-top: 20px;
  background-color: #dff0d8;
  color: #3c763d;
  border-radius: 4px;
}
</style>