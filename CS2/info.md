
# 📖 Инструкция по установке / Installation Guide

[English](#english) | [Русский](#russian)

---
<a name="russian"></a>
## 🇷🇺 Русский (Russian)

### 🚀 Быстрая установка (Windows)

#### Автоматическая установка (рекомендуется)
1. Скачайте весь репозиторий (Code → Download ZIP)
2. Разархивируйте папку `ALL-CONFIGS-main`
3. Запустите файл `installers/setup_cs2.bat`
4. Следуйте инструкциям в окне командной строки

#### Ручная установка
1. Скопируйте файлы `autoexec.cfg` и `cs2_video.txt`
2. Вставьте их по пути: `%USERPROFILE%\AppData\Local\Counter-Strike Global Offensive\game\csgo\cfg`
3. Добавьте в параметры запуска Steam: `+exec autoexec.cfg`

### ⚙️ Файлы конфигурации
| Файл | Назначение |
|------|------------|
| `autoexec.cfg` | Основные настройки игры, прицел, сетка, бинды |
| `cs2_video.txt` | Настройки графики и производительности |

### 🔧 Настройка параметров запуска Steam
1. Откройте Steam → Библиотека
2. ПКМ по Counter-Strike 2 → Свойства
3. В поле "Параметры запуска" введите: `+exec autoexec.cfg`

### 3. Проверка в игре
Запустите игру и откройте консоль (клавиша `~` или `Ё`). Если настройки не применились, введите вручную:
`exec autoexec`

> **⚠️Предупреждение:** Перед запуском проверьте разрешение в файле `cs2_video.txt`, чтобы оно соответствовало вашему монитору, и впишите свою герцовку монитора в параметрах запуска!

### Пользуюся обычно двумя разрешениями (4 на 3 конечно же): 
 * 1440 x 1080 - основной
 * 1920 x 1440 - редко (лучше качество = меньше FPS)


---
<a name="english"></a>
## 🇺🇸 English

### 🚀 Quick Installation (Windows)

#### Automatic Installation (Recommended)
1. Download the entire repository (Code → Download ZIP)
2. Unzip the `ALL-CONFIGS-main` folder
3. Run the `installers/setup_cs2.bat` file
4. Follow the instructions in the command prompt window

#### Manual Installation
1. Copy the files `autoexec.cfg` and `cs2_video.txt`
2. Paste them to the path: `%USERPROFILE%\AppData\Local\Counter-Strike Global Offensive\game\csgo\cfg`
3. Add to Steam launch options: `+exec autoexec.cfg`

### ⚙️ Configuration Files
| File | Purpose |
|------|---------|
| `autoexec.cfg` | Main game settings, crosshair, viewmodel, binds |
| `cs2_video.txt` | Graphics and performance settings |

### 🔧 Setting Steam Launch Options
1. Open Steam → Library
2. Right-click Counter-Strike 2 → Properties
3. In "Launch Options" enter: `+exec autoexec.cfg`

### 3. Verification
Launch the game and open the console (press `~`). If the settings are not applied, type:
`exec autoexec`

---
> **⚠️ Warning:** Check your resolution in `cs2_video.txt` before launching to match your monitor, and enter your monitor hertz in the launch parameters!

### I usually use two resolutions (4 by 3, of course): 
 * 1440 x 1080 - main
 * 1920 x 1440 - rarely (better quality = lower FPS)
