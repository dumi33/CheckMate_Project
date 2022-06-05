<template>
    <div class="head">
        <header>
            <div class ="head_lan">
            <div class = main-nav-left> 
            <img id="menu_img" src="../../icons/menu_color.svg" alt="menu">
            <div class = "sub-menu">
                <div class ="class_menu">
                <h3 style="cursor:default">출석부</h3>
                <tr v-for="(classItem, classindex) in classList" v-bind:key="classItem.classIdx">
                <div v-if="classItem.status == 'active'" class = "class_list">
                <td style="cursor:pointer" @click="CheckPage(classItem)" id ="class_name">({{classindex + 1}}) {{classItem.className}}</td>
                </div>
            </tr>
            </div>
            </div>
            </div>
            <img style="cursor:pointer" @click="ClassMain()" id="title_img" src="../../icons/title_color.svg" alt="title">
            </div>
            <ul class="menu">
                <li><router-link to='/login'><img id="logout_img" src="../../icons/logout_color.svg" alt="logout"></router-link></li>
                <li style="cursor:default" id="mypage">{{ name }}</li>
                <li id ="icon">
                <img style="cursor:pointer" @click="UserPage()" id="user_img" src="../../icons/user_color.svg" alt="user">
                </li>
            </ul>
        </header>
    </div> 
</template>
<script>
import axios from 'axios'

export default{
    name: 'ClassHeader',
    data : function() {
        return {
            name: '',
            classList: []
        }
    },
    methods: {
        getClassList() {
          // Http get 메서드로 요청
          // this.$router.query.user_id,
            // this.$router.query.user_id
            axios.get("http://localhost:8080/classes/" + this.$route.query.user_id
           ).then((res)=>{
            this.classList = res.data
            console.log(this.classList)
          }).catch((err) => {
            console.log(err);
          });
        },
        CheckPage(classItem) {
            this.$router.push({path : '/checks/', query : {user_id: this.$route.query.user_id, classIdx : classItem.classIdx, className: classItem.className}} );
        },
        ClassMain() {
          this.$router.push({path: '/classes', query : {user_id:this.$route.query.user_id}});
        }, UserPage() {
            this.$router.push({path: '/user', query : {user_id:this.$route.query.user_id}});
        }
    },
    mounted() {
        this.name = this.$route.query.user_id
        this.getClassList()
    }
}
</script>

<style scoped>
  * {
    font-family: 'Noto Sans KR', sans-serif;
    margin: 0;
    }

    #menu_img{
        position: absolute;
        width: 40px;
        height: 40px;
        left: 1%;
        top: 3%;
    }

    #logout_img{
        width: 70px;
        height: 70px;
    }
    #user_img{
        margin-top: 15px;
        width: 25px;
        height: 25px;
    }

    #title_img {
        width: 300px;
        margin-left: 5%;
        margin-top: 10px;
    }
    .class_menu h3 {
        display: block;
        margin-left: 20px;
    }

    .class_menu {
        color: white;
        margin: 40px;
        margin-top: 50px;
        line-height: 50px;
        border: 1px solid;
    }
    .class_list {
        margin-left: 30px;
        width: 100%;
    }

    .sub-menu {
        position: fixed;
        width: 200px;
        height: 100%;
        transition: 0.5s;
    }

    .sub-menu{
        z-index: 1;
        width: 0;
        height: 100%;
        overflow: hidden;
        background-color: rgba(73, 73, 232, 0.8);
        transition-duration: 0.5s;
    }
    .main-nav-left:hover > .sub-menu{
        height: 100%;
        width: 300px;
        overflow: hidden
    }
    .head h2 {
        color: white;
        text-align: center;
        font-weight: bold;
        float: left;
        display: inline;
        padding: 10px;
        padding-left: 25px;
    }

    .head .menu {
        position: absolute;
        top: 5px;
        right: 10px;
    }

    .head .h_menu li {
        float: left;
        display: inline;
        color: white;
        font-weight: bold;
        padding: 8px;
        font-size: 15px;
        padding-top:15px
    }

    .head .menu li {
        float: right;
        display: inline;
        color: #4949E8;
        padding: 8px;
        font-size: 15px;
    }

    .head a {
        display: block;
        text-decoration: none;
        color: white;
    }

    #mypage {
        border-bottom: 0.5px solid #4949E8;
        padding: 0px;
        font-weight: bold;
        margin-left: 5px;
        margin-top: 25px;
    }
</style>