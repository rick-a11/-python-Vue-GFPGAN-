import argparse
from flask import Flask, request, jsonify
from flask_cors import CORS
import paddle
from ppgan.apps.first_order_predictor import FirstOrderPredictor
import os
import base64
import json
app = Flask(__name__)

CORS(app)
value=0

app.config['UPLOAD_FOLDER'] = r'D:\python\project-finally\GFPGAN\GFPGAN\applications\input\source_image'



@app.route('/value', methods=['POST'])
def value():
    data = request.json
    global value
    value = data.get('selectedValue')
    print("value:", value)
    return jsonify({'message': 'Received selected value: {}'.format(value)})


@app.route('/process_image', methods=["GET",'POST'])
def process_image():
    print("Success!")
    global value
    if (value == 3):
        os.environ['DRIVING_VIDEO'] = r'D:\python\project-finally\GFPGAN\GFPGAN\applications\input\driving_video\微笑眨眼.mp4'
    elif (value == 6):
        print(value)
        os.environ['DRIVING_VIDEO'] = r'D:\python\project-finally\GFPGAN\GFPGAN\applications\input\driving_video\困惑.mp4'
    elif (value == 9):
        print(value)
        os.environ['DRIVING_VIDEO'] = r'D:\python\project-finally\GFPGAN\GFPGAN\applications\input\driving_video\同意点头.mp4'
    elif (value == 12):
        print(value)
        os.environ['DRIVING_VIDEO'] = r'D:\python\project-finally\GFPGAN\GFPGAN\applications\input\driving_video\摇头.mp4'
    else:
        os.environ['DRIVING_VIDEO'] = r'D:\python\project-finally\GFPGAN\GFPGAN\applications\input\driving_video\驱动视频.MOV'
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    else:
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        default_filepath = app.config['UPLOAD_FOLDER'] + '/' + file.filename
        parser = argparse.ArgumentParser()
        parser.add_argument("--config", default=None, help="path to config")
        parser.add_argument("--weight_path",
                            default=None,
                            help="path to checkpoint to restore")
        parser.add_argument("--source_image", type=str,
                            default=default_filepath,
                            help="path to source image")
        parser.add_argument("--driving_video", type=str,
                            default=os.environ.get('DRIVING_VIDEO',
                                                   r'D:\python\project-finally\GFPGAN\GFPGAN\applications\input\driving_video\驱动视频.MOV'),
                            help="path to driving video")
        parser.add_argument("--output",
                            default=r'D:\python\project-finally\GFPGAN\GFPGAN\applications\output',
                            help="path to output")
        parser.add_argument("--filename",
                            default='result.mp4',
                            help="filename to output")
        parser.add_argument("--relative",
                            dest="relative",
                            action="store_true",
                            default=True,
                            help="use relative or absolute keypoint coordinates")
        parser.add_argument(
            "--adapt_scale",
            dest="adapt_scale",
            action="store_true",
            default=True,
            help="adapt movement scale based on convex hull of keypoints")

        parser.add_argument(
            "--find_best_frame",
            dest="find_best_frame",
            action="store_true",
            help=
            "Generate from the frame that is the most alligned with source. (Only for faces, requires face_aligment lib)"
        )

        parser.add_argument("--best_frame",
                            dest="best_frame",
                            type=int,
                            default=None,
                            help="Set frame to start from.")

        # for device
        group = parser.add_mutually_exclusive_group()
        group.add_argument("--cpu", dest="cpu", action="store_true", help="cpu mode.")
        group.add_argument("--xpu", dest="xpu", action="store_true", help="xpu mode.")

        parser.add_argument("--ratio",
                            dest="ratio",
                            type=float,
                            default=0.01,
                            help="margin ratio")
        parser.add_argument(
            "--face_detector",
            dest="face_detector",
            type=str,
            default='sfd',
            help="face detector to be used, can choose s3fd or blazeface")
        parser.add_argument("--multi_person",
                            dest="multi_person",
                            action="store_true",
                            default=False,
                            help="whether there is only one person in the image or not")
        parser.add_argument("--image_size",
                            dest="image_size",
                            type=int,
                            default=512,
                            help="size of image")
        parser.add_argument("--batch_size",
                            dest="batch_size",
                            type=int,
                            default=1,
                            help="Batch size for fom model")
        parser.add_argument("--face_enhancement",
                            dest="face_enhancement",
                            action="store_true",
                            default=True,
                            help="use face enhance for face")
        parser.add_argument("--mobile_net",
                            dest="mobile_net",
                            action="store_true",
                            help="use mobile_net for fom")
        parser.set_defaults(relative=True)
        parser.set_defaults(adapt_scale=True)
        parser.set_defaults(face_enhancement=True)
        parser.set_defaults(mobile_net=False)

        parser.add_argument(
            "--slice_size",
            dest="slice_size",
            type=int,
            default=0,
            help=
            "slice driving video to smaller parts to bypass XPU's 4G byte tensor restriction"
        )
        args = parser.parse_args()
        args.relative = True
        args.adapt_scale = True
        args.face_enhancement = True
        if args.cpu:
            paddle.set_device('cpu')
        if args.xpu:
            paddle.set_device('xpu')

        predictor = FirstOrderPredictor(output=args.output,
                                        filename=args.filename,
                                        weight_path=args.weight_path,
                                        config=args.config,
                                        relative=args.relative,
                                        adapt_scale=args.adapt_scale,
                                        find_best_frame=args.find_best_frame,
                                        best_frame=args.best_frame,
                                        ratio=args.ratio,
                                        face_detector=args.face_detector,
                                        multi_person=args.multi_person,
                                        image_size=args.image_size,
                                        batch_size=args.batch_size,
                                        face_enhancement=args.face_enhancement,
                                        mobile_net=args.mobile_net)
        print(args.source_image)
        print(args.driving_video)
        print(args.adapt_scale)
        print(args.relative)
        print(args.face_enhancement)


        predictor.run(args.source_image, args.driving_video)


        # 读取 result.mp4 文件
        result_file_path = r'D:\python\project-finally\GFPGAN\GFPGAN\applications\output\result.mp4'
        with open(result_file_path, 'rb') as file:
            result_data = file.read()

        # 将文件内容转换为 base64 编码
        result_base64 = 'data:video/mp4;base64,' +  base64.b64encode(result_data).decode('utf-8')

        # 输出 base64 编码后的结果

        result_json = json.dumps({"result_base64": result_base64})

        return  result_json


if __name__ == "__main__":
    app.run(debug=True)
