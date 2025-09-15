from flask import Flask, request, jsonify, make_response
import os
import subprocess
from PIL import Image
import time
import uuid
from werkzeug.utils import secure_filename
from extension import db, cors
from inference_gfpgan2 import image_handle
app = Flask(__name__)
cors.init_app(app)  # 注册跨域请求伪造相关

# 获取当前文件的绝对路径
current_file_path = os.path.abspath(__file__)
print("current_file_path", current_file_path)
# 获取当前文件所在的目录
project_root_path = os.path.dirname(current_file_path)
print("current_dir", project_root_path)
UPLOAD_FOLDER = r'\static\images\uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
output_path = "custom_results"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['current_selectimage'] = os.path.join(project_root_path, output_path, "restored_imgs")
app.config['current_uploadimage'] = os.path.join(project_root_path, "uploads")

@app.route('/upload', methods=['POST'])
def upload_pic():
    print("进行上传")
    if 'file' not in request.files:
        return jsonify({'error': '没有文件部分'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': '没有选择文件'}), 400
    if file:

        filename = secure_filename(file.filename).split('.')[0] + "_" + str(int(time.time())) + '.' + secure_filename(file.filename).split('.')[1]
        print("filename:", filename)
        file_path = os.path.join(r'D:\python\project-finally\GFPGAN\GFPGAN\static\images\uploads', filename)
        file.save(os.path.join(project_root_path, file_path))
        return jsonify({'message': '文件上传成功', 'path': file_path}), 200

@app.route('/img/<string:name>', methods=['GET'])
def show_img(name):
    img_url = os.path.join(app.config['current_selectimage'], name)
    if name:
        image_data = open(img_url, "rb").read()
        response = make_response(image_data)
        response.headers['Content-Type'] = 'image/jpg'
        return response

@app.route('/getupload/<string:name>', methods=['GET'])
def get_upload(name):
    img_url = os.path.join(app.config['current_uploadimage'], name)
    if name:
        image_data = open(img_url, "rb").read()
        response = make_response(image_data)
        response.headers['Content-Type'] = 'image/jpg'
        return response

@app.route('/gfpgan', methods=['GET'])
def gfpgan():
    input_path = request.args.get('input')
    input_path_full = os.path.join(project_root_path, input_path)
    if not input_path_full:
        return jsonify({'error': 'Input path is required'}), 400

    getupload = f"http://localhost:5000/getupload/{os.path.basename(input_path)}"
    handle_res = image_handle({
        'input': input_path_full,
        'output': 'static/images/results',
    })
    result_image = f"http://127.0.0.1:5000/{handle_res[0]}"

    return jsonify({'message': 'Face restoration completed', 'input': getupload, 'output': result_image}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)