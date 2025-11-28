import os
import subprocess

def main() -> None:
    print(f'Hello from moloko at {os.path.abspath(os.path.dirname(__file__))}!')
    subprocess.run([
#     	'uv',
#     	'run',
    	'streamlit',
    	'run',
    	os.path.abspath(os.path.dirname(__file__)) + '/app.py',
    ])
