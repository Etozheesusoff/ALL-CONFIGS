
# 📖 Инструкция по установке / Installation Guide

[English](#english) | [Русский](#russian)

---
<a name="russian"></a>
## 🇷🇺 Русский (Russian)

### 1. Куда копировать файлы?
Вам нужно перенести скачанные файлы в две разные папки:

* **Файл `autoexec.cfg`** (Бинды, прицел, настройки интерфейса):
    * **Путь:** `C:\Program Files (x86)\Steam\steamapps\common\Counter-Strike Global Offensive\game\csgo\cfg\`
* **Файл `cs2_video.txt`** (Настройки графики и видео):
    * **Путь:** `C:\Program Files (x86)\Steam\userdata\ВАШ_ID_STEAM\730\local\cfg\`
    * *Примечание:* `ВАШ_ID_STEAM` — это папка с цифрами. Если вы единственный пользователь ПК, там будет всего одна такая папка.

### 2. Как активировать конфиг?
Чтобы игра автоматически загружала настройки:
1. Зайдите в **Steam** -> **Библиотека**.
2. Нажмите правой кнопкой на **Counter-Strike 2** -> **Свойства**.
3. Во вкладке **Общие** найдите поле **Параметры запуска**.
4. Впишите туда: `+exec autoexec.cfg`

**Параметры запуска:** `-novid -allow_third_party_software -freq 165 -refresh 165 +fps_max 0 +exec autoexec.cfg`

### 3. Проверка в игре
Запустите игру и откройте консоль (клавиша `~` или `Ё`). Если настройки не применились, введите вручную:
`exec autoexec`

> **⚠️Предупреждение:** Перед запуском проверьте разрешение в файле `cs2_video.txt`, чтобы оно соответствовало вашему монитору, и впишите свою герцовку монитора в параметрах запуска!

---
<a name="english"></a>
## 🇺🇸 English

### 1. File Locations
You need to copy the downloaded files to these two locations:

* **File `autoexec.cfg`** (Binds, crosshair, HUD):
    * **Path:** `...\Steam\steamapps\common\Counter-Strike Global Offensive\game\csgo\cfg\`
* **File `cs2_video.txt`** (Video and Graphics settings):
    * **Path:** `...\Steam\userdata\YOUR_STEAM_ID\730\local\cfg\`
    * *Note:* `YOUR_STEAM_ID` is a folder named with your unique numeric ID.

### 2. Activation
To make the game load your config automatically:
1. Open **Steam** -> **Library**.
2. Right-click **Counter-Strike 2** -> **Properties**.
3. In the **General** tab, look for **Launch Options**.
4. Enter: `+exec autoexec.cfg`

**Launch Options:** `-novid -allow_third_party_software -freq 165 -refresh 165 +fps_max 0 +exec autoexec.cfg`

### 3. Verification
Launch the game and open the console (press `~`). If the settings are not applied, type:
`exec autoexec`

---
> **⚠️ Warning:** Check your resolution in `cs2_video.txt` before launching to match your monitor, and enter your monitor hertz in the launch parameters!
