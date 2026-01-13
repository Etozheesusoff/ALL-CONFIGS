# **🎮 CS2 Configs — ALL-CONFIGS**

**Этот раздел содержит оптимизированные конфиги для **Counter-Strike 2**, разделённые по типу видеокарты и уровню производительности.**


---


## **📂 Структура**


```text
CS2/
  ├── README.md
  ├── configs/
  │   ├── nvidia/
  │   │   ├── low-end/
  │   │   │   ├── autoexec.cfg
  │   │   │   ├── video.txt
  │   │   │   └── README.md
  │   │   ├── mid-range/
  │   │   │   ├── autoexec.cfg
  │   │   │   ├── video.txt
  │   │   │   └── README.md
  │   │   └── high-end/
  │   │       ├── autoexec.cfg
  │   │       ├── video.txt
  │   │       └── README.md
  │   ├── amd/
  │   │   ├── low-end/autoexec.cfg
  │   │   ├── mid-range/video.txt
  │   │   └── high-end/README.md
  │   └── intel/
  │       ├── low-end/autoexec.cfg
  │       ├── mid-range/video.txt
  │       └── high-end/README.md
  └── benchmarks/
      └── results.md

```

---


## **🧬 Выбор пресета**

**Определите вашу GPU:** NVIDIA / AMD / Intel.

**Оцените уровень системы:**
* Low-end — старые/слабые видеокарты, 8 GB RAM;
* Mid-range — популярный мейнстрим (RTX 2060–3060, RX 5600–6600);
* High-end — топовые GPU и CPU.

**Перейдите в соответствующую папку и используйте файлы:**

	* autoexec.cfg — игровые настройки и сетевые параметры;
	* cs2_video.txt — графические настройки.


## **📁 Пути установки (Windows)**

**CS2 хранит конфиги примерно по пути:**

```text
C:\\Program Files (x86)\\Steam\\userdata\\<STEAM\_ID>\\730\\local\\cfg\\
```

**Рекомендуется:**

* Скопировать autoexec.cfg в эту папку;
* Убедиться, что в параметрах запуска CS2 есть: `+exec autoexec.cfg`;
* video.txt скопировать в папку пользовательских настроек CS2 (обычно тот же cfg или videosettings).


## **🧪 Тестирование**

**После установки:**

* Запустите CS2;
* Откройте консоль `~` и введите: `exec autoexec.cfg`, чтобы убедиться, что файл загружается.
* Сыграйте несколько матчей и оцените: **FPS**, **стабильность**, **input lag**.


## **🔗 Полезные материалы**

Общий гайд по оптимизации CS2:
docs/guides/optimization/cs2-guide.md

Общие best practices:
docs/guides/optimization/best-practices.md

Устранение проблем:
docs/troubleshooting/common-issues.md



