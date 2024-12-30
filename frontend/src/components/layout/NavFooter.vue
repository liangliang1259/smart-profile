<template>
  <footer class="nav-footer">
    <div class="container">
      <p>&copy; {{ currentYear }} Smart Profile. All rights reserved.</p>
    </div>
  </footer>
</template>

<script setup>
import { ref } from 'vue'

const currentYear = ref(new Date().getFullYear())
</script>

<style lang="scss" scoped>
.nav-footer {
  text-align: center;
  padding: 20px;
  color: #666;
  
  .container {
    max-width: 1200px;
    margin: 0 auto;
  }
}
</style>
