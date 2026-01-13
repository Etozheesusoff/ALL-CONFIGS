#!/usr/bin/env python3
"""
ALL-CONFIGS Universal Installer
Works on Windows, Linux, and Mac
Automatically installs optimized game configs
"""

import os
import sys
import platform
import shutil
from pathlib import Path

VERSION = "1.0.0"

def print_header():
    """Print welcome header"""
    print("\n" + "="*60)
    print("🎮 ALL-CONFIGS UNIVERSAL INSTALLER v" + VERSION)
    print("="*60)
    print("Counter-Strike 2 | Valorant | Overwatch 2")
    print("="*60 + "\n")

def select_game():
    """Select game to install configs for"""
    print("📌 SELECT GAME:")
    print("─" * 40)
    print("1. Counter-Strike 2")
    print("2. Valorant")
    print("3. Overwatch 2")
    print("0. Exit\n")
    
    while True:
        choice = input("Enter number (0-3): ").strip()
        if choice in ["0", "1", "2", "3"]:
            return choice
        print("❌ Invalid choice. Try again.\n")

def select_gpu():
    """Select GPU manufacturer"""
    print("\n📌 SELECT GPU MANUFACTURER:")
    print("─" * 40)
    print("1. NVIDIA")
    print("2. AMD")
    print("3. Intel")
    print("0. Back\n")
    
    while True:
        choice = input("Enter number (0-3): ").strip()
        if choice in ["0", "1", "2", "3"]:
            return choice
        print("❌ Invalid choice. Try again.\n")

def select_level():
    """Select performance level"""
    print("\n📌 SELECT PERFORMANCE LEVEL:")
    print("─" * 40)
    print("1. Low-end (60-100 FPS)")
    print("   GTX 1650, RX 6700 XT, Arc A750")
    print()
    print("2. Mid-range (144-200 FPS)")
    print("   RTX 4070, RX 6800 XT, Arc A770")
    print()
    print("3. High-end (240+ FPS)")
    print("   RTX 4090, RX 7900 XTX")
    print()
    print("0. Back\n")
    
    while True:
        choice = input("Enter number (0-3): ").strip()
        if choice in ["0", "1", "2", "3"]:
            return choice
        print("❌ Invalid choice. Try again.\n")

def map_choices(game, gpu, level):
    """Map choices to folder names"""
    games = {"1": "CS2", "2": "Valorant", "3": "Overwatch2"}
    gpus = {"1": "nvidia", "2": "amd", "3": "intel"}
    levels = {"1": "low-end", "2": "mid-range", "3": "high-end"}
    
    game_name = games.get(game, "unknown")
    gpu_name = gpus.get(gpu, "unknown")
    level_name = levels.get(level, "unknown")
    
    return game_name, gpu_name, level_name

def find_game_path(game):
    """Find game installation path"""
    system = platform.system()
    game_paths = {
        "CS2": {
            "Windows": "C:\\Program Files (x86)\\Steam\\steamapps\\common\\Counter-Strike Global Offensive\\game\\csgo\\cfg",
            "Linux": "~/.steam/root/steamapps/common/Counter-Strike Global Offensive/game/csgo/cfg",
            "Darwin": "~/Library/Application Support/Steam/steamapps/common/Counter-Strike Global Offensive/game/csgo/cfg"
        },
        "Valorant": {
            "Windows": "%APPDATA%\\Riot Games\\Riot Client\\Data",
            "Linux": "~/.local/share/riot_client",
            "Darwin": "~/Library/Riot Games/Riot Client/Data"
        },
        "Overwatch2": {
            "Windows": "C:\\Program Files\\Overwatch\\Config",
            "Linux": "~/.local/share/overwatch",
            "Darwin": "~/Library/Application Support/Blizzard/Overwatch"
        }
    }
    
    if game in game_paths and system in game_paths[game]:
        path = game_paths[game][system]
        path = os.path.expanduser(path)
        path = os.path.expandvars(path)
        return path
    return None

def create_backup(config_path):
    """Create backup of existing configs"""
    if not os.path.exists(config_path):
        print(f"⚠️  Config path doesn't exist: {config_path}")
        return False
    
    backup_path = config_path + "_backup"
    if os.path.exists(backup_path):
        print(f"✅ Backup already exists: {backup_path}")
        return True
    
    try:
        shutil.copytree(config_path, backup_path)
        print(f"✅ Backup created: {backup_path}")
        return True
    except Exception as e:
        print(f"❌ Error creating backup: {e}")
        return False

def copy_configs(source, destination):
    """Copy config files"""
    if not os.path.exists(source):
        print(f"❌ Source not found: {source}")
        return False
    
    if not os.path.exists(destination):
        print(f"❌ Destination not found: {destination}")
        return False
    
    try:
        for file in os.listdir(source):
            src = os.path.join(source, file)
            dst = os.path.join(destination, file)
            if os.path.isfile(src):
                shutil.copy2(src, dst)
                print(f"  ✓ Copied: {file}")
        return True
    except Exception as e:
        print(f"❌ Error copying files: {e}")
        return False

def set_readonly(path):
    """Set config files to read-only"""
    try:
        for file in os.listdir(path):
            filepath = os.path.join(path, file)
            if os.path.isfile(filepath):
                os.chmod(filepath, 0o444)
        print("✅ Files set to read-only")
        return True
    except Exception as e:
        print(f"⚠️  Could not set read-only: {e}")
        return True  # Not critical

def main():
    """Main installer function"""
    print_header()
    
    # Select game
    game_choice = select_game()
    if game_choice == "0":
        print("👋 Goodbye!\n")
        return
    
    # Select GPU
    gpu_choice = select_gpu()
    if gpu_choice == "0":
        return main()
    
    # Select level
    level_choice = select_level()
    if level_choice == "0":
        return main()
    
    # Map choices
    game, gpu, level = map_choices(game_choice, gpu_choice, level_choice)
    
    print(f"\n📦 INSTALLATION SUMMARY:")
    print("─" * 40)
    print(f"Game: {game}")
    print(f"GPU: {gpu.upper()}")
    print(f"Level: {level}")
    print()
    
    # Find game path
    game_path = find_game_path(game)
    if not game_path:
        print("❌ Could not find game installation!")
        print(f"Please install {game} first.\n")
        return
    
    print(f"Config path: {game_path}\n")
    
    # Confirm
    confirm = input("Continue with installation? (yes/no): ").strip().lower()
    if confirm not in ["yes", "y"]:
        print("❌ Installation cancelled.\n")
        return
    
    # Create backup
    print("\n⏳ Creating backup...")
    if not create_backup(game_path):
        print("⚠️  Continue anyway? (yes/no): ", end="")
        if input().strip().lower() not in ["yes", "y"]:
            return
    
    # Copy configs
    print("\n⏳ Copying config files...")
    source_path = os.path.join(f"./{game}/configs/{gpu}/{level}")
    
    if not os.path.exists(source_path):
        print(f"❌ Config files not found: {source_path}")
        print("Make sure you're running this script from ALL-CONFIGS directory.\n")
        return
    
    if not copy_configs(source_path, game_path):
        print("❌ Installation failed!\n")
        return
    
    # Set read-only
    print("\n⏳ Setting permissions...")
    set_readonly(game_path)
    
    # Success message
    print("\n" + "="*60)
    print("✅ INSTALLATION SUCCESSFUL!")
    print("="*60)
    print(f"\n✨ {game} configs installed successfully!")
    print("\n📋 NEXT STEPS:")
    print("1. Close and reopen your game")
    print("2. Configs should load automatically")
    print("3. Check in-game settings to verify")
    print("4. Test in practice mode first")
    print("\n💡 If something goes wrong:")
    print(f"   Restore from: {game_path}_backup\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⏹️  Installation cancelled.\n")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}\n")
        sys.exit(1)