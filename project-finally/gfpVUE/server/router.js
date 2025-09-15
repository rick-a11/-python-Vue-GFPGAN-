// import express from 'express';  
// import { login,register } from './API/login'; // 确保 login 模块正确导出函数  

// const router = express.Router();  

// router.get('/login', (req, res) => {  
//     // 调试代码，打印请求信息  
//     console.log('GET /login request received');  
//     login(req, res); // 调用 login 函数处理请求  
// });  

// router.post('/register', (req, res) => {  
//     // 调试代码，打印请求信息  
//     console.log('POST /register request received');  
//     register(req, res); // 调用 register 函数处理请求  
// });  

// export default router; // 使用 ES6 模块导出语法
let express = require('express')
let router = express.Router()
let login = require('./API/login')

router.post('/login', login.login)
router.post('/register', login.register)

module.exports = router