import { createStore } from 'vuex';
import createPersistedState from 'vuex-persistedstate';
import loginStore from './modules/login.js';
import captureStore from './modules/capture.js';

export default createStore({
	modules: {
		loginStore: loginStore,
		captureStore: captureStore
	},plugins: [createPersistedState({ paths: ["userStore"] })]
});