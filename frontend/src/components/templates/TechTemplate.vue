<template>
  <div class="tech-template" :style="containerStyle">
    <div class="grid-background"></div>
    
    <div class="content">
      <div class="header">
        <div class="name-section">
          <div class="bracket">{</div>
          <div class="info">
            <h1>{{ data.name }}</h1>
            <p class="title">{{ data.title }}</p>
            <p class="company">{{ data.company }}</p>
          </div>
          <div class="bracket">}</div>
        </div>
      </div>
      
      <div class="main-content">
        <div class="section bio-section">
          <div class="section-header">
            <div class="dot"></div>
            <h2>// Bio</h2>
          </div>
          <p>{{ data.bio }}</p>
        </div>
        
        <div class="section skills-section">
          <div class="section-header">
            <div class="dot"></div>
            <h2>// Skills</h2>
          </div>
          <div class="skill-matrix">
            <div
              v-for="skill in data.skills"
              :key="skill"
              class="skill-item"
            >
              <span class="arrow">→</span>
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
.tech-template {
  position: relative;
  background: #1a1a1a;
  color: #e0e0e0;
  border-radius: 8px;
  overflow: hidden;
  font-family: 'Fira Code', monospace;
  
  .grid-background {
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background-image: 
      linear-gradient(rgba(255, 255, 255, 0.05) 1px, transparent 1px),
      linear-gradient(90deg, rgba(255, 255, 255, 0.05) 1px, transparent 1px);
    background-size: 20px 20px;
    opacity: 0.5;
  }
  
  .content {
    position: relative;
    z-index: 1;
    padding: 40px;
    height: 100%;
  }
  
  .header {
    margin-bottom: 40px;
    
    .name-section {
      display: flex;
      align-items: center;
      
      .bracket {
        font-size: 48px;
        color: #409EFF;
        padding: 0 20px;
      }
      
      .info {
        h1 {
          font-size: 36px;
          color: #409EFF;
          margin-bottom: 8px;
        }
        
        .title {
          font-size: 18px;
          color: #00ff00;
          margin-bottom: 4px;
        }
        
        .company {
          font-size: 16px;
          color: #888;
        }
      }
    }
  }
  
  .section {
    margin-bottom: 30px;
    
    .section-header {
      display: flex;
      align-items: center;
      margin-bottom: 20px;
      
      .dot {
        width: 12px;
        height: 12px;
        background: #00ff00;
        border-radius: 50%;
        margin-right: 12px;
      }
      
      h2 {
        font-size: 20px;
        color: #00ff00;
      }
    }
  }
  
  .bio-section {
    p {
      line-height: 1.6;
      color: #e0e0e0;
    }
  }
  
  .skills-section {
    .skill-matrix {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 12px;
      
      .skill-item {
        display: flex;
        align-items: center;
        
        .arrow {
          color: #409EFF;
          margin-right: 8px;
        }
      }
    }
  }
}
</style>
