import os.path as osp

import numpy as np
import pandas as pd

import motmetrics
import cv2


def load_mod_annotations(file_path, start_frame_id=0, end_frame_id=200, **kwargs):
    gts = motmetrics.io.loadtxt(osp.expanduser(file_path))

    idx = pd.IndexSlice
    gts = gts.loc[idx[np.arange(start_frame_id, end_frame_id)], :]

    return gts


def select_annotations_by_frame_id(data_frame: pd.DataFrame, frame_id: int):
    frame_data = data_frame.iloc[data_frame.index.get_level_values('FrameId') == frame_id]
    xs = np.asarray(frame_data['X'].tolist())
    ys = np.asarray(frame_data['Y'].tolist())
    ws = np.asarray(frame_data['Width'].tolist())
    hs = np.asarray(frame_data['Height'].tolist())

    data = np.vstack([xs, ys, ws, hs]).transpose()

    return data


def load_video(file_path, start_frame_id=0, end_frame_id=200):
    file_path = osp.expanduser(file_path)

    video_capture = cv2.VideoCapture(file_path)

    frames = []
    for frame_id in range(end_frame_id):
        _, frame_3c = video_capture.read()
        frame = cv2.cvtColor(frame_3c, cv2.COLOR_BGR2GRAY)

        frame_shape = frame.shape

        if start_frame_id <= frame_id:
            frames.append(frame)

    return frames, frame_shape


if __name__ == '__main__':
    input_video_path = osp.join(osp.curdir, '001', 'video.mp4')
    input_gt_path = osp.join(osp.curdir, '001', 'gt_0_700.csv')

    frames, frame_shape = load_video(input_video_path)
    gts = load_mod_annotations(input_gt_path)
    for frame_id, frame in enumerate(frames):
        brg_frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)

        boxes = select_annotations_by_frame_id(gts, frame_id)
        for x, y, w, h in boxes:
            cv2.rectangle(brg_frame, (x, y), (x + w - 1, y + h - 1), (0, 0, 255))

        cv2.imshow('Annotation', brg_frame)
        cv2.waitKey(100)

