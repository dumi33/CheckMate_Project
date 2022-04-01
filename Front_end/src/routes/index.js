// import Vue from 'vue'
import { createWebHistory, createRouter } from 'vue-router';
import ClassMain from '../components/ClassMain.vue'
import UserLogin from '../components/UserLogin.vue'
import UserRegister from '../components/UserRegister.vue'
import ClassRegister from '../components/ClassRegister.vue'
import ClassSetting from '../components/ClassSetting.vue'
import ClassList from '../components/ClassList.vue'

const router = new createRouter({
    history: createWebHistory(),
    routes:[
        {
            path:'/',
            name:ClassMain,
            component:ClassMain
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