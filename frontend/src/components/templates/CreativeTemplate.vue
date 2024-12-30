<template>
  <div class="creative-template" :style="containerStyle">
    <div class="background-pattern"></div>
    
    <div class="content">
      <div class="header">
        <div class="name-title">
          <h1>{{ data.name }}</h1>
          <p class="title">{{ data.title }}</p>
          <p class="company">{{ data.company }}</p>
        </div>
      </div>
      
      <div class="main-content">
        <div class="bio-section">
          <h2>About Me</h2>
          <p>{{ data.bio }}</p>
        </div>
        
        <div class="skills-section">
          <h2>Skills</h2>
          <div class="skill-bubbles">
            <div
              v-for="skill in data.skills"
              :key="skill"
              class="skill-bubble"
            >
              {{ skill }}
            </div>
          </div>
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
.creative-template {
  position: relative;
  overflow: hidden;
  background: #2c3e50;
  border-radius: 12px;
  color: white;
  
  .background-pattern {
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: linear-gradient(135deg, rgba(64, 158, 255, 0.1) 0%, rgba(54, 209, 220, 0.1) 100%);
    clip-path: polygon(0 0, 100% 0, 100% 85%, 0 100%);
  }
  
  .content {
    position: relative;
    z-index: 1;
    padding: 40px;
    height: 100%;
    display: flex;
    flex-direction: column;
  }
  
  .header {
    margin-bottom: 40px;
    
    h1 {
      font-size: 48px;
      font-weight: 800;
      margin-bottom: 8px;
      background: linear-gradient(135deg, #409EFF 0%, #36D1DC 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }
    
    .title {
      font-size: 24px;
      color: #409EFF;
      margin-bottom: 4px;
    }
    
    .company {
      font-size: 18px;
      color: rgba(255, 255, 255, 0.7);
    }
  }
  
  .main-content {
    display: grid;
    grid-template-columns: 1.2fr 0.8fr;
    gap: 40px;
    
    h2 {
      font-size: 24px;
      margin-bottom: 20px;
      color: #409EFF;
    }
    
    .bio-section {
      p {
        font-size: 16px;
        line-height: 1.6;
        color: rgba(255, 255, 255, 0.9);
      }
    }
    
    .skill-bubbles {
      display: flex;
      flex-wrap: wrap;
      gap: 12px;
      
      .skill-bubble {
        background: rgba(64, 158, 255, 0.2);
        padding: 8px 16px;
        border-radius: 20px;
        font-size: 14px;
        color: #409EFF;
        border: 1px solid rgba(64, 158, 255, 0.3);
        transition: all 0.3s ease;
        
        &:hover {
          background: rgba(64, 158, 255, 0.3);
          transform: translateY(-2px);
        }
      }
    }
  }
}
</style>
