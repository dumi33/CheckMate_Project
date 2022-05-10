<template>
<div>
  <ClassHeader />
  <div class ="set_class">
      <input type ="text" v-model = 'className' ref= "class_name" name = "class_name" id="set_name" placeholder="자료를 입력하세요">
      <svg @click="SetClassName()" id = "name_btn" xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="currentColor" class="bi bi-pencil-square" viewBox="0 0 16 16">
        <path d="M15.502 1.94a.5.5 0 0 1 0 .706L14.459 3.69l-2-2L13.502.646a.5.5 0 0 1 .707 0l1.293 1.293zm-1.75 2.456-2-2L4.939 9.21a.5.5 0 0 0-.121.196l-.805 2.414a.25.25 0 0 0 .316.316l2.414-.805a.5.5 0 0 0 .196-.12l6.813-6.814z"/>
        <path fill-rule="evenodd" d="M1 13.5A1.5 1.5 0 0 0 2.5 15h11a1.5 1.5 0 0 0 1.5-1.5v-6a.5.5 0 0 0-1 0v6a.5.5 0 0 1-.5.5h-11a.5.5 0 0 1-.5-.5v-11a.5.5 0 0 1 .5-.5H9a.5.5 0 0 0 0-1H2.5A1.5 1.5 0 0 0 1 2.5v11z"/>
      </svg>
  </div>
  <div class ="set_student">
    <p>학생 등록</p>
    <svg ref=btn_img @click="SetStudent()" xmlns="http://www.w3.org/2000/svg" width="35" height="35" fill="currentColor" class="bi bi-plus-circle-fill" viewBox="0 0 16 16">
      <path d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zM8.5 4.5a.5.5 0 0 0-1 0v3h-3a.5.5 0 0 0 0 1h3v3a.5.5 0 0 0 1 0v-3h3a.5.5 0 0 0 0-1h-3v-3z"/>
    </svg>
  </div>
  <div class = "student_list">
      <p>학생 리스트</p>
      <div id = "db_list">
        <tr v-for="studentList in studentLists" v-bind:key="studentList.id">
          <td>{{studentList.name}}</td>
        </tr>
      </div>
  </div>
  <button type = "button" @click="ClassMain()" id="set_btn">수정</button>
  </div>
</template>

<script>
  import ClassHeader from './common/ClassHeader.vue'
  import axios from 'axios'
  export default {
    name: 'ClassSetting',
    data : function() {
      return {
        className : '',
        studentLists : {}
      }
    },
    components: {
      ClassHeader
    }, methods: {
      //학생 리스트 출력
        GetStudent() { 
          this.$refs.class_name.placeholder = this.$route.query.className
          axios.get("/students/"+ this.$route.query.classIdx).then((res) => {
            this.studentLists = res.data
            console.log(this.studentLists)
          })
        },
        //클래스 이름 수정
        SetClassName() {
          var result = confirm("이름을 수정하시겠습니까?");
          console.log(this.className)
          if (result) {
            axios.patch("/classes/classname/" + this.$route.query.classIdx, 
            {"className" : this.className}).then((res) => {
              console.log(res);
              this.className = res.data.data;
              // this.$route.query.className = this.classItem
              // this.$refs.class_name.placeholder = this.classItem
              console.log(this.className)
              this.$router.push({path: '/class/setting', query : {user_id: this.$route.query.user_id, classIdx: this.$route.query.classIdx, className: this.className}} )
            }).catch((err) => {
              console.log(err);
            });
          }
        },
        // 학생 등록
        SetStudent() {
          axios.post("http://localhost:8080/students/"+ this.$route.query.classIdx).then((res) => {
            console.log(res)
          }).catch((err) => {
              console.log(err);
          });
        },
        ClassMain() {
          this.$router.push({path: '/', query : {user_id:this.$route.query.user_id}});
        }
    }, mounted() {
      this.GetStudent();
    }
  }
</script>

<style scoped>

.set_class {
    border-color: #7171e09a;
    margin: 30px;
    width: 30%;
}

.set_class input[type=text] {
    border-top: none;
    border-left: none;
    border-right: none;
    background-color: rgba( 255, 255, 255, 0 );
    border-bottom: 3px solid #7171e09a;
    margin: 10px;
    text-align: center;
    font-size: 25px;
    width: 60%;
}

.set_class input::placeholder {
    color: #6b6b92;
}

.set_class svg{
    color: #4949E8;
}

.set_student {
    border: 4px solid;
    border-radius: 5px;
    border-color: #7171e09a;
    margin-left: 30px;
    margin-right: 30px;
    margin-top: 10px;
    margin-bottom: 30px;
    display: inline-block;
    width: 60%;
}

.set_student p {
    display: inline-block;
    margin: 10px;
    margin-left: 30px;
    font-size: 27px;
    font-family:'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Verdana, sans-serif;
}

.set_student svg {
    color: #4949E8;
    float: right;
    margin: 10px;
}

#set_btn {
    background:linear-gradient(to bottom, #4949e87c,#4949e8d0);
    color: white;
    height: 50px;
    width: 300px;
    border-radius: 5px;
    font-size: 25px;
    border-color: #ffffff7c;  
    position: absolute;
    top: 70%;
    left:50%;
}

.student_list {
    border: 4px solid;
    border-radius: 5px;
    border-color: #7171e09a;
    margin-left: 30px;
    margin-right: 30px;
    margin-top: 10px;
    display: inline-block;
    width: 60%;
}

.student_list p {
    display: inline-block;
    margin: 10px;
    margin-left: 30px;
    font-size: 27px;
    font-family:'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Verdana, sans-serif;
}

#db_list {
  margin: 5px;
  margin-left: 60px;
  font-size: 20px;
  font-weight: bold;
  font-family:'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Verdana, sans-serif;
}

</style>