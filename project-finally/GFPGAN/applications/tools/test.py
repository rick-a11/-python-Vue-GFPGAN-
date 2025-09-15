

import argparse

import paddle
from ppgan.apps.first_order_predictor import FirstOrderPredictor

parser = argparse.ArgumentParser()
parser.add_argument("--config", default=None, help="path to config")
parser.add_argument("--weight_path",
                    default=None,
                    help="path to checkpoint to restore")
parser.add_argument("--source_image", type=str,default=r'C:\Users\20754\Desktop\project\project\GFPGAN\GFPGAN\applications\input\source_image\0013.jpeg',help="path to source image")
parser.add_argument("--driving_video", type=str,default=r'C:\Users\20754\Desktop\project\project\GFPGAN\GFPGAN\applications\input\driving_video\驱动视频.MOV', help="path to driving video")
parser.add_argument("--output", default=r'C:\Users\20754\Desktop\project\project\GFPGAN\GFPGAN\applications\output', help="path to output")
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
                    default=0.4,
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
parser.set_defaults(relative=False)
parser.set_defaults(adapt_scale=False)
parser.set_defaults(face_enhancement=False)
parser.set_defaults(mobile_net=False)

parser.add_argument(
    "--slice_size",
    dest="slice_size",
    type=int,
    default=0,
    help=
    "slice driving video to smaller parts to bypass XPU's 4G byte tensor restriction"
)

if __name__ == "__main__":
    args = parser.parse_args()
    args.relative=True
    args.adapt_scale=True
    args.face_enhancement=True
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
