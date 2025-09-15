<template>
    <div class="container">
        <div>
            <div class="content-title">图片数据上传</div>
            <div class="plugins-tips">
                <!--      <a href="https://element-plus.org/zh-CN/component/upload.html" target="_blank">Element Plus Upload</a>-->
                <p style="line-height: 20px">
                    建议上传的图片格式为JPG & PNG
                </p>
            </div>

            <el-upload class="upload-demo" drag :limit="1" :show-file-list="true"
                action="http://127.0.0.1:5000/process_image" v-loading.fullscreen.lock="fullscreenLoading" multiple
                :on-success="dealimage" :on-error="uploadFileError" @change="handleUploadChanged">

                <!--   action是将图片file文件直接上传到后端服务器上，要想将图片附带的数据信息上传必须要实现额外函数 -->
                <el-icon class="el-icon--upload"><upload-filled /></el-icon>
                <div class="el-upload__text">
                    将图片拖到此处，或
                    <em>点击上传</em>
                </div>
            </el-upload>

            <div>
                <!-- <div class="content-title">检测结果</div> -->
                <video id="videoElement" controls ref="videoPlayer" v-show="videoValue !== null">
                    <!-- 使用Base64字符串作为数据源 -->
                    <source :src="videoValue" type="video/mp4">
                </video>

            </div>
        </div>
        <el-radio-group v-model="radio" @change="updateRadioValue">  
            <el-radio :value="3">微笑眨眼</el-radio>  
            <el-radio :value="6">困惑</el-radio>  
            <el-radio :value="9">点头</el-radio>  
            <el-radio :value="12">摇头</el-radio>  
    </el-radio-group>  
    <div>
    <el-button type="primary" @click="sendToBackend">提交</el-button>
    </div>
    </div>
</template>


<script lang="ts" setup>
import { ref, reactive, computed, watch } from 'vue';
import { ElMessage, ElMessageBox } from 'element-plus';
import { Delete, Edit, Search, Plus } from '@element-plus/icons-vue';
import axios from "axios";
import { defineComponent} from 'vue';  
const radio = ref(3)


const query = reactive({
    curPage: 1,
    pageSize: 10,
    tableName: "file",
    keyword: ""
});

const videoValue = ref(null)



const pageTotal = ref(0);
const fullscreenLoading = ref(false)
const openFullScreen1 = () => {
    fullscreenLoading.value = false
    // setTimeout(() => {
    //   fullscreenLoading.value = false
    // }, 2000)
}
const url = ref('../src\\assets\\img\\null.png')
const srcList = [
    "http://localhost:5000/img/10045_1710698433.png", ""
]
const handleUploadChanged = (fileList) =>{
    
}

const videoPlayer = ref(null);
watch(videoValue, (newValue, oldValue) => {
    if (newValue !== oldValue) {
        // 视频源发生变化时重新加载视频
        videoPlayer.value.load()
    }
});


// 本地文件上传相关操作
const dealimage = (response: any, file: any, filelist: any) => {
    console.log(response)
    console.log(response.result_base64)
    videoValue.value = response.result_base64
    


};
const uploadFileError = (err: any, file: any, fileList: any) => {
    console.log("上传失败")
}



const radioValue = ref<number | null>(null); // 使用ref来定义响应式数据  
    const updateRadioValue = () => {
        radioValue.value = radio.value;
    };
    const sendToBackend = async () => {  
        console.log("value:",radioValue.value)
      if (radioValue.value !== null) { // 确保有一个值被选中  
        try {  
        const response = await axios.post('http://127.0.0.1:5000/value', {  
            selectedValue: radioValue.value, // 将选中的值发送到后端  
        });  
          // 处理响应...
        console.log("发送成功")  
        console.log(response.data);  
        } catch (error) {  
          // 处理错误...  
            console.error(error);  
        }  
    } else {  
        console.log('请先选择一个选项！');  
    }  
};  

</script>

<style scoped>
.content-title {
    font-weight: 400;
    line-height: 50px;
    margin: 10px 0;
    font-size: 22px;
    color: #1f2f3d;
}

.upload-demo {
    width: 360px;
}

.handle-box {
    margin-bottom: 20px;
}

.handle-select {
    width: 120px;
}

.handle-input {
    width: 300px;
}

.table {
    width: 100%;
    font-size: 14px;
}

.red {
    color: #F56C6C;
}

.mr10 {
    margin-right: 10px;
}

.table-td-thumb {
    display: block;
    margin: auto;
    width: 40px;
    height: 40px;
}
</style>