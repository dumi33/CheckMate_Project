<template>
  <ClassHeader />
  <div class ="class_reg">
      <input type ="text" name = "class_name" id="class_name" placeholder="수업 이름 입력">
  </div>
  <div class ="student_reg">
    <p>학생 등록</p>
    <svg xmlns="http://www.w3.org/2000/svg" width="35" height="35" fill="currentColor" class="bi bi-plus-circle-fill" viewBox="0 0 16 16">
      <path d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zM8.5 4.5a.5.5 0 0 0-1 0v3h-3a.5.5 0 0 0 0 1h3v3a.5.5 0 0 0 1 0v-3h3a.5.5 0 0 0 0-1h-3v-3z"/>
    </svg>
  </div>
  <button type = "button" @click="ClassRegisterCreate()" id="reg_btn">등록</button>
</template>

<script>
  import ClassHeader from './common/ClassHeader.vue'

  export default {
    name: 'ClassRegister',
    components: {
      ClassHeader
    }, methods: {
        ClassRegisterCreate() {
          this.$router.push('/');
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
    width: 30%;
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
    width: 90%;
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

.student_reg p {
    display: inline-block;
    margin: 10px;
    margin-left: 30px;
    font-size: 27px;
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
    left:50%;
}

</style>