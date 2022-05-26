<template>
<div>
  <ClassHeader />
    <div class ="class_reg">
        <input v-if="isClicked" v-model = 'class_name' type ="text" name = "class_name" id="class_name" placeholder="수업 이름 입력">
        <p v-else >{{this.class_name}}</p>
      <svg style="cursor:pointer" @click="registerClassName()" id = "name_btn" xmlns="http://www.w3.org/2000/svg" width="40" height="40" fill="currentColor" class="bi bi-pencil-square" viewBox="0 0 16 16">
        <path d="M15.502 1.94a.5.5 0 0 1 0 .706L14.459 3.69l-2-2L13.502.646a.5.5 0 0 1 .707 0l1.293 1.293zm-1.75 2.456-2-2L4.939 9.21a.5.5 0 0 0-.121.196l-.805 2.414a.25.25 0 0 0 .316.316l2.414-.805a.5.5 0 0 0 .196-.12l6.813-6.814z"/>
        <path fill-rule="evenodd" d="M1 13.5A1.5 1.5 0 0 0 2.5 15h11a1.5 1.5 0 0 0 1.5-1.5v-6a.5.5 0 0 0-1 0v6a.5.5 0 0 1-.5.5h-11a.5.5 0 0 1-.5-.5v-11a.5.5 0 0 1 .5-.5H9a.5.5 0 0 0 0-1H2.5A1.5 1.5 0 0 0 1 2.5v11z"/>
      </svg>
    </div>
    <div class ="student_reg">
      <p style="cursor:default">학생 등록</p>
        <svg style="cursor:pointer" @click="selectUploadFile()" xmlns="http://www.w3.org/2000/svg" width="35" height="35" fill="currentColor" class="bi bi-plus-circle-fill" viewBox="0 0 16 16">
          <path d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zM8.5 4.5a.5.5 0 0 0-1 0v3h-3a.5.5 0 0 0 0 1h3v3a.5.5 0 0 0 1 0v-3h3a.5.5 0 0 0 0-1h-3v-3z"/>
        </svg>
        <hr>
        <div class ="student_list">
          <tr v-for="studentItem in studentList" v-bind:key="studentItem.studentIdx">
            <td id ="std_name">{{studentItem.name}}</td>
          </tr>
        </div>
    </div>
  <button style="cursor:pointer" type = "button" @click="ClassRegisterCreate()" id="reg_btn">등록 완료</button>
</div>
</template>

<script>
  import ClassHeader from './common/ClassHeader.vue'
  import axios from 'axios'
  export default {
    name: 'ClassRegister',
    data: function() {
      return {
        class_name : '',
        studentList : [],
        response: '',
        classIdx: '',
        isClicked: true
      };
    },
    components: {
      ClassHeader
    }, methods: {
      // 수업 생성 - 이름 등록
        registerClassName() {
          this.isClicked = false;
          console.log(this.class_name)
          const classData = {"className": this.class_name, "userIdx" : this.$route.query.user_id}
          axios.post('http://172.31.35.46:8080/classes/',classData)
            .then((res) => {
              console.log(res.data)
              this.classIdx = res.data.data.classIdx
          }).catch((err) => {
            console.log(err);
          });
        },
        // 수업 학생 등록
        selectUploadFile() {
          console.log(this.classIdx)
          axios.post('http://172.31.35.46:8080/students/' + this.classIdx).then((res) => {
            console.log(res.data)
            this.studentList = res.data.data
          })
        },
        // 메인 화면 이동
        ClassRegisterCreate() {
          this.$router.push({path: '/classes', query : {user_id:this.$route.query.user_id}});
        }
    }
  }
</script>

<style scoped>

.class_reg {
    border: 4px solid;
    border-radius: 5px;
    border-color: #7171e09a;
    margin: 30px;
    margin-right:10px;
    width: 30%;
    display: inline-block;
}

.class_reg p {
  font-weight: bold;
  display: inline-block;
  background-color: rgba( 255, 255, 255, 0 );
  margin: 10px;
  text-align: center;
  font-size: 25px;
  width: 70%;
}

.class_reg input[type=text] {
    border-top: none;
    border-left: none;
    border-right: none;
    background-color: rgba( 255, 255, 255, 0 );
    border-bottom: 3px solid #7171e09a;
    margin: 10px;
    text-align: center;
    font-size: 25px;
    width: 70%;
    font-weight: bold;
}

#name_btn{
  color: #4949e8d0;
  padding-top:10px;
  border-color: #ffffff7c;  
}

.class_reg input::placeholder {
    color: #6b6b92;
}

.student_reg {
    border: 4px solid;
    border-radius: 5px;
    border-color: #7171e09a;
    margin-left: 30px;
    margin-right: 30px;
    margin-top: 10px;
    width: 60%;
}

.student_reg hr{
  border : 0px;
  border-top:4px dotted #7171e09a;
  margin-left:4px;
  margin-right:4px;
}

.student_reg p {
    display: inline-block;
    margin: 10px;
    margin-left: 30px;
    font-size: 27px;
    font-weight: bold;
    font-family:'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Verdana, sans-serif;
}

.student_reg svg {
    color: #4949E8;
    float: right;
    margin: 10px;
}

#reg_btn {
    background:linear-gradient(to bottom, #4949e87c,#4949e8d0);
    color: white;
    height: 50px;
    width: 300px;
    border-radius: 5px;
    font-size: 25px;
    border-color: #ffffff7c;  
    position: absolute;
    top: 70%;
    left:40%;
}

.student_list {
    margin: 5px;
    margin-left: 45px;
    font-size: 20px;
    font-weight: bold;
    font-family:'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Verdana, sans-serif;
}

</style>