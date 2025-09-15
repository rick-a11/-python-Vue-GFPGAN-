// import mysql from 'mysql';  

// const poolConfig = {  
    // host: '127.0.0.1',  
    // user: 'root',  
    // password: '518518xhl',  
    // database: 'gan'  
// };  

// const db = mysql.createPool(poolConfig);  

// export default db;


// 1 引入
const mysql = require('mysql');
// 2 创建链接配置
const db = mysql.createPool({
    host: 'localhost',  
    user: 'root',  
    password: '1234',  
    database: 'su' 
})

// // 4 生成sql语句 增删改查操作
// let sql = 'SELECT * FROM user'
// //5  执行sql语句
// db.query(sql, (err, result) => {
//     if(err){
//         console.log("err:",err);
//         return
//     }
//     // 6 处理结果
//     console.log("result:",result)
// })

module.exports = db