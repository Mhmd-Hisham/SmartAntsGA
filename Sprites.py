#!/usr/bin/env python2
"""
    Ant sprite animation.

"""

import json

class SpriteAnimation():
    """ Sprite Animation class for showing the ant animation."""
    def __init__(self, frames, frame_width, frame_height):

        # self.frames = frames
        self.frame_width = frame_width
        self.frame_height = frame_height
        self.aspect_ratio = self.frame_width/self.frame_height

        self.frame_index = 0
        self.frames = frames
        self.no_frames = len(frames)
    
    # draw a frame on the screen
    def show(self, x, y):
        imageMode(CENTER)
        image(self.frames[self.frame_index], x, y, self.frame_width, self.frame_height)

    # move the frame index pointer to the next frame
    # if the current frame is the last one, point to the first frame (0)
    def update(self):
        self.frame_index = (self.frame_index+1)%self.no_frames

def load_frames(sprite_sheet_filename, sprite_json_filename):
    """ Loads the sprite sheet animation frames into memory."""
    frames = []

    # opens the json file data
    with open(sprite_json_filename, 'r') as fh:    
        json_data = json.load(fh)

    frames_dict = json_data["frames"]
    sprite_sheet = loadImage(sprite_sheet_filename)

    for frame in frames_dict:
        pos = frame["position"]
        img = sprite_sheet.get(pos["x"], pos["y"], pos["w"], pos["h"])
    
        frames.append(img)
    
    frame_width  = frames_dict[0]["position"]['w']
    frame_height = frames_dict[0]["position"]['h']
    
    # return a a tuple (list of frames, frame_width, frame_height)
    return frames, frame_width, frame_height

