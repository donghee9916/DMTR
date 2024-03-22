#
#
#
# Written by Donghui Eom
# All Rights Reserved

import sys, os 
import numpy as np
import pickle
import tensorflow as tf
import multiprocessing
import glob
from tqdm import tqdm

'''
from waymo_open_dataset.protos import scenario_pb2
from waymo_types import object_type, lane_type, road_line_type, road_edge_type, signal_state, polyline_type

위의 waymo 데이터셋 처리 부분을 custom의 경우 어떻게 처리할지 고려해야한다.
'''

# 불필요한 warning 무시
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

def decode_tracks_from_proto(tracks):
    track_infos = {
        'object_id' : [], # {기존 waymo에서 0: unset, 1: vehicle, 2: pedestrain, 3: cyclist, 4: others}
        'object_type' : [],
        'trajs' : [] 
    }
    for cur_data in tracks: # number of objects
        cur_traj = [np.array([x.center_x, x.center_y, x.center_z, x.length, x.width, x.height, x.heading,
                              x.velocity_x, x.velocity_y, x.valid], dtype=np.float32) for x in cur_data.states]
        cur_traj = np.stack(cur_traj, axis=0)

        track_infos['object_id'].append(cur_data.id)
        # track_infos['object_type'].append(object_type[cur_data.object_type])
        # 위의 부분에서 object_type은 waymo_types의 type이다. 
        track_infos['trajs'].append(cur_traj)