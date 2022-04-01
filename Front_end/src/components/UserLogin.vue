<template>
<body>
    <div class = "login_all">
    <div class = "login_block">
        <h2>CheckMate</h2>
        <div class = "login_id">
            <input type ="text" name = "login_id" id="login_id" placeholder="ID">
        </div>
        <div class ="login_pw">
            <input type ="text" name = "login_pw" id="login_pw" placeholder="Password">
        </div>
        <div class="login_submit">
            <button type = "button" @click="LoginCreate()" id="login_btn" value="로그인">로그인</button>
            <button type = "button" @click="LoginUserRegister()" id="register_btn" value="회원가입">회원가입</button>
        </div>
    </div>
    </div>
</body>
</template>


<script>
export default {
    name: 'UserLogin',
    methods: {
        LoginCreate() {
            this.$router.push('/');
        },
        LoginUserRegister(){
            this.$router.push('/register')
        }
    }
}
</script>

<style>

* {
    box-sizing: border-box;
    font-family: 'Noto Sans KR', sans-serif;
}

body {
    margin: 0;
}

.login_all {
    width: 100%;
    height: 100vh;
    background-size: cover;
    background:linear-gradient(to bottom, #7171e031,#4949E8);
}

.login_block {
    width: 300px;
    background-color: rgba( 255, 255, 255, 0.5 );
    margin-right: auto;
    margin-left: auto;
    padding: 20px;
    border-radius: 5px;
    position: relative;
    top: 100px;
}

.login_block h2 {
    font-size: 30px;
    text-align: center;
    color: #4949e8da;
}

.login_block input[type=text] {
    border-top: none;
    border-left: none;
    border-right: none;
    background-color: rgba( 255, 255, 255, 0 );
    border-bottom: 3px solid #7171e09a;
    margin: 10px;
    font-size: 15px;
    width: 240px;
}

.login_block input::placeholder {
    color: #a0a0d4;
}

.login_pw {
    margin-bottom: 40px;
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
}

</style>