@echo off
cd /d "%~dp0"
echo Iniciando servidor do Riff Rush (com suporte a links do YouTube)...
start "" "http://localhost:5000"
python server.py
pause
