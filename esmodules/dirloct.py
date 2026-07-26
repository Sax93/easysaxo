#=================================================
# File management
#=================================================

import os, platform, subprocess
from colorama import Fore, Style

base_dir = os.path.dirname(os.path.abspath(__file__))
dir_forcreate = os.path.join(base_dir, "filecreation")

class DirLocation:
    @staticmethod
    def runloc():
        print(f"Running in {Fore.MAGENTA}{base_dir}{Style.RESET_ALL}.")

    @staticmethod
    def _resolve_path(filepath: str) -> str:
        os.makedirs(dir_forcreate, exist_ok=True)

        return filepath if os.path.isabs(filepath) else os.path.join(dir_forcreate, filepath)

    @staticmethod
    def fileopn(filepath):
        try:
            full_path = DirLocation._resolve_path(filepath)
            if not os.path.exists(full_path):
                print(f"File {Fore.RED}{filepath}{Style.RESET_ALL} does not exist.")
                return
            print(f"Opening {Fore.GREEN}{filepath}{Style.RESET_ALL}...")
            if os.name == "nt": os.startfile(full_path)
            elif platform.system() == "Darwin": subprocess.run(["open", full_path])
            else: subprocess.run(["xdg-open", full_path])
        except Exception as e:
            print(f"{Fore.RED}Error opening file: {e}{Style.RESET_ALL}")

    @staticmethod
    def filecls(process_name_or_file):
        import psutil
        try:
            target = os.path.basename(process_name_or_file).lower()
            terminated = False
            for proc in psutil.process_iter(["pid", "name"]):
                try:
                    if target in proc.info["name"].lower():
                        proc.terminate()
                        print(f"Closed process {Fore.GREEN}{proc.info['name']}{Style.RESET_ALL} (PID: {proc.info['pid']}).")
                        terminated = True
                except (psutil.NoSuchProcess, psutil.AccessDenied): continue
            if not terminated: print(f"No running process found matching {Fore.YELLOW}{process_name_or_file}{Style.RESET_ALL}.")
        except Exception as e:
            print(f"{Fore.RED}Error closing file process: {e}{Style.RESET_ALL}")

    @staticmethod
    def fileloc(filetool):
        # Searches both base_dir and subfolders (like filecreation)
        for root, dirs, files in os.walk(base_dir):
            if filetool in files:
                print(f"File {Fore.GREEN}{filetool}{Style.RESET_ALL} found at: {Fore.CYAN}{os.path.join(root, filetool)}{Style.RESET_ALL}")
                return
        print(f"File {Fore.RED}{filetool}{Style.RESET_ALL} not found.")

    @staticmethod
    def filecrt(filepath):
        try:
            full_path = DirLocation._resolve_path(filepath)
            if os.path.exists(full_path): print(f"File {Fore.YELLOW}{filepath}{Style.RESET_ALL} already exists.")
            else:
                open(full_path, "a").close()
                print(f"File {Fore.GREEN}{filepath}{Style.RESET_ALL} created successfully.")
        except Exception as e: print(f"{Fore.RED}Error creating file: {e}{Style.RESET_ALL}")

    @staticmethod
    def filerd(filepath):
        try:
            full_path = DirLocation._resolve_path(filepath)
            if os.path.exists(full_path):
                with open(full_path, "r", encoding="utf-8") as f: content = f.read()
                print(f"\n--- Contents of {Fore.CYAN}{filepath}{Style.RESET_ALL} ---\n{content}\n--- End of file ---")
            else: print(f"File {Fore.RED}{filepath}{Style.RESET_ALL} does not exist.")
        except Exception as e: print(f"{Fore.RED}Error reading file: {e}{Style.RESET_ALL}")

    @staticmethod
    def filedel(filepath):
        try:
            full_path = DirLocation._resolve_path(filepath)
            if os.path.exists(full_path):
                os.remove(full_path)
                print(f"File {Fore.GREEN}{filepath}{Style.RESET_ALL} deleted successfully.")
            else: print(f"File {Fore.RED}{filepath}{Style.RESET_ALL} does not exist.")
        except Exception as e: print(f"{Fore.RED}Error deleting file: {e}{Style.RESET_ALL}")

    @staticmethod
    def filewrt(filepath, content):
        try:
            full_path = DirLocation._resolve_path(filepath)
            with open(full_path, "w", encoding="utf-8") as f: f.write(content)
            print(f"Content written to {Fore.GREEN}{filepath}{Style.RESET_ALL} successfully.")
        except Exception as e: print(f"{Fore.RED}Error writing to file: {e}{Style.RESET_ALL}")