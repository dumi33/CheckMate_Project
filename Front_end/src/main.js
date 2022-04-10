import { createApp } from 'vue'
import router from './routes/index'
import App from './App.vue'
import axios from 'axios'
import store from './store'

const app = createApp(App).use(router).use(store)
app.config.globalProperties.axios = axios;
// app.use(store);
// app.use(router);
app.mount('#app')