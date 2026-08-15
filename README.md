🛠️ MTK Tool (v0.0.1.1 Alpha) (a build from 15.08.2026)

The tool is based on bkerler's mtkclient (huge thanks for processor's information and BROM handshake (beta testing))

More will be added soon.

Huge thanks to everyone who will give tips and/or find bugs on any stage of production. 


A lightweight Python utility for querying and managing MediaTek (MTK) processor configurations, including BROM/DA payload addresses, Watchdog register locations, and authentication requirements.



📋 Features



🔍 Flexible Search: Find processors by HW\_CODE (e.g., 0x717), commercial name (e.g., Helio G99), or SoC designation (e.g., MT6789).

🛡️ Protected Database: Immutably structured chip database to ensure data integrity during runtime.

📋 Comprehensive Chip Cards: Direct visibility into BROM payload addresses, DA payload addresses, DA execution modes (XFLASH, XML, LEGACY), Watchdog addresses, and SLA/DAA security flags.



📁 Project Structure



mtk-tool/

├── chips_db.py      # Chip database, search logic, and lookup functions

├── utils.py         # Utility functions and output formatting helpers

├── main.py          # Main entry point for the application

├── README.md        # Project documentation

├── LICENSE          # GPLv3 License

└── .gitignore       # Git exclusion rules



🚀 Getting Started

Prerequisites

Python 3.10 or higher.



Installation \& Usage

Clone the repository:

git clone https://github.com/Vsevolod1255/mtk-tool.git

cd mtk-tool



Run the project:

python main.py



License

Distributed under the GNU General Public License v3.0 (GPLv3). See LICENSE for more details.



Acknowledgements:

bkerler (creator of mtkclient) -> his BROM handshake will be implemented later in beta-testing

Chaosmaster and cyrozap (database of processors)

Updates information:
alpha-v.0.0.1.1 (build date: 2026-08-15) - small bugs fixed around the main menu, HWID, user_input. Main.py rewritten


