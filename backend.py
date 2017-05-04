'''
1. Call the function responsible for listing the files from video folder.
2. Call the function for extracting keywords.
3. Call the function for extracting timestamps for the respective keywords.
'''
#!/usr/bin/python
import os, sys, json
from file_listing import recordings
from keywords import keywords_with_word_count
from keywords import keywords_with_timestamps

def summarize_recording(metadata_path):
    # Generate output JSON having all the recording files
    files = recordings('../videos', '../metadata/recordings.json')
    # Parse JSON output and create keywords summary per recording
    for obj in files['data']:
        # Generate output containing word and count for word cloud
        keywords_with_word_count(metadata_path + os.path.splitext(obj['fileName'])[0], metadata_path + obj['fileId'])
        # Generate output containing word with timestamp values from transcript
        keywords_with_timestamps(metadata_path + os.path.splitext(obj['fileName'])[0], metadata_path + obj['fileId'])

if __name__ == '__main__':
    summarize_recording('../metadata/')
