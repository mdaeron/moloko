import subprocess

def main() -> None:
    print('Hello from moloko!')
    subprocess.run('uv run streamlit run moloko/src/moloko/app.py'.split())
