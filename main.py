"""======================= Main ======================="""
# NOTE: `main.py` is the file that has to be debugged/executed for the program to fully work.
# Runs main processes like command input and user data processing

import sys, os, unicodedata, time, shlex, subprocess, shutil
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1" # was tired of the pygame msg

def install_package(package_name): 
    try:
        # installation with uv
        subprocess.run(
            [sys.executable, "-m", "uv", "pip", "install", package_name],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        try:
            # fallback to pip
            subprocess.run(
                [sys.executable, "-m", "pip", "install", package_name],
                check=True,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )
            return True
        except subprocess.CalledProcessError: return False

def ensure_dependencies():
    print("EasySaxo will check all modules it needs to work properly. Please wait...\n")
    
    # ensure uv is available first before processing other packages
    try: __import__("uv")
    except ImportError:
        subprocess.run(
            [sys.executable, "-m", "pip", "install", "uv"],
            check=False, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
            )

    try: # using uv
        subprocess.run(
            [sys.executable, "-m", "uv", "pip", "uninstall", "pygame"], 
            check=False, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
        )
    except FileNotFoundError: #fallback to pip
        subprocess.run(
            [sys.executable, "-m", "pip", "uninstall", "pygame", "-y"], 
            check=False, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
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
        "cputil": "cputil",
        "cpuinfo": "cpuinfo",
        "gputil": "gputil",
        "ascii_magic": "ascii_magic",
    }

    for module_name, pip_name in required_packages.items():
        try: __import__(module_name)
        except ImportError:
            print(f"\n[Boot] Required dependency '{module_name}' not found.\n")
            if not install_package(pip_name):
                sys.exit(f"Critical Error: Cannot proceed without '{pip_name}'. Exiting.")

    for module_name, pip_name in optional_packages.items():
        try: __import__(module_name)
        except ImportError: install_package(pip_name)

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
except ImportError: RICH_AVAILABLE = False

# Prompt Toolkit support
try:
    from prompt_toolkit import PromptSession
    from prompt_toolkit.completion import WordCompleter
    from prompt_toolkit.patch_stdout import patch_stdout
    PROMPT_TOOLKIT_AVAILABLE = True
except ImportError: PROMPT_TOOLKIT_AVAILABLE = False

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
            for key, val in raw_data.items():
                if isinstance(val, dict): translations.update(val)
                else: translations[key] = val

    if session_info is None:
        preboot_file = None
        if len(sys.argv) > 1:
            if sys.argv[1].lower() == "load" and len(sys.argv) > 2: preboot_file = sys.argv[2]
            elif sys.argv[1].endswith(".json"): preboot_file = sys.argv[1]

        session_info = SessionManager.load_session(preboot_file)

    if isinstance(session_info, dict):
        ThreadData.current_user = session_info.get("user_name", "User")
        ThreadData.current_pswd = session_info.get("password")
    else: ThreadData.current_user = session_info
        
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
    
    while True:
        try:
            print()
            prompt_str = Fore.BLACK + Style.BRIGHT + f"{ThreadData.current_user} > " + Style.RESET_ALL
            
            if PROMPT_TOOLKIT_AVAILABLE:
                with patch_stdout(): usit = session.prompt(f"{ThreadData.current_user} > ").strip()
            else: usit = input(prompt_str).strip()
                
        except KeyboardInterrupt:
            extoken = input(f"{Fore.LIGHTBLACK_EX}Want to exit? (Y/N){Style.RESET_ALL}").lower()
            try:
                if extoken == "y":
                    SessionManager.save_session(ThreadData.current_user)
                    break
                else: continue
            except (KeyboardInterrupt, EOFError): break # aka subtle exit
        
        except EOFError: break
            
        if not usit: continue

        usit = unicodedata.normalize("NFKC", usit).strip()

        # parse inline suffix flags (" e" or " s")
        override_mode = None
        if usit.endswith(" e"):
            override_mode = "easysaxo"
            usit = usit[:-2].strip()
        elif usit.endswith(" s"):
            override_mode = "system"
            usit = usit[:-2].strip()

        # priority: Inline suffix flag -> ThreadData.target_mode -> "auto"
        effective_mode = override_mode if override_mode is not None else getattr(ThreadData, "target_mode", "auto")

        parts = usit.split(maxsplit=1)
        cmd = parts[0].lower()
        arg = parts[1] if len(parts) > 1 else None
        
        if cmd in translations: cmd = translations[cmd]
        
        if cmd in ["exit", "quit"]:
            SessionManager.save_session(ThreadData.current_user)
            break

        in_easysaxo = cmd in COMMAND_REGISTRY
        sys_binary = shutil.which(cmd)

        if effective_mode == "system": # forced syscmd
            if sys_binary:
                try: subprocess.run(usit, shell=True)
                except Exception as err: print(f"{Fore.RED}System command error: {err}{Style.RESET_ALL}")
            else: print(f"{Fore.RED}System command '{cmd}' not found in PATH.{Style.RESET_ALL}")
            
        elif effective_mode == "easysaxo": # forced escmd
            if in_easysaxo: COMMAND_REGISTRY[cmd](arg)
            else: print(f"{Fore.RED}EasySaxo command '{cmd}' not found.{Style.RESET_ALL}")
            
        else: # if our target match is auto
            if in_easysaxo: COMMAND_REGISTRY[cmd](arg)
            elif sys_binary:
                try: subprocess.run(usit, shell=True)
                except Exception as err: print(f"{Fore.RED}System command error: {err}{Style.RESET_ALL}")
                
            # easter egg support (built-in to hide from the user view)    
            elif cmd not in COMMAND_REGISTRY and enable_ee:
                if cmd == "getmeaneasteregg": commands.e1()
                elif cmd in ["noeasteregg", "falseget", "lookatthis", "lookatts"]: commands.e2()
                elif cmd == "osaka": commands.e3()
                elif cmd in ["del yourself", "jokecracker", "dumbass", "fuck you", "smd"]:
                    if commands.ee4: commands.e4()
                elif cmd in ["traceback", "error", "locateerror", "errorloc"]: commands.e5()
                else: print(f"{Fore.RED}Unknown command. Type 'help' for assistance.{Style.RESET_ALL}")
                
            #allow easter eggs (also hidden)
            elif cmd in ["secretenable", "enable_ee", "eastereggenable"] and scee:
                enable_ee = True
                scee = False
                print(f"{Fore.LIGHTBLACK_EX}Something happened.{Style.RESET_ALL} You have to find it out.")
            else: print(f"{Fore.RED}Unknown command. Type 'help' for assistance.{Style.RESET_ALL}")

if __name__ == "__main__":
    preboot_file = None
    #session loader
    if len(sys.argv) > 1:
        if sys.argv[1].lower() == "load" and len(sys.argv) > 2: preboot_file = sys.argv[2]
        elif sys.argv[1].endswith(".json"): preboot_file = sys.argv[1]

    session_data = SessionManager.load_session(preboot_file)
    if isinstance(session_data, dict):
        ThreadData.current_user = session_data.get("user_name", "User")
        ThreadData.current_pswd = session_data.get("password")
    else: ThreadData.current_user = session_data
    
    if ThreadData.current_pswd is not None: # password checker
        while True:
            keyacc = input(f"{Fore.LIGHTRED_EX}Insert password: {Style.RESET_ALL}{Fore.LIGHTBLACK_EX}")
            
            if keyacc == ThreadData.current_pswd:
                print(f"{Fore.LIGHTGREEN_EX}Opening app...{Style.RESET_ALL}")
                time.sleep(0.5)
                os.system('cls' if os.name == 'nt' else 'clear')
                break
                
            print(f"{Fore.RED}Wrong password, try again.{Style.RESET_ALL}\n")

    Core(session_info=session_data) # nothing special yet 