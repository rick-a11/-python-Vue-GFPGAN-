<template>
<div class="login-wrap">
	<div class="ms-login">
		<div class="ms-title">图像处理系统(BUPT)</div>
		<el-tabs stretch>
			<el-tab-pane label="登录" name="login">
				<el-form :model="Loginform" :rules="rules" ref="Loginform" label-width="0px" class="ms-content" status-icon>
			<el-form-item prop="username">
				<el-input v-model="Loginform.username" placeholder="username">
					<template #prepend>
						<el-button :icon="User"></el-button>
					</template>
				</el-input>
			</el-form-item>
			<el-form-item prop="password">
				<el-input
					type="password"
					placeholder="password"
					v-model="Loginform.password"
				>
					<template #prepend>
						<el-button :icon="Lock"></el-button>
					</template>
				</el-input>
			</el-form-item>
			<div class="login-btn">
				<el-button type="primary" @click='loginmethod'>登录</el-button>
				
			</div>
			<el-button type="primary" @click='youke'>游客登录</el-button>
		</el-form>
			</el-tab-pane>
			<el-tab-pane label="注册" name="register">
				<el-form :model="Registerform" :rules="rules" ref="Registerform" label-width="0px" class="ms-content" status-icon>
			<el-form-item prop="username">
				<el-input v-model="Registerform.username" placeholder="username">
					<template #prepend>
						<el-button :icon="User"></el-button>
					</template>
				</el-input>
			</el-form-item>
			<el-form-item prop="password">
				<el-input
					type="password"
					placeholder="password"
					v-model="Registerform.password"
				>
					<template #prepend>
						<el-button :icon="Lock"></el-button>
					</template>
				</el-input>
			</el-form-item>
			<el-form-item prop="confirmpassword">
				<el-input
					type="confirmpassword"
					placeholder="confirmpassword"
					v-model="Registerform.confirmpassword"
				>
					<template #prepend>
						<el-button :icon="Lock"></el-button>
					</template>
				</el-input>
			</el-form-item>
			<div class="login-btn">
				<el-button type="primary" @click='registermethod'>注册</el-button>
			</div>
		</el-form>
			</el-tab-pane>
		</el-tabs>
	</div>
</div>
</template>

