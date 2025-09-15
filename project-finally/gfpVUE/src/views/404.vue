<template>
	<div class="error-page">
		<div class="error-code">4<span>0</span>4</div>
		<div class="error-desc">啊哦~ 你所访问的页面不存在</div>
		<div class="error-handle">
			<router-link to="/">
				<el-button type="primary" size="large">返回首页</el-button>
			</router-link>
			<el-button class="error-btn" type="primary" size="large" @click="goBack">返回上一页</el-button>
		</div>
	</div>
</template>

<script setup lang="ts" name="404">
import { useRouter } from 'vue-router';

const router = useRouter();
const goBack = () => {
	router.go(-1);
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
	color: #2d8cf0;
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
<!--这段代码是一个 Vue 组件，用于显示一个 404 错误页面。具体来说，它实现了以下功能：

页面布局与样式：页面中央显示一个错误码（404），下面是一个描述性的文字（啊哦~ 你所访问的页面不存在）。错误码和描述性文字都有特定的样式，例如字体大小、颜色等。整个页面使用了 Flexbox 布局，使内容在垂直方向上居中显示，并且背景色为 #f3f3f3。

错误处理选项：页面底部提供了两个按钮供用户选择。

返回首页：这是一个 router-link 组件，当用户点击此按钮时，他们会导航到应用的首页。
返回上一页：这是一个 el-button（可能是 Element UI 的按钮组件），用户点击这个按钮时，会触发 goBack 方法。在 goBack 方法中，使用了 Vue Router 的 router.go(-1)，这意味着浏览器会返回到上一个页面。
脚本部分：组件的 <script> 部分导入了 Vue Router 的 useRouter 函数，用于获取当前的路由实例。通过 useRouter，组件能够调用 router.go(-1) 来控制浏览器的导航。

样式隔离：使用 <style scoped> 确保了这些样式只应用于这个组件，不会影响其他组件。

综上所述，这个 Vue 组件为用户提供了一个友好的界面，告诉他们所访问的页面不存在，并提供了两个选项让他们选择如何继续浏览应用。这是 Web 开发中常见的做法，特别是在单页应用（SPA）中，当路由导航到一个不存在的页面时，通常会显示这样的错误页面。-->