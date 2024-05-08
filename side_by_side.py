from pathlib import Path
import cv2
import argparse
def concatenate_videos(left_video_path, right_video_path, output_path):
    left_video = cv2.VideoCapture(left_video_path)
    right_video = cv2.VideoCapture(right_video_path)

    width = int(left_video.get(cv2.CAP_PROP_FRAME_WIDTH) + right_video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = max(int(left_video.get(cv2.CAP_PROP_FRAME_HEIGHT)), int(right_video.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    fps = min(left_video.get(cv2.CAP_PROP_FPS), right_video.get(cv2.CAP_PROP_FPS))
    frame_size = (width, height)

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, frame_size)

    while True:
        ret1, frame_left = left_video.read()
        ret2, frame_right = right_video.read()
        if not (ret1 and ret2):
            break

        concatenated_frame = cv2.hconcat([frame_left, frame_right])
        out.write(concatenated_frame)

    left_video.release()
    right_video.release()
    out.release()

    print("finished concatenate videos.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("leftname", help="videofile for left")
    parser.add_argument("rightname", help="videofile for right")
#    parser.add_argument("--outname", default="side_by_side.mp4", help="output video name")
    args = parser.parse_args()

    left = Path(args.leftname)
    right = Path(args.rightname)
#    outname = Path(args.outname)

    # 2つの入力動画ファイルパス
    left_video_path = args.leftname
    right_video_path = args.rightname
    output_path = "concatenated_video.mp4"
    concatenate_videos(left_video_path, right_video_path, output_path)
