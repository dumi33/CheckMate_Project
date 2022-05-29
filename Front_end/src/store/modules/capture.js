const captureStore = {
    state: {
        state_data: false
    },getters:{
        nowState(state) {
            return state.state_data
        }
    },
    mutations: {
        async change_data(state, change){
            state.state_data = change
        }
    }
};

export default captureStore;