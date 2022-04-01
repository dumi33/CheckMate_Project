<template>
  <ClassHeader />
  <div class ="reg_class">
    <p>수업 등록</p>
    <svg @click="ClassRegister()" xmlns="http://www.w3.org/2000/svg" width="35" height="35" fill="currentColor" class="bi bi-plus-circle-fill" viewBox="0 0 16 16">
      <path d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zM8.5 4.5a.5.5 0 0 0-1 0v3h-3a.5.5 0 0 0 0 1h3v3a.5.5 0 0 0 1 0v-3h3a.5.5 0 0 0 0-1h-3v-3z"/>
    </svg>
  </div>
  <div class ="reg_list">
    <p>My 수업 리스트</p>
    <ul class ="class_list">
    <li>
      <div class ="list_name">
        <p id ="class_name">수업명</p>
        <div class = "list_btn">
          <button type = "button" @click="ClassManagement()" id ="reg_btn">관리</button>
          <button type = "button" @click="ClassSelect()" id="select_btn">선택</button>
        </div>
      </div>
    </li>
    </ul>
  </div>
</template>

<script>
  import ClassHeader from './common/ClassHeader.vue'

  export default {
    name: 'ClassMain',
    components: {
      ClassHeader
    },
    methods: {
        ClassRegister() {
          this.$router.push('/class/register');
        },
        ClassManagement() {
          this.$router.push('/class/setting')
        },
        ClassSelect() {
          this.$router.push('/class/list');
        }
    },
    data() {
      
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
    width: 60%;
    margin-top: 20px;
}

.reg_list p {    
    display: inline-block;
    margin: 10px;
    padding: 5px;
    font-size: 25px;
    font-family:'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Verdana, sans-serif;
}

.list_name {
    text-align: center;
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

.reg_list li {
    list-style-type: none;
    width: 100%;
}

#class_name {
    display: inline-block;
    text-align: center;
    color: #4949e8d0;
    height: 40px;
    font-size: 25px;
    width: 50%;
    padding-top: 2px;
    margin-left: 0;
    border-bottom: 3px solid;
    border-radius: 2px;
    border-color: #4949e8d0;
}
#reg_btn {
    width: 40%;
}
#select_btn {
    width: 40%;
    margin-left:5px;
}
</style>
