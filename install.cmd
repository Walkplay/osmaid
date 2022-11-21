pipenv install 
pipenv run py ./src/main.py install -o %~f1
setx OS_MAID_CWD %~f1
mklink /H "%APPDATA%/Microsoft/Windows/Start Menu/Programs/Startup/osmaid.cmd" ".\osmaid.cmd"