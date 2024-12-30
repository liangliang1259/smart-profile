<script setup>
import NavHeader from '@/components/layout/NavHeader.vue'
import NavFooter from '@/components/layout/NavFooter.vue'
</script>

<template>
  <el-container class="app-wrapper">
    <el-header>
      <nav-header />
    </el-header>
    <el-main>
      <router-view />
    </el-main>
    <el-footer>
      <nav-footer />
    </el-footer>
  </el-container>
</template>

<style lang="scss">
.app-wrapper {
  min-height: 100vh;
  .el-header {
    padding: 0;
    height: 60px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  }
  .el-main {
    padding: 20px;
    background-color: #f5f7fa;
  }
  .el-footer {
    padding: 20px 0;
    background-color: #fff;
  }
}
</style>
