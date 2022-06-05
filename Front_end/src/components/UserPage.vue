<template>
<div id="all">
  <ClassHeader />
    <div class = "profile">
    <h2>마이페이지</h2>
        <div id = "icon">
            <h3>프로필</h3>
            <hr>
            <!-- <svg style="cursor:default" xmlns="http://www.w3.org/2000/svg" width="150" height="150" fill="currentColor" class="bi bi-person-circle" viewBox="0 0 16 16">
                <path d="M11 6a3 3 0 1 1-6 0 3 3 0 0 1 6 0z"/>
                <path fill-rule="evenodd" d="M0 8a8 8 0 1 1 16 0A8 8 0 0 1 0 8zm8-7a7 7 0 0 0-5.468 11.37C3.242 11.226 4.805 10 8 10s4.757 1.225 5.468 2.37A7 7 0 0 0 8 1z"/>
            </svg> -->
            <img style="cursor:pointer" id="user_img" src="../icons/user_color.svg" alt="user">
            <h3 id = 'name'>{{name}}</h3>
        </div>
        <div id ="info">
            <h3>이메일 변경</h3>
            <input v-model="email" type="text" id="email" name="email">
            <button style="cursor:pointer" type = "button" @click="UpdateUserEmail()" class="update_btn">수정</button>
            <hr>
            <h3>비밀번호 변경</h3>
            <input v-model="passwd" type="text" id="passwd" name="passwd">
            <button style="cursor:pointer" type = "button" @click="UpdateUserPasswd()" class="update_btn">수정</button>
        </div>
    </div>
  </div>
</template>

<script>
    import ClassHeader from './common/ClassHeader_left.vue'
    import axios from 'axios'
    
    export default {
        name: 'UserPage',
        data : function() {
            return {
                name: '',
                email: 'email',
                passwd: 'password'
            }
        },
        components: {
            ClassHeader
        }, methods: {
            GetUserInfo() {
                axios.get('http://localhost:8080/user/'+ this.$route.query.user_id).then((res)=> {
                    console.log(res.data)
                    this.email = res.data.email
                    this.passwd = res.data.passwd
                })
            },
            UpdateUserEmail(){
                var emailCheck= /^[A-Za-z0-9_]+[A-Za-z0-9]*[@]{1}[A-Za-z0-9]+[A-Za-z0-9]*[.]{1}[A-Za-z]{1,3}$/;
                // 유효성 체크
                if (!emailCheck.test(this.email)) {
                    alert("이메일 형식이 올바르지 않습니다!");
                    this.$refs.reg_email.focus();
                    return;
                }
                var result = confirm('값을 변경하시겠습니까?')
                if(result) {
                    axios.patch('http://localhost:8080/user/email'+ this.$route.query.user_id, 
                        {   email : this.email}).then((res)=> {
                        console.log(res.data)
                    })
                }
            },
            UpdateUserPasswd() {
                var pwdCheck = /^(?=.*[a-zA-Z])(?=.*[!@#$%^*+=-])(?=.*[0-9]).{8,25}$/;

                if (!pwdCheck.test(this.passwd)) {
                    alert("비밀번호는 영문자+숫자+특수문자 조합으로 8~25자리 사용해야 합니다.");
                    this.$refs.reg_pw.focus();
                    return;
                }
                var result = confirm('값을 변경하시겠습니까?')
                if(result) {
                    axios.patch('http://localhost:8080/user/passwd'+ this.$route.query.user_id, 
                        { passwd : this.passwd}).then((res)=> {
                        console.log(res.data)
                    })
                }
            }
        }, mounted() {
            this.name = this.$route.query.user_id,
            this.GetUserInfo()
        }
    }
</script>

<style scoped>

#all {

}

.profile {
    width: 100%;

}

.profile h2 {
    border: 4px dotted #4949E8  ;
    border-color: #7171e09a;
    color:#4949E8;
    margin-top: 30px;
    margin-left: 50px;
    margin-bottom: 20px;
    width: 200px;
    text-align: center;
    padding: 4px 20px 4px 20px;
    font-size: 30px;
    display: block;
}

#icon{
    border: 3px groove #4949E8;
    border-radius: 5px;
    width: 250px;
    margin-top: 20px;
    height: 300px;
    margin-left: 80px;
    vertical-align: top;
    display: inline-block;
}

.profile hr {
    border: 1px dashed #4949E8;
    margin: 10px;
    border-radius: 20px;
    color:#4949E8;
}

.profile #name{
    margin: 0px;
    margin-top: 10px;
    text-align: center;
}

#icon img{
    display: inline-block;
    text-align: center;
    color: #4949E8;
    margin-left: 50px;
    margin-top: 15px;
    width: 150px;
    font-weight: bold;
}

#photo_btn {
    display: block;
    margin-left:100px;
    text-align: center;
    margin-top:5px;
    margin-bottom: 5px;
    background:linear-gradient(to bottom, #4949e87c,#4949e8d0);
    color: white;
    height: 30px;
    border-radius: 5px;
    font-size: 20px;
    border-color: #ffffff7c;
}

.profile h3 {
    color:#4949E8;
    margin-left:20px;
}

#info {
    border: 3px groove #4949E8;
    border-radius: 5px;
    width: 400px;
    height: 250px;
    margin-top: 20px;
    margin-left: 30px;
    display: inline-block;
    position : relative;
}

#info input {
    margin-left: 40px;
    font-size: 15px;
    display: inline-block;
    height:30px;
    width: 200px;
    margin-top: 10px;
    margin-bottom:10px;
    color: rgba(73, 73, 232, 0.8);
}

.update_btn {
    display: inline-block;
    text-align: center;
    margin-left: 20px;
    background:linear-gradient(to bottom, #4949e87c,#4949e8d0);
    color: white;
    height: 30px;
    border-radius: 5px;
    font-size: 20px;
    border-color: #ffffff7c;
}

</style>