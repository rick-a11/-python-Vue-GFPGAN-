// import express from 'express';  
// import cors from 'cors';  
// import bodyParser from 'body-parser';  
// import router from './router'; // 确保您的 router 模块正确导出  

// const app = express();  

// // 配置解析，用于解析 json 和 urlencoded 格式的数据  
// app.use(bodyParser.json());  
// app.use(bodyParser.urlencoded({ extended: false }));  

// // 配置跨域  
// app.use(cors());  

// // 配置路由  
// app.use(router);  

// // 启动服务器并监听 80 端口  
// app.listen(3000, () => {  
//     console.log('服务器启动成功');  
// });
let express = require('express')
let app = express()
let cors = require('cors')
let bodyParser = require('body-parser')
let router = require('./router')


// 设置 CORS 响应头
app.use((req, res, next) => {
  res.header('Access-Control-Allow-Origin', '*');
  res.header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE');
  res.header('Access-Control-Allow-Headers', 'Content-Type, Authorization');
  next();
});


app.use(bodyParser.json());  //配置解析，用于解析json和urlencoded格式的数据
app.use(bodyParser.urlencoded({extended: false}));
app.use(cors())              //配置跨域
app.use(router)              //配置路由

app.listen(3000, () => {
    console.log('服务器启动成功');
})