<template>
  <div class="create-profile">
    <el-steps :active="activeStep" finish-status="success" class="steps">
      <el-step title="输入信息" />
      <el-step title="选择模板" />
      <el-step title="预览生成" />
    </el-steps>

    <div class="main-content">
      <!-- Step 1: Information Input -->
      <div v-if="activeStep === 0" class="step-content">
        <el-form :model="formData" label-width="100px">
          <el-tabs v-model="inputMethod">
            <el-tab-pane label="手动输入" name="manual">
              <el-form-item label="姓名">
                <el-input v-model="formData.name" />
              </el-form-item>
              <el-form-item label="职位">
                <el-input v-model="formData.title" />
              </el-form-item>
              <el-form-item label="公司">
                <el-input v-model="formData.company" />
              </el-form-item>
              <el-form-item label="个人简介">
                <el-input
                  v-model="formData.bio"
                  type="textarea"
                  :rows="4"
                />
                <el-button type="primary" text @click="optimizeBio">
                  AI优化简介
                </el-button>
              </el-form-item>
              <el-form-item label="技能标签">
                <el-select
                  v-model="formData.skills"
                  multiple
                  filterable
                  allow-create
                  default-first-option
                  placeholder="请选择或输入技能标签"
                >
                  <el-option
                    v-for="skill in skillOptions"
                    :key="skill"
                    :label="skill"
                    :value="skill"
                  />
                </el-select>
              </el-form-item>
            </el-tab-pane>
            <el-tab-pane label="链接导入" name="import">
              <el-form-item label="个人主页">
                <el-input v-model="importUrl" placeholder="输入LinkedIn或GitHub链接">
                  <template #append>
                    <el-button @click="importProfile">导入</el-button>
                  </template>
                </el-input>
              </el-form-item>
            </el-tab-pane>
          </el-tabs>
        </el-form>
      </div>

      <!-- Step 2: Template Selection -->
      <div v-if="activeStep === 1" class="step-content">
        <el-row :gutter="20">
          <el-col v-for="template in templates" :key="template.id" :span="8">
            <div
              class="template-card"
              :class="{ active: selectedTemplate === template.id }"
              @click="selectedTemplate = template.id"
            >
              <img :src="template.preview" :alt="template.name">
              <div class="template-info">
                <h3>{{ template.name }}</h3>
                <p>{{ template.description }}</p>
              </div>
            </div>
          </el-col>
        </el-row>
      </div>

      <!-- Step 3: Preview -->
      <div v-if="activeStep === 2" class="step-content">
        <div class="preview-container">
          <div class="preview-card" ref="previewCard">
            <component
              :is="currentTemplate"
              :data="formData"
              :width="800"
              :height="450"
            />
          </div>
          <div class="preview-actions">
            <el-button type="primary" @click="generateAndSaveImage">生成图片</el-button>
            <el-button type="success" @click="shareToWeChat">分享到微信</el-button>
          </div>
        </div>
      </div>
    </div>

    <div class="step-actions">
      <el-button v-if="activeStep > 0" @click="activeStep--">上一步</el-button>
      <el-button
        v-if="activeStep < 2"
        type="primary"
        @click="activeStep++"
      >
        下一步
      </el-button>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive, computed } from 'vue'
import BusinessTemplate from '@/components/templates/BusinessTemplate.vue'
import CreativeTemplate from '@/components/templates/CreativeTemplate.vue'
import TechTemplate from '@/components/templates/TechTemplate.vue'
import { generateImage, downloadImage, copyToClipboard } from '@/utils/image'
import { ElMessage } from 'element-plus'
import { optimizeProfile, importProfile as importProfileApi } from '@/api/profile'

const activeStep = ref(0)
const inputMethod = ref('manual')
const importUrl = ref('')
const selectedTemplate = ref(null)
const previewCard = ref(null)
let generatedImage = null

const formData = reactive({
  name: '',
  title: '',
  company: '',
  bio: '',
  skills: []
})

const skillOptions = [
  'JavaScript',
  'Python',
  'Vue.js',
  'React',
  'Node.js',
  'Product Management',
  'UI/UX Design'
]

