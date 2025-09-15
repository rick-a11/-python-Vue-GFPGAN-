<template>
	<div class="error-page">
		<div class="error-code">4<span>0</span>3</div>
		<div class="error-desc">啊哦~ 你没有权限访问该页面哦</div>
		<div class="error-handle">
			<router-link to="/">
				<el-button type="primary" size="large">返回首页</el-button>
			</router-link>
			<el-button class="error-btn" type="primary" size="large" @click="goBack">返回上一页</el-button>
		</div>
	</div>
</template>

<script setup lang="ts" name="403">
import { useRouter } from 'vue-router';

const router = useRouter();
const goBack = () => {
	router.go(-2);
};
</script>

<style scoped>
.error-page {
	display: flex;
	justify-content: center;
	align-items: center;
	flex-direction: column;
	width: 100%;
	height: 100%;
	background: #f3f3f3;
	box-sizing: border-box;
}
.error-code {
	line-height: 1;
	font-size: 250px;
	font-weight: bolder;
	color: #f02d2d;
}
.error-code span {
	color: #00a854;
}
.error-desc {
	font-size: 30px;
	color: #777;
}
.error-handle {
	margin-top: 30px;
	padding-bottom: 200px;
}
.error-btn {
	margin-left: 100px;
}
</style>
<!--这段代码是一个 Vue 组件，用于显示一个 403 错误页面。具体来说，它实现了以下功能：

页面布局：页面中央显示一个错误码（403），下面是一个描述性的文字（啊哦~ 你没有权限访问该页面哦）。

错误码样式：error-code 类的样式定义了错误码 403 的显示方式，其中数字 4 和 0 的颜色不同，分别使用了 #f02d2d 和 #00a854。

描述性文字样式：error-desc 类的样式定义了描述性文字的字体大小和颜色。

错误处理选项：页面底部提供了两个按钮供用户选择。

返回首页：使用 Vue Router 的 router-link 组件，用户点击此按钮会导航到应用的首页。
返回上一页：这是一个 el-button（可能是 Element UI 的按钮组件），当用户点击这个按钮时，会触发 goBack 方法，该方法会使浏览器返回两页（因为 router.go(-2)）。
样式与布局：整个页面使用了 Flexbox 布局，使得内容在垂直方向上居中显示。背景色是 #f3f3f3。

总的来说，这个组件为用户提供了一个友好的界面，告诉他们没有权限访问某个页面，并提供了两个选项让他们选择如何继续浏览应用。-->