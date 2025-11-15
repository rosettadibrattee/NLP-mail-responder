<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import './main.css'
import { openaiKey } from './composables/useSettings'

const router = useRouter()

const message = ref("")
const context = ref("")
const prompt = ref(null)   // always null
const response = ref("")
const loading = ref(false)

const API_URL = import.meta.env.VITE_API_URL

async function sendRequest() {
  loading.value = true
  response.value = ""

  const payload = {
    message: message.value,
    context: context.value,
    prompt: prompt.value
  }

  try {
    const res = await fetch(API_URL, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "x-openai-key": openaiKey.value   // <-- USER'S OPENAI KEY
      },
      body: JSON.stringify(payload)
    })

    const data = await res.json()
    response.value = data.response || JSON.stringify(data)
  } catch {
    response.value = "Error connecting to the server."
  }

  loading.value = false
}

</script>

<template>
  <div class="page">

    <h1>AI Email Responder</h1>

    <textarea
      v-model="message"
      placeholder="Paste the incoming email here..."
      class="input"
    />

    <textarea
      v-model="context"
      placeholder="Optional context..."
      class="context-input"
    />

    <div class="prompt-box">
      <button class="prompt-button" disabled>
        NLP (default)
      </button>
    </div>

    <button @click="sendRequest" :disabled="loading">
      {{ loading ? "Processing..." : "Generate Response" }}
    </button>

    <div v-if="response" class="response-box">
      <h2>Generated Reply</h2>
      <div class="response-text">{{ response }}</div>
    </div>

    <button class="settings-btn" @click="router.push('/settings')">
      ⚙️
    </button>

  </div>
</template>
