"""
A customizable lightweight Python library for real-time multi-object tracking.

Examples
--------
>>> from norfair import Detection, Tracker, Video, draw_tracked_objects
>>> detector = MyDetector()  # Set up a detector
>>> video = Video(input_path="video.mp4")
>>> tracker = Tracker(distance_function="euclidean", distance_threshold=50)
>>> for frame in video:
>>>    detections = detector(frame)
>>>    norfair_detections = [Detection(points) for points in detections]
>>>    tracked_objects = tracker.update(detections=norfair_detections)
>>>    draw_tracked_objects(frame, tracked_objects)
>>>    video.write(frame)
"""

import sys

from .distances import (
    create_keypoints_voting_distance,
    create_normalized_mean_euclidean_distance,
    frobenius,
    get_distance_by_name,
    iou,
    iou_opt,
    mean_euclidean,
    mean_manhattan,
)
from .drawing import (
    AbsolutePaths,
    Color,
    ColorType,
    Drawable,
    FixedCamera,
    Palette,
    Paths,
    draw_absolute_grid,
    draw_boxes,
    draw_points,
    draw_tracked_boxes,
    draw_tracked_objects,
)
from .filter import (
    FilterPyKalmanFilterFactory,
    NoFilterFactory,
    OptimizedKalmanFilterFactory,
)
from .tracker import Detection, Tracker
from .utils import get_cutout, print_objects_as_table
from .video import Video

if sys.version_info >= (3, 8):
    import importlib.metadata

    __version__ = importlib.metadata.version(__name__)
elif sys.version_info < (3, 8):
    import importlib_metadata

    __version__ = importlib_metadata.version(__name__)


__all__ = [
    "FilterPyKalmanFilterFactory",
    "NoFilterFactory",
    "OptimizedKalmanFilterFactory",
    "Detection",
    "Tracker",
    "get_cutout",
    "print_objects_as_table",
    "Video",
    "draw_absolute_grid",
    "Color",
    "ColorType",
    "Palette",
    "draw_boxes",
    "draw_tracked_boxes",
    "draw_points",
    "draw_tracked_objects",
    "Drawable",
    "FixedCamera",
    "AbsolutePaths",
    "Paths",
    "frobenius",
    "mean_manhattan",
    "mean_euclidean",
    "iou",
    "iou_opt",
    "get_distance_by_name",
    "create_keypoints_voting_distance",
    "create_normalized_mean_euclidean_distance",
]
