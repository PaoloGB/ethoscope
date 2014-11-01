__author__ = 'quentin'


from pysolovideo.tracking.roi_builders import SleepDepROIBuilder
from pysolovideo.tracking.cameras import MovieVirtualCamera
from pysolovideo.tracking.monitor import Monitor
from pysolovideo.tracking.trackers import AdaptiveBGModel
from pysolovideo.tracking.interactors import SystemPlaySoundOnStop




cam = MovieVirtualCamera("/stk/pysolo_video_samples/long_realistic_recording.avi")
roi_builder = SleepDepROIBuilder()

rois = roi_builder(cam)
# inters = [SystemPlaySoundOnStop(500 + i * 30) for i in range(13)]
inters = None




monit = Monitor(cam, AdaptiveBGModel, interactors= inters, roi_builder=roi_builder)
monit.run()

#