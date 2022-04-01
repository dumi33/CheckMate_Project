<template>
  <ClassHeader />
  <div class = "class_all">
  <div class ="class_list">
      <h2>수업 이름</h2>
      <div class="class_capture">
          <button type = "button" id="capture_btn">캡처</button>
    </div>
    <div class = "btn_a">
      <button type = "button" id="check_btn">출석확인</button>
      <button type = "button" @click="ClassHome()" id="home_btn">홈화면</button>
    </div>
  </div>
  <div class ="student_list">
      <div class = "check_std">
        <p>출석 학생 리스트</p>
        <div id = "check_db_list">
                학생 리스트---
                {{ student }}
        </div>
      </div>
      <div class = "uncheck_std">
            <p>결석 학생 리스트</p>
            <div id = "uncheck_db_list">
                학생 리스트---
                {{ unstudent }}
            </div>
      </div>
      <button type = "button" id="excel_btn">EXCEL</button>
  </div>
  </div>
</template>

<script>
  import ClassHeader from './common/ClassHeader.vue'

  export default {
    name: 'ClassRegister',
    components: {
      ClassHeader
    }, methods: {
        ClassHome() {
          this.$router.push('/');
        }
    }
  }
</script>

<style scoped>

.class_all {
    width: 100%;
}

.class_list {
    width:60%;
    float:left;
}

.student_list {
    width:40%;
    float:right;
}

.class_list h2 {
    border-color: #7171e09a;
    color:#4949E8;
    margin-top: 30px;
    margin-left: 30px;
    margin-bottom: 20px;
    width: 50%;
    font-size: 40px;
}

.class_capture {
    border-radius: 5px;
    border-top: none;
    border-left: none;
    border-right: none;
    background-color: #4949E8;
    margin-left : 50px;
    text-align: center;
    font-size: 25px;
    width: 80%;
    height: 500px;
}

#capture_btn {
    display: inline-block;
    float: right;
    margin:10px;
    background-color: #ffffff;
    color: #4949E8;
    font-weight: bold;
    border-radius: 5px;
    padding-left:20px;
    padding-right:20px;
    padding-top:5px;
    padding-bottom:5px;
    font-size: 25px;
    border-color: #ffffff7c;
}

.btn_a {
    display: block;
    margin-left: auto;
    margin-right:auto;
    text-align: center;
    margin-top: 20px;
}


#check_btn {
    display: inline-block;
    background:linear-gradient(to bottom, #4949e87c,#4949e8d0);
    color: white;
    height: 50px;
    width: 30%;
    border-radius: 5px;
    font-size: 25px;
    border-color: #ffffff7c;  
}

#home_btn {
    display: inline-block;
    background:linear-gradient(to bottom, #4949e87c,#4949e8d0);
    color: white;
    height: 50px;
    width: 30%;
    border-radius: 5px;
    font-size: 25px;
    border-color: #ffffff7c;  
    margin-left: 20px;
}

.check_std{
    border: 4px solid;
    border-radius: 5px;
    border-color: #7171e09a;
    margin-top:30px;
    margin-left:10px;
    margin-right:20px;
    margin-bottom:20px;
}

.uncheck_std{
    border: 4px solid;
    border-radius: 5px;
    border-color: #7171e09a;
    margin-top:30px;
    margin-left:10px;
    margin-right:20px;
    margin-bottom:20px;
}

#excel_btn {
    display: block;
    background:linear-gradient(to bottom, #4949e87c,#4949e8d0);
    color: white;
    height: 50px;
    width: 50%;
    border-radius: 5px;
    font-size: 25px;
    border-color: #ffffff7c;
    margin-right: auto;
    margin-left: auto;
    margin-top: 20px;
    text-align: center;
}

.check_std p {
    display: inline-block;
    margin: 10px;
    margin-left: 30px;
    font-size: 20px;
    font-weight: bold;
    font-family:'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Verdana, sans-serif;
}

#check_db_list {
    margin: 10px;
    margin-left: 60px;
    font-size: 15px;
}

.uncheck_std p {
    display: inline-block;
    margin: 10px;
    margin-left: 30px;
    font-size: 20px;
    font-weight: bold;
    font-family:'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Verdana, sans-serif;
}

#uncheck_db_list {
    margin: 10px;
    margin-left: 60px;
    font-size: 15px;
}


</style>