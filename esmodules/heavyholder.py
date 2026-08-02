#=================================================
# Threading + Session Saving-Loading
#=================================================

# `heavyholder.py` ONLY FOR COMPLEX TASK & OVERLAP COMMAND DEFINING
# you know what else is heavy?

import threading, os, json, time
from colorama import Fore, Style
from esmodules.dirloct import base_dir, DirLocation
from esmodules.mathf import MathFunc

try:
    from prompt_toolkit.formatted_text import HTML
    from prompt_toolkit import print_formatted_text
    PROMPT_TOOLKIT_AVAILABLE = True
except ImportError:
    PROMPT_TOOLKIT_AVAILABLE = False
    HTML = None
    print_formatted_text = None

class ThreadData:
    current_user = "User"
    current_pswd = None
    # why storing this here? to make ezsaxo less comprehensible

    @staticmethod
    def getthreads():
        print(f"Active background threads: {Fore.GREEN}{threading.active_count()}{Style.RESET_ALL}")

    @staticmethod
    def _timer_task(seconds, message):
        time.sleep(seconds)
        if PROMPT_TOOLKIT_AVAILABLE: print_formatted_text(HTML(f"<ansiyellow>==== [TIMER ALERT]: {message} ====</ansiyellow>"))
        else: print(f"\n{Fore.YELLOW}==== [TIMER ALERT]: {message} ===={Style.RESET_ALL}\n")

    @staticmethod
    def set_timer(seconds, message):
        try:
            sec = int(seconds)
            msg = message if message else "Timer finished!"
            threading.Thread(target=ThreadData._timer_task, args=(sec, msg), daemon=True).start()
            print(f"Timer set for {Fore.CYAN}{sec} seconds{Style.RESET_ALL} in the background.")
        except ValueError: print(f"{Fore.RED}Please provide a valid integer for seconds.{Style.RESET_ALL}")
        
class SessionManager:
    active_session_file = os.path.join(base_dir, "session.json")

    @staticmethod
    def save_session(user_name: str = None, filepath: str = None):
        uname = user_name if user_name else ThreadData.current_user
        target = DirLocation._resolve_path(filepath) if filepath else SessionManager.active_session_file
        user_vars = {k: v for k, v in MathFunc.mathset.items() if k not in MathFunc._reserved}
        try:
            with open(target, "w", encoding="utf-8") as f:
                json.dump({
                    "user_name": uname, 
                    "variables": user_vars, 
                    "password": ThreadData.current_pswd # Use ThreadData's password variable!
                }, f, indent=4)
            SessionManager.active_session_file = target
            print(f"{Fore.GREEN}Session saved successfully to '{os.path.basename(target)}'.{Style.RESET_ALL}")
        except Exception as e: print(f"{Fore.RED}Error saving session: {e}{Style.RESET_ALL}")

    @staticmethod
    def load_session(filepath: str = None) -> dict:
        target = DirLocation._resolve_path(filepath) if filepath else SessionManager.active_session_file
        default_data = {"user_name": "User", "password": None}

        if not os.path.exists(target): 
            return default_data

        try:
            # Check if file is empty (0 bytes) before attempting json.load
            if os.path.getsize(target) == 0:
                return default_data

            with open(target, "r", encoding="utf-8") as f: 
                data = json.load(f)

            user_name = data.get("user_name", "User")
            password = data.get("password", None)

            for k in [k for k in MathFunc.mathset.keys() if k not in MathFunc._reserved]: 
                del MathFunc.mathset[k]
            for var_name, value in data.get("variables", {}).items(): 
                MathFunc.mathset[var_name] = value

            SessionManager.active_session_file = target
            print(f"{Fore.CYAN}Loaded session from '{os.path.basename(target)}' for user '{user_name}'.{Style.RESET_ALL}")
        
            return {"user_name": user_name, "password": password}

        except (json.JSONDecodeError, Exception) as e:
            print(f"{Fore.RED}Failed to load session: {e}{Style.RESET_ALL}")
            return default_data
        
# 100 lines pretty please?

# there u go