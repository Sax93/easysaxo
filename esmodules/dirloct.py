#=================================================
# File management
#=================================================

# `dirloct.py` ONLY FOR FILE-RELATED COMMAND DEFINING

import os, platform, subprocess
from colorama import Fore, Style

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
dir_forcreate = os.path.join(base_dir, "esmodules", "filecreation")

class DirLocation:
    @staticmethod
    def runloc():
        print(f"Running in {Fore.MAGENTA}{base_dir}{Style.RESET_ALL}.")
    

    @staticmethod
    def _resolve_path(filepath: str) -> str:
        if os.path.isabs(filepath): return filepath
        
        # 1. Check direct path relative to project root
        root_path = os.path.join(base_dir, filepath)
        if os.path.exists(root_path): return root_path
            
        # 2. Check inside \esmodules
        es_path = os.path.join(base_dir, "esmodules", filepath)
        if os.path.exists(es_path): return es_path

        # 3. Fallback to \filecreation
        os.makedirs(dir_forcreate, exist_ok=True)
        return os.path.join(dir_forcreate, filepath)

    @staticmethod
    def allowance():
        print(
            f"{Fore.LIGHTYELLOW_EX}This might take a few seconds, please wait...{Style.RESET_ALL}"
        )

        files_to_allow = [
            "main",
            "config",
            "commands",
            "esmodules/__init__",
            "esmodules/computer",
            "esmodules/heavyholder",
            "esmodules/telemetry",
            "esmodules/jsonregex",
            "esmodules/mathf",
            "esmodules/medi",
            "esmodules/misc",
        ]

        files_to_allow = [f"{file}.py" for file in files_to_allow]

        for file in files_to_allow:
            resolved_path = DirLocation._resolve_path(file)
            
            if not os.path.exists(resolved_path):
                print(f"Missing file: {Fore.RED}{file}{Style.RESET_ALL}")
                continue

            is_init = file.endswith("__init__.py")
            is_valid_size = is_init or os.path.getsize(resolved_path) > 0

            if is_valid_size:
                print(f"File exists: {Fore.GREEN}{file}{Style.RESET_ALL}")
            else:
                print(f"Empty file (expected non-empty): {Fore.YELLOW}{file}{Style.RESET_ALL}")
    
    @staticmethod
    def filesz(filepath):
        """Prints the size of a specified file in a human-readable format."""
        try:
            full_path = DirLocation._resolve_path(filepath)
            if not os.path.exists(full_path):
                print(f"File {Fore.RED}{filepath}{Style.RESET_ALL} does not exist.")
                return
            if os.path.isdir(full_path):
                print(f"{Fore.RED}{filepath}{Style.RESET_ALL} is a directory, not a file.")
                return

            size_bytes = os.path.getsize(full_path)
            
            # Format bytes to human-readable format
            for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
                if size_bytes < 1024.0:
                    readable_size = f"{size_bytes:.2f} {unit}"
                    break
                size_bytes /= 1024.0

            print(f"Size of {Fore.CYAN}{filepath}{Style.RESET_ALL}: {Fore.YELLOW}{readable_size}{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}Error getting file size: {e}{Style.RESET_ALL}")
    
    @staticmethod
    def ls(filepath=None):
        try:
            target_dir = DirLocation._resolve_path(filepath) if filepath else base_dir
            if not os.path.exists(target_dir):
                print(f"Directory {Fore.RED}{filepath}{Style.RESET_ALL} does not exist.")
                return
            if not os.path.isdir(target_dir):
                print(f"{Fore.RED}{filepath}{Style.RESET_ALL} is not a directory.")
                return

            items = os.listdir(target_dir)
            print(f"\n--- Directory Contents of {Fore.CYAN}{target_dir}{Style.RESET_ALL} ---")
            for item in sorted(items):
                item_path = os.path.join(target_dir, item)
                if os.path.isdir(item_path):
                    print(f"{Fore.BLUE}[DIR]  {item}{Style.RESET_ALL}")
                else:
                    # Get file size in bytes
                    size_bytes = os.path.getsize(item_path)
                    
                    # Convert to human-readable string
                    for unit in ['B', 'KB', 'MB', 'GB']:
                        if size_bytes < 1024.0:
                            size_str = f"{size_bytes:.2f} {unit}"
                            break
                        size_bytes /= 1024.0
                    
                    print(f"{Fore.GREEN}[FILE] {item}{Style.RESET_ALL} ({Fore.YELLOW}{size_str}{Style.RESET_ALL})")
            print("--- End of Directory Listing ---\n")
        except Exception as e:
            print(f"{Fore.RED}Error listing directory: {e}{Style.RESET_ALL}")

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
    def dircrt(filepath):
        try:
            full_path = DirLocation._resolve_path(filepath)
            if os.path.exists(full_path):
                print(f"Directory or path {Fore.YELLOW}{filepath}{Style.RESET_ALL} already exists.")
            else:
                os.makedirs(full_path, exist_ok=True)
                print(f"Directory {Fore.GREEN}{filepath}{Style.RESET_ALL} created successfully.")
        except Exception as e: 
            print(f"{Fore.RED}Error creating directory: {e}{Style.RESET_ALL}")
    
    @staticmethod
    def dirdel(filepath):
        try:
            full_path = DirLocation._resolve_path(filepath)
            if os.path.exists(full_path) and os.path.isdir(full_path):
                os.rmdir(full_path)
                print(f"Directory {Fore.GREEN}{filepath}{Style.RESET_ALL} deleted successfully.")
            else:
                print(f"Directory {Fore.RED}{filepath}{Style.RESET_ALL} does not exist or is not a folder.")
        except Exception as e:
            print(f"{Fore.RED}Error deleting directory: {e}{Style.RESET_ALL}")
                
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

# do not move, its sensitive and it may do nothing