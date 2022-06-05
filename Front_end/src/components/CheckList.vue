<template>
<div id="all">
  <ClassHeader />
  <div class ="set_class">
      <h2 style="cursor:default">{{className}}</h2>
      <hr>
  </div>
  <div class ="get_student">
    <p style="cursor:default">학생 출결 현황</p>
    <button style="cursor:pointer" type = "button" id="excel_btn" @click="DownloadCheckExcel()">EXCEL</button>
    <table id = "std_list" >
      <tr align="center" >
        <th>학생</th>
        <th v-for="(value, key) in uncheckstds" v-bind:key="key">
          {{key}}
        </th>
      </tr>
      <tr v-for="stdlist in stdlists" v-bind:key="stdlist.studentIdx">
        <td>{{stdlist.name}}</td>
        <td v-for="(value, key) in uncheckstds" v-bind:key="key">
          <span v-for="(v, k) in value" v-bind:key="k">
            <span v-if="stdlist.name == v">
              <span v-if="checkresult">
                <p>결석</p>
              </span>
            </span>
          </span>
        </td>
      </tr>
    </table>
  </div>
  <!-- <div class ="check_list">
      <p style="cursor:default" id = "check_header">결석 학생 리스트</p>
      <button style="cursor:pointer" type = "button" id="excel_btn" @click="DownloadUncheckExcel()">EXCEL</button>
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
  </div> -->
  </div>
</template>

<script>
  import ClassHeader from './common/ClassHeader_left.vue'
  import axios from 'axios'
  import * as XLSX from 'xlsx'
  export default {
    name: 'CheckList',
    data : function() {
      return {
        className : this.$route.query.className,
        stdlists : [],
        checkstds : [],
        uncheckstds: [],
        checkstatus: true,
        checkresult: false
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
                console.log("checklist", this.uncheckstds)
            })
            let i = 0
            for(i;i<this.uncheckstds.length;i++){
              console.log("list",this.uncheckstds[i])
            }
        },
        ClassMain() {
          this.$router.push({path: '/classes', query : {user_id:this.$route.query.user_id}});
        },DownloadCheckExcel() {
            var stdData = XLSX.utils.table_to_sheet(document.getElementById('std_list'));
            // var checkData = XLSX.utils.json_to_sheet(this.checkStdList); // this.items 는 json object 를 가지고있어야함 
            // var uncheckData = XLSX.utils.json_to_sheet(this.uncheckStdList);
            var workBook = XLSX.utils.book_new(); // 새 시트 생성 
            XLSX.utils.book_append_sheet(workBook, stdData, '학생출결현황'); // 시트 명명, 데이터 지정
            // XLSX.utils.book_append_sheet(workBook, uncheckData, '결석');
            XLSX.writeFile(workBook, '학생_출결_현황.xlsx');
        }, DownloadUncheckExcel() {
            var stdData = XLSX.utils.table_to_sheet(document.getElementById('check_list'));
            // var checkData = XLSX.utils.json_to_sheet(this.checkStdList); // this.items 는 json object 를 가지고있어야함 
            // var uncheckData = XLSX.utils.json_to_sheet(this.uncheckStdList);
            var workBook = XLSX.utils.book_new(); // 새 시트 생성 
            XLSX.utils.book_append_sheet(workBook, stdData, '결석학생리스트'); // 시트 명명, 데이터 지정
            // XLSX.utils.book_append_sheet(workBook, uncheckData, '결석');
            XLSX.writeFile(workBook, '결석_학생_리스트.xlsx');
        }, 
    }, mounted() {
      this.GetStudent();
      this.GetCheckList();
    }
  }
</script>

<style scoped>

#all {
  width: 100%;
  height: 100vh;
  background: linear-gradient(270.09deg, 
  #6161E0 35.85%, 
  rgba(104, 144, 247, 0.47) 80.26%, 
  rgba(255, 255, 255, 0.47) 90.93%);
}

.set_class {
  position: absolute;
  top:200px;
  left:50px;
  width: 300px;
}

.set_class h2 {
  color:#4949E8;
  text-align: left;
  font-size: 50px;
  margin: 0;
}

.set_class hr{
  border : 0px;
  border-top:3px solid #4949E8;
  margin-top: 0px;
  margin-left: 0;
  width: 40%;
}

.get_student {
  position: absolute;
  left:400px;
  top: 100px;
  margin-bottom: 30px;
  display: block;
}

.get_student p {
    display: inline-block;
    margin: 20px;
    color: white;
    margin-left: 100px;
    font-size: 30px;
    font-weight: bold;
    font-family:'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Verdana, sans-serif;
}

#std_list {
  display: block;
  border: 0;
  color:white;
  margin-left: 150px;
  width: 1000px;
  margin-top: 20px;
}

#std_list th{
  font-size: 20px;
  border-left: 1px solid white;
  padding: 5px;
}

#std_list td{
  font-size: 20px;
  border-top: 1px solid white;
  border-left: 1px solid white;
  padding: 5px;
  text-align: center;
}

#std_list td:first-child{
  border-left:none;
}

#std_list th:first-child{
  border-left:none;
}

#std_list p{
  font-size: 20px;
  text-align: center;
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



#check_list {
  display: block;
  border-radius: 5px;
  border-color: #7171e09a;
  margin-left: 30px;
  margin-right: 30px;
  margin-bottom: 10px;
}

#excel_btn {
    background:white;
    color: #4949E8;
    height: 30px;
    border-radius: 5px;
    font-size: 20px;
    font-weight: bold;
    border-color: #ffffff7c;
    margin-left: 10px;
    text-align: center;
}

</style>