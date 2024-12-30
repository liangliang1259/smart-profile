<template>
  <div class="business-template" :style="containerStyle">
    <div class="header">
      <h1>{{ data.name }}</h1>
      <p class="title">{{ data.title }}</p>
      <p class="company">{{ data.company }}</p>
    </div>
    
    <div class="content">
      <div class="bio">
        <h2>个人简介</h2>
        <p>{{ data.bio }}</p>
      </div>
      
      <div class="skills">
        <h2>专业技能</h2>
        <div class="skill-tags">
          <el-tag
            v-for="skill in data.skills"
            :key="skill"
            class="skill-tag"
          >
            {{ skill }}
          </el-tag>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  data: {
    type: Object,
    required: true
  },
  width: {
    type: Number,
    default: 800
  },
  height: {
    type: Number,
    default: 450
  }
})

const containerStyle = computed(() => ({
  width: `${props.width}px`,
  height: `${props.height}px`
}))
</script>

<style lang="scss" scoped>
.business-template {
  background: white;
  padding: 40px;
  border-radius: 8px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  
  .header {
    text-align: center;
    margin-bottom: 40px;
    
    h1 {
      font-size: 32px;
      margin-bottom: 8px;
      color: #2c3e50;
    }
    
    .title {
      font-size: 18px;
      color: #409EFF;
      margin-bottom: 4px;
    }
    
    .company {
      font-size: 16px;
      color: #666;
    }
  }
  
  .content {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 40px;
    
    h2 {
      font-size: 20px;
      margin-bottom: 16px;
      color: #2c3e50;
    }
    
    .bio {
      p {
        color: #666;
        line-height: 1.6;
      }
    }
    
    .skill-tags {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      
      .skill-tag {
        margin-right: 8px;
        margin-bottom: 8px;
      }
    }
  }
}
</style>
