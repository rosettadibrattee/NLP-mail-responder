<script setup>
import { ref } from 'vue'

const message = ref("")
const context = ref("")
const prompt = ref(null)  // always null
const response = ref("")
const loading = ref(false)

const API_URL = "http://localhost:8000/api/response"

async function sendRequest() {
  loading.value = true
  response.value = ""

  const payload = {
    message: message.value,
    context: context.value,
    prompt: prompt.value   // always null
  }

  try {
    const res = await fetch(API_URL, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload)
    })

    const data = await res.json()
    response.value = data.response || JSON.stringify(data)
  } catch (err) {
    response.value = "Error connecting to the server."
  }

  loading.value = false
}
</script>

<template>
  <div class="page">

    <h1>AI Email Responder</h1>

    <!-- MAIN EMAIL INPUT -->
    <textarea
      v-model="message"
      placeholder="Paste the incoming email here..."
      class="input"
    />

    <!-- SMALLER CONTEXT AREA -->
    <textarea
      v-model="context"
      placeholder="Optional context..."
      class="context-input"
    />

    <!-- FIXED NLP BUTTON (unclickable) -->
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
      <pre>{{ response }}</pre>
    </div>

  </div>
</template>

<style>
.page {
  margin: 40px auto;
  max-width: 600px;
  font-family: sans-serif;
}

.input {
  width: 100%;
  height: 160px;
  padding: 10px;
  margin-bottom: 20px;
  font-size: 14px;
  resize: vertical;
}

.context-input {
  width: 100%;
  height: 60px; /* smaller */
  padding: 10px;
  margin-bottom: 20px;
  font-size: 14px;
  resize: vertical;
}

.prompt-box {
  margin-bottom: 20px;
}

.prompt-button {
  padding: 8px 14px;
  font-size: 14px;
  background: #e0e0e0;
  border: 1px solid #ccc;
  border-radius: 6px;
  color: #555;
  cursor: not-allowed;
  opacity: 0.8;
}

button {
  padding: 10px 20px;
  font-size: 15px;
  cursor: pointer;
}

.response-box {
  color: #222;
  font-size: 14px;
  margin-top: 30px;
  padding: 20px;
  background: #f5f5f5;
  white-space: pre-wrap;
  border-radius: 8px;
}

.response-box pre {
  white-space: pre-wrap;    /* wraps long lines */
  word-wrap: break-word;    /* breaks long words if needed */
  overflow-wrap: break-word; /* ensures wrapping */
}
</style>
