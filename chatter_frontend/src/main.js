import { createApp } from 'vue'
import "./assets/styles.css"
import App from './App.vue'
import { createPinia } from 'pinia';
import axios from "axios"
import router from './router'

const pinia = createPinia();
const app = createApp(App);

axios.defaults.baseURL = "http://localhost:8000"

app.use(pinia)
app.use(router, axios)
app.mount('#app')
