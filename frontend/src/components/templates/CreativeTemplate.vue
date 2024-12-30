<template>
  <div class="min-h-screen bg-gradient-to-r from-gray-50 to-slate-50">
    <!-- 顶部导航栏 -->
    <nav class="fixed top-0 left-0 right-0 w-full bg-white/90 backdrop-blur-md shadow-sm z-50 h-14 flex items-center justify-between px-4">
      <h1 class="text-lg font-semibold bg-gradient-to-r from-blue-600 to-indigo-600 text-transparent bg-clip-text">名片展示</h1>
      <div class="flex items-center space-x-4">
        <button class="w-8 h-8 flex items-center justify-center text-gray-500 hover:text-blue-500 transition-colors rounded-button">
          <i class="fas fa-bell text-lg"></i>
        </button>
        <button class="w-8 h-8 flex items-center justify-center text-gray-500 hover:text-blue-500 transition-colors rounded-button">
          <i class="fas fa-ellipsis-h text-lg"></i>
        </button>
      </div>
    </nav>

    <!-- 主要内容区域 -->
    <div class="container mx-auto max-w-2xl pt-20 px-4 pb-24">
      <!-- 个人信息卡片 -->
      <div class="bg-white rounded-2xl shadow-sm p-6 mb-6">
        <div class="flex flex-col">
          <input v-model="userInfo.name" placeholder="输入姓名" 
                 class="text-2xl font-semibold text-gray-800 border-none bg-transparent w-full mb-4"/>
          <div class="flex flex-wrap gap-6 text-sm text-gray-600">
            <div class="flex items-center">
              <i class="fas fa-building text-blue-500 mr-2"></i>
              <input v-model="userInfo.company" placeholder="公司" 
                     class="border-none bg-transparent hover:bg-gray-50 px-2 py-1 rounded"/>
            </div>
            <div class="flex items-center">
              <i class="fas fa-map-marker-alt text-blue-500 mr-2"></i>
              <input v-model="userInfo.location" placeholder="地点" 
                     class="border-none bg-transparent hover:bg-gray-50 px-2 py-1 rounded"/>
            </div>
          </div>
        </div>
      </div>

      <!-- 专业技能 -->
      <div class="bg-white rounded-2xl shadow-sm p-6 mb-6">
        <div class="flex items-center justify-between mb-6">
          <h2 class="text-lg font-semibold text-gray-800 flex items-center">
            <i class="fas fa-star text-yellow-400 mr-3"></i>专业技能
          </h2>
          <button @click="addSkill" 
                  class="px-4 py-2 bg-gradient-to-r from-blue-500 to-indigo-500 text-white text-sm rounded-full flex items-center hover:opacity-90 transition-opacity">
            <i class="fas fa-plus mr-2"></i>添加
          </button>
        </div>
        <div class="flex flex-wrap gap-3">
          <div v-for="(skill, index) in skills" :key="index"
               class="px-4 py-2 bg-gradient-to-r from-blue-500 to-indigo-500 rounded-full text-white text-sm flex items-center group">
            {{ skill }}
            <i class="fas fa-times ml-2 cursor-pointer opacity-50 group-hover:opacity-100" 
               @click="removeSkill(index)"></i>
          </div>
        </div>
      </div>

      <!-- 核心优势 -->
      <div class="bg-white rounded-2xl shadow-sm p-6 mb-6">
        <h2 class="text-lg font-semibold text-gray-800 mb-6 flex items-center">
          <i class="fas fa-chart-line text-blue-500 mr-3"></i>核心优势
        </h2>
        <div class="space-y-4">
          <div v-for="(advantage, index) in advantages" :key="index"
               class="bg-gradient-to-r from-blue-50 to-indigo-50 rounded-xl p-5 hover:from-blue-100 hover:to-indigo-100 transition-colors">
            <div class="flex items-center mb-3">
              <img :src="advantage.icon" alt="advantage icon" class="w-12 h-12 rounded-lg object-cover mr-4"/>
              <h3 class="text-lg font-medium text-gray-800">{{ advantage.title }}</h3>
            </div>
            <p class="text-gray-600 leading-relaxed">{{ advantage.description }}</p>
          </div>
        </div>
      </div>

      <!-- 工作经历 -->
      <div class="bg-white rounded-2xl shadow-sm p-6 mb-6">
        <h2 class="text-lg font-semibold text-gray-800 mb-6 flex items-center">
          <i class="fas fa-briefcase text-blue-500 mr-3"></i>工作经历
        </h2>
        <div class="space-y-8">
          <div v-for="(job, index) in workExperience" :key="index"
               class="relative pl-8 border-l-2 border-blue-100 hover:border-blue-300 transition-colors">
            <div class="absolute w-4 h-4 bg-gradient-to-r from-blue-500 to-indigo-500 rounded-full -left-[9px] top-0"></div>
            <div class="mb-3">
              <h3 class="text-lg font-medium text-gray-800">{{ job.company }}</h3>
              <p class="text-sm text-blue-500">{{ job.title }} | {{ job.period }}</p>
            </div>
            <p class="text-gray-600 leading-relaxed">{{ job.description }}</p>
          </div>
        </div>
      </div>

      <!-- 教育背景 -->
      <div class="bg-white rounded-2xl shadow-sm p-6 mb-6">
        <h2 class="text-lg font-semibold text-gray-800 mb-6 flex items-center">
          <i class="fas fa-graduation-cap text-blue-500 mr-3"></i>教育背景
        </h2>
        <div class="space-y-4">
          <div v-for="(edu, index) in education" :key="index"
               class="bg-gradient-to-r from-blue-50 to-indigo-50 rounded-xl p-5 hover:from-blue-100 hover:to-indigo-100 transition-colors">
            <h3 class="text-lg font-medium text-gray-800 mb-2">{{ edu.school }}</h3>
            <p class="text-blue-500">{{ edu.degree }} | {{ edu.period }}</p>
          </div>
        </div>
      </div>

      <!-- 联系方式 -->
      <div class="bg-white rounded-2xl shadow-sm p-6">
        <h2 class="text-lg font-semibold text-gray-800 mb-6 flex items-center">
          <i class="fas fa-address-card text-blue-500 mr-3"></i>联系方式
        </h2>
        <div class="space-y-4">
          <div class="flex items-center text-gray-600 hover:text-blue-500 transition-colors p-2 rounded-lg hover:bg-blue-50">
            <i class="fas fa-envelope w-8 text-lg"></i>
            <span class="ml-3">{{ contact.email }}</span>
          </div>
          <div class="flex items-center text-gray-600 hover:text-blue-500 transition-colors p-2 rounded-lg hover:bg-blue-50">
            <i class="fas fa-phone w-8 text-lg"></i>
            <span class="ml-3">{{ contact.phone }}</span>
          </div>
        </div>
      </div>
    </div>

    <!-- 底部导航 -->
    <nav class="fixed bottom-0 left-0 right-0 w-full bg-white border-t flex items-center justify-around h-16 px-4">
      <button class="flex flex-col items-center justify-center text-gray-400 hover:text-blue-500 transition-colors">
        <i class="fas fa-home text-xl mb-1"></i>
        <span class="text-xs">首页</span>
      </button>
      <button class="flex flex-col items-center justify-center text-gray-400 hover:text-blue-500 transition-colors">
        <i class="fas fa-qrcode text-xl mb-1"></i>
        <span class="text-xs">扫码</span>
      </button>
      <button class="flex flex-col items-center justify-center text-gray-400 hover:text-blue-500 transition-colors">
        <i class="fas fa-user text-xl mb-1"></i>
        <span class="text-xs">我的</span>
      </button>
    </nav>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const userInfo = ref({
  name: '陈思远',
  company: '远景科技集团',
  location: '上海浦东'
})

const skills = ref(['数据分析', '商业策略', '项目管理', '团队领导', '市场营销'])

const advantages = ref([
  {
    icon: 'https://ai-public.mastergo.com/ai/img_res/4ad8a2ad74dbc79803472cc920e9ae9e.jpg',
    title: '数据驱动决策',
    description: '擅长运用数据分析工具，从海量数据中提取关键信息，为企业制定精准的发展战略和运营决策提供支持。'
  },
  {
    icon: 'https://ai-public.mastergo.com/ai/img_res/c51fc750a0447d678b255707715ddf3a.jpg',
    title: '团队管理能力',
    description: '具备出色的团队领导才能，擅长激励团队成员，提高团队效率和凝聚力，成功带领团队完成多个重大项目。'
  },
  {
    icon: 'https://ai-public.mastergo.com/ai/img_res/408443b0a3b7fd6d31a51ea4da3a27d0.jpg',
    title: '创新思维',
    description: '善于突破传统思维模式，提出创新解决方案，帮助企业在竞争激烈的市场中保持领先优势。'
  }
])

const workExperience = ref([
  {
    company: '远景科技集团',
    title: '商业战略总监',
    period: '2020 - 至今',
    description: '负责公司整体商业战略规划与执行，主导多个重大战略项目落地，带领团队实现业务增长超过 200%'
  },
  {
    company: '腾讯科技',
    title: '高级产品经理',
    period: '2017 - 2020',
    description: '主导企业级 SaaS 产品的规划与开发，服务超过 5000 家企业客户，获得多项行业创新奖项'
  }
])

const education = ref([
  {
    school: '复旦大学',
    degree: '工商管理硕士（MBA）',
    period: '2015 - 2017'
  },
  {
    school: '上海交通大学',
    degree: '计算机科学与技术',
    period: '2011 - 2015'
  }
])

const contact = ref({
  email: 'chensy@outlook.com',
  phone: '+86 135 8888 8888'
})

const addSkill = () => {
  const newSkill = prompt('请输入新技能')
  if (newSkill && skills.value.length < 8) {
    skills.value.push(newSkill)
  }
}

const removeSkill = (index) => {
  skills.value.splice(index, 1)
}
</script>

<style>
:root {
  --app-height: 100%;
}

html, body {
  height: 100%;
  margin: 0;
  padding: 0;
}

input:focus {
  outline: none;
}

.min-h-screen {
  min-height: var(--app-height);
}

/* 添加平滑滚动 */
html {
  scroll-behavior: smooth;
}

/* 优化输入框样式 */
input {
  transition: all 0.2s ease-in-out;
}

input:hover {
  background-color: rgba(243, 244, 246, 0.5);
}

/* 优化卡片阴影 */
.shadow-sm {
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05), 0 1px 2px rgba(0, 0, 0, 0.1);
}
</style>
