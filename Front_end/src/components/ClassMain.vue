<template>
<div id="all">
  <ClassHeader />
    
    <img id="human2_img" src="../icons/human2.svg">
    <img id="human1_img" src="../icons/human1.png">
  <div class ="reg_class" >
    
    <p id="class_h" style="cursor:default">수업 등록</p>
    <svg style="cursor:pointer" @click="ClassRegister()" xmlns="http://www.w3.org/2000/svg" width="40" height="40" fill="currentColor" class="bi bi-plus-circle-fill" viewBox="0 0 16 16">
      <path d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zM8.5 4.5a.5.5 0 0 0-1 0v3h-3a.5.5 0 0 0 0 1h3v3a.5.5 0 0 0 1 0v-3h3a.5.5 0 0 0 0-1h-3v-3z"/>
    </svg>
    <span class="explain" style="cursor:default">
      <div class="sentence">
      <img id="point_img2" src="../icons/point.svg"> <p> 수업 등록 버튼을 클릭하여 본인의 수업을 등록하세요</p>
      </div>
      <div class="sentence">
      <img id="point_img2" src="../icons/point.svg"> <p> 수업을 클릭하여 출석체크 화면으로 이동하세요</p>
      </div>
      <div class="sentence">
      <img id="point_img2" src="../icons/point.svg"> <p> 수업 중인 화면을 캡처한 뒤, 출석체크 버튼을 클릭하여 출석체크를 완료하세요 </p>
      </div>
      <div class="sentence">
      <img id="point_img2" src="../icons/point.svg"> <p> 출석부를 확인하세요 </p>
      </div>
    </span>
  </div>
  <div class ="reg_list">
      <img id="search_bar_img" src="../icons/search_bar.svg">
      <img id="search_img" src="../icons/search.svg">
      <input v-model="search" type="text" placeholder="search">
      <div class ="list_name">
        <tr v-for="classItem in searchList" v-bind:key="classItem.classIdx" >
          <div v-if="classItem.status == 'active'" class = "class_list">
          <img id="point_img" src="../icons/point.svg">
          <td style="cursor:pointer" @click="ClassSelect(classItem)"  id ="class_name">{{classItem.className}}</td>
          <div class = "list_btn">
            <button style="cursor:pointer" type = "button" @click="ClassDelete(classItem)" id="delete_btn">삭제</button>
          </div>
        </div>
        </tr>
      </div>
  </div>
  </div>
</template>

<script>
  import axios from 'axios'
import ClassHeader from './common/ClassHeader.vue'
  export default {
    name: 'ClassMain',
    data : function(){
      return {
        classList : [],
        search: ''
      };
    },    
    components: {
      ClassHeader
    }, computed: {
      searchList() {
        if(this.search){
          return this.classList.filter((classItem) => {
            return classItem.name.match(this.search)
          })
        }
        else {
          return this.classList
        }
      }
    },
    methods: {
      //수업 리스트 출력
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
        // 수업 등록 페이지로 이동
        ClassRegister() {
          this.$router.push({path : '/classes/register', query : {user_id: this.$route.query.user_id}});
        },
        // 수업 선택 페이지로 이동
        ClassSelect(classItem) {
          this.$router.push({path: '/classes/list', query : {user_id: this.$route.query.user_id, classIdx : classItem.classIdx, className: classItem.className}});
        },
        // 수업 삭제
        ClassDelete(classItem) {
          let path = "http://localhost:8080/classes/"
          axios.patch(path + classItem.classIdx).then((res)=>{
            console.log(res);
            this.$router.go();
          }).catch((err) => {
            console.log(err);
          })
        }
    },mounted() {
      this.getClassList();
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

#human1_img{
  position: absolute;
  margin-top: 30px;
  width: 450px;
}

#human2_img {
  position: absolute;
  width: 350px;
  left: 370px;
  top: 350px;
}

.reg_class {
  position: absolute;
  left: 70px;
  top: 550px;
}

.reg_class #class_h {
  display: inline-block;
  color: white;
  margin: 0;
  font-size: 40px;
  margin-right: 10px;
  font-weight: bold;
  font-family:'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Verdana, sans-serif;
}

.reg_class .explain {
  display: block;
  margin: 0;
  margin-left: 20px;
  margin-top: 20px;
  font-size: 20px;
  color: white;
}

.reg_class svg {
  color: white;
  padding-top: 10px;
}

.reg_list {
  position: absolute;
  left: 750px;
  /* border: 4px solid;
  border-radius: 5px;
  border-color: white; */
}

#search_img{
  position: absolute;
  left:60px;
  top: 56px;
  width: 30px;
}



#search_bar_img{
  position: absolute;
  left: 50px;
  top: 50px;
  width: 250px;
  
}

.reg_list input{
  position: absolute;
  left: 100px;
  top: 60px;
  border: none;
  background: none;
  font-size: 20px;
  width: 170px;
}

#point_img{
  width: 35px;
}

.list_name {
  margin-top: 110px;
  margin-left: 50px;
  height: 450px;
  width: 600px;
  overflow: scroll
}

.list_name::-webkit-scrollbar {
  width: 10px;
}

.list_name::-webkit-scrollbar-thumb {
  background: white;
  height: 20%;
  border-radius: 7px;
}

.list_name::-webkit-scrollbar-track{
  background:none;
  
}

.class_list{
  margin-top: 20px;
}

.list_btn {
    display: inline-block;
    
}

.list_btn Button {
    display: inline-block;
    text-align: center;
    /* background:linear-gradient(to bottom, #4949e87c,#4949e8d0); */
    /* color: white; */
    background: white;
    color: #4949e8d0;
    font-weight: bold;
    height: 40px;
    border-radius: 5px;
    font-size: 25px;
    border-color: #ffffff7c;
}

#class_name {
  font-weight: bold;
  display: inline-block;
  color: white;
  height: 40px;
  font-size: 25px;
  width: 450px;
  margin-left: 5px;
}
#reg_btn {
  margin-left:5px;
}
#select_btn {
    margin-left:5px;
}
#delete_btn {
    margin-left:5px;
}

#point_img2{
  display: inline-block;
  width: 22px;
  margin-top: 10px;
}

.explain p{
  display: inline-block;
  margin: 0;
  margin-top: 10px;
}

.sentence{
  display: block;
}

</style>
