// import Vue from 'vue'
import { createWebHistory, createRouter } from 'vue-router';
import ClassMain from '../components/ClassMain.vue'
import UserLogin from '../components/UserLogin.vue'
import UserRegister from '../components/UserRegister.vue'
import ClassRegister from '../components/ClassRegister.vue'
import ClassSetting from '../components/ClassSetting.vue'
import ClassList from '../components/ClassList.vue'
// import store from '../store';

const router = new createRouter({
    history: createWebHistory(),
    base: process.env.BASE_URL,
    routes:[
        {
            path:'/',
            name:ClassMain,
            component:ClassMain,
            // 로그인 여부 확인 
            // beforeEnter: (to, from, next) => {
            //     const isLogin = store.getters['loginStore/isLogin'];
            //     //로그인이 되지 않은 경우, /login으로 이동
            //     // 로그인시에 /로 이동
            //     if(!isLogin) {
            //         next('/login?returnUrl='+to.fullPath);
            //     }else {
            //         next();
            //     }
            // }
        },
        {
            path:'/login',
            name:UserLogin,
            component:UserLogin
        },{
            path:'/register',
            name:UserRegister,
            component:UserRegister
        },{
            path:'/class/register',
            name:ClassRegister,
            component:ClassRegister
        },{
            path:'/class/setting',
            name:ClassSetting,
            component:ClassSetting
        },{
            path:'/class/list',
            name:ClassList,
            component:ClassList
        }
    ]
})

export default router;