import os
from config  import *
import numpy as np
import pandas as pd
import sys
sys.path.insert(0, '/home/adeyemi/Documents/mypythonlibrary')
from myfunctions import images_to_video


root_path = '../../Velpsis_data/data/processed/'



for blur in blur_rate:
    for location in locations:

        blur_and_downsample_str = 'blur_'+str(blur)+'_pixels_'+'downsample_factor_'+str(downsam_factor)

        #make output directory if it doesnt exisit
        output_dir = '../data/processed/'+blur_and_downsample_str
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        image_path = root_path+blur_and_downsample_str + '/test/' + location + '/images'

        output_file_name = location+'_'+ blur_and_downsample_str
        images_to_video(image_path, output_file_name, output_dir)