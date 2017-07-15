from __future__ import unicode_literals
import subprocess
from prompt_toolkit import prompt
from google.cloud import vision

url = prompt('Give me a local image url or a web url to a image: ')

if 'www.' not in url:
    print("(choose from 'faces', 'labels', 'landmarks', 'text',  'logos', 'safe-search', 'properties', 'web', 'crophints', 'document')")
    detect_choice = prompt('Please enter an identification type from list above: ')
    subprocess.call(['python', 'detect.py', detect_choice, url])
else:
    print("(choose from 'faces-uri', 'labels-uri', 'landmarks-uri', 'text-uri', 'logos-uri', 'safe-search-uri', 'properties-uri', 'web-uri', 'crophints-uri', 'document-uri')")
    detect_choice = prompt('Please enter an identification type from list above: ')
    subprocess.call(['python', 'detect.py', detect_choice, url])
