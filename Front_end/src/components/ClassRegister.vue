<template>
<div id ='all'>
  <ClassHeader />
    <div class ="class_reg">
      <h2> 수업 등록 </h2>
        <input v-if="isClicked" v-model = 'class_name' type ="text" name = "class_name" id="class_name" placeholder="Class Name">
        <p v-else >{{this.class_name}}</p>
      <svg style="cursor:pointer" @click="registerClassName()" id = "name_btn" xmlns="http://www.w3.org/2000/svg" width="45" height="45" fill="currentColor" class="bi bi-pencil-square" viewBox="0 0 16 16">
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
          <tr class = "flex_container" v-for="studentItem in studentList" v-bind:key="studentItem.studentIdx">
            <td class="flex_item"  style="cursor:default" id ="std_name">{{studentItem.name}}</td>
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
        isClicked: true,
        classList: []
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
          axios.post('http://localhost:8080/classes/',classData)
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
          axios.post('http://localhost:8080/students/' + this.classIdx).then((res) => {
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

#all {
  width: 100%;
  height: 100vh;
  background: linear-gradient(180deg, 
  #4949E8 0%, rgba(74, 74, 220, 0.850791) 31.77%, 
  rgba(74, 74, 218, 0.824091) 53.65%, 
  rgba(153, 67, 220, 0.616062) 89.58%, 
  rgba(208, 62, 221, 0.47) 100%);
}

.class_reg {
  position: absolute;
  top:100px;
  left:50px;
  margin: 30px;
  margin-right:10px;
  width: 400px;
}

.class_reg h2{
  display: inline-block;
  color: white;
  font-weight: bold;
  font-size: 60px;
}

.class_reg p {
  font-weight: bold;
  display: inline-block;
  background-color: rgba(255, 255, 255, 0);
  margin: 10px;
  text-align: center;
  font-size: 35px;
  width: 220px;
  margin-left: 50px;
}

.class_reg input[type=text] {
    border-top: none;
    border-left: none;
    border-right: none;
    background-color: rgba( 255, 255, 255, 0 );
    border-bottom: 3px dotted #ffffff;
    margin: 10px;
    margin-left:50px;
    text-align: center;
    font-size: 35px;
    width: 220px;
    color: #ffffff;
    font-weight: bold;
}

#name_btn{
  color: #ffffffd0;
  padding-top:10px;
  border-color: #ffffff7c;
}

.class_reg input::placeholder {
    color: #b6b6ff;
}

.student_reg {
  position: absolute;
  left:45%;
  top:100px;
  border-radius: 5px;
  margin-left: 30px;
  margin-right: 30px;
  margin-top: 10px;
}

.student_reg hr{
  border : 0px;
  border-top:4px dotted #9898f59a;
  margin-left:4px;
  margin-right:4px;
}

.student_reg p {
    display: inline-block;
    color:white;
    margin: 10px;
    margin-left: 30px;
    font-size: 35px;
    font-weight: bold;
    font-family:'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Verdana, sans-serif;
}

.student_reg svg {
  color: #ffffff;
  padding-top:7px;
}

#reg_btn {
  position: absolute;
  background:white;
  color: #4949e8d0;
  height: 50px;
  width: 200px;
  border-radius: 5px;
  border-color: #ffffff7c;  
  position: absolute;
  font-size: 25px;
  font-weight: bold;
  top: 70%;
  left:45%;
}

.student_list {
  margin: 5px;
  margin-left: 50px;
  font-size: 20px;
  font-weight: bold;
  width:600px;
  font-family:'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Verdana, sans-serif;
}

.flex_container{
  display: inline-flex;
  flex-direction: row;
  flex-wrap:wrap;
  justify-content: space-around;
}

.flex_item {
  margin: 15px;
  padding: 10px;
  width: 100px;
  height: 50px;
  border-radius: 5px;
  background: white;
  color: #4949e8d0;
  font-size: 20px;
  font-weight: bold;
  text-align: center;
  border-bottom: none;
  border-top: none;
  border-left: none;
  border-right: none;
  box-shadow: 2px 2px 2px #e8e8ff7c;
}

</style>