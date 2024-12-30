import html2canvas from 'html2canvas'

export const generateImage = async (element) => {
  try {
    const canvas = await html2canvas(element, {
      scale: 2,
      useCORS: true,
      backgroundColor: null
    })
    
    return canvas.toDataURL('image/png')
  } catch (error) {
    console.error('Error generating image:', error)
    throw error
  }
}

export const downloadImage = (dataUrl, filename = 'profile.png') => {
  const link = document.createElement('a')
  link.href = dataUrl
  link.download = filename
  document.body.appendChild(link)
  link.click()
  document.body.removeChild(link)
}

export const copyToClipboard = async (dataUrl) => {
  try {
    const response = await fetch(dataUrl)
    const blob = await response.blob()
    const item = new ClipboardItem({ 'image/png': blob })
    await navigator.clipboard.write([item])
    return true
  } catch (error) {
    console.error('Error copying to clipboard:', error)
    return false
  }
}
