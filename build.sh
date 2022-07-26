#!/bin/bash
python3 -m pip install pyinstaller
pyinstaller --onefile pyfetch.py
rm -rf build pyfetch.spec && mv dist/pyfetch ./ && rmdir ./dist && chmod +x pyfetch
sudo mv ./pyfetch /usr/bin/pyfetch
echo "Build completed. Now you can run pyfetch command."