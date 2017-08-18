#!/usr/local/bin/python
import sys
import json
import os
from PIL import Image
import pytesseract
import argparse
from os import listdir
from os.path import isfile, join
import requests

KEYWORDS_OUTPUT_FILE="/tmp/out.txt"

def process_video(rec_url, password):
    resp = download_video(rec_url, password)
    images_path = convert_video_to_images(resp)
    extract_keywords(images_path)

def download_video(rec_url, password):
    try:
        rcid = rec_url.split('=')[1]
        dl_url = 'https://cisco.webex.com/lsr.php'
        data = {
            'RCID': rcid,
        }
        return requests.post(dl_url, data=data)
    except requests.Requestexception as err:
        print 'Error while downloading video: Error: {0}'.format(str(err))

def convert_video_to_images(mp4path):
    images_path = mp4path+'/images'
    return images_path

def extract_keywords(images_path):
    print images_path
    onlyfiles = [f for f in listdir(images_path) if isfile(join(images_path, f))]
    print onlyfiles
    for image in onlyfiles:
        print image


if __name__ == '__main__':
    #if len(sys.argv) < 3:
    #    print 'Argument required...'
    #    sys.exit(1)
    #process_video(sys.argv[1], sys.argv[2])
    extract_keywords('/Users/lthati/dev/hackathon/trans-it/src/app/data/voicetranscript/videos/video1/images')