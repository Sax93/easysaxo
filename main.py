"""======================= Main ======================="""
# NOTE: `main.py` is the file that has to be debugged/executed for the program to fully work.
# Runs main processes like command input and user data processing

import sys, os, unicodedata, time, shlex, subprocess

def install_package(package_name):
    try:
        print(f"[Auto-Installer] Installing missing package via uv: {package_name}...")
        # Uses `uv pip install` inside the active Python environment
        subprocess.run(
            [sys.executable, "-m", "uv", "pip", "install", package_name],
            check=True
        )
        print(f"[Auto-Installer] Successfully installed {package_name}!")
        return True
    except (subprocess.CalledProcessError, FileNotFoundError) as e:
        # Fallback to standard pip if uv isn't installed in the environment yet
        print(f"[Auto-Installer] 'uv' failed or not found ({e}). Falling back to standard pip...")
        try:
            subprocess.run(
                [sys.executable, "-m", "pip", "install", package_name],
                check=True
            )
            print(f"[Auto-Installer] Successfully installed {package_name} via pip!")
            return True
        except subprocess.CalledProcessError as pip_error:
            print(f"[Auto-Installer] Failed to install {package_name}. Error: {pip_error}")
            return False

def ensure_dependencies():
    """Checks required and optional dependencies, installing them if missing."""
    
    # ensure uv is available first before processing other packages
    try:
        __import__("uv")
    except ImportError:
        print("[Boot] 'uv' package installer not found. Installing 'uv'...")
        subprocess.run([sys.executable, "-m", "pip", "install", "uv"], check=False)

    try: # using uv
        print("[Auto-Installer] Clearing out standard pygame to prevent conflicts...")
        subprocess.run(
            [sys.executable, "-m", "uv", "pip", "uninstall", "pygame"], 
            check=False
        )
    except FileNotFoundError: #fallback to pip
        subprocess.run(
            [sys.executable, "-m", "pip", "uninstall", "pygame", "-y"], 
            check=False
        )
    
    required_packages = {
        "colorama": "colorama",
    }
    
    optional_packages = {
        "rich": "rich",
        "prompt_toolkit": "prompt_toolkit",
        "psutil": "psutil",
        "cpuinfo": "py-cpuinfo",
        "speedtest": "speedtest-cli",
        "pygame": "pygame-ce",
    }

    for module_name, pip_name in required_packages.items():
        try:
            __import__(module_name)
        except ImportError:
            print(f"[Boot] Required dependency '{module_name}' not found.")
            if not install_package(pip_name):
                sys.exit(f"Critical Error: Cannot proceed without '{pip_name}'. Exiting.")

    for module_name, pip_name in optional_packages.items():
        try:
            __import__(module_name)
        except ImportError:
            print(f"[Boot] Optional dependency '{module_name}' not found.")
            install_package(pip_name)

ensure_dependencies()

# if this code works, it was written by sxf
# if it doesnt, ion know who did :p

# =================================================
# Imports directly in Main File
# =================================================

from colorama import Fore, Style, just_fix_windows_console
just_fix_windows_console()

# Import project modules
from config import easysaxo, COMMAND_REGISTRY
import commands
from esmodules.heavyholder import ThreadData, SessionManager

# Rich support
try:
    from rich.console import Console
    from rich.table import Table
    console = Console()
    RICH_AVAILABLE = True
except ImportError:
    RICH_AVAILABLE = False

# Prompt Toolkit support
try:
    from prompt_toolkit import PromptSession
    from prompt_toolkit.completion import WordCompleter
    from prompt_toolkit.patch_stdout import patch_stdout
    PROMPT_TOOLKIT_AVAILABLE = True
except ImportError:
    PROMPT_TOOLKIT_AVAILABLE = False

#=================================================
# Core main loop
#=================================================
def Core(session_info=None):
    enable_ee = False
    scee = True
    import json
    from pathlib import Path
    
    Tdir = Path(__file__).resolve().parent
    TRANSLATIONS_FILE = Tdir / "translations.json"
    
    translations = {}
    if TRANSLATIONS_FILE.exists():
        with open(TRANSLATIONS_FILE, "r", encoding="utf-8") as f:
            raw_data = json.load(f)
            
            # Unpack nested dictionaries ("es", "ja", etc.) into a single lookup dict
            for key, val in raw_data.items():
                if isinstance(val, dict):
                    translations.update(val)
                else:
                    translations[key] = val

    if session_info is None:
        preboot_file = None
        if len(sys.argv) > 1:
            if sys.argv[1].lower() == "load" and len(sys.argv) > 2: preboot_file = sys.argv[2]
            elif sys.argv[1].endswith(".json"): preboot_file = sys.argv[1]

        session_info = SessionManager.load_session(preboot_file)

    if isinstance(session_info, dict):
        ThreadData.current_user = session_info.get("user_name", "User")
        ThreadData.current_pswd = session_info.get("password")
    else:
        ThreadData.current_user = session_info
        
    print(f"Welcome to {Fore.CYAN}{easysaxo.name}{Style.RESET_ALL}! Insert commands down below.")

    all_commands = list(COMMAND_REGISTRY.keys()) + list(translations.keys())

    if PROMPT_TOOLKIT_AVAILABLE:
        completer = WordCompleter(all_commands, ignore_case=True)
        session = PromptSession(completer=completer)
    else:
        try:
            import readline
            def completer(text, state):
                options = [c for c in all_commands if c.startswith(text)]
                return options[state] if state < len(options) else None
            readline.set_completer(completer)
            readline.parse_and_bind("tab: complete")
        except ImportError: pass

    # ==== Main Loop ====
    
    while True: #bc sxf doesnt know how to create good loops
        try:
            print()
            prompt_str = Fore.BLACK + Style.BRIGHT + f"[{ThreadData.current_user}]: " + Style.RESET_ALL
            
            if PROMPT_TOOLKIT_AVAILABLE:
                with patch_stdout(): usit = session.prompt(f"[{ThreadData.current_user}]: ").strip()
            else: usit = input(prompt_str).strip()
                
        except (KeyboardInterrupt, EOFError): break
        if not usit: continue

        usit = unicodedata.normalize("NFKC", usit).strip()
        parts = usit.split(maxsplit=1)
        cmd = parts[0].lower()
        arg = parts[1] if len(parts) > 1 else None
        
        if cmd in translations: 
            cmd = translations[cmd]
        
        if cmd in ["exit", "quit"]:
            SessionManager.save_session(ThreadData.current_user)
            break
        elif cmd in COMMAND_REGISTRY: COMMAND_REGISTRY[cmd](arg)
        elif cmd not in COMMAND_REGISTRY and enable_ee:
            if cmd == "getmeaneasteregg": commands.e1()
            elif cmd in ["noeasteregg", "falseget", "lookatthis", "lookatts"]: commands.e2()
            elif cmd == "osaka": commands.e3()
            elif cmd in ["del yourself", "jokecracker", "dumbass", "fuck you", "smd"]:
                if commands.ee4: commands.e4()
            elif cmd in ["traceback", "error", "locateerror", "errorloc"]: commands.e5()
            else: print(f"{Fore.RED}Unknown command. Type 'help' for assistance.{Style.RESET_ALL}")
        elif cmd in ["secretenable", "enable_ee", "eastereggenable"] and scee:
            enable_ee = True
            scee = False
            print(f"{Fore.LIGHTBLACK_EX}Something happened.{Style.RESET_ALL} You have to find it out.")
        else: print(f"{Fore.RED}Unknown command. Type 'help' for assistance.{Style.RESET_ALL}")

if __name__ == "__main__":
    preboot_file = None
    if len(sys.argv) > 1:
        if sys.argv[1].lower() == "load" and len(sys.argv) > 2: preboot_file = sys.argv[2]
        elif sys.argv[1].endswith(".json"): preboot_file = sys.argv[1]

    session_data = SessionManager.load_session(preboot_file)
    if isinstance(session_data, dict):
        ThreadData.current_user = session_data.get("user_name", "User")
        ThreadData.current_pswd = session_data.get("password")
    else:
        ThreadData.current_user = session_data
    
    if ThreadData.current_pswd is not None:
        while True:
            keyacc = input(f"{Fore.LIGHTRED_EX}Insert password: {Style.RESET_ALL}{Fore.LIGHTBLACK_EX}")
            
            if keyacc == ThreadData.current_pswd:
                print(f"{Fore.LIGHTGREEN_EX}Opening app...{Style.RESET_ALL}")
                time.sleep(0.5)
                os.system('cls' if os.name == 'nt' else 'clear')
                break
                
            print(f"{Fore.RED}Wrong password, try again.{Style.RESET_ALL}\n")

    Core(session_info=session_data) # yoooo im the 224th line yay