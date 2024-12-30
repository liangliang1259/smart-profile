<template>
  <div class="home">
    <div class="hero-section">
      <h1>创建你的专业个人名片</h1>
      <p>使用AI智能优化，一键生成精美的个人介绍</p>
      <el-button type="primary" size="large" @click="$router.push('/create')">
        立即开始
      </el-button>
    </div>

    <div class="features-section">
      <el-row :gutter="40">
        <el-col :span="8">
          <div class="feature-card">
            <el-icon><Edit /></el-icon>
            <h3>智能编辑</h3>
            <p>AI辅助优化内容，让你的介绍更专业</p>
          </div>
        </el-col>
        <el-col :span="8">
          <div class="feature-card">
            <el-icon><Picture /></el-icon>
            <h3>精美模板</h3>
            <p>多种精选模板，一键套用</p>
          </div>
        </el-col>
        <el-col :span="8">
          <div class="feature-card">
            <el-icon><Share /></el-icon>
            <h3>便捷分享</h3>
            <p>生成图片，轻松分享到社交平台</p>
          </div>
        </el-col>
      </el-row>
    </div>
  </div>
</template>

<script setup>
import { Edit, Picture, Share } from '@element-plus/icons-vue'
</script>

<style lang="scss" scoped>
.home {
  .hero-section {
    text-align: center;
    padding: 80px 0;
    background: linear-gradient(135deg, #409EFF 0%, #36D1DC 100%);
    color: white;
    border-radius: 8px;
    margin-bottom: 60px;

    h1 {
      font-size: 48px;
      margin-bottom: 20px;
    }

    p {
      font-size: 20px;
      margin-bottom: 40px;
      opacity: 0.9;
    }
  }

  .features-section {
    padding: 40px 0;

    .feature-card {
      text-align: center;
      padding: 40px;
      background: white;
      border-radius: 8px;
      transition: all 0.3s ease;

      &:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 24px rgba(0,0,0,0.1);
      }

      .el-icon {
        font-size: 48px;
        color: #409EFF;
        margin-bottom: 20px;
      }

      h3 {
        font-size: 24px;
        margin-bottom: 16px;
      }

      p {
        color: #666;
        line-height: 1.6;
      }
    }
  }
}
</style>
