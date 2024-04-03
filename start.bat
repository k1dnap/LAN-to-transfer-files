@echo off
echo 正在设置pip源为清华源...

:: 清华源地址
set TSINGHUA_MIRROR=https://pypi.tuna.tsinghua.edu.cn/simple

:: pip配置文件路径
set PIP_CONFIG_FILE=%USERPROFILE%\.pip\pip.ini

:: 检查pip配置文件目录是否存在，不存在则创建
if not exist "%USERPROFILE%\.pip" mkdir "%USERPROFILE%\.pip"

:: 创建或更新pip配置文件
echo [global]> %PIP_CONFIG_FILE%
echo index-url=%TSINGHUA_MIRROR%>> %PIP_CONFIG_FILE%
echo trusted-host=pypi.tuna.tsinghua.edu.cn>> %PIP_CONFIG_FILE%

echo pip源已成功更改为清华源！

pip -r requirements.txt
python Transfer.py

pause