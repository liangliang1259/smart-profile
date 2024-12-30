import axios from 'axios'

const api = axios.create({
  baseURL: 'http://localhost:8000',  // 修改为端口 8000
  timeout: 15000,
  headers: {
    'Content-Type': 'application/json'
  }
})

export const optimizeProfile = async (text) => {
  try {
    const response = await api.post('/ai/optimize', { text })
    return response.data
  } catch (error) {
    console.error('Error optimizing profile:', error)
    throw error
  }
}

export const importProfile = async (url) => {
  try {
    const response = await api.post('/ai/import', { url })
    return response.data
  } catch (error) {
    console.error('Error importing profile:', error)
    throw error
  }
}

// 添加响应拦截器
api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response) {
      console.error('Response error:', error.response.data)
    }
    return Promise.reject(error)
  }
)
