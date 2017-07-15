from __future__ import unicode_literals
import subprocess
from prompt_toolkit import prompt

text = prompt('Give me some input: ')
print('You said: %s' % text)
if text:
    subprocess.call(["ls", "-l"])
