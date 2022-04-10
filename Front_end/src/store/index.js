import { createStore } from 'vuex';
import createPersistedState from 'vuex-persistedstate';
import loginStore from './modules/login.js';

export default createStore({
	modules: {
		loginStore: loginStore
	},plugins: [createPersistedState({ paths: ["userStore"] })]
});