import argparse

from mmdet.apis import inference_detector, init_detector
from mmdet.core import get_classes

from norfair import Detection, Tracker, Video, draw_tracked_objects

parser = argparse.ArgumentParser(description="Track human poses in a video.")
parser.add_argument("files", type=str, nargs="+", help="Video files to process")
parser.add_argument("--output-path", type=str, nargs="?", default=".", help="Output path")
args = parser.parse_args()

#
# MMDetection setup
#

CONFIG_FILE = "/mmdetection/configs/faster_rcnn/faster_rcnn_r50_fpn_1x_coco.py"
CHECKPOINT_FILE = "/mmdetection/faster_rcnn_r50_fpn_1x_coco_20200130-047c8118.pth"
model = init_detector(CONFIG_FILE, CHECKPOINT_FILE, device="cuda:0")

# Get the classes id mmdet uses
VEHICLE_CLASSES = [i for i, n in enumerate(get_classes("coco")) if n in ["car", "motorcycle", "bus", "truck"]]


for input_path in args.files:
    tracker = Tracker(distance_function="euclidean", distance_threshold=20, detection_threshold=0.6)

    video = Video(input_path=input_path, output_path=args.output_path)

    for frame in video:
        result = inference_detector(model, frame)
        detections = []
        for label, bboxes in enumerate(result):
            # filter non-vehicles
            if label not in VEHICLE_CLASSES:
                continue
            if bboxes.shape[0] > 0:
                for bbox in bboxes:
                    # bbox is a 1 dimensional array with [x1, y1, x2, y2, score]
                    centroid = bbox[:4].reshape((2, 2)).mean(axis=0)
                    detections.append(
                        Detection(
                            centroid,
                            scores=bbox[[-1]],
                            label=label,
                        )
                    )

        tracked_objects = tracker.update(detections=detections)
        draw_tracked_objects(frame, tracked_objects)
        video.write(frame)
