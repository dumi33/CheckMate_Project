<template>
  <ClassHeader />
  <div class ="set_class">
      <input type ="text" name = "class_name" id="set_name" placeholder="수업 이름 입력">
      <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" class="bi bi-pencil" viewBox="0 0 16 16">
        <path d="M12.146.146a.5.5 0 0 1 .708 0l3 3a.5.5 0 0 1 0 .708l-10 10a.5.5 0 0 1-.168.11l-5 2a.5.5 0 0 1-.65-.65l2-5a.5.5 0 0 1 .11-.168l10-10zM11.207 2.5 13.5 4.793 14.793 3.5 12.5 1.207 11.207 2.5zm1.586 3L10.5 3.207 4 9.707V10h.5a.5.5 0 0 1 .5.5v.5h.5a.5.5 0 0 1 .5.5v.5h.293l6.5-6.5zm-9.761 5.175-.106.106-1.528 3.821 3.821-1.528.106-.106A.5.5 0 0 1 5 12.5V12h-.5a.5.5 0 0 1-.5-.5V11h-.5a.5.5 0 0 1-.468-.325z"/>
      </svg>
  </div>
  <div class ="set_student">
    <p>학생 등록</p>
    <svg xmlns="http://www.w3.org/2000/svg" width="35" height="35" fill="currentColor" class="bi bi-plus-circle-fill" viewBox="0 0 16 16">
      <path d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zM8.5 4.5a.5.5 0 0 0-1 0v3h-3a.5.5 0 0 0 0 1h3v3a.5.5 0 0 0 1 0v-3h3a.5.5 0 0 0 0-1h-3v-3z"/>
    </svg>
  </div>
  <div class = "student_list">
      <p>학생 리스트</p>
      <div id = "db_list">
            학생 리스트---
            {{ student }}
      </div>
  </div>
  <button type = "button" @click="SetStudent()" id="set_btn">수정</button>
</template>

<script>
  import ClassHeader from './common/ClassHeader.vue'

  export default {
    name: 'ClassSetting',
    components: {
      ClassHeader
    }, methods: {
        SetStudent() {
          this.$router.push('/');
        }
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
    margin: 10px;
    margin-left: 60px;
    font-size: 20px;
}

</style>