<template>
  <div class="creative-template" :style="containerStyle">
    <h1 class="page-title">个人名片</h1>

    <!-- 主要内容区域 -->
    <div class="content-wrapper">
      <!-- 个人信息卡片 -->
      <div class="info-card">
        <!-- 头像和基本信息 -->
        <div class="flex items-start mb-8">
          <div class="avatar-wrapper">
            <img :src="data.avatar || 'https://ai-public.mastergo.com/ai/img_res/766ae7e3422e069abe169b013eb46649.jpg'" 
                 class="avatar" />
            <div class="camera-button">
              <i class="fas fa-camera text-white text-sm"></i>
            </div>
          </div>
          <div class="basic-info">
            <h2 class="name">{{ data.name }}</h2>
            <div class="location">
              <i class="fas fa-map-marker-alt"></i>
              <span>{{ data.location }}</span>
            </div>
          </div>
        </div>

        <!-- 职业和年限 -->
        <div class="info-items">
          <div class="info-item">
            <i class="fas fa-briefcase text-blue-500"></i>
            <span>{{ data.title }}</span>
          </div>
          <div class="info-item">
            <i class="fas fa-clock text-blue-500"></i>
            <span>从业年限</span>
            <span class="year-count">{{ data.years }}</span>
            <span>年</span>
          </div>
        </div>
      </div>

      <!-- 技能标签 -->
      <div class="section-card">
        <div class="section-header">
          <h3>专业技能</h3>
          <button class="add-button">
            <i class="fas fa-plus-circle"></i>
          </button>
        </div>
        <div class="skills-wrapper">
          <div v-for="skill in data.skills" :key="skill"
               class="skill-tag">
            {{ skill }}
          </div>
        </div>
      </div>

      <!-- 核心优势 -->
      <div class="section-card">
        <div class="section-header">
          <h3>
            <i class="fas fa-star text-yellow-400"></i>
            核心优势
          </h3>
        </div>
        <div class="advantages-wrapper">
          <div v-for="(advantage, index) in data.advantages" :key="index"
               class="advantage-item">
            <i class="fas fa-check-circle"></i>
            <p>{{ advantage }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// 默认数据
const DEFAULT_DATA = {
  name: 'Fendy',
  location: '北京朝阳',
  title: '汽车之家内容运营 / 私人订制旅行社老板',
  years: '8',
  avatar: '',
  skills: [
    '出境旅游',
    '俄罗斯地接',
    '新加坡游学',
    '海外营销',
    '流量投放',
    '汽车行业',
    'Google投放',
    'Facebook投放'
  ],
  advantages: [
    '拥有出境旅行社，专注俄罗斯及新加坡目的地接待，可承接旅游、商务、展会等多样化需求',
    '8年互联网产品海外流量投放经验，覆盖社交、教育、工具、汽车等领域',
    '深耕汽车行业资源，拥有丰富的汽车媒体渠道合作经验'
  ]
}

export default {
  name: 'CreativeTemplate',
  props: {
    data: {
      type: Object,
      required: true,
      default: () => DEFAULT_DATA
    },
    width: {
      type: Number,
      default: 800
    },
    height: {
      type: Number,
      default: 450
    }
  }
}
</script>

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
  font-family: system-ui, -apple-system, sans-serif;
  background: #f5f7fa;
  height: 100%;
  overflow-y: auto;

  .page-title {
    font-size: 18px;
    font-weight: 500;
    text-align: center;
    padding: 16px;
    color: #333;
  }

  .content-wrapper {
    padding: 16px;
  }

  // 信息卡片
  .info-card {
    background: white;
    border-radius: 12px;
    padding: 16px;
    margin-bottom: 16px;

    .avatar-wrapper {
      position: relative;
      width: 80px;
      height: 80px;

      .avatar {
        width: 100%;
        height: 100%;
        border-radius: 50%;
        object-fit: cover;
      }

      .camera-button {
        position: absolute;
        right: -4px;
        bottom: -4px;
        width: 28px;
        height: 28px;
        background: #4096ff;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
      }
    }

    .basic-info {
      margin-left: 16px;
      flex: 1;

      .name {
        font-size: 20px;
        font-weight: 500;
        margin-bottom: 4px;
      }

      .location {
        display: flex;
        align-items: center;
        color: #666;
        font-size: 14px;
        
        i {
          margin-right: 4px;
        }
      }
    }

    .info-items {
      display: flex;
      flex-direction: column;
      gap: 16px;

      .info-item {
        display: flex;
        align-items: center;
        font-size: 14px;
        color: #666;

        i {
          width: 24px;
          margin-right: 4px;
        }

        .year-count {
          width: 64px;
          text-align: center;
        }
      }
    }
  }

  // 通用卡片样式
  .section-card {
    background: white;
    border-radius: 12px;
    padding: 16px;
    margin-bottom: 16px;

    .section-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 16px;

      h3 {
        font-size: 16px;
        font-weight: 500;
        display: flex;
        align-items: center;

        i {
          margin-right: 8px;
        }
      }

      .add-button {
        color: #4096ff;
        font-size: 20px;
      }
    }
  }

  // 技能标签
  .skills-wrapper {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;

    .skill-tag {
      padding: 8px 16px;
      background: linear-gradient(to right, #e6f0ff, #f0f5ff);
      color: #4096ff;
      border-radius: 100px;
      font-size: 14px;
    }
  }

  // 核心优势
  .advantages-wrapper {
    display: flex;
    flex-direction: column;
    gap: 12px;

    .advantage-item {
      display: flex;
      align-items: flex-start;
      padding: 12px;
      background: #f0f5ff;
      border-radius: 8px;
      font-size: 14px;
      color: #333;

      i {
        color: #4096ff;
        margin-top: 4px;
        margin-right: 12px;
      }

      p {
        flex: 1;
        line-height: 1.5;
      }
    }
  }
}

::-webkit-scrollbar {
  display: none;
}
</style>
