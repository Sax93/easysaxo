#=================================================
# JSON and Regex Processing
#=================================================

from esmodules.dirloct import DirLocation
import os, json, re
from colorama import Fore, Style

class JsonData:
    @staticmethod
    def jsonrd(filepath):
        try:
            full_path = DirLocation._resolve_path(filepath)
            if os.path.exists(full_path):
                with open(full_path, "r", encoding="utf-8") as f:
                    print(f"\n--- Formatted JSON ---\n{json.dumps(json.load(f), indent=4)}\n--- End of JSON ---")
            else: print(f"File {Fore.RED}{filepath}{Style.RESET_ALL} does not exist.")
        except Exception as e: print(f"{Fore.RED}Error reading JSON: {e}{Style.RESET_ALL}")

class RegexData:
    @staticmethod
    def match_pattern(pattern, text):
        try:
            matches = re.findall(pattern, text)
            if matches: print(f"Found {Fore.GREEN}{len(matches)}{Style.RESET_ALL} matches: {Fore.CYAN}{matches}{Style.RESET_ALL}")
            else: print(f"{Fore.YELLOW}No matches found for pattern '{pattern}'.{Style.RESET_ALL}")
        except Exception as e: print(f"{Fore.RED}Regex matching error: {e}{Style.RESET_ALL}")