'''
Parse through the list of file under given directory and create the following output:
   {
    "data": {
        "recordings": [{
            "fileName": "SIG Nginx Config Changes - Knowledge Share-20161206 1633-1",
            "recordingDate": 1493893961,
            "author": "Sanjeev Maheve",
            "url": "http://file1.mp4"
        }]
    }
   }
'''
#!/usr/bin/python

import os, sys
import json
import hashlib
from datetime import datetime

def recordings(input_path, output_file):
    recordings_dict = {'data': []}  # Create an empty dict

    for root, dirs, files in os.walk(input_path):
        for file in files:
            if file.endswith(".mp4"):
                file_path = os.path.join(root, file)
                file_data = {'fileName': os.path.basename(file),
                             'fileId': hashlib.md5(os.path.basename(file)).hexdigest(),
                             'recordingDate': datetime.fromtimestamp(int(os.stat(file_path).st_ctime)).strftime('%Y-%m-%d %H:%M:%S'),
                             'recordingDate': int(os.stat(file_path).st_ctime),
                             'author': 'Amitabh Bachan',
                             'url': 'http://<bucket_name>/<folder>/%s'%(os.path.basename(file)),
                             'url': '%s/%s'%('/app/data/voicetranscript/videos', os.path.basename(file))}
                recordings_dict['data'].append(dict(file_data))
                '''
                print(os.path.join(root, file))
                print(os.stat(file))
                '''
    print(json.dumps(recordings_dict))
    '''
    Write to output a file
    '''
    with open(output_file, 'w') as output_file:
        json.dump(recordings_dict, output_file)
    return recordings_dict

if __name__ == '__main__':
    recordings('../videos', '../metadata/recordings.json')