<script>
// import { registerPlugin } from "wangeditor/dist/plugins";
// import { mapMutations } from "vuex"
// import api from "../api"
// import { ref, reactive } from 'vue';
// import { usePermissStore } from '../store/permiss';
// import { useRouter } from 'vue-router';
// import { ElMessage } from 'element-plus';
// import type { FormInstance, FormRules } from 'element-plus';
import { useTagsStore } from '../store/tags';
import { Lock, User } from '@element-plus/icons-vue';
import axios from 'axios';
import { useRouter } from 'vue-router';
import { usePermissStore } from '../store/permiss';
const tags = useTagsStore();
tags.clearTags();
export default {
setup() {  
    const router = useRouter();
	function toPage(){
		router.push("/home");
    }
    return {
		toPage
    }
}, 
data () {
return {
Loginform: {
	username: '',
	password: ''  
},
Registerform: {
	username: '',
	password: '',
	confirmpassword: '',
},
rules:{
username: [
	{
		required: true,
		message: '请输入用户名',
		trigger: 'blur'
	}
],
password: [{ required: true, message: '请输入密码', trigger: 'blur' }],
confirmpassword:[{required:true,message:'请再次输入密码',},{  
	validator: (rule, value, callback) => {  
	if (value === '') {  
		callback(new Error('请再次输入密码'));  
	} else if (value !== this.Registerform.password) { // 假设 this.password 是 password 字段的值  
		callback(new Error('两次输入的密码不一致，注册不成功'));  
	} else {  
		callback();  
	}  
	},  trigger:'blur'}]
},
Lock,
User,

};
},


methods: {
	async registermethod() {  
		try {  
			// 发送注册请求  
            axios.defaults.baseURL = "http://localhost:3000" 
			const response = await axios.post('/register', {  
			username: this.Registerform.username,  
			password: this.Registerform.password  
			});  
			console.log("response.data.status",response.data.status)
			// 根据响应状态处理结果  
			if (response.data.status === 200) {  
			alert('注册成功')
			axios.defaults.baseURL = "http://localhost:5000" 
			this.toPage();// 跳转到应用页面  
			} else if (response.data.status === 202) { 
				this.Registerform.username = '',  
				this.Registerform.password = '',
				this.Registerform.confirmpassword = ''
			alert('用户名已存在', '注册失败')
			} else if (response.data.status === 400) {  
			this.$message.error(response.data.message || '注册失败，请检查输入信息');  
			} else if (response.data.status === 500) {  
			this.$message.error(response.data.message || '数据库查找失败');  
			} else {  
			this.$message.error('未知错误，请稍后再试');  
			}  
		} catch (error) {  
			// 处理错误  
		if (error.response) {  
		// 请求已发出，服务器也响应了状态码，但是状态码不在 2xx 范围内  
		console.error('服务器返回错误', error.response.data);  
		this.$message.error('注册失败，请稍后再试');  
		} else if (error.request) {  
		// 请求已发出，但是没有收到任何响应  
		console.error('请求已发出，但未收到响应', error.request);  
		this.$message.error('网络错误，请检查您的网络连接');  
		} else {  
		// 在设置请求时触发了某些错误  
		console.error('请求设置错误', error.message);  
		this.$message.error('未知错误，请稍后再试');  
		}    
		}  
		},

async loginmethod() {
	try {  
			// 发送登录请求  
			axios.defaults.baseURL = "http://localhost:3000"
			const response = await axios.post('/login', {  
			username: this.Loginform.username,  
			password: this.Loginform.password  
			});  
			console.log("response.data.status",response.data.status)
			// 根据响应状态处理结果  
			if (response.data.status === 200) {  
			alert('登录成功')
			axios.defaults.baseURL = "http://localhost:5000" 
			// localStorage.setItem('ms_username', this.Loginform.username);
			// const keys = permiss.defaultList[this.Loginform.username == 'admin' ? 'admin' : 'user'];
			// permiss.handleSet(keys);
			// localStorage.setItem('ms_keys', JSON.stringify(keys));
			this.toPage();// 跳转到登录页面  
			} else if (response.data.status === 202) { 
				this.Loginform.password='',
				this.Loginform.username=''
			alert('用户名密码错误')
			} else if (response.data.status === 400) {  
			this.$message.error(response.data.message || '登录失败，请检查输入信息');  
			} else {  
			this.$message.error('未知错误，请稍后再试');  
			}  
		} catch (error) {  
			// 处理错误  
		if (error.response) {  
		// 请求已发出，服务器也响应了状态码，但是状态码不在 2xx 范围内  
		console.error('服务器返回错误', error.response.data);  
		this.$message.error('注册失败，请稍后再试');  
		} else if (error.request) {  
		// 请求已发出，但是没有收到任何响应  
		console.error('请求已发出，但未收到响应', error.request);  
		this.$message.error('网络错误，请检查您的网络连接');  
		} else {  
		// 在设置请求时触发了某些错误  
		console.error('请求设置错误', error.message);  
		this.$message.error('未知错误，请稍后再试');  
		}    
		}  
		},
async youke() {
	try {  
			// 发送登录请求  
			axios.defaults.baseURL = "http://localhost:3000"  
			const response = await axios.post('/login', {  
			username: '1',  
			password: '1'
			});  
			console.log("response.data.status",response.data.status)
			// 根据响应状态处理结果  
			if (response.data.status === 200) {  
			alert('登录成功')
			axios.defaults.baseURL = "http://localhost:5000"  
			const permiss = usePermissStore();
			localStorage.setItem('ms_username', this.Loginform.username);
			const keys = permiss.defaultList[this.Loginform.username];
			permiss.handleSet(keys);
			this.toPage();// 跳转到登录页面  
			} else if (response.data.status === 202) { 
				this.Loginform.password='',
				this.Loginform.username=''
			alert('用户名密码错误')
			} else if (response.data.status === 400) {  
			this.$message.error(response.data.message || '登录失败，请检查输入信息');  
			} else {  
			this.$message.error('未知错误，请稍后再试');  
			}  
		} catch (error) {  
			// 处理错误  
		if (error.response) {  
		// 请求已发出，服务器也响应了状态码，但是状态码不在 2xx 范围内  
		console.error('服务器返回错误', error.response.data);  
		this.$message.error('注册失败，请稍后再试');  
		} else if (error.request) {  
		// 请求已发出，但是没有收到任何响应  
		console.error('请求已发出，但未收到响应', error.request);  
		this.$message.error('网络错误，请检查您的网络连接');  
		} else {  
		// 在设置请求时触发了某些错误  
		console.error('请求设置错误', error.message);  
		this.$message.error('未知错误，请稍后再试');  
		}    
		}  
		},
	}
}
</script>











<style scoped>
.login-wrap {
position: relative;
width: 100%;
height: 100%;
background-image: url(../assets/img/bg.jpg);
background-size: 100%;
}
.ms-title {
width: 100%;
line-height: 50px;
text-align: center;
font-size: 20px;
color: #fff;
border-bottom: 1px solid #ddd;
}
.ms-login {
position: absolute;
left: 50%;
top: 50%;
width: 350px;
margin: -190px 0 0 -175px;
border-radius: 5px;
background: rgba(255, 255, 255, 0.3);
overflow: hidden;
}
.ms-content {
padding: 30px 30px;
}
.login-btn {
text-align: center;
}
.login-btn button {
width: 100%;
height: 36px;
margin-bottom: 10px;
}
.login-tips {
font-size: 12px;
line-height: 30px;
color: #fff;
}

</style>
