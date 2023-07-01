#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import subprocess
from argparse import ArgumentParser

def get_option(mode, nextShapeMode, random_seed, drop_interval, resultlogjson, train_yaml, predict_weight, user_name, ShapeListMax, BlockNumMax, art_config_filepath):
    argparser = ArgumentParser()
    argparser.add_argument('-m', '--mode', type=str,
                           default=mode,
                           help='Specify mode (keyboard/gamepad/sample/art/train/predict/train_sample/predict_sample/train_sample2/predict_sample2) if necessary')
    argparser.add_argument('--nextShapeMode', type=str,
                           default=nextShapeMode,
                           help='Specify nextShapeMode (default/hate) if necessary')
    argparser.add_argument('-r', '--random_seed', type=int,
                           default=random_seed,
                           help='Specify random seed if necessary') 
    argparser.add_argument('-d', '--drop_interval', type=int,
                           default=drop_interval,
                           help='Specify drop interval (msec) if necessary') 
    argparser.add_argument('-f', '--resultlogjson', type=str,
                           default=resultlogjson,
                           help='Specigy result log file path if necessary')
    argparser.add_argument('--train_yaml', type=str,
                           default=train_yaml,
                           help='yaml file for machine learning')
    argparser.add_argument('--predict_weight', type=str,
                           default=predict_weight,
                           help='weight file for machine learning')
    argparser.add_argument('-u', '--user_name', type=str,
                           default=user_name,
                           help='Specigy user name if necessary')
    argparser.add_argument('--ShapeListMax', type=int,
                           default=ShapeListMax,
                           help='Specigy ShapeListMax if necessary')
    argparser.add_argument('--BlockNumMax', type=int,
                           default=BlockNumMax,
                           help='Specigy BlockNumMax if necessary')
    argparser.add_argument('--art_config_filepath', type=str,
                           default=art_config_filepath,
                           help='art_config file path')
    return argparser.parse_args()

def start():
    ## default value
    IS_MODE = "default"
    IS_NEXTSHAPEMODE = "default"
    IS_SAMPLE_CONTROLL = "n"
    INPUT_RANDOM_SEED = -1
    INPUT_DROP_INTERVAL = -1
    DROP_INTERVAL = 1000          # drop interval
    RESULT_LOG_JSON = "result.json"
    USER_NAME = "window_sample"
    SHAPE_LIST_MAX = 6
    BLOCK_NUM_MAX = -1
    TRAIN_YAML = "config/default.yaml"
    PREDICT_WEIGHT = "outputs/latest/best_weight.pt"
    ART_CONFIG = "default.json"

    ## update value if args are given
    args = get_option(IS_MODE,
                      IS_NEXTSHAPEMODE,
                      INPUT_RANDOM_SEED,
                      INPUT_DROP_INTERVAL,
                      RESULT_LOG_JSON,
                      TRAIN_YAML,
                      PREDICT_WEIGHT,
                      USER_NAME,
                      SHAPE_LIST_MAX,
                      BLOCK_NUM_MAX,
                      ART_CONFIG)
    if args.mode in ("keyboard", "gamepad", "sample", "art", "train", "predict", "train_sample", "predict_sample", "train_sample2", "predict_sample2"):
        IS_MODE = args.mode
    if args.nextShapeMode in ("default", "hate"):
        IS_NEXTSHAPEMODE = args.nextShapeMode
    if args.random_seed >= 0:
        INPUT_RANDOM_SEED = args.random_seed
    if args.drop_interval > 0:
        INPUT_DROP_INTERVAL = args.drop_interval
    if len(args.resultlogjson) != 0:
        RESULT_LOG_JSON = args.resultlogjson
    if len(args.user_name) != 0:
        USER_NAME = args.user_name
    if args.ShapeListMax > 1:
        SHAPE_LIST_MAX = args.ShapeListMax
    if args.BlockNumMax > 1:
        BLOCK_NUM_MAX = args.BlockNumMax
    if len(args.train_yaml) != 0:
        TRAIN_YAML = args.train_yaml
    if args.predict_weight != None:
        PREDICT_WEIGHT = args.predict_weight
    if len(args.art_config_filepath) != 0:
        ART_CONFIG = args.art_config_filepath

    ## set field parameter for level 1
    RANDOM_SEED = 0            # random seed for field
    OBSTACLE_HEIGHT = 0        # obstacle height (blocks)
    OBSTACLE_PROBABILITY = 0   # obstacle probability (percent)

    ## update field parameter level
    RANDOM_SEED = 0
    BLOCK_NUM_MAX = 180

    ## update random seed
    if INPUT_RANDOM_SEED >= 0:
        RANDOM_SEED = INPUT_RANDOM_SEED
    ## update drop interval
    if INPUT_DROP_INTERVAL > 0:
        DROP_INTERVAL = INPUT_DROP_INTERVAL
    ## hate mode parameter
    if IS_NEXTSHAPEMODE == "hate":
        SHAPE_LIST_MAX = 2

    ## print
    print('RANDOM_SEED: ' + str(RANDOM_SEED))
    print('IS_MODE :' + str(IS_MODE))
    print('IS_NEXTSHAPEMODE :' + str(IS_NEXTSHAPEMODE))
    print('OBSTACLE_HEIGHT: ' + str(OBSTACLE_HEIGHT))
    print('OBSTACLE_PROBABILITY: ' + str(OBSTACLE_PROBABILITY))
    print('USER_NAME: ' + str(USER_NAME))
    print('SHAPE_LIST_MAX: ' + str(SHAPE_LIST_MAX))
    print('BLOCK_NUM_MAX: ' + str(BLOCK_NUM_MAX))
    print('RESULT_LOG_JSON: ' + str(RESULT_LOG_JSON))
    print('TRAIN_YAML: ' + str(TRAIN_YAML))
    print('PREDICT_WEIGHT: ' + str(PREDICT_WEIGHT))
    print('ART_CONFIG: ' + str(ART_CONFIG))

    ## start game
    cmd = 'python game_manager.py' \
        + ' ' + '--seed' + ' ' + str(RANDOM_SEED) \
        + ' ' + '--obstacle_height' + ' ' + str(OBSTACLE_HEIGHT) \
        + ' ' + '--obstacle_probability' + ' ' + str(OBSTACLE_PROBABILITY) \
        + ' ' + '--drop_interval' + ' ' + str(DROP_INTERVAL) \
        + ' ' + '--mode' + ' ' + str(IS_MODE) \
        + ' ' + '--nextShapeMode' + ' ' + str(IS_NEXTSHAPEMODE) \
        + ' ' + '--user_name' + ' ' + str(USER_NAME) \
        + ' ' + '--resultlogjson' + ' ' + str(RESULT_LOG_JSON) \
        + ' ' + '--train_yaml' + ' ' + str(TRAIN_YAML) \
        + ' ' + '--predict_weight' + ' ' + str(PREDICT_WEIGHT) \
        + ' ' + '--ShapeListMax' + ' ' + str(SHAPE_LIST_MAX) \
        + ' ' + '--BlockNumMax' + ' ' + str(BLOCK_NUM_MAX) \
        + ' ' + '--art_config_filepath' + ' ' + str(ART_CONFIG)

    ret = subprocess.run(cmd, shell=True, stderr=subprocess.PIPE, text=True)
    if ret.returncode != 0:
        raise Exception(ret.stderr)

if __name__ == '__main__':
    start()
