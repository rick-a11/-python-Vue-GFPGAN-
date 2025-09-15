
// import express, { Request, Response } from 'express';  
// import db from '../db/index'; // 假设你的数据库连接池对象从这里导入  
// import { dataColorPaletteTask } from 'echarts/types/src/visual/style.js';

// // 定义查询结果的类型  
// interface User {  
// // 这里添加你的用户字段，比如 id, username, password 等  
// id: number;  
// username: string;  
// password: string;  
// // ... 其他字段  
// }  

// // 定义 login 函数  
// export const login = (req: Request, res: Response) => {  
// const sql = 'SELECT * FROM user WHERE username = ? AND password = ?';  
// db.query(sql, [req.query.username, req.query.password], (err, data: User[]) => {  
// if (err) {  
//     return res.status(400).send({  
//     status: 400,  
//     message: "登录失败"  
//     });  
// }  
    
// if (data.length > 0) {  
//     res.status(200).send({  
//     status: 200,  
//     message: "登录成功"  
//     });  
// } else {  
//     res.status(202).send({  
//     status: 202,  
//     message: '用户名或密码错误'  
//     });  
// }  
// });  
// };

// // 定义请求体的类型  
// interface Register {  
//   params: {  
//     username: string;  
//     password: string;  
//   };  
// }  
  
// // 定义注册函数  
// export const register = async (req: Request<{}, {}, Register>, res: Response) => {  
//   try {  
//     const { username, password } = req.body.params;  

//     const sql1 = 'SELECT * FROM user WHERE username = ?';  
//     db.query(sql1, [username],(err ,data: User[])=>{
//         if (data.length > 0) {  
//             return res.status(202).send({  
//               status: 202,  
//               message: '用户名已存在'  
//             });  
//           } else {  
//             const sql2 = 'INSERT INTO user (username, password) VALUES (?, ?)';  
//             db.query(sql2, [username, password]); // 注意：这里应该使用加密后的密码  
//             return res.status(200).send({  
//               status: 200,  
//               message: "注册成功"  
//             });  
//           }  
//     });  
      
    
//   } catch (err) {  
//     console.error(err); // 在生产环境中，你可能想要记录错误而不是输出到控制台  
//     return res.status(500).send({  
//       status: 500,  
//       message: "服务器内部错误，注册失败"  
//     });  
//   }  
// };
let db = require('../db/index')
let mysql = require('mysql')
let express = require('express')

exports.login = (req, res) => {
  var sql = 'SELECT * FROM suer WHERE username = ? AND password = ?';
  console.log("req.query.username:",req.body.username,req.body.password)
  db.query(sql, [req.body.username, req.body.password], (err, result) => {
    console.log("result.length:",result.length)
      if(err) {
          return res.send({
            status: 400,
            message: "登录失败"
          })
      }
      if(result.length === 1) {
        res.send({
          status: 200,
          message: "登录成功"
        })
      }else{
        res.send({
          status: 202,
          message: '用户名或密码错误'
        })
      }
  })
}

exports.register = (req, res) => {
  const sql1 = 'SELECT * FROM suer WHERE username = ?;'
  const sql2 = 'insert into suer (username, password) value (?, ?)'
  db.query(sql1, [req.body.username], (err, result) => {
    console.log("result:",result)
    if(err) {
      return res.send({
        status: 500,
        message: "操作失败"
      })
    }
    if(result.length > 0) {
      return res.send({
        status: 202,
        message: '用户名已存在'
      })
    }else{
      // return res.send({
      //   status: 200,
      //   message: '注册成功'
      // })
      db.query(sql2, [req.body.username, req.body.password], (err, result) => {
        if(err) {
            return res.send({
              status: 400,
              message: "注册失败"
            })
        }
        res.send({
          status: 200,
          message: "注册成功"
        })
      })
    }
  })
}