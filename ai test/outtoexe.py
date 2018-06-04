from PyInstaller.__main__ import run
if __name__ == '__main__':
    opts = ['chatrobot.py','-F',r'--distpath=C:\pythontest',r'--workpath=C:\pythontest',r'--specpath=C:\pythontest',r'--icon=C:\pythontest\enemy.ico']
    run(opts)