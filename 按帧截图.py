import cv2
import argparse
import os


def parse_args():
    parser = argparse.ArgumentParser(description='Process pic')
    parser.add_argument('--input', help='video to process', dest='input', default=None, type=str)
    parser.add_argument('--output', help='pic to store', dest='output', default=None, type=str)
    parser.add_argument('--skip_frame', dest='skip_frame', help='skip number of video', default=1, type=int)### default修改步长
    args = parser.parse_args(['--input', r'C:\FFOutput\Clip_mp4\03.mp4', '--output', r'C:\FFOutput\mp403220'])###文件夹名称、视频名称
    return args


def process_video(i_video, o_video, num):
    cap = cv2.VideoCapture(i_video)
    num_frame = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    print("this video has " + str(num_frame) + " frame.")
    # expand_name = '.jpg'
    if not cap.isOpened():
        print("Please check the path.")
    cnt = 0
    count = 0
    while 1:
        ret, frame = cap.read()
        cnt += 1
        if cnt % num == 0:
            count += 1
            filename = "44" + "%04d.jpg" % count
            # cv2.imwrite(os.path.join(o_video, str(count) + expand_name), frame)
            cv2.imwrite(os.path.join(o_video, filename), frame)
        if not ret:
            break


if __name__ == '__main__':
    args = parse_args()
    if not os.path.exists(args.output):
        os.makedirs(args.output)
    print('Called with args:')
    print(args)
    process_video(args.input, args.output, args.skip_frame)
    print("process is finished now")
