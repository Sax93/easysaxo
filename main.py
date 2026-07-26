"""======================= Main ======================="""

import sys
import unicodedata
from config import easysaxo, COMMAND_REGISTRY
import commands
from esmodules.heavyholder import ThreadData, SessionManager

# Sub for successful boot
try:
    from colorama import Fore, Style, just_fix_windows_console
    just_fix_windows_console()
    print(Fore.GREEN + "Colorama loaded successfully." + Style.RESET_ALL)
except ImportError as e:
    print("Failed to load Colorama:", e)
    sys.exit()

try:
    from rich.console import Console
    from rich.table import Table
    console = Console()
    RICH_AVAILABLE = True
except ImportError:
    RICH_AVAILABLE = False
    print(Fore.YELLOW + "Recommendation: 'pip install rich' for enhanced tables." + Style.RESET_ALL)

try:
    from prompt_toolkit import PromptSession
    from prompt_toolkit.completion import WordCompleter
    from prompt_toolkit.patch_stdout import patch_stdout
    PROMPT_TOOLKIT_AVAILABLE = True
except ImportError:
    PROMPT_TOOLKIT_AVAILABLE = False
    print(Fore.YELLOW + "Recommendation: 'pip install prompt_toolkit' for non-blocking timers." + Style.RESET_ALL)

#=================================================
# Core main loop
#=================================================
def Core():
    TRANSLATIONS = {
        "へるぷ": "help", "たすけ": "help", "herupu": "help", "おわる": "exit", "じかん": "time", "ふぁっくよう": "exit",
        "ayuda": "help", "salir": "exit", "tiempo": "time", "hora": "time", "guardar": "save", "cargar": "load",
        "aide": "help", "quitter": "exit", "temps": "time", "heure": "time", "sauvegarder": "save",
        "hilfe": "help", "beenden": "exit", "zeit": "time", "speichern": "save",
        "ajuda": "help", "sair": "exit", "tempo": "time", "salvar": "save",
        "aiuto": "help", "esci": "exit", "salva": "save",
        "помощь": "help", "выход": "exit", "время": "time", "pomosh": "help", "vyhod": "exit",
    }

    preboot_file = None
    if len(sys.argv) > 1:
        if sys.argv[1].lower() == "load" and len(sys.argv) > 2: preboot_file = sys.argv[2]
        elif sys.argv[1].endswith(".json"): preboot_file = sys.argv[1]

    ThreadData.current_user = SessionManager.load_session(preboot_file)

    print(f"Welcome to {Fore.CYAN}{easysaxo.name}{Style.RESET_ALL}! Insert commands down below.")

    if PROMPT_TOOLKIT_AVAILABLE:
        completer = WordCompleter(list(COMMAND_REGISTRY.keys()) + list(TRANSLATIONS.keys()), ignore_case=True)
        session = PromptSession(completer=completer)
    else:
        try:
            import readline
            def completer(text, state):
                options = [cmd for cmd in list(COMMAND_REGISTRY.keys()) if cmd.startswith(text)]
                return options[state] if state < len(options) else None
            readline.set_completer(completer)
            readline.parse_and_bind("tab: complete")
        except ImportError: pass

    # ==== Main Loop ====
    
    while True:
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
        
        if cmd in TRANSLATIONS: cmd = TRANSLATIONS[cmd]

        if cmd in ["exit", "quit"]:
            SessionManager.save_session(ThreadData.current_user)
            break
        elif cmd in COMMAND_REGISTRY: COMMAND_REGISTRY[cmd](arg)
        else: print(f"{Fore.RED}Unknown command. Type 'help' for assistance.{Style.RESET_ALL}")

if __name__ == "__main__":
    Core()