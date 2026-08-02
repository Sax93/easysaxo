#=================================================
# Computer Data
#=================================================

# `computer.py` ONLY FOR COMPUTER COMMAND DEFINING

# dark magic, only watching

import os, sys, platform, subprocess, getpass, socket, locale
from colorama import Fore, Style

try:
    from rich.console import Console
    from rich.table import Table
    console = Console()
    RICH_AVAILABLE = True
except ImportError:
    RICH_AVAILABLE = False

class ComputerData:
    @staticmethod
    def getcpu():
        import psutil
        try: import cpuinfo
        except ImportError: cpuinfo = None

        print(f"Processor Model: {Fore.BLUE}{platform.processor() or 'Unknown'}{Style.RESET_ALL}")
        if cpuinfo:
            try:
                info = cpuinfo.get_cpu_info()
                print(f"Brand: {Fore.CYAN}{info.get('brand_raw', 'N/A')}{Style.RESET_ALL}")
                print(f"Architecture: {Fore.CYAN}{info.get('arch', 'N/A')}{Style.RESET_ALL}")
                print(f"L2 Cache: {Fore.CYAN}{info.get('l2_cache_size', 'N/A')}{Style.RESET_ALL}")
                print(f"L3 Cache: {Fore.CYAN}{info.get('l3_cache_size', 'N/A')}{Style.RESET_ALL}")
            except Exception: pass

        print(f"Cores: {Fore.BLUE}{psutil.cpu_count(logical=False)} Physical | {psutil.cpu_count(logical=True)} Logical{Style.RESET_ALL}")
        try:
            freq = psutil.cpu_freq()
            if freq:
                print(f"Speed: {Fore.BLUE}{freq.current:.2f} MHz (Min: {freq.min:.2f} MHz, Max: {freq.max:.2f} MHz){Style.RESET_ALL}")
        except Exception: pass

        print(f"Total CPU Usage: {Fore.BLUE}{psutil.cpu_percent(interval=0.0)}{Style.RESET_ALL}%")
        print(f"Core Usage: {Fore.BLUE}{psutil.cpu_percent(interval=0.2, percpu=True)}{Style.RESET_ALL}%")

    @staticmethod
    def getarch():
        print(f"Architecture: {Fore.BLUE}{Style.BRIGHT}{platform.architecture()[0]} ({platform.machine()}){Style.RESET_ALL}")
        print(f"Byte Order: {Fore.BLUE}{sys.byteorder.upper()}-endian{Style.RESET_ALL}")

    @staticmethod
    def getram():
        import psutil
        mem = psutil.virtual_memory()
        print(f"Total RAM: {Fore.GREEN}{mem.total / (1024**3):.2f} GB{Style.RESET_ALL}")
        print(f"Available RAM: {Fore.GREEN}{mem.available / (1024**3):.2f} GB{Style.RESET_ALL}")
        print(f"Used RAM: {Fore.GREEN}{mem.used / (1024**3):.2f} GB ({mem.percent}%){Style.RESET_ALL}")
        try:
            swap = psutil.swap_memory()
            print(f"Swap Total: {Fore.GREEN}{swap.total / (1024**3):.2f} GB{Style.RESET_ALL}")
            print(f"Swap Used: {Fore.GREEN}{swap.used / (1024**3):.2f} GB ({swap.percent}%){Style.RESET_ALL}")
        except RuntimeError:
            print(f"Swap Memory: {Fore.YELLOW}Unavailable{Style.RESET_ALL}")

    @staticmethod
    def getgpu():
        try: import GPUtil
        except ImportError: GPUtil = None

        if GPUtil:
            try:
                gpus = GPUtil.getGPUs()
                if gpus:
                    for gpu in gpus:
                        print(f"GPU Name: {Fore.RED}{gpu.name}{Style.RESET_ALL}")
                        print(f"  VRAM Total: {Fore.RED}{gpu.memoryTotal} MB{Style.RESET_ALL}")
                        print(f"  VRAM Used: {Fore.RED}{gpu.memoryUsed} MB ({gpu.memoryUtil*100:.1f}%){Style.RESET_ALL}")
                        print(f"  Temperature: {Fore.RED}{gpu.temperature} °C{Style.RESET_ALL}")
                    return
            except Exception: pass
        
        try:
            if os.name == "nt":
                result = subprocess.run(["powershell", "-Command", "Get-CimInstance Win32_VideoController | Select-Object Name, AdapterRAM, DriverVersion"], capture_output=True, text=True, timeout=5)
                output = result.stdout.strip()
                if output: print(f"GPU Details:\n{Fore.RED}{output}{Style.RESET_ALL}")
                else: print(f"GPU: {Fore.RED}No GPU detected{Style.RESET_ALL}")
            else:
                result = subprocess.run(["lspci", "-v", "-mm"], capture_output=True, text=True, timeout=5)
                for line in result.stdout.split("\n"):
                    if "VGA" in line or "Display" in line:
                        print(f"GPU: {Fore.RED}{Style.BRIGHT}{line.strip()}{Style.RESET_ALL}")
                        break
                else:
                    print(f"GPU: {Fore.RED}No GPU detected{Style.RESET_ALL}")
        except Exception:
            print(f"GPU: {Fore.RED}Unable to detect GPU{Style.RESET_ALL}")

    @staticmethod
    def getmotherboard():
        try:
            if os.name == "nt":
                result = subprocess.run(["powershell", "-Command", "Get-CimInstance Win32_BaseBoard | Select-Object Manufacturer, Product, SerialNumber"], capture_output=True, text=True, timeout=5)
                print(f"Motherboard Info:\n{Fore.CYAN}{result.stdout.strip()}{Style.RESET_ALL}")
            else:
                print(f"Motherboard: {Fore.CYAN}Requires root permissions (dmidecode) on Linux/Unix{Style.RESET_ALL}")
        except Exception as e:
            print(f"Motherboard: {Fore.RED}Error fetching motherboard data: {e}{Style.RESET_ALL}")

    @staticmethod
    def getdisk():
        import psutil
        partitions = psutil.disk_partitions()
        
        if RICH_AVAILABLE:
            table = Table(title="Disk Partitions & Usage")
            table.add_column("Drive", style="yellow")
            table.add_column("Type", style="cyan")
            table.add_column("Total", style="green")
            table.add_column("Free", style="green")
            table.add_column("Usage", style="magenta")
            
            for p in partitions: #what do u call 2 partitions in math? a pp hahalol
                try:
                    u = psutil.disk_usage(p.mountpoint)
                    table.add_row(p.mountpoint, p.fstype, f"{u.total / (1024**3):.2f} GB", f"{u.free / (1024**3):.2f} GB", f"{u.percent}%")
                except PermissionError:
                    table.add_row(p.mountpoint, p.fstype, "Access Denied", "-", "-")
            console.print(table)
        else:
            print("\n--- Disk Partitions & Usage ---")
            for partition in partitions:
                try:
                    usage = psutil.disk_usage(partition.mountpoint)
                    print(f"Drive {Fore.YELLOW}{partition.mountpoint}{Style.RESET_ALL} ({partition.fstype}): {Fore.YELLOW}{usage.total / (1024**3):.2f} GB{Style.RESET_ALL} Total, {Fore.YELLOW}{usage.free / (1024**3):.2f} GB{Style.RESET_ALL} Free ({usage.percent}% Used)")
                except PermissionError:
                    print(f"Drive {Fore.YELLOW}{partition.mountpoint}{Style.RESET_ALL}: Access denied.")

        try:
            io = psutil.disk_io_counters()
            if io:
                print(f"\n--- Disk I/O Metrics ---\nRead: {Fore.YELLOW}{io.read_bytes / (1024**2):.2f} MB{Style.RESET_ALL} | Written: {Fore.YELLOW}{io.write_bytes / (1024**2):.2f} MB{Style.RESET_ALL}")
        except Exception: pass

    @staticmethod
    def getbattery():
        import psutil
        try:
            battery = psutil.sensors_battery()
            if battery:
                plugged = "Plugged In" if battery.power_plugged else "On Battery"
                print(f"Battery Charge: {Fore.CYAN}{battery.percent}%{Style.RESET_ALL} ({plugged})")
                if battery.secsleft not in [psutil.POWER_TIME_UNLIMITED, psutil.POWER_TIME_UNKNOWN]:
                    mins = battery.secsleft // 60
                    print(f"Time Remaining: {Fore.CYAN}{mins // 60}h {mins % 60}m{Style.RESET_ALL}")
            else:
                print(f"Battery: {Fore.CYAN}No battery detected{Style.RESET_ALL}")
        except Exception:
            print(f"Battery: {Fore.RED}Unable to detect battery status{Style.RESET_ALL}") # poor

    @staticmethod
    def getos():
        print(f"Operating System: {Fore.BLUE}{platform.system()} {platform.release()}{Style.RESET_ALL}")
        print(f"OS Version: {Fore.BLUE}{platform.version()}{Style.RESET_ALL}")
        print(f"Full Platform Tag: {Fore.BLUE}{platform.platform()}{Style.RESET_ALL}")
        # unless you barely have a kboard

    @staticmethod
    def getpythoninfo():
        print(f"Python Version: {Fore.GREEN}{platform.python_version()} ({platform.python_compiler()}){Style.RESET_ALL}")
        print(f"Executable Path: {Fore.GREEN}{sys.executable}{Style.RESET_ALL}")
        print(f"Virtual Environment: {Fore.GREEN}{'Active' if sys.prefix != sys.base_prefix else 'Inactive'}{Style.RESET_ALL}")
        loc, enc = locale.getlocale()
        print(f"System Locale: {Fore.GREEN}{loc or 'Default'} | Encoding: {enc or 'UTF-8'}{Style.RESET_ALL}")

    @staticmethod
    def getuserinfo():
        print(f"Logged User: {Fore.CYAN}{getpass.getuser()}{Style.RESET_ALL}")
        print(f"Device Name (Hostname): {Fore.CYAN}{socket.gethostname()}{Style.RESET_ALL}")

    @staticmethod
    def getenvvars():
        print("\n--- Environment Variables ---")
        for key, value in list(os.environ.items())[:15]:
            print(f"{Fore.MAGENTA}{key}{Style.RESET_ALL}: {value}")
        print(f"... total {len(os.environ)} variables loaded.")

    @staticmethod
    def getinstalledpackages():
        try:
            reqs = subprocess.check_output([sys.executable, "-m", "pip", "list"])
            print(f"\n--- Installed Pip Packages ---\n{reqs.decode('utf-8')}")
        except Exception as e:
            print(f"{Fore.RED}Error retrieving installed packages: {e}{Style.RESET_ALL}")

    @staticmethod
    def getprocesses():
        import psutil
        processes = sorted(psutil.process_iter(["pid", "name", "cpu_percent", "memory_percent"]), 
                           key=lambda p: p.info["cpu_percent"] or 0, reverse=True)[:5]
        
        if RICH_AVAILABLE:
            table = Table(title="Top 5 CPU Processes")
            table.add_column("PID", style="magenta")
            table.add_column("Name", style="cyan")
            table.add_column("CPU %", style="yellow")
            table.add_column("RAM %", style="green")
            for p in processes:
                table.add_row(str(p.info['pid']), p.info['name'], str(p.info['cpu_percent']), f"{p.info['memory_percent']:.2f}")
            console.print(table)
        else:
            print("\nTop 5 CPU-Consuming Processes:")
            for p in processes:
                print(f"  PID: {p.info['pid']} | Name: {Fore.CYAN}{p.info['name']}{Style.RESET_ALL} | CPU: {p.info['cpu_percent']}% | RAM: {p.info['memory_percent']:.2f}%")

# note: 8 out of 10 intel celeron inside cpus crash here