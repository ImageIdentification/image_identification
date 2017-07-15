from __future__ import unicode_literals
import subprocess
from prompt_toolkit import prompt
from google.cloud import vision

url = prompt('Give me a local image url or a web url to a image: ')

if 'www.' not in url:
    subprocess.call(['python', 'detect.py', 'document', url])
