<template>
  <div class="atividades-container">
    <h1>Cadastrar Atividade:</h1> 

    <div v-if="!loading && !error">
      <form @submit.prevent="cadastrarAtividade" class="atividade-form">
        <h3>Disciplina: {{ disciplinaNome }}</h3>
        <div class="form-group">
          <label for="nome">Nome da Atividade:</label>
          <input type="text" id="nome" v-model="novaAtividade.nome" required>
        
          <label for="valor">Valor (pontos):</label>
          <input type="number" id="valor" v-model="novaAtividade.valor" required>

          <label for="data_atividade">Data da Atividade:</label>
          <input type="date" id="data_atividade" v-model="novaAtividade.data_atividade" required>
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
      <p v-if="!isSubmitting">Carregando...</p>
      <p v-if="isSubmitting">Enviando dados...</p>
    </div>
    
    <div v-if="error" class="error-message">
      <p>Erro: {{ error }}</p>
      <button @click="resetPage">Tentar novamente</button>
    </div>
 </div> 
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { getAPI } from '@/axios-api'

const route = useRoute()
const router = useRouter()

const disciplinaId = ref(route.query.disciplina_id)
const disciplinaNome = ref(route.query.disciplina_nome || 'Disciplina não especificada')

const novaAtividade = ref({
  nome: '',
  valor: '',
  data_atividade: '',
  disciplina: disciplinaId.value
})

const loading = ref(false)
const isSubmitting = ref(false)
const error = ref(null)
const successMessage = ref(null)

const resetPage = () => {
  error.value = null
  loading.value = false
  isSubmitting.value = false
}

const cadastrarAtividade = async () => {
  error.value = null
  successMessage.value = null
  isSubmitting.value = true
  loading.value = true
  
  try {
    const response = await getAPI.post('/atividades/', novaAtividade.value)
    
    if (response.status === 201) {
      successMessage.value = 'Atividade cadastrada com sucesso!'
      novaAtividade.value = {  // Reset dos campos
        nome: '',
        valor: '',
        data_atividade: '',
        disciplina: disciplinaId.value
      }      
    }
  } catch (err) {
    error.value = 'Erro ao cadastrar atividade: ' + (err.response?.data?.message || err.message)
    console.error(err)
  } finally {
    loading.value = false
    isSubmitting.value = false    
  }
}

onMounted(() => {
  if (!disciplinaId.value) {
    router.push({ name: 'disciplinas' })
  }
})
</script>

<style scoped>
.atividades-container {
  padding: 20px;
  max-width: 600px;
  margin: 0 auto;
}

.atividade-form {
  background-color: #f9f9f9;
  padding: 20px;
  border-radius: 10px;
  margin-top: 10px;
}

.atividade-form h3{
  text-align: center;
  margin: 15px 0;
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

.form-group input {
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