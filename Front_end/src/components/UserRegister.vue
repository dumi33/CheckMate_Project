<template>
    <body>
        <div class ="register_all">
        <div class = "register">
            <h2>CheckMate</h2>
            <div class = "reg_name">
                <input v-model="reg_name" type ="text" name = "reg_name" id="reg_name" placeholder="Name">
            </div>
            <div class ="reg_email">
                <input v-model="reg_email" type ="text" name = "reg_email" id="reg_email" placeholder="E-mail">
            </div>
            <div class ="reg_id">
                <input v-model="reg_id" type ="text" name = "reg_id" id="reg_id" placeholder="ID">
            </div>
            <div class ="reg_pw">
                <input v-model="reg_pw" type ="text" name = "reg_pw" id="reg_pw" placeholder="Password">
            </div>
            <div id="reg_submit">
                <button type = "button" @click="UserRegister()" id="register_btn">등록</button>
            </div>
        </div>
        </div>
    </body>
</template>

<script>
export default {
    name: 'UserRegister',
    methods: {
        login_push() {
            this.$router.push('/login');
        }
    }
}
</script>

<style scoped>
* {
    box-sizing: border-box;
    font-family: 'Noto Sans KR', sans-serif;
}

.register_all {
    width: 100%;
    height: 100vh;
    background-size: cover;
    background:linear-gradient(to bottom, #7171e031,#4949E8);
}

body {
    margin: 0;
}

.register {
    width: 300px;
    background-color: rgba( 255, 255, 255, 0.5 );
    margin-right: auto;
    margin-left: auto;
    padding: 20px;
    border-radius: 5px;
    position: relative;
    top: 100px;
}

.register h2 {
    font-size: 30px;
    text-align: center;
    color: #4949e8da;
}

.register input[type=text] {
    border-top: none;
    border-left: none;
    border-right: none;
    background-color: rgba( 255, 255, 255, 0 );
    border-bottom: 3px solid #7171e09a;
    margin: 10px;
    margin-bottom: 15px;
    font-size: 15px;
    width: 240px;
}

.register input::placeholder {
    color: #a0a0d4;
}

.reg_pw {
    margin-bottom: 30px;
}

.register button {
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