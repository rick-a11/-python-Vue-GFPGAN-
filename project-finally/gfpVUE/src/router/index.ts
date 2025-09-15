import { createApp } from 'vue';  
import App from './App.vue';  
import VueRouter from 'vue-router';  
  



import { createRouter, createWebHashHistory, RouteRecordRaw } from 'vue-router';
import { usePermissStore } from '../store/permiss';
import Home from '../views/home.vue';


const routes: RouteRecordRaw[] = [
    {
        path: '/',
        redirect: '/login',
    },
    {
        path: '/home',
        name: 'Home',
        component: Home,
        children: [
            {
                path: '/upload',
                name: 'upload',
                meta: {
                    title: '上传插件',
                    permiss: '6',
                },
                component: () => import('../views/upload.vue'),
            },
            {
                path: '/icon',
                name: 'icon',
                meta: {
                    title: '自定义图标',
                    permiss: '10',
                },
                component: () => import( '../views/icon.vue'),
            },
            {
                path: '/user',
                name: 'user',
                meta: {
                    title: '个人中心',
                },
                component: () => import( '../views/user.vue'),
            },
            {
                path: '/uploadFile_static_state',
                name: 'uploadFile_static_state',
                meta: {
                    title: '图像修复处理',
                    permiss: '2',
                },
                component: () => import('../viewDetect/uploadFile_static_state.vue'),
            },
            {
                path: '/uploadFile_dynamic_state',
                name: 'uploadFile_dynamic_state',
                meta: {
                    title: '图像动态处理',
                    permiss: '2',
                },
                component: () => import('../viewDetect/uploadFile_Dynamic.vue'),
            },
        ],
    },
    {
        path: '/login',
        name: 'Login',
        meta: {
            title: '登录',
        },
        component: () => import('../views/login.vue'),
    },
    {
        path: '/403',
        name: '403',
        meta: {
            title: '没有权限',
        },
        component: () => import('../views/403.vue'),
    },
];

const router = createRouter({
    history: createWebHashHistory(),
    routes,
});



export default router;
