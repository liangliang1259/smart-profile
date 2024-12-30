import axios from 'axios'

const api = axios.create({
  baseURL: '/api',
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

// 添加请求拦截器
api.interceptors.request.use(
  (config) => {
    // 在发送请求之前做些什么
    return config
  },
  (error) => {
    // 对请求错误做些什么
    return Promise.reject(error)
  }
)

// 添加响应拦截器
api.interceptors.response.use(
  (response) => {
    // 对响应数据做点什么
    return response
  },
  (error) => {
    // 对响应错误做点什么
    if (error.response) {
      // 服务器返回错误状态码
      console.error('Response error:', error.response.data)
    } else if (error.request) {
      // 请求发送成功，但没有收到响应
      console.error('No response received:', error.request)
    } else {
      // 请求配置发生错误
      console.error('Request error:', error.message)
    }
    return Promise.reject(error)
  }
)
