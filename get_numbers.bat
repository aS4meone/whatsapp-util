@echo off
echo Активируем виртуальное окружение...
call venv\Scripts\activate
echo Запускаем Python скрипт...
python get_numbers.py
echo Скрипт завершен.
pause
