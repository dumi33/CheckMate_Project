<template>
<div>
  <ClassHeader />
  <div class ="set_class">
      <h2 style="cursor:default">{{className}}</h2>
      <svg style="cursor:pointer" @click="ClassMain()" xmlns="http://www.w3.org/2000/svg" width="35" height="35" fill="currentColor" class="bi bi-house-heart-fill" viewBox="0 0 16 16">
        <path fill-rule="evenodd" d="M8.707 1.5a1 1 0 0 0-1.414 0L.646 8.146a.5.5 0 0 0 .708.707L8 2.207l6.646 6.646a.5.5 0 0 0 .708-.707L13 5.793V2.5a.5.5 0 0 0-.5-.5h-1a.5.5 0 0 0-.5.5v1.293L8.707 1.5Z"/>
        <path fill-rule="evenodd" d="m8 3.293 6 6V13.5a1.5 1.5 0 0 1-1.5 1.5h-9A1.5 1.5 0 0 1 2 13.5V9.293l6-6Zm0 5.189c1.664-1.673 5.825 1.254 0 5.018-5.825-3.764-1.664-6.691 0-5.018Z"/>
      </svg>
  </div>
  <div class ="get_student">
    <p style="cursor:default">학생 출결 현황</p>
    <table id = "std_list" border ="1" >
      <tr align="center" bgcolor="white">
        <th></th>
        <th v-for="(value, key) in uncheckstds" v-bind:key="key">
          {{key}}
        </th>
      </tr>
      <tr v-for="stdlist in stdlists" v-bind:key="stdlist.studentIdx">
        <td>{{stdlist.name}}</td>
        <td v-for="(value, key) in uncheckstds" v-bind:key="key">
          <span v-for="(v, k) in value" v-bind:key="k">
            <span v-if="stdlist.name == v">
              <p>x</p>
            </span>
          </span>
        </td>
      </tr>
    </table>
  </div>
  <div class ="check_list">
      <p style="cursor:default" id = "check_header">결석 학생 리스트</p>
    <table id = "check_list" border ="1">
      <tr align="center" bgcolor="white">
        <th>날짜</th>
        <th>결석한 학생</th>
      </tr>
      <tr v-for="(value, key) in uncheckstds" v-bind:key="key">
        <td>{{key}}</td>
        <td>
        <ul v-for="(v, k) in value" v-bind:key="k">
          <li>{{v}}</li>
        </ul>
        </td>
      </tr>
  </table>
  </div>
  </div>
</template>

<script>
  import ClassHeader from './common/ClassHeader.vue'
  import axios from 'axios'
  export default {
    name: 'CheckList',
    data : function() {
      return {
        className : this.$route.query.className,
        stdlists : [],
        checkstds : [],
        uncheckstds: [],
        checkstatus: true
      }
    },
    components: {
      ClassHeader
    }, methods: {
      //학생 리스트 출력
        GetStudent() {
            axios.get('http://localhost:8080/students/'+ this.$route.query.classIdx).then((res)=> {
                this.stdlists = res.data
                console.log(this.stdlists)
            })
        },
      //학생 출석 리스트 출력
        GetCheckList() {
            axios.get('http://localhost:8080/checks/attendance/'+ this.$route.query.classIdx).then((res)=> {
                this.uncheckstds = res.data[0]
                console.log(this.uncheckstds)
            })
        },
        ClassMain() {
          this.$router.push({path: '/classes', query : {user_id:this.$route.query.user_id}});
        }
    }, mounted() {
      this.GetStudent();
      this.GetCheckList();
    }
  }
</script>

<style scoped>

.set_class {
    margin: 30px;
    margin-bottom:10px;
    width:60%;
}

.set_class h2 {
  border: 5px dotted #4949E8  ;
  border-color: #7171e09a;
  color:#4949E8;
  margin-top: 30px;
  margin-left: 50px;
  margin-bottom: 20px;
  text-align: center;
  padding-top:4px;
  width: 40%;
  font-size: 35px;
  display: inline-block;
}

.set_class svg {
  margin-left: 20px;
  color:#4949E8;
}

.get_student {
    border: 4px solid;
    border-radius: 5px;
    border-color: #7171e09a;
    margin-left: 30px;
    margin-right: 30px;
    margin-top: 10px;
    margin-bottom: 30px;
    display: block;
    width: 60%;
}

.get_student p {
    display: inline-block;
    margin: 10px;
    margin-left: 30px;
    font-size: 27px;
    font-weight: bold;
    font-family:'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Verdana, sans-serif;
}


.check_list {
  display: block;
  border: 4px solid;
  border-radius: 5px;
  border-color: #7171e09a;
  margin-left: 30px;
  margin-right: 30px;
  margin-top: 10px;
  width: 40%;
}

.check_list p {
    display: inline-block;
    margin: 10px;
    margin-left: 30px;
    font-size: 27px;
    font-weight: bold;
    font-family:'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Verdana, sans-serif;
}

.check_list ul {
  list-style-type: none;
  float:left;
}

#check_header {
    display: inline-block;
    margin: 10px;
    margin-left: 30px;
    font-size: 27px;
    font-family:'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Verdana, sans-serif;
}

#std_list {
  display: block;
  border-radius: 5px;
  border-color: #7171e09a;
  margin-left: 30px;
  margin-right: 30px;
  margin-bottom: 10px;
}

#check_list {
  display: block;
  border-radius: 5px;
  border-color: #7171e09a;
  margin-left: 30px;
  margin-right: 30px;
  margin-bottom: 10px;
}

</style>