<template>
<div>
  <ClassHeader />
  <div class = "class_all">
    <div class ="class_list">
        <h2>{{className}}</h2>
        <div class="class_capture">
            <button @click ="CaptureImage()" type = "button" id="capture_btn">캡처</button>
            <img id = "cap_img" src = this.img>
        </div>
        <div class = "btn_a">
        <button type = "button" @click="CheckStd()" id="check_btn">출석확인</button>
        <button type = "button" @click="ClassHome()" id="home_btn">홈화면</button>
        </div>
    </div>
    <div class ="student_list">
        <div class = "check_std">
            <p>출석 학생 리스트</p>
            <tr id = "check_db_list" v-for="checkItem in checkStdList" v-bind:key="checkItem.id">
                <td>{{ checkItem.name }}</td>
            </tr>
        </div>
        <div class = "uncheck_std">
                <p>결석 학생 리스트</p>
                <tr id = "uncheck_db_list" v-for="uncheckItem in uncheckStdList" v-bind:key="uncheckItem.id">
                    <td>{{ uncheckItem.name }}</td>
                    <button type = "button" @click="StdCheck(uncheckItem.id)" id ="stdcheck_btn">관리</button>
                </tr>
        </div>
        <button type = "button" id="excel_btn" @click="downloadExcel()">EXCEL</button>
    </div>
  </div>
</div>
</template>

<script>
    import ClassHeader from './common/ClassHeader.vue'
    import XLSX from 'xlsx';

  export default {
    name: 'ClassRegister',
    data: function() {
      return {
        img : '',
        StdList : [],
        checkStdList : [],
        uncheckStdList : [],
        className:''
      };
    },
    components: {
      ClassHeader
    },
    methods: {
        getStdList() {
          // Http get 메서드로 요청
            this.axios.get('/class/list/' + this.$router.query.classId, {params: {userid : this.$router.query.classId}}).then((res)=>{
            console.log(res);
            this.className = res.data.className
            this.checkStdList = res.data.CheckStd
            this.uncheckStdList = res.data.uncheckStd
          }).catch((err) => {
            console.log(err);
            });
        },
        CaptureImage() {
            // import pyautogui from pyautogui  

            // html2canvas(document.body).then(canvas => {
            //     document.body.appendChild(canvas);
            // });
            // html2canvas(document.body).then(canvas => {
            //     const link = document.createElement('a')
            //     link.download = 'filename'
            //     link.href = canvas.toDataURL()
            //     document.body.appendChild(link)
            //     link.click()
            // });
        },
        CheckStd() {
            this.axios.post("/class/list",{img: this.img, classId: this.$router.query.classId} ).then((res)=>{
                console.log(res);
                this.checkStdList = res.data.CheckStd
                this.uncheckStdList = res.data.uncheckStd
            }).catch((err) => {
                console.log(err);
            });
        },
        async StdCheck(uncheckId) {
            var result = confirm("출석체크하시겠습니까?");
            if (result) {
                try {
                    this.axios.put("/class/list/" + uncheckId, uncheckId).then((res) => {
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
        downloadExcel() {
            var checkData = XLSX.utils.json_to_sheet(this.checkStdList); // this.items 는 json object 를 가지고있어야함 
            var uncheckData = XLSX.utils.json_to_sheet(this.uncheckStdList);
            var workBook = XLSX.utils.book_new(); // 새 시트 생성 
            XLSX.utils.book_append_sheet(workBook, checkData, '출석'); // 시트 명명, 데이터 지정
            XLSX.utils.book_append_sheet(workBook, uncheckData, '결석');
            XLSX.writeFile(workBook, 'check_list.xlsx');
        },
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