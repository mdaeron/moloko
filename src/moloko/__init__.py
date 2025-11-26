import subprocess

def main() -> None:
    print('Hello from moloko!')
    subprocess.run('uv run streamlit run src/moloko/app.py'.split())
