@echo off
echo Активируем виртуальное окружение...
call venv\Scripts\activate
echo Запускаем скрипт...
python main.py
echo Скрипт завершен.
pause
