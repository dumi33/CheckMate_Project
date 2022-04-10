import axios from 'axios'

const loginStore = {
    // 모듈이 독립적으로 사용
	namespaced: true,
    state: {
        // id, pw, 로그인 후 전달되는 accessToken 값 저장
        user_id: '',
        user_pw: '',
        user_name: '',
        accessToken: ''
    },
	getters: {
        // 로그인 여부를 가져옴
        isLogin(state) {
            return state.accessToken == '' ? false : true;
        }
	},
	mutations: {
        // user_id 설정
        setUserId(state, user_id) {
            state.user_id = user_id;
        },
        // user_pw 설정
        setUserPw(state, user_pw){
            state.user_pw = user_pw;
        },
        setUserName(state, user_name) {
            state.user_name = user_name
        },
        // accessToken 설정
        setAccessToken(state, accessToken) {
            state.accessToken = accessToken;
        },
        // 값 초기화
        reset(state) {
            state.user_id = '';
            state.user_pw = '';
            state.accessToken = '';
        }
	},
    //로그인 처리를 위해 RestApi 서버의 login API 호출
    //login이 성공하면 setAccessToken() 메서드를 commit 하고 실패하면 에러메시지
    // 리턴은 Promise로 하여 Login.vue에서 성공(resolve), 실패(reject)로 처리
	actions: {
        // 로그인
        async doLogin({ commit }, userInfo) {
            let result = false;
            let resultErr = null;
            try {
                // API 연결
                let res = await axios.post("http://localhost:8080/login",userInfo);
                if (res.data.success == true) {
                    alert.log("로그인되었습니다.");
                    commit('setUserId', userInfo.user_id);
                    commit('setUserPw', userInfo.user_pw);
                    commit('setUserName', userInfo.user_name);
                    commit('setAccessToken', res.data.accessToken);
                    // 헤더 추가
                    axios.defaults.headers.common['Access-Token'] = res.data.accessToken;
                    result = true;
                } else {
                    alert.log("로그인되지 않았습니다.");
                    let err = new Error("Request failed with status code 401");
                    err.response = {data:{"success":false, "errormessage":"로그인되지 않았습니다."}};
                    resultErr = err;
                }
            } catch(err) {
                console.log(err);
                if (!err.response) {
                    err.response = {data:{"success":false, "errormessage":err.message}};
                }
                resultErr = err;
            }
            return new Promise((resolve, reject) => {
                if (result) {
                    resolve();
                } else {
                    reject(resultErr);
                }
            });
	},
        // 로그아웃
        doLogout({commit}) {
            commit('reset');
            // 헤더 삭제
            delete axios.defaults.headers.common['Access-Token'];
        }
	}
};

export default loginStore;