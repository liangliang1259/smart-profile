<template>
  <div class="nav-header">
    <div class="logo">
      <router-link to="/">Smart Profile</router-link>
    </div>
    <div class="nav-menu">
      <el-menu mode="horizontal" router>
        <el-menu-item index="/">首页</el-menu-item>
        <el-menu-item index="/create">创建名片</el-menu-item>
        <el-menu-item index="/templates">模板中心</el-menu-item>
      </el-menu>
    </div>
    <div class="user-actions">
      <el-button type="primary" @click="$router.push('/create')">开始制作</el-button>
    </div>
  </div>
</template>

<script setup>
</script>

<style lang="scss" scoped>
.nav-header {
  height: 60px;
  display: flex;
  align-items: center;
  padding: 0 20px;
  background-color: #fff;

  .logo {
    font-size: 24px;
    font-weight: bold;
    margin-right: 40px;
    a {
      color: #409EFF;
      text-decoration: none;
    }
  }

  .nav-menu {
    flex: 1;
    .el-menu {
      border: none;
    }
  }

  .user-actions {
    margin-left: 20px;
  }
}
</style>
