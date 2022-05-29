<template>
    <div class ="black-bg">
        <div class="white-bg">
            <img src="../../assets/video-call.png">
            <h4>출석체크할 화면을 띄워주세요</h4>
            <p>학생들의 얼굴이 보이는 화면을 띄우신 뒤에</p>
            <p>아래의 캡처 버튼을 클릭하세요.</p>
            <button @click="ChildCaptureImage()">캡처</button>
        </div>
    </div>
</template>

<script>

export default {
    name: 'AlertModal',
    methods:{
        ChildCaptureImage(){
            localStorage.setItem('open', 'true')
            window.opener.parent.location.reload()
            window.close()
        }
    }
};

</script>


<style>
.black-bg {
    width:100%;
    height:100%;
    /* background: rgba(0, 0, 0, 0.5); */
    padding: 10px;
}

.white-bg{
    width: 100%;
    background: white;
    border-radius: 8px;
    text-align: center;
    padding: 20px;
}

.white-bg img{
    width: 70px;
}

.white-bg button{
    width: 100%;
    height: 30px;
    background:linear-gradient(to bottom, #4949e87c,#4949e8d0);
    color: white;
    border-radius: 5px;
    border: 0px;
    box-shadow: 2px 2px 2px #4949e87c;
    font-style: bold;
    font-size: 15px;
    font-family:'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
}

</style>