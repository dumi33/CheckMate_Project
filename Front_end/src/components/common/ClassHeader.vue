<template>
    <div class="head">
        <header>
            <h2>Checkmate</h2>
            <ul class="menu">
                <li><router-link to='/login'>로그아웃</router-link></li>
                <li id="mypage">{{ name }}</li>
                <li id ="icon">
                <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" class="bi bi-person-circle" viewBox="0 0 16 16">
                    <path d="M11 6a3 3 0 1 1-6 0 3 3 0 0 1 6 0z"/>
                    <path fill-rule="evenodd" d="M0 8a8 8 0 1 1 16 0A8 8 0 0 1 0 8zm8-7a7 7 0 0 0-5.468 11.37C3.242 11.226 4.805 10 8 10s4.757 1.225 5.468 2.37A7 7 0 0 0 8 1z"/>
                </svg>
                </li>
            </ul>
        </header>
    </div> 
</template>
<script>
export default{
    name: 'HeaderName',
    data : function() {
        return {
            name: this.$store.state.loginStore.user_name
        };
    }
}
</script>

<style scoped>
  * {
    font-family: 'Noto Sans KR', sans-serif;
    margin: 0;
    }

    .head{
        background-color: #4949E8;
        width: 100%;
        list-style-type: none;
        margin: 0;
        padding: 0;
        display: inline-block;
    }

    .head h2 {
        color: white;
        text-align: center;
        font-weight: bold;
        float: left;
        display: inline;
        padding-left: 20px;
        padding: 10px;
    }

    .head li {
        float: right;
        display: inline;
        color: white;
        padding: 8px;
        font-size: 15px;
        padding-top:15px
    }

    .head a {
        display: block;
        text-decoration: none;
        color: white;
    }
</style>