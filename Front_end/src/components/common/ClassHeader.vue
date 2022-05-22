<template>
    <div class="head">
        <header>
            <div class ="head_lan">
            <div class = main-nav-left> 
            <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-list" viewBox="0 0 16 16">
            <path fill-rule="evenodd" d="M2.5 12a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5zm0-4a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5zm0-4a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5z"/>
            </svg>
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
            <h2 style="cursor:pointer" @click="ClassMain()">Checkmate</h2>
            </div>
            <ul class="menu">
                <li><router-link to='/login'>로그아웃</router-link></li>
                <li style="cursor:default" id="mypage">{{ name }}</li>
                <li id ="icon">
                <svg style="cursor:pointer" @click="UserPage()" xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" class="bi bi-person-circle" viewBox="0 0 16 16">
                    <path d="M11 6a3 3 0 1 1-6 0 3 3 0 0 1 6 0z"/>
                    <path fill-rule="evenodd" d="M0 8a8 8 0 1 1 16 0A8 8 0 0 1 0 8zm8-7a7 7 0 0 0-5.468 11.37C3.242 11.226 4.805 10 8 10s4.757 1.225 5.468 2.37A7 7 0 0 0 8 1z"/>
                </svg>
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
            let path = "http://localhost:8080/classes/";
            // this.$router.query.user_id
            axios.get(path + this.$route.query.user_id
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

    .head{
        background-color: rgb(73, 73, 232);
        width: 100%;
        list-style-type: none;
        margin: 0;
        padding: 0;
        display: inline-block;
    }
    .head .head_lan svg {
        float: left;
        display: inline;
        color: white;
        margin-left: 15px;
        margin-top: 10px;
        font-weight: bold;
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
        color: white;
        padding: 8px;
        font-size: 15px;
        padding-top:15px
    }

    .head a {
        display: block;
        text-decoration: none;
        color: white;
    }
</style>