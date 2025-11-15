<script setup>
import { ref } from 'vue'
import './main.css'
import { openaiKey, saveKey } from './composables/useSettings'
import { useRouter } from 'vue-router'

const router = useRouter()
const tempKey = ref(openaiKey.value)
const showKey = ref(false)     // 👈 NEW

async function validateKey(key) {
    try {
        const res = await fetch("https://api.openai.com/v1/models", {
            headers: { "Authorization": `Bearer ${key}` }
        })
        return res.status === 200
    } catch (err) {
        return false
    }
}

async function handleSaveKey() {
    const key = tempKey.value.trim()

    if (!key) {
        alert("Please enter a key.")
        return
    }

    const valid = await validateKey(key)

    if (!valid) {
        alert("Invalid API key.")
        return
    }

    saveKey(key)

    router.push("/")
}
</script>

<template>
  <div class="page">
    <h1>Settings</h1>

    <div class="settings-box">
        <label>OpenAI API Key</label>
        <div class="input-eye-wrapper">
            <input
                :type="showKey ? 'text' : 'password'"
                v-model="tempKey"
                class="settings-input"
                placeholder="Enter your API key..."
            />
            <span class="eye" @click="showKey = !showKey">
                {{ showKey ? '🙈' : '👁️' }}
            </span>
        </div>

        <button @click="handleSaveKey">Save Key</button>
        <button @click="router.push('/')" class="back-btn">Back</button>

    </div>
  </div>
</template>
