# ALL-CONFIGS Repository Structure 📁

## Directory Organization

```
ALL-CONFIGS/
│
├── 📋 ROOT FILES (Documentation & Configuration)
│   ├── README.md                    # Main project documentation
│   ├── CHANGELOG.md                 # Version history
│   ├── CONTRIBUTING.md              # Contributor guidelines
│   ├── CODE_OF_CONDUCT.md           # Community standards
│   ├── SECURITY.md                  # Security policy
│   ├── LICENSE                      # MIT License
│   ├── .gitignore                   # Git exclusions
│   └── STRUCTURE.md                 # This file
│
├── 📚 docs/ - DOCUMENTATION FOLDER
│   ├── guides/
│   │   ├── installation/
│   │   │   ├── CS2.md               # CS2 installation guide
│   │   │   ├── Valorant.md          # Valorant installation guide
│   │   │   └── OW2.md               # Overwatch 2 installation guide
│   │   │
│   │   ├── optimization/
│   │   │   ├── best-practices.md    # Best optimization practices
│   │   │   ├── cs2-guide.md         # CS2-specific tips
│   │   │   ├── valorant-guide.md    # Valorant-specific tips
│   │   │   └── ow2-guide.md         # OW2-specific tips
│   │   │
│   │   ├── hardware-requirements.md # GPU compatibility matrix
│   │   └── performance-tuning.md    # Advanced tuning guide
│   │
│   ├── troubleshooting/
│   │   ├── common-issues.md         # FAQ for problems
│   │   ├── config-conflicts.md      # Config conflict resolution
│   │   ├── driver-issues.md         # GPU driver problems
│   │   └── game-crashes.md          # Crash troubleshooting
│   │
│   ├── benchmarks/
│   │   ├── methodology.md           # How we benchmark
│   │   ├── results.md               # Benchmark results
│   │   └── hardware-database.md     # Hardware performance DB
│   │
│   └── FAQ.md                       # Frequently Asked Questions
│
├── 🎮 CS2/ - COUNTER-STRIKE 2 CONFIGS
│   ├── README.md                    # CS2-specific readme
│   ├── configs/
│   │   ├── nvidia/
│   │   │   ├── low-end/
│   │   │   │   ├── video.txt        # Video settings
│   │   │   │   ├── autoexec.cfg     # Exec config
│   │   │   │   └── README.md        # Config description
│   │   │   ├── mid-range/
│   │   │   │   ├── video.txt
│   │   │   │   ├── autoexec.cfg
│   │   │   │   └── README.md
│   │   │   └── high-end/
│   │   │       ├── video.txt
│   │   │       ├── autoexec.cfg
│   │   │       └── README.md
│   │   │
│   │   ├── amd/
│   │   │   ├── low-end/
│   │   │   ├── mid-range/
│   │   │   └── high-end/
│   │   │
│   │   └── intel/
│   │       ├── low-end/
│   │       ├── mid-range/
│   │       └── high-end/
│   │
│   └── benchmarks/
│       ├── results_2026_01.md      # January 2026 results
│       └── comparison.md            # GPU comparison
│
├── 🎯 Valorant/ - VALORANT CONFIGS
│   ├── README.md                    # Valorant-specific readme
│   ├── configs/
│   │   ├── nvidia/
│   │   │   ├── low-end/
│   │   │   ├── mid-range/
│   │   │   └── high-end/
│   │   ├── amd/
│   │   │   ├── low-end/
│   │   │   ├── mid-range/
│   │   │   └── high-end/
│   │   └── intel/
│   │       ├── low-end/
│   │       └── mid-range/
│   │
│   └── benchmarks/
│       └── results.md
│
├── 🕹️ Overwatch2/ - OVERWATCH 2 CONFIGS
│   ├── README.md                    # OW2-specific readme
│   ├── configs/
│   │   ├── nvidia/
│   │   │   ├── low-end/
│   │   │   ├── mid-range/
│   │   │   └── high-end/
│   │   └── amd/
│   │       ├── low-end/
│   │       └── mid-range/
│   │
│   └── benchmarks/
│       └── results.md
│
├── 🔧 scripts/ - INSTALLATION & UTILITY SCRIPTS
│   ├── README.md                    # Scripts documentation
│   ├── install.py                   # Universal Python installer
│   ├── install.bat                  # Windows batch installer
│   ├── install.sh                   # Linux/Mac shell installer
│   ├── verify.py                    # Config verification script
│   ├── benchmark.py                 # Benchmarking script
│   └── utils/
│       ├── config_parser.py         # Config file parser
│       └── gpu_detector.py          # GPU detection utility
│
├── 📸 screenshots/ - VISUAL ASSETS
│   ├── before-after/
│   │   ├── cs2_before.png
│   │   ├── cs2_after.png
│   │   ├── valorant_before.png
│   │   └── valorant_after.png
│   │
│   ├── installation/
│   │   ├── step1_download.png
│   │   ├── step2_extract.png
│   │   ├── step3_run.png
│   │   └── step4_complete.png
│   │
│   ├── benchmarks/
│   │   ├── fps_comparison.png
│   │   ├── gpu_comparison.png
│   │   └── results_chart.png
│   │
│   ├── guides/
│   │   ├── settings_menu.png
│   │   ├── console_commands.png
│   │   └── config_location.png
│   │
│   └── logos/
│       ├── all-configs-logo.png
│       ├── nvidia-badge.png
│       ├── amd-badge.png
│       └── intel-badge.png
│
├── 🌐 wiki/ - GITHUB WIKI FILES
│   ├── Home.md                      # Wiki home page
│   ├── Getting-Started.md           # Quick start guide
│   ├── Installation-Guide.md        # Detailed installation
│   ├── Configuration-Guide.md       # Config customization
│   ├── Troubleshooting-FAQ.md       # Common problems
│   ├── Hardware-Compatibility.md    # GPU compatibility
│   ├── Performance-Benchmarks.md    # Benchmark results
│   ├── Contributing-Guide.md        # How to contribute
│   ├── Roadmap.md                   # Project roadmap
│   ├── Glossary.md                  # Terms explained
│   ├── _Sidebar.md                  # Wiki navigation
│   └── _Footer.md                   # Wiki footer
│
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug-report.md           # Bug report template
│   │   ├── feature-request.md      # Feature request template
│   │   └── config-submission.md    # Config submission template
│   │
│   ├── PULL_REQUEST_TEMPLATE.md    # PR template
│   │
│   └── workflows/
│       ├── lint.yml                # Code linting
│       ├── validate.yml            # Config validation
│       └── release.yml             # Release automation
│
└── 📦 .gitignore                    # Git ignore rules

```

---

## File Descriptions

### Root Level Files

| File | Purpose |
|------|---------|
| **README.md** | Main documentation, quick start, features overview |
| **CHANGELOG.md** | Version history and changes log |
| **CONTRIBUTING.md** | Guidelines for contributors |
| **CODE_OF_CONDUCT.md** | Community standards and behavior |
| **SECURITY.md** | Security policy and vulnerability reporting |
| **LICENSE** | MIT License terms |
| **.gitignore** | Files to exclude from Git |
| **STRUCTURE.md** | This file - repository organization |

### Documentation (docs/)

| Folder | Contents |
|--------|----------|
| **guides/installation/** | Step-by-step installation for each game |
| **guides/optimization/** | Game-specific optimization tips |
| **troubleshooting/** | Common problems and solutions |
| **benchmarks/** | Performance test results and methodology |
| **FAQ.md** | Frequently asked questions |

### Game Configs

Each game folder contains:
- **configs/** - Configuration files organized by GPU and performance level
- **README.md** - Game-specific information
- **benchmarks/** - Performance results for that game

### Scripts (scripts/)

- **install.py** - Python installer (cross-platform)
- **install.bat** - Windows batch installer
- **install.sh** - Linux/Mac shell installer
- **verify.py** - Validates config files
- **benchmark.py** - Runs performance benchmarks
- **utils/** - Helper utilities and libraries

### Screenshots (screenshots/)

Organized by category:
- **before-after/** - Performance comparisons
- **installation/** - Setup process images
- **benchmarks/** - Performance charts
- **guides/** - Instructional images
- **logos/** - Project and brand assets

### Wiki (wiki/)

GitHub Wiki files for extended documentation:
- Getting started guides
- Detailed configuration instructions
- Community resources
- Navigation and sidebar

### GitHub Files (.github/)

Templates and workflows:
- Issue templates for bug reports and features
- Pull request template
- CI/CD workflows for automation

---

## File Naming Conventions

### Config Files
```
[game]-[gpu]-[level].cfg
Example: cs2-nvidia-high-end.cfg
```

### Documentation
```
[topic]-[detail].md
Example: installation-cs2.md
```

### Scripts
```
[action]-[platform].extension
Example: install-windows.bat
```

### Screenshots
```
[category]-[description].png
Example: benchmark-fps-comparison.png
```

---

## Configuration File Structure

Each config folder contains:

```
level-name/
├── README.md                # Config description & benchmarks
├── video.txt               # Video settings (if applicable)
├── autoexec.cfg            # Config commands
├── config.txt              # Additional settings
└── INSTALL.md              # Installation instructions
```

---

## Adding New Content

### New Game Config
```bash
mkdir -p [GameName]/configs/{nvidia,amd,intel}/{low-end,mid-range,high-end}
touch [GameName]/README.md
touch [GameName]/configs/nvidia/low-end/README.md
```

### New Documentation
```bash
touch docs/guides/[topic]/[subtopic].md
```

### New Script
```bash
touch scripts/[action].[extension]
chmod +x scripts/[action].sh  # For Unix scripts
```

---

## Important Notes

- **Never commit** personal configuration files
- **Always document** new configs with benchmarks
- **Keep structure** consistent and organized
- **Update CHANGELOG** when adding new content
- **Test thoroughly** before submitting
- **Follow naming** conventions for consistency

---

## Total File Count

- Documentation files: 20+
- Configuration examples: 50+
- Scripts: 5-10
- Screenshots: 20+
- Wiki pages: 10+

**Total: 100+ files**

---

## Quick Navigation

- 📖 [README](README.md) - Start here
- 🤝 [Contributing](CONTRIBUTING.md) - How to help
- 📝 [Changelog](CHANGELOG.md) - What's new
- 📚 [Docs](docs/) - Detailed guides
- 🔧 [Scripts](scripts/) - Installation tools
- 🎮 [Configs](CS2/, Valorant/, Overwatch2/) - Game configs

---

<div align="center">

**Last Updated:** January 2026  
**Version:** 1.0.0

[Back to README](README.md)

</div>