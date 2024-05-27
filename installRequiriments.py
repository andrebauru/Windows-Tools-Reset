import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

try:
    import tkinter
    print("tkinter já está instalado.")
except ImportError:
    print("tkinter não está instalado. Instalando agora...")
    install("tkinter")

print("O script está pronto para ser executado.")
