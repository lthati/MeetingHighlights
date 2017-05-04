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

import os
import json
from datetime import datetime

def main():
    recordings_dict = {'data': {'recordings':[]}}  # Create an empty dict

    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(".mp4"):
                file_data = {'fileName': os.path.basename(file),
                             'recordingDate': datetime.fromtimestamp(int(os.stat(file).st_ctime)).strftime('%Y-%m-%d %H:%M:%S'),
                             'recordingDate': int(os.stat(file).st_ctime),
                             'author': 'Amitabh Bachan',
                             'url': 'http://<bucket_name>/<folder>/%s'%(os.path.basename(file))}
                recordings_dict['data']['recordings'].append(dict(file_data))
                '''
                print(os.path.join(root, file))
                print(os.stat(file))
                '''
    print(json.dumps(recordings_dict))

if __name__ == '__main__':
    main()
