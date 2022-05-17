<template>
<div>
  <ClassHeader />
  <div class = "class_all">
    <div class ="class_list">
        <h2 style="cursor:default">{{className}}</h2>
        <div class="class_capture">
            <svg style="cursor:pointer" @click="PreviousImage()" xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="currentColor" class="bi bi-arrow-left-circle-fill" viewBox="0 0 16 16">
            <path d="M8 0a8 8 0 1 0 0 16A8 8 0 0 0 8 0zm3.5 7.5a.5.5 0 0 1 0 1H5.707l2.147 2.146a.5.5 0 0 1-.708.708l-3-3a.5.5 0 0 1 0-.708l3-3a.5.5 0 1 1 .708.708L5.707 7.5H11.5z"/>
            </svg>
            <svg style="cursor:pointer" @click="NextImage()" xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="currentColor" class="bi bi-arrow-right-circle-fill" viewBox="0 0 16 16">
            <path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0zM4.5 7.5a.5.5 0 0 0 0 1h5.793l-2.147 2.146a.5.5 0 0 0 .708.708l3-3a.5.5 0 0 0 0-.708l-3-3a.5.5 0 1 0-.708.708L10.293 7.5H4.5z"/>
            </svg>
            <button style="cursor:pointer" @click ="CaptureImage()" type = "button" id="capture_btn">캡처</button>
            <!-- <img src='https://cdn.boan24.com/news/photo/202009/12440_11770_3815.jpg' id="cap_img"> -->

        </div>
        <div class = "btn_a">
        <button style="cursor:pointer" type = "button" @click="CheckStd()" id="check_btn">출석확인</button>
        <button style="cursor:pointer" type = "button" @click="ClassHome()" id="home_btn">홈화면</button>
        </div>
    </div>
    <div class ="student_list">
        <div class = "check_std">
            <p style="cursor:default">출석 학생 리스트</p>
            <tr id = "check_db_list" v-for="(checkItem, index) in checkStdList" v-bind:key="index">
                <td>{{ checkItem }}</td>
            </tr>
        </div>
        <div class = "uncheck_std">
                <p style="cursor:default">결석 학생 리스트</p>
                <tr id = "uncheck_db_list" v-for="(uncheckItem, index) in uncheckStdList" v-bind:key="index">
                    <td>{{ uncheckItem }}</td>
                    <button type = "button" @click="StdCheck(uncheckItem.id)" id ="stdcheck_btn">관리</button>
                </tr>
        </div>
        <button style="cursor:pointer" type = "button" id="excel_btn" @click="downloadExcel()">EXCEL</button>
    </div>
  </div>
  </div>
</template>

<script>
    import ClassHeader from './common/ClassHeader.vue'
    import * as XLSX from 'xlsx'
    import axios from 'axios'

  export default {
    name: 'ClassRegister',
    data: function() {
      return {
        // img : require('/Users/namsujin/checkmate_frontend/CheckMate_Project/capture_img.png'),
        img : [],
        now_img : 0,
        StdList : [],
        checkStdList : [],
        uncheckStdList : [],
        className: this.$route.query.className
      };
    },
    components: {
      ClassHeader
    },
    methods: {
        // 화면 전체 캡처
        CaptureImage() {
            axios.post('http://localhost:8080/checks/').then((res)=> {
                console.log(res)
                this.img = res.data
            })
        },
        // 출석체크
        CheckStd() {
            axios.post('http://localhost:8080/checks/attendance/'+ this.$route.query.classIdx).then((res)=> {
                console.log(res.data)
                this.StdList = res.data
                this.checkStdList = res.data.출석
                this.uncheckStdList = res.data.미출석
            })
        },
        NextImage() {
            if(this.now_img < this.img.length){
                this.now_img = this.now_img + 1
            } else {
                this.now_img = 0
            }
        },PreviousImage() {
            if(this.now_img > this.img.length) {
                this.now_img = this.now_img - 1
            } else {
                this.now_img = this.img.length - 1
            }
        },
        // 출석체크 업데이트
        StdCheck(uncheckId) {
            var result = confirm("출석체크하시겠습니까?");
            if (result) {
                try {
                    axios.put("/class/list/" + uncheckId, uncheckId).then((res) => {
                        console.log(res.data.success);
                        if (res.data.success == true) {
                            alert("출석체크되었습니다.");
                            this.getStdList();
                        } else {
                            alert("출석체크되지 않았습니다.");
                        }
                    })
                } catch(err) {
                    console.log(err);
                    alert("수정되지 않았습니다.");
                }
            }
        },
        // 엑셀 파일
        downloadExcel() {
            var stdData = XLSX.utils.json_to_sheet(this.StdList);
            // var checkData = XLSX.utils.json_to_sheet(this.checkStdList); // this.items 는 json object 를 가지고있어야함 
            // var uncheckData = XLSX.utils.json_to_sheet(this.uncheckStdList);
            var workBook = XLSX.utils.book_new(); // 새 시트 생성 
            XLSX.utils.book_append_sheet(workBook, stdData, '출석'); // 시트 명명, 데이터 지정
            // XLSX.utils.book_append_sheet(workBook, uncheckData, '결석');
            XLSX.writeFile(workBook, 'check_list.xlsx');
        },
        ClassHome() {
          this.$router.push({path: '/classes', query : {user_id:this.$route.query.user_id}});
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

img {
    text-align: center;
    font-size: 25px;
    width: 90%;
    height: 500px;
    margin-left : 20px;
    height: 400px;
}

.class_list h2 {
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

.class_capture svg{
    color: white;
    margin-top: 20px;
    margin-left: 20px;
    display: inline-block;
    float: left;
}

#capture_btn {
    display: block;
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

#cap_img {
    display: block;

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
    display: block;
    margin: 10px;
    margin-left: 30px;
    font-size: 20px;
    font-weight: bold;
    font-family:'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Verdana, sans-serif;
}

#check_db_list {
    display: block;
    margin: 10px;
    margin-left: 60px;
    font-size: 15px;
}

.uncheck_std p {
    display: block;
    margin: 10px;
    margin-left: 30px;
    font-size: 20px;
    font-weight: bold;
    font-family:'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Verdana, sans-serif;
}

#uncheck_db_list {
    display: block;
    margin: 10px;
    margin-left: 60px;
    font-size: 15px;
}

#stdcheck_btn{
    display: inline-block;
    text-align: center;
    background:linear-gradient(to bottom, #4949e87c,#4949e8d0);
    color: white;
    height: 20px;
    border-radius: 5px;
    font-size: 15px;
    border-color: #ffffff7c;
}

</style>