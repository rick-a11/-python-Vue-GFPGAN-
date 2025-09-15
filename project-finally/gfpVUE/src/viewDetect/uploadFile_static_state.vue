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
      <el-upload
          class="upload-demo"
          drag
          :limit="1"
          :show-file-list="true"
          action="http://localhost:5000/upload"
          v-loading.fullscreen.lock="fullscreenLoading"
          multiple
          :on-success="dealimage"
          :on-error="uploadFileError"
      >
        <!--   action是将图片file文件直接上传到后端服务器上，要想将图片附带的数据信息上传必须要实现额外函数 -->
        <el-icon class="el-icon--upload"><upload-filled /></el-icon>
        <div class="el-upload__text">
          将图片拖到此处，或
          <em>点击上传</em>
        </div>
      </el-upload>
      <div>
        <div class="content-title">检测结果</div>
        <div class="demo-image__preview">
          <el-image
                  style="width: 100px; height: 100px"
                  :src="url"
                  :zoom-rate="1.2"
                  :max-scale="7"
                  :min-scale="0.2"
                  :preview-src-list="srcList"
                  :initial-index="4"
                  fit="cover"
          />
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
import {ref, reactive, onMounted} from 'vue';
import { ElMessage, ElMessageBox } from 'element-plus';
import { Delete, Edit, Search, Plus } from '@element-plus/icons-vue';
import axios from "axios";
const query = reactive({
  curPage: 1,
  pageSize: 10,
  tableName: "file",
  keyword: ""
});
const pageTotal = ref(0);
const fullscreenLoading = ref(false)
const openFullScreen1 = () => {
  fullscreenLoading.value = false
  // setTimeout(() => {
  //   fullscreenLoading.value = false
  // }, 2000)
}
const url =ref('../src\\assets\\img\\null.png')
const srcList = [
"http://localhost:5000/img/10045_1710698433.png",""
]

onMounted(() => {
  // getNum()
})

// 本地文件上传相关操作
const dealimage = (response: any, file: any, filelist: any) => {
    console.log(response.path)
    fullscreenLoading.value = true
    axios.get(
        `/gfpgan`, {
            params: { input: response.path }
        }
    ).then(res=>{
      if(res.data.message == 'Face restoration completed'){
        console.log(1919810)
        fullscreenLoading.value = false
        url.value = res.data.output

        srcList[0] = res.data.output
        srcList[1] = res.data.input

      }
    })
};
const uploadFileError=(err:any, file:any, fileList:any)=>{
    console.log("上传失败")
}


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
