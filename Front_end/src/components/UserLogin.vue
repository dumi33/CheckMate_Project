<template>
<body>
    <div class = "login_all">
        <div class="photo">
            <img id="user_img4" src="../icons/user4.svg">
            <img id="user_img1" src="../icons/user1.svg">
            <img id="user_img2" src="../icons/user2.svg">
            <img id="user_img3" src="../icons/user3.svg">
            
        </div>
    <div class = "login_block">
        
        <div class="login_block2">
            <img id="title_img" src="../icons/title_color.svg" alt="title">
        <div class = "login_id">
            <input type ="text" ref = "login_id" name = "login_id" id="login_id" v-model = "user_id" placeholder="ID">
        </div>
        
        <div class ="login_pw">
            <input type ="text" ref = "login_pw" name = "login_pw" id="login_pw" v-model = "user_pw" placeholder="Password">
        </div>
        <div class="login_submit">
            <button style="cursor:pointer" type = "button" @click="LoginCreate()" id="login_btn" value="로그인">로그인</button>
            <button style="cursor:pointer" type = "button" @click="LoginUserRegister()" id="register_btn" value="회원가입">회원가입</button>
            <img style="cursor:pointer" @click="Kakao_login()" src="../assets/kakao_img.png" id="kakao_image">
        </div>
    </div>
    </div>
    </div>
</body>
</template>


<script>
import axios from 'axios'

export default {
    name: 'UserLogin',
    data: function() {
        return {
            user_id : '',
            user_pw : '',
            kakao_url : ''
        };
    },
    methods: {
        LoginCreate() {
            // let userInfo = {user_id : this.user_id, user_pw: this.user_pw}; 
            // 값이 입력되지 않을 때
            if(this.user_id == "") {
                alert("아이디를 입력하세요");
                this.$refs.login_id.focus();
                return;
            }else if (this.user_pw == "") {
                alert("패스워드를 입력하세요.");
                this.$refs.login_pw.focus();
                return;
            }
            // loginStore의 doLogin() 메서드 호출
            // login 성공시 return Url로 이동, 실패시 에러메세지
            // this.$store.dispatch("loginStore/doLogin", userInfo).then(() => {
            //     const returnUrl = window.location.search.replace(/^\?returnUrl=/, "");
            //     console.log(returnUrl)
            //     this.$router.push({path: returnUrl, query: {user_id: this.user_id}});
            // }).catch((err) => {
            //     this.errorMessage = err.response.data.errormessage;
            // });
            this.success = true
            this.$router.push({path:'/classes', query: {user_id : this.user_id}})
        },
        LoginUserRegister(){
            this.$router.push('/register')
        },
        async Kakao_login() {
            const response = await axios.get('http://localhost:8080/oauth/url')
            console.log(response)
        }
    },
    mounted() {
		this.$refs.login_id.focus()
	}
}
</script>

<style>

* {
    box-sizing: border-box;
    font-family: 'Noto Sans KR', sans-serif;
    margin: 0;
    padding: 0;
}

body {
    margin: 0;
}

.login_all {
    width: 100%;
    height: 100vh;
    background-size: cover;
    background: linear-gradient(250.94deg, 
    #8053FF 40.94%, 
    rgba(255, 255, 255, 0.47) 40.94%);
}

#user_img1 {
    position: absolute;
    top:50px;
    width: 400px;
    left: 20px;
}
#user_img2 {
    position: absolute;
    bottom:100px;
    left: 30px;
    width:700px;
}
#user_img3 {
    position: absolute;
    bottom: 30px;
    left: 470px;
    width:600px;
}

#user_img4 {
    position: absolute;
    top: 30px;
    left: 300px;
    width:500px;
}

.login_block {
    position: absolute;
    left: 70%;
    top:125px;
    width: 350px;
}

.login_block2 {
    background-color: rgba( 255, 255, 255, 0.5 );
    padding: 20px;
    border-radius: 5px;
}

#title_img {
    width: 300px;
    display: block;
    margin-right: auto;
    margin-left: auto;
    margin-top: 20px;
    margin-bottom: 20px;
}

.login_block input[type=text] {
    border-top: none;
    border-left: none;
    border-right: none;
    display: block;
    margin-right: auto;
    margin-left: auto;
    background-color: rgba( 255, 255, 255, 0 );
    border-bottom: 3px solid #7171e09a;
    font-size: 20px;
    width: 270px;
    margin-top: 30px;

}

.login_block input::placeholder {
    color: #a0a0d4;
}

.login_pw {
    margin-bottom: 50px;
}

.login_block button {
    background:linear-gradient(to bottom, #4949e87c,#4949e8d0);
    margin-top: 10px;
    width:250px;
    display: block;
    margin-right: auto;
    margin-left: auto;
    /* background-color: #4848e6;*/
    color: #ffffff;
    border-radius: 5px;
    border-bottom: none;
    border-top: none;
    border-left: none;
    border-right: none;
    padding:10px;
    font-size: 15px;
    box-shadow: 3px 3px 3px #4949e87c;
}

button:active {
    box-shadow:none;
}

#kakao_image {
    margin-top: 20px;
    text-align: center;
    display: block;
    margin-right: auto;
    margin-left: auto;
    width:250px;
    height: 40px;
    box-shadow: 3px 3px 3px #eed601;
    border-radius: 5px;
}

#kakao_image:active {
    box-shadow:none;
}

</style>