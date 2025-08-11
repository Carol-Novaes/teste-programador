<script setup>
import { RouterLink } from 'vue-router'
import brasao from '@/assets/brasao.png'
</script>

<template>
  <header class="main-header">
    <nav class="nav-menu">
      <router-link to="/" class="logo-link">
        <img :src="brasao" alt="Brasão" class="brasao-header">
      </router-link>
      <div class="nav-links">
        <RouterLink to="/" class="nav-link" active-class="active">
          Disciplinas
        </RouterLink>
        <RouterLink to="/Desempenhos" class="nav-link" active-class="active">
          Cadastro de Desempenho
        </RouterLink>
      </div>
    </nav>
  </header>

  <RouterView />
</template>

<style scoped>
.main-header {
  background-color: #f8f9fa;
  border-bottom: 1px solid #e0e0e0;

}

.brasao-header {
  height: 70px;
  width: auto;
  padding: 1rem;
}
.nav-menu {
  display: flex;
  justify-content: space-between;
  align-items: center;
  max-width: 95%;
}

.nav-spacer {
  flex: 1;
}

.nav-links {
  display: flex;
  gap: 1.5rem;
}

.nav-link {
  color: #495057;
  text-decoration: none;
  font-size: 1rem;
  font-weight: 500;
  padding: 0.5rem 0;
  position: relative;
  transition: color 0.3s ease;
}

.nav-link:hover {
  color: #212529;
}

.active {
  color: #212529;
  font-weight: 600;
}

.active::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 2px;
  background-color: #6c757d;
}

</style>