<template>
  <div class="desempenhos-container">
    <h1>Cadastro de Pontuação</h1>

    <div v-if="!loading && !error">
      <form @submit.prevent="cadastrarDesempenho" class="desempenho-form">
        <div class="form-group">
          <label for="aluno">Aluno:</label>
          <select id="aluno" v-model="novoDesempenho.aluno" required>
            <option value="" disabled selected>Selecione um aluno</option>
            <option v-for="aluno in alunos" :key="aluno.codigo" :value="aluno.codigo">
              {{ aluno.nome }} 
            </option>
          </select>

          <label for="atividade">Atividade:</label>
          <select id="atividade" v-model="novoDesempenho.atividade" required :disabled="!novoDesempenho.aluno || atividades.length === 0">
            <option value="" disabled selected>{{ atividades.length ? 'Selecione uma atividade' : 'Nenhuma atividade disponível' }}</option>
            <option v-for="atividade in atividades" :key="atividade.id" :value="atividade.id">
              {{ atividade.nome }} - (Valor: {{ atividade.valor }} pts)
            </option>
          </select>

          <label for="nota">Nota:</label>
          <input type="number" id="nota" v-model.number="novoDesempenho.nota" step="0.1" min="0" required>
        </div>
        
        <button type="submit" class="btn-submit">Cadastrar</button>
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
import { ref, onMounted, watch } from 'vue'
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
    console.log('Alunos carregados:', alunos.value)
  } catch (err) {
    throw new Error('Erro ao carregar alunos: ' + err.message)
  }
}

const carregarAtividadesPorAluno = async (alunoId) => {
  try {
    loading.value = true
    const response = await getAPI.get(`/alunos/${alunoId}/atividades/`)
    atividades.value = response.data
  } catch (err) {
    error.value = 'Erro ao carregar atividades: ' + (err.response?.data?.error || err.message)
  } finally {
    loading.value = false
  }
}

watch(() => novoDesempenho.value.aluno, (alunoId) => {
  if (alunoId) {
    carregarAtividadesPorAluno(alunoId)
    novoDesempenho.value.atividade = '' 
  } else {
    atividades.value = [] 
  }
})

const carregarDados = async () => {
  error.value = null
  loading.value = true
  try {
    await carregarAlunos()
    atividades.value = []
  } catch (err) {
    error.value = err.message
  } finally {
    loading.value = false
  }
}

const resetarFormulario = () => {
  novoDesempenho.value = {
    aluno: '',
    atividade: '',
    nota: null
  }
  atividades.value = [] 
}

const cadastrarDesempenho = async () => {
  error.value = null
  successMessage.value = null
  isSubmitting.value = true
  
  try {
    if (!novoDesempenho.value.aluno) {
      throw new Error('Selecione um aluno')
    }
    if (!novoDesempenho.value.atividade) {
      throw new Error('Selecione uma atividade')
    }
    if (novoDesempenho.value.nota === null || isNaN(novoDesempenho.value.nota)) {
      throw new Error('Informe uma nota válida')
    }
    
    const payload = {
      aluno: novoDesempenho.value.aluno,
      atividade: novoDesempenho.value.atividade,
      nota: parseFloat(novoDesempenho.value.nota)
    }

    console.log('Enviando payload:', payload)
    
    const response = await getAPI.post('/desempenhos/', payload)
    
    if (response.status === 201) {
      successMessage.value = 'Desempenho cadastrado com sucesso!'
      resetarFormulario()
    }
    } catch (err) {
        if (err.response?.data?.error === 'Já existe uma nota registrada para este aluno(a) nesta atividade!') {
        error.value = err.response.data.error
        resetarFormulario()
    } else {
      error.value = 'Erro ao cadastrar: ' + 
      (err.response?.data?.aluno?.[0] || 
       err.response?.data?.atividade?.[0] ||
       err.response?.data?.nota?.[0] ||
       err.response?.data?.message || 
       err.message)
       resetarFormulario()
    }   
    
    console.error('Detalhes do erro:', {
      mensagem: err.message,
      resposta: err.response?.data,
      payload: {
        aluno: novoDesempenho.value.aluno,
        atividade: novoDesempenho.value.atividade,
        nota: novoDesempenho.value.nota
      },
      config: err.config
    })
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
  padding: 10px 15px;
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
  transition: background-color 0.3s;
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
  border: 1px solid #d6e9c6;
}
</style>