#!/bin/bash
python3 -m pip install -r requirements.txt
python3 -m pip install pyinstaller
python3 -m PyInstaller --onefile pyfetch.py
rm -rf build pyfetch.spec && mv dist/pyfetch ./ && rmdir ./dist && chmod +x pyfetch
sudo mv ./pyfetch /usr/bin/pyfetch
echo "Build completed. Now you can run pyfetch command."