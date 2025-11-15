import { ref } from 'vue'

const storedKey = localStorage.getItem("openai_key") || ""

export const openaiKey = ref(storedKey)

export function saveKey(key) {
  openaiKey.value = key
  localStorage.setItem("openai_key", key)
}
