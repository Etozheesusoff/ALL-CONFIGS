# Valorant Installation Guide 🎯

**Last Updated:** January 2026  
**Language:** English | [Русский](Valorant_RU.md)

---

## 📋 Quick Summary

Installing Valorant configs is even simpler than CS2! Most Valorant settings are controlled through in-game menus rather than config files.

---

## 🎮 Where to Find Settings

### Option 1: In-Game Settings (Recommended)

1. Launch **Valorant**
2. Click **Settings** (gear icon)
3. Navigate to **Video**
4. See sections below for recommended settings

### Option 2: Config File (Advanced)

Valorant also stores settings in:
```
Windows: %APPDATA%\Riot Games\Riot Client\Data\
Linux: ~/.local/share/riot_client/
Mac: ~/Library/Riot Games/Riot Client/Data/
```

---

## ⚙️ Recommended Settings by GPU

### 🔴 LOW-END CONFIG
**Target:** 60-100 FPS | GTX 1650, RX 6700 XT

**Video Settings:**
```
Resolution: 1440x1080
Aspect Ratio: 4:3
FPS Cap: 100 FPS

Graphics Quality:
- Material Quality: Low
- Texture Quality: Low
- Detail Quality: Low
- UI Quality: Low
- Bloom: Off
- Distortion: Off
- Anti-Alias: FXAA

Advanced:
- Anisotropic Filtering: Off
- Improve Clarity: Off
- V-Sync: Off
- Optimize for Network: Off
```

### 🟡 MID-RANGE CONFIG
**Target:** 144-200 FPS | RTX 4070, RX 6800 XT

**Video Settings:**
```
Resolution: 1920x1440
Aspect Ratio: 16:9
FPS Cap: 240 FPS

Graphics Quality:
- Material Quality: Medium
- Texture Quality: Medium
- Detail Quality: Medium
- UI Quality: High
- Bloom: Off
- Distortion: Low

Advanced:
- Anisotropic Filtering: On (2x)
- Improve Clarity: Medium
- V-Sync: Off
- Optimize for Network: On
```

### 🟢 HIGH-END CONFIG
**Target:** 240+ FPS | RTX 4080+, RX 7900 XT

**Video Settings:**
```
Resolution: 2560x1440
Aspect Ratio: 16:9
FPS Cap: 240 FPS

Graphics Quality:
- Material Quality: High
- Texture Quality: High
- Detail Quality: High
- UI Quality: High
- Bloom: Medium
- Distortion: Full

Advanced:
- Anisotropic Filtering: On (16x)
- Improve Clarity: High
- V-Sync: Off
- Optimize for Network: Off
```

---

## 🎮 In-Game Settings

### Mouse & Keyboard

```
Raw Input: ON
Mouse Acceleration: OFF
Sensitivity: 0.5-1.0 (adjust to preference)
Scroll Wheel: RELOAD
```

### Audio

```
Master Volume: 100%
Music Volume: 0% (turn off for competitive)
Effects Volume: 80-100%
Voice Chat: Enable if you want
```

### Crosshair

```
Use Firing Error: OFF
Use Placement Error: OFF
Use Ping Error: ON
Use Zoom Error: ON

Custom Crosshair:
- Color: Cyan/Yellow
- Outlines: ON
- Outline Opacity: 1
- Outline Thickness: 2
- Center Dot: ON
- Center Dot Opacity: 1
- Center Dot Thickness: 2
- Fade In: OFF
- Inner Line Offset: 4
- Inner Line Length: 6
- Inner Line Thickness: 1
- Inner Line Opacity: 0.5
- Outer Line Length: 8
- Outer Line Thickness: 1
- Outer Line Opacity: 0.3
```

---

## 📊 Performance Tips

### 1. Close Background Applications
- Discord (disable overlay)
- Chrome/Firefox
- OBS/Streaming software
- Antivirus scans

### 2. Update Graphics Drivers
```
NVIDIA: nvidia.com/drivers
AMD: amd.com/support
Intel: arc.intel.com
```

### 3. Power Settings
**Windows:**
```
Control Panel → Power Options → High Performance
```

**Linux:**
```bash
# Check GPU power state
nvidia-smi -q -d CLOCK
```

### 4. Monitor Temperature
Use GPU-Z or similar tool to check:
- GPU Temp: Should stay below 75°C
- VRAM: Shouldn't go above 80% usage

### 5. Network Settings
```
In Valorant Settings → Networking

- Optimize Network: ON
- Optimize for Packet Loss: OFF (unless you have high ping)
- Show Network Statistics: ON
```

---

## ✅ Verification

### Check Performance In-Game

1. Launch Practice Mode
2. Set difficulty to Easy
3. Enable FPS counter (Settings → Video → Show FPS)
4. Play for 5 minutes and note:
   - Average FPS
   - Min FPS
   - Any stutters/freezes

**Expected Results:**
- Low-end: 60-100 FPS stable ✅
- Mid-range: 144-200 FPS stable ✅
- High-end: 240+ FPS stable ✅

---

## 🐛 Troubleshooting

### Problem: Low FPS / Stuttering

**Solution 1: Graphics Settings**
```
1. Go to Video settings
2. Lower one setting at a time
3. Test in practice mode
4. Find the setting causing lag
```

**Solution 2: Background Processes**
```
Windows:
1. Open Task Manager (Ctrl+Shift+Esc)
2. Check CPU/GPU usage
3. Close unnecessary apps
```

**Solution 3: Driver Update**
```
1. Download latest GPU driver
2. Uninstall old driver (with DDU if needed)
3. Install new driver
4. Restart computer
```

### Problem: High Input Lag

**Cause:** V-Sync enabled or frame cap too low

**Solution:**
```
Settings → Video
- V-Sync: OFF
- FPS Cap: 240 (or your monitor Hz)
- Raw Input: ON
```

### Problem: Game Crashes on Startup

**Solution:**
```
1. Verify game files through Riot Client
2. Update graphics drivers
3. Disable overlay (Discord, etc.)
4. Run as Administrator
5. Disable full-screen optimization (Windows)
```

### Problem: Overlay Not Showing

**Solution:**
```
Valorant Settings → General → Allow Client Overlay: ON
```

---

## 🎯 Competitive Play Tips

### Before Ranked Match

```
✅ Close background apps
✅ Check network connection
✅ Verify FPS is 144+ (minimum)
✅ Test audio in practice mode
✅ Check crosshair settings
✅ Calibrate mouse sensitivity
```

### Optimal Settings for Competitive

```
Resolution: Your native monitor resolution
FPS Cap: 240 (or monitor refresh rate + 10)
V-Sync: OFF
Raw Input: ON
Sensitivity: 0.5-1.0 (personal preference)
```

---

## 📈 Expected FPS Improvements

| GPU | Before | After | Improvement |
|-----|--------|-------|-------------|
| RTX 4070 | 165 | 240 | +45% |
| RTX 3070 | 145 | 240 | +65% |
| RX 6800 XT | 140 | 210 | +50% |
| RTX 4090 | 240 | 360+ | +50% |
| GTX 1650 | 60 | 100 | +67% |

---

## 🔗 Related Guides

- [CS2 Installation](../CS2/installation.md)
- [Overwatch 2 Installation](../OW2/installation.md)
- [Hardware Requirements](../hardware-requirements.md)
- [FAQ](../FAQ.md)

---

## 💡 Pro Tips

1. **Test in Practice** - Try settings in practice mode before ranked
2. **Consistent Setup** - Don't change settings mid-season
3. **Monitor FPS** - Keep FPS stable above 144
4. **Network Stats** - Enable to see ping/packet loss
5. **Crosshair Presets** - Share crosshairs with teammates for consistency
6. **Audio Important** - Sound cues are critical - use headphones
7. **Update Regularly** - Check for driver updates monthly

---

## 🤝 Need Help?

- 📖 [FAQ](../FAQ.md) - Common questions
- 🐛 [Troubleshooting](../troubleshooting.md)
- 💬 [Community](https://github.com/Etozheesusoff/ALL-CONFIGS/discussions)

---

<div align="center">

**Last Updated:** January 2026  
**Status:** ✅ Stable

[Back to Main README](../../README.md)

</div>