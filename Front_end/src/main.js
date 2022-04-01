import { createApp } from 'vue'
import router from './routes/index'
import App from './App.vue'
import axios from 'axios'

// const app = createApp(App);

// app.use(router); // 사용 설정 하기

// app.mount('#app');

const app = createApp(App) 
app.config.globalProperties.axios = axios; 
app.use(router).mount('#app')