const templates = [
  {
    id: 1,
    name: '简约商务',
    description: '适合职场人士的简约风格',
    preview: 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNk+A8AAQUBAScY42YAAAAASUVORK5CYII='
  },
  {
    id: 2,
    name: '创意设计',
    description: '适合设计师的创意风格',
    preview: 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNk+A8AAQUBAScY42YAAAAASUVORK5CYII='
  },
  {
    id: 3,
    name: '科技极简',
    description: '适合开发者的科技风格',
    preview: 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNk+A8AAQUBAScY42YAAAAASUVORK5CYII='
  }
]

const currentTemplate = computed(() => {
  switch (selectedTemplate.value) {
    case 1:
      return BusinessTemplate
    case 2:
      return CreativeTemplate
    case 3:
      return TechTemplate
    default:
      return BusinessTemplate
  }
})

const optimizeBio = async () => {
  try {
    ElMessage.info('正在优化简介...')
    const result = await optimizeProfile(formData.bio)
    formData.bio = result.optimized_text
    ElMessage.success('简介优化完成')
  } catch (error) {
    ElMessage.error('简介优化失败，请重试')
    console.error(error)
  }
}

const importProfile = async () => {
  if (!importUrl.value) {
    ElMessage.warning('请输入个人主页链接')
    return
  }

  try {
    ElMessage.info('正在导入个人信息...')
    const result = await importProfileApi(importUrl.value)
    
    formData.name = result.name || formData.name
    formData.title = result.title || formData.title
    formData.company = result.company || formData.company
    formData.bio = result.bio || formData.bio
    formData.skills = result.skills || formData.skills
    
    ElMessage.success('个人信息导入成功')
  } catch (error) {
    ElMessage.error('导入失败，请检查链接是否正确')
    console.error(error)
  }
}

const generateAndSaveImage = async () => {
  try {
    ElMessage.info('正在生成图片...')
    generatedImage = await generateImage(previewCard.value)
    await downloadImage(generatedImage)
    ElMessage.success('图片已保存到下载文件夹')
  } catch (error) {
    ElMessage.error('生成图片失败，请重试')
    console.error(error)
  }
}

const shareToWeChat = async () => {
  try {
    if (!generatedImage) {
      generatedImage = await generateImage(previewCard.value)
    }
    
    const success = await copyToClipboard(generatedImage)
    if (success) {
      ElMessage.success('图片已复制到剪贴板，可直接粘贴到微信')
    } else {
      throw new Error('复制失败')
    }
  } catch (error) {
    ElMessage.error('分享失败，请重试')
    console.error(error)
  }
}
</script>

<style lang="scss" scoped>
.create-profile {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;

  .steps {
    margin-bottom: 40px;
  }

  .main-content {
    background: white;
    padding: 30px;
    border-radius: 8px;
    min-height: 400px;
  }

  .step-content {
    margin-bottom: 30px;
  }

  .template-card {
    border: 2px solid transparent;
    border-radius: 8px;
    overflow: hidden;
    cursor: pointer;
    transition: all 0.3s ease;
    margin-bottom: 20px;

    &:hover {
      transform: translateY(-5px);
      box-shadow: 0 8px 16px rgba(0,0,0,0.1);
    }

    &.active {
      border-color: #409EFF;
    }

    img {
      width: 100%;
      height: 200px;
      object-fit: cover;
    }

    .template-info {
      padding: 15px;

      h3 {
        margin: 0 0 10px;
      }

      p {
        margin: 0;
        color: #666;
        font-size: 14px;
      }
    }
  }

  .preview-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 20px;

    .preview-card {
      width: 100%;
      max-width: 600px;
      aspect-ratio: 16/9;
      background: white;
      box-shadow: 0 4px 12px rgba(0,0,0,0.1);
      border-radius: 8px;
    }

    .preview-actions {
      display: flex;
      gap: 16px;
    }
  }

  .step-actions {
    display: flex;
    justify-content: space-between;
    margin-top: 30px;
  }
}
</style>
