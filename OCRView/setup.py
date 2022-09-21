# coding: utf-8
# cx_Freeze 用セットアップファイル

import sys
from cx_Freeze import setup, Executable

base = None

build_exe_options = {
    "packages": [
        "io",
        "os",
        "sys",
        "cv2",
        "tkinter",
        "pandas",
        "numpy",
        "datetime",
        "toml",
        "csv",
        "mojimoji",
        "difflib",
        "math",
        "pdf2image",
    ]
}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="ViewGUI.py",
    version="0.1",
    description="My GUI application!",
    options={"build_exe": build_exe_options},
    executables=[Executable("ViewGUI.py", base=base)],
)
