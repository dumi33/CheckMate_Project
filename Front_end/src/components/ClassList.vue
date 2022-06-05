<template>
<div id="all">
  <ClassHeader/>
  <div class = "class_all">
    <div class ="class_list">
        <div class="title_list">
        <h2 style="cursor:default">{{className}}</h2>
        <svg id = "home_btn" style="cursor:pointer" @click="ClassHome()" xmlns="http://www.w3.org/2000/svg" width="50" height="50" fill="currentColor" class="bi bi-house-heart-fill" viewBox="0 0 16 16">
            <path fill-rule="evenodd" d="M8.707 1.5a1 1 0 0 0-1.414 0L.646 8.146a.5.5 0 0 0 .708.707L8 2.207l6.646 6.646a.5.5 0 0 0 .708-.707L13 5.793V2.5a.5.5 0 0 0-.5-.5h-1a.5.5 0 0 0-.5.5v1.293L8.707 1.5Z"/>
            <path fill-rule="evenodd" d="m8 3.293 6 6V13.5a1.5 1.5 0 0 1-1.5 1.5h-9A1.5 1.5 0 0 1 2 13.5V9.293l6-6Zm0 5.189c1.664-1.673 5.825 1.254 0 5.018-5.825-3.764-1.664-6.691 0-5.018Z"/>
      </svg>
      </div>
        <div class="class_capture">
            <svg style="cursor:pointer" @click="PreviousImage()" xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="currentColor" class="bi bi-arrow-left-circle-fill" viewBox="0 0 16 16">
            <path d="M8 0a8 8 0 1 0 0 16A8 8 0 0 0 8 0zm3.5 7.5a.5.5 0 0 1 0 1H5.707l2.147 2.146a.5.5 0 0 1-.708.708l-3-3a.5.5 0 0 1 0-.708l3-3a.5.5 0 1 1 .708.708L5.707 7.5H11.5z"/>
            </svg>
            <svg style="cursor:pointer" @click="NextImage()" xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="currentColor" class="bi bi-arrow-right-circle-fill" viewBox="0 0 16 16">
            <path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0zM4.5 7.5a.5.5 0 0 0 0 1h5.793l-2.147 2.146a.5.5 0 0 0 .708.708l3-3a.5.5 0 0 0 0-.708l-3-3a.5.5 0 1 0-.708.708L10.293 7.5H4.5z"/>
            </svg>
            <button style="cursor:pointer" @click ="openPopup()" type = "button" id="capture_btn">캡처</button>
            <img v-if ="capStatus" :src='`${capture_img[now_img]}`' />
        </div>
        <div class = "btn_a">
        <button style="cursor:pointer" type = "button" @click="CheckStd()" id="check_btn">출석확인</button>
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
                    <button type = "button" @click="StdCheck(uncheckItem.id)" id ="stdcheck_btn">추가</button>
                </tr>
        </div>
    </div>
  </div>

</div>
</template>


<script>

    import ClassHeader from './common/ClassHeader_color.vue'
    import axios from 'axios'


  export default {
    name: 'ClassRegister',
    data: function() {
        return {
        capture_img : [],
        now_img : 0,
        StdList : [],
        checkStdList : [],
        uncheckStdList : [],
        capture_num: 0,
        className: this.$route.query.className,
        capStatus: false,
        open: localStorage.getItem('open')
      };
    },
    components: {
      ClassHeader
    },
    methods: {
        // 화면 전체 캡처
        openPopup(){
            this.popup = window.open('/newAlter',
            'Window Capture',
            "left=2000, top=50, width=350, height=300"
            )
            localStorage.setItem('open', 'false')
            this.open = localStorage.getItem('open')
        },
        async GetCaptureImage(){
            await axios.get('http://localhost:8080/checks/img/' +  this.$route.query.classIdx).then((res)=>{
                console.log(res.data)
                this.capture_img = res.data.img_url
                this.capture_img.length = res.data.img_url.length
            })
            console.log('img: ', this.capture_img)
            localStorage.setItem('open','false')
            this.open = localStorage.getItem('open')
        },
        CaptureImage() {
            if(this.open == 'true') {
                this.capStatus = true
                axios.post('http://localhost:8080/checks/'+ this.$route.query.classIdx).then((res)=> {
                    console.log(res)
                })
                this.GetCaptureImage()
            }
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
            console.log('next')
            if(this.now_img < this.capture_img.length - 1){
                this.now_img = this.now_img + 1
            } 
            else {
                this.now_img = 0
            }
            console.log(this.now_img, this.capture_img[this.now_img])
            console.log(this.capture_img.length)
        },PreviousImage() {
            console.log('previous')
            if(this.now_img <= 0) {
                this.now_img = this.capture_img.length - 1
            } else if (this.capture_img.length == 0 ) {
                this.now_img = 0
            } else {
                this.now_img = this.now_img - 1
            }
            console.log(this.now_img, this.capture_img[this.now_img])
            console.log(this.capture_img.length)
        },
        // 출석체크 업데이트
        StdCheck(uncheckId) {
            var result = confirm("출석체크하시겠습니까?");
            if (result) {
                try {
                    axios.put("/classes/list/" + uncheckId, uncheckId).then((res) => {
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
        ClassHome() {
            localStorage.setItem('open','false')
            this.$router.push({path: '/classes', query : {user_id:this.$route.query.user_id}});
        }
    }, mounted() {
        this.CaptureImage(),
        window.addEventListener('keypress', (e) => {
            if(e.key === 37)
                this.PreviousImage()
            else if (e.key === 39)
                this.NextImage()
        })
    },created() {
        this.open = localStorage.getItem('open')
        
    }
}
</script>

<style scoped>

#all {
    width: 100%;
  height: 100vh;
    background: linear-gradient(180deg, 
    rgba(208, 62, 221, 0.47) 0.01%, 
    rgba(255, 255, 255, 0.616062) 68.75%, 
    rgba(255, 255, 255, 0.47) 100%);
}

img {
    text-align: center;
    font-size: 25px;
    width: 90%;
    height: 500px;
    margin-left : 20px;
    height: 400px;
}

.title_list {
    position: absolute;
    top:150px;
    left:40px;
    height: 300px;
}

.class_list h2 {
    writing-mode: tb-rl;
    color:#4949E8;
    text-align: center;
    font-size: 45px;
}

#home_btn {
    margin-left: 50px;
    margin-top: 10px;
    color: #4949E8;
}

.class_capture {
    position: absolute;
    top:120px;
    left:160px;
    border-radius: 5px;
    border-top: none;
    border-left: none;
    border-right: none;
    background-color: #4949E8;
    margin-left : 50px;
    text-align: center;
    font-size: 25px;
    width: 800px;
    height: 600px;
}

.class_capture img{
    width: 750px;
    margin-top: 10px;
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
    position: absolute;
    top: 730px;
    left: 520px;
    display: inline-block;
    background:linear-gradient(to bottom, #4949e87c,#4949e8d0);
    color: white;
    height: 50px;
    width: 200px;
    border-radius: 5px;
    font-size: 25px;
    border-color: #ffffff7c;  
}



.check_std{
    position: absolute;
    top:100px;
    left:1030px;
    border: 4px solid;
    border-radius: 5px;
    border-color: #6262da;
    margin-top:30px;
    margin-left:10px;
    margin-right:20px;
    margin-bottom:20px;
}

.uncheck_std{
    position: absolute;
    top:100px;
    left:1250px;
    border: 4px solid;
    border-radius: 5px;
    border-color: #6262da;
    margin-top:30px;
    margin-left:10px;
    margin-right:20px;
    margin-bottom:20px;
}

.check_std p {
    display: block;
    margin: 10px;
    width: 180px;
    font-size: 20px;
    font-weight: bold;
    font-family:'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Verdana, sans-serif;
}

#check_db_list {
    display: block;
    margin: 20px;
    margin-top: 18px;
    font-size: 15px;
}

.uncheck_std p {
    display: block;
    margin: 10px;
    font-size: 20px;
    width: 200px;
    font-weight: bold;
    font-family:'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Verdana, sans-serif;
}

#uncheck_db_list {
    display: block;
    margin: 20px;
    margin-top: 20px;
    font-size: 18px;
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