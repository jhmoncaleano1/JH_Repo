@echo off
cd /d %~dp0

echo Activando entorno virtual...
call .venv\Scripts\activate.bat

echo Ejecutando script de actualización inteligente...
python actualizar_github.py

echo.
echo ===========================================
echo 🧠 Proceso completado inteligentemente.
echo Presione una tecla para cerrar esta ventana.
pause >nul