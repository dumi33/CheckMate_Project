<template>
    <body>
        <div class ="register_all">
        <div class = "register">
            <h2>CheckMate</h2>
            <div class = "reg_name">
                <input ref = "reg_name" v-model="reg_name" type ="text" name = "reg_name" id="reg_name" placeholder="Name">
            </div>
            <div class ="reg_email">
                <input ref = "reg_email" v-model="reg_email" type ="text" name = "reg_email" id="reg_email" placeholder="E-mail">
            </div>
            <div class ="reg_id">
                <input ref = "reg_id" v-model="reg_id" type ="text" name = "reg_id" id="reg_id" placeholder="ID">
            </div>
            <div class ="reg_pw">
                <input ref = "reg_pw" v-model="reg_pw" type ="text" name = "reg_pw" id="reg_pw" placeholder="Password">
            </div>
            <div id="reg_submit">
                <button type = "button" @click="UserRegister()" id="register_btn">등록</button>
            </div>
        </div>
        </div>
    </body>
</template>

<script>
// function checkPassword(pwd) {
//     var pwdCheck = /^(?=.*[a-zA-Z])(?=.*[!@#$%^*+=-])(?=.*[0-9]).{8,25}$/;
//     if (!pwdCheck.test(pwd.value)) {
//         alert("비밀번호는 영문자+숫자+특수문자 조합으로 8~25자리 사용해야 합니다.");
//         pwd.focus();
//         return false;
//     }
// }


export default {
    name: 'UserRegister',
    data: function() {
        return {
            reg_info: {
                reg_name: '',
                reg_email: '',
                reg_id: '',
                reg_pw: ''
            }
        };
    },
    methods: {
        UserRegister() {
            var pwdCheck = /^(?=.*[a-zA-Z])(?=.*[!@#$%^*+=-])(?=.*[0-9]).{8,25}$/;
            var emailCheck= /^[A-Za-z0-9_]+[A-Za-z0-9]*[@]{1}[A-Za-z0-9]+[A-Za-z0-9]*[.]{1}[A-Za-z]{1,3}$/;
            // 값이 입력되지 않을 때
            if(this.reg_name == "") {
                alert("이름을 입력하세요");
                this.$refs.reg_name.focus();
                return;
            }else if (this.reg_email == "") {
                alert("이메일을 입력하세요.");
                this.$refs.reg_email.focus();
                return;
            }else if (this.reg_id == "") {
                alert("아이디를 입력하세요.");
                this.$refs.reg_id.focus();
                return;
            }else if (this.reg_pw == "") {
                alert("비밀번호를 입력하세요.");
                this.$refs.reg_pw.focus();
                return;
            }
            // 유효성 체크
            else if (!emailCheck.test(this.reg_email)) {
                alert("이메일 형식이 올바르지 않습니다!");
                this.$refs.reg_email.focus();
                return;
            }
            else if (!pwdCheck.test(this.reg_pw)) {
                alert("비밀번호는 영문자+숫자+특수문자 조합으로 8~25자리 사용해야 합니다.");
                this.$refs.reg_pw.focus();
                return;
            }
            // 통신
            this.axios.post('/register', {
                user: this.reg_info
            }).then((res) => {
                if (res.data.success == true) {
                alert("회원가입에 성공하셨습니다.");
                this.$router.push('/login')
            } else if (res.data.success == false) {
                alert(res.data.errorMsg);
            }
            })
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