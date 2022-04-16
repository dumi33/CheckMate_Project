<template>
<div>
  <ClassHeader />
  <div class ="reg_class">
    <p>수업 등록</p>
    <svg @click="ClassRegister()" xmlns="http://www.w3.org/2000/svg" width="35" height="35" fill="currentColor" class="bi bi-plus-circle-fill" viewBox="0 0 16 16">
      <path d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zM8.5 4.5a.5.5 0 0 0-1 0v3h-3a.5.5 0 0 0 0 1h3v3a.5.5 0 0 0 1 0v-3h3a.5.5 0 0 0 0-1h-3v-3z"/>
    </svg>
  </div>
  <div class ="reg_list">
    <p>My 수업 리스트</p>
      <div class ="list_name">
        <tr v-for="classItem in classList" v-bind:key="classItem.classIdx">
          <div class = "one_list">
          <td id ="class_name">{{classItem.className}}</td>
          <div class = "list_btn">
            <button type = "button" @click="ClassManagement(classItem)" id ="reg_btn">관리</button>
            <button type = "button" @click="ClassSelect(classItem)" id="select_btn">선택</button>
            </div>
        </div>
        </tr>
      </div>
  </div>
</div>
</template>

<script>
  import ClassHeader from './common/ClassHeader.vue'
  import axios from 'axios'

  export default {
    name: 'ClassMain',
    components: {
      ClassHeader
    },
    data : function(){
      return {
        classList : []
      };
    },
    methods: {
        getClassList() {
          // Http get 메서드로 요청
          // this.$router.query.user_id,
            let path = "http://192.168.0.6:8080/classes/";
            // this.$router.query.user_id
            axios.get(path + this.$route.query.user_id
           ).then((res)=>{
            this.classList = res.data
            console.log(this.classList)
          }).catch((err) => {
            console.log(err);
          });
        },
        ClassRegister() {
          this.$router.push({path : '/class/register', query : {user_id: this.$route.query.user_id}});
        },
        ClassManagement(classItem) {
          this.$router.push({path: '/class/setting', query : {classId : classItem.class_id}} )
        },
        ClassSelect(classItem) {
          this.$router.push({path: '/class/list', query : {classId : classItem.class_id}});
        }
    },mounted() {
      this.getClassList();
    }
  }
</script>

<style scoped>

.reg_class {
    border: 4px solid;
    border-radius: 5px;
    border-color: #7171e09a;
    margin: 30px;
    width: 40%;
}

.reg_class p {
    display: inline-block;
    margin: 10px;
    font-size: 30px;
    font-weight: bold;
    font-family:'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Verdana, sans-serif;
}

.reg_class svg {
    color: #4949E8;
    float: right;
    margin: 10px;
}

.reg_list {
    border: 4px solid;
    border-radius: 5px;
    border-color: #7171e09a;
    margin-left: 30px;
    margin-right: 30px;
    margin-top: 10px;
    width: 70%;
    margin-top: 20px;
}

.reg_list p {    
    display: inline-block;
    margin: 10px;
    padding: 5px;
    font-size: 25px;
    font-weight: bold;
    font-family:'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Verdana, sans-serif;
}

.list_name {
  text-align: center;
  display: block;

  width: 100%;
}
.list_name tr {
  text-align: center;
  display: block;
  margin: 10px;
  width: 80%;
}

.list_btn {
    display: inline-block;
    width: 40%;
}

.list_btn Button {
    display: inline-block;
    text-align: center;
    background:linear-gradient(to bottom, #4949e87c,#4949e8d0);
    color: white;
    height: 40px;
    border-radius: 5px;
    font-size: 25px;
    border-color: #ffffff7c;
}

#class_name {
  font-weight: bold;
    display: inline-block;
    text-align: center;
    color: #4949e8d0;
    height: 40px;
    font-size: 25px;
    width: 60%;
    padding-top: 2px;
    margin-left: 0;
    border-bottom: 3px solid;
    border-radius: 2px;
    border-color: #4949e8d0;
}
#reg_btn {
}
#select_btn {
    margin-left:5px;
}
</style>
