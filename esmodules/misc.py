from config import easysaxo
from colorama import Fore, Style
import time, importlib, os

# `misc.py` may handle miscellaneous data and functions.

# eslogo (20 minutes doing ts)

easysaxoLogo = r"""
                          [EasySaxo Alpha]
  |==============================================================
  |
            -----========-----             /----|   /\   |----\ 
        ----==================----         \----|  /^^\  |----/
      --======              ======--
    -=========              =========-             --=====--
    ==========      --------==========         ----=========----
    ==========      --================        --=====-----=====--
    ==========              ==========       -======-     -======-
    ==========              ==========       -=======-       --=-
    ==========      --================         -=======-
    ==========      --------==========   -=--       -=====-
    -=========              =========- -======-     -======-
      --======              ======--    --=====-----=====--
        ----==================----       ----=========----
            -----========-----               --=====--
                                                                 |
   ==============================================================|         
        """

# What's new
def whats_new():
    print(
        f"\n===== {Fore.CYAN}What's New!{Style.RESET_ALL} ({Fore.YELLOW}{easysaxo.name} v{easysaxo.ver}{Style.RESET_ALL}) =====\n"
        f"2. Added commands: {Fore.BLUE}render, unins{Style.RESET_ALL}.\n"
        f"2. Fixed {Fore.LIGHTGREEN_EX}code & miscellaneous{Style.RESET_ALL} bugs.\n"
        f"3. Modified {Fore.GREEN}module installer/checking{Style.RESET_ALL}.\n"
    )

# Time and Date
def hrs():
    print(f"Time: {time.strftime('%H:%M:%S')}.")
    print(f"Date: {time.strftime('%Y-%m-%d')}.")

# Status Handler for modules

class StatusHandler:
    def __init__(self, label_width=25):
        self.ok = f"{Fore.GREEN}OK{Style.RESET_ALL}"
        self.er = f"{Fore.RED}ERROR{Style.RESET_ALL}"
        self.label_width = label_width

    def print_status(self, label: str, success: bool, extra_info: str = ""):
        status = self.ok if success else self.er
        print(f"{label:<{self.label_width}}: [{status}] {extra_info}".strip())

    def check_imports(self, modules: list[str]):
        all_success = True
        for mod in modules:
            try:
                importlib.import_module(mod)
                self.print_status(f"Module {Fore.BLUE}{mod.upper()}{Style.RESET_ALL}", success=True)
            except ImportError as e:
                self.print_status(f"Module {Fore.BLUE}{mod.upper()}{Style.RESET_ALL}", success=False, extra_info=str(e))
                all_success = False
        return all_success

StHd = StatusHandler(label_width=20)
required_modules = [
    "os", "sys", "re", "time", "subprocess", "platform", "random", "locale",
    "psutil", "json", "math", "pygame", "threading", "socket", "colorama", "rich", "prompt_toolkit",
    "gputil", "cputil", "cpuinfo", "importlib",
]

def module_importing():
    StHd.check_imports(required_modules)
    print()

module_importing()
time.sleep(2)

os.system("cls" if os.name == "nt" else "clear")

# misc.py shall live argargagrgragragra