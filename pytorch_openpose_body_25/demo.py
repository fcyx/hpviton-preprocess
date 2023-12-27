#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 19:17:47 2020

@author: joe
"""


from src import torch_openpose,util
import numpy as np
import cv2
import json
if __name__ == "__main__":
    tp = torch_openpose.torch_openpose('body_25')
    img = cv2.imread("images/1_8.png")
    poses,_ = tp(img)
    aaa = []
    new_lst = []
    for sublist in poses[0]:
        for element in sublist:
           aaa.append(element)
    pose_data = {"version": 1,
                 "people":  [
                                {"pose_keypoints_2d": aaa}
                            ]
                }
    json_object = json.dumps(pose_data, indent = 4)
    
    print(poses)
    print(json_object)
    output_json_path = "output/json/1_8_keypoints.json"
    output_img_path = "output/img/1_8.png"
    with open(output_json_path, "w") as outfile:
        outfile.write(json_object)
    img = util.draw_bodypose(np.zeros_like(img), poses,'body_25')
    cv2.imwrite(output_img_path,img)
    cv2.imshow('v',img)
    cv2.waitKey(0)
