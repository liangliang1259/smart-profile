<template>
  <div class="creative-template bg-white rounded-xl shadow-sm" :style="containerStyle">
    <!-- 个人信息卡片 -->
    <div class="p-6 mb-4">
      <div class="flex items-start mb-6">
        <div class="relative w-20 h-20">
          <img :src="data.avatar || 'https://ai-public.mastergo.com/ai/img_res/766ae7e3422e069abe169b013eb46649.jpg'" 
               class="w-full h-full rounded-full object-cover shadow-md" />
        </div>
        <div class="ml-4 flex-1">
          <h1 class="text-xl font-medium mb-1">{{ data.name }}</h1>
          <div class="flex items-center text-sm text-gray-600">
            <i class="fas fa-map-marker-alt mr-1"></i>
            <span>{{ data.location }}</span>
          </div>
        </div>
      </div>

      <div class="space-y-4">
        <div class="flex items-center">
          <i class="fas fa-briefcase text-blue-500 w-6"></i>
          <span class="flex-1 text-sm">{{ data.title }}</span>
        </div>
        
        <div class="flex items-center">
          <i class="fas fa-clock text-blue-500 w-6"></i>
          <span class="text-sm text-gray-600">从业年限</span>
          <span class="w-16 text-center text-sm text-gray-600">{{ data.years }}</span>
          <span class="text-sm text-gray-600">年</span>
        </div>
      </div>
    </div>

    <!-- 技能标签 -->
    <div class="p-6 mb-4 border-t border-gray-100">
      <div class="flex items-center mb-4">
        <h3 class="text-base font-medium">专业技能</h3>
      </div>
      <div class="flex flex-wrap gap-2">
        <div v-for="skill in data.skills" :key="skill"
             class="px-4 py-2 bg-gradient-to-r from-blue-50 to-blue-100 rounded-full text-sm text-blue-600">
          {{ skill }}
        </div>
      </div>
    </div>

    <!-- 核心优势 -->
    <div class="p-6 border-t border-gray-100">
      <h3 class="text-base font-medium mb-4 flex items-center">
        <i class="fas fa-star text-yellow-400 mr-2"></i>
        核心优势
      </h3>
      <div class="space-y-3">
        <div v-for="(advantage, index) in data.advantages" :key="index"
             class="flex items-start p-3 rounded-lg bg-blue-50">
          <i class="fas fa-check-circle text-blue-500 mt-1"></i>
          <p class="ml-3 text-sm text-gray-700 flex-1">{{ advantage }}</p>
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
    required: true,
    default: () => ({
      name: '',
      location: '',
      title: '',
      company: '',
      years: 0,
      avatar: '',
      skills: [],
      advantages: []
    })
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
  font-family: 'Inter', system-ui, -apple-system, sans-serif;
}

/* 隐藏滚动条 */
::-webkit-scrollbar {
  display: none;
}
</style>
