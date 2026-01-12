@echo off
chcp 65001 >nul
echo ========================================
echo  ALL-CONFIGS: Установщик конфига для CS2
echo ========================================
echo.

rem Определяем ТОЧНЫЙ путь к папке с конфигами CS2 (используя путь из info.md)
set "CS2_CONFIG_ROOT=%USERPROFILE%\AppData\Local\Counter-Strike Global Offensive\game\csgo"
set "TARGET_PATH=%CS2_CONFIG_ROOT%\cfg"

rem Проверяем существование пути
if not exist "%TARGET_PATH%" (
    echo [ОШИБКА] Не найдена папка конфигов CS2:
    echo %TARGET_PATH%
    echo.
    echo 1. Убедитесь, что CS2 установлена
    echo 2. Проверьте путь в файле CS2/info.md
    echo 3. Скопируйте файлы ВРУЧНУЮ по указанному выше пути
    pause
    exit /b 1
)

echo Найдена папка конфигов: %TARGET_PATH%
echo.

rem Переходим в папку со скриптом, чтобы найти исходные файлы
cd /d "%~dp0"

rem Проверяем, существуют ли исходные файлы конфигов
if not exist "..\CS2\autoexec.cfg" (
    echo [ОШИБКА] Не найден файл autoexec.cfg в папке CS2
    pause
    exit /b 1
)
if not exist "..\CS2\cs2_video.txt" (
    echo [ПРЕДУПРЕЖДЕНИЕ] Не найден cs2_video.txt
)

rem СОЗДАЕМ РЕЗЕРВНЫЕ КОПИИ (только если файлы уже существуют)
echo Создание резервных копий...
if exist "%TARGET_PATH%\autoexec.cfg" (
    set "timestamp=%date:~-4%%date:~-7,2%%date:~-10,2%_%time:~0,2%%time:~3,2%"
    copy "%TARGET_PATH%\autoexec.cfg" "%TARGET_PATH%\autoexec_backup_%timestamp%.cfg" >nul
    echo  autoexec.cfg -> autoexec_backup_%timestamp%.cfg
)

if exist "%TARGET_PATH%\cs2_video.txt" (
    if not defined timestamp set "timestamp=%date:~-4%%date:~-7,2%%date:~-10,2%_%time:~0,2%%time:~3,2%"
    copy "%TARGET_PATH%\cs2_video.txt" "%TARGET_PATH%\cs2_video_backup_%timestamp%.txt" >nul
    echo  cs2_video.txt -> cs2_video_backup_%timestamp%.txt
)

rem КОПИРУЕМ ВСЕ КОНФИГИ из папки CS2
echo.
echo Копирование конфигов...
xcopy /Y "..\CS2\*" "%TARGET_PATH%\" >nul
if errorlevel 1 (
    echo [ОШИБКА] Не удалось скопировать файлы
    pause
    exit /b 1
)

rem ПРОВЕРЯЕМ, КАКИЕ ФАЙЛЫ БЫЛИ СКОПИРОВАНЫ
echo Установленные файлы:
dir "%TARGET_PATH%\autoexec.cfg" "%TARGET_PATH%\cs2_video.txt" 2>nul | find "Файл"
if errorlevel 1 dir "%TARGET_PATH%\autoexec.cfg" "%TARGET_PATH%\cs2_video.txt" 2>nul | find "File"

echo.
echo ========================================
echo УСПЕХ! Конфиг CS2 установлен.
echo.
echo ВАЖНЫЕ ШАГИ:
echo 1. Добавьте в параметры запуска Steam:
echo      +exec autoexec.cfg
echo.
echo 2. Запустите CS2 и проверьте настройки видео
echo.
echo 3. Если будут проблемы - удалите файлы:
echo      autoexec.cfg и cs2_video.txt
echo      (резервные копии сохранены)
echo ========================================
pause