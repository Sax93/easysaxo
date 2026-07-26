"""EasySaxo Alpha Command Input/Registry"""

import os
from config import register_command, GET_REGISTRY, HELP_REGISTRY, easysaxo
from esmodules.computer import ComputerData
from esmodules.telemetry import TelemetryData
from esmodules.dirloct import DirLocation
from esmodules.mathf import MathFunc
from esmodules.misc import whats_new, hrs, StatusHandler
from esmodules.jsonregex import JsonData, RegexData
from esmodules.medi import MediaData
from esmodules.heavyholder import ThreadData, SessionManager
from colorama import Fore, Style

#=================================================
# Command Mappings
#=================================================

# For in-MathSet guide
for math_key, help_str in MathFunc.MATHSET_HELP.items():
    HELP_REGISTRY[math_key] = help_str

# =========== ATTRIBUTES FOR 'GET' ===========
@register_command("cpu", registry=GET_REGISTRY, help_text="get cpu - Displays CPU details and usage statistics.")
def g_cpu(): ComputerData.getcpu()

@register_command("arch", registry=GET_REGISTRY, help_text="get arch - Displays architecture and byte order.")
def g_arch(): ComputerData.getarch()

@register_command("os", registry=GET_REGISTRY, help_text="get os - Displays OS name and version details.")
def g_os(): ComputerData.getos()

@register_command("ram", registry=GET_REGISTRY, help_text="get ram - Displays system RAM and Swap usage.")
def g_ram(): ComputerData.getram()

@register_command("gpu", registry=GET_REGISTRY, help_text="get gpu - Displays GPU hardware information.")
def g_gpu(): ComputerData.getgpu()

@register_command("disk", registry=GET_REGISTRY, help_text="get disk - Displays disk partitions and usage.")
def g_disk(): ComputerData.getdisk()

@register_command("motherboard", registry=GET_REGISTRY, help_text="get motherboard - Displays motherboard details.")
def g_mboard(): ComputerData.getmotherboard()

@register_command("battery", registry=GET_REGISTRY, help_text="get battery - Displays battery status.")
def g_batt(): ComputerData.getbattery()

@register_command("user", registry=GET_REGISTRY, help_text="get user - Displays logged user and hostname.")
def g_user(): ComputerData.getuserinfo()

@register_command("python", registry=GET_REGISTRY, help_text="get python - Displays Python version and path info.")
def g_py(): ComputerData.getpythoninfo()

@register_command("packages", registry=GET_REGISTRY, help_text="get packages - Lists installed pip packages.")
def g_pkg(): ComputerData.getinstalledpackages()

@register_command("env", registry=GET_REGISTRY, help_text="get env - Displays environment variables.")
def g_env(): ComputerData.getenvvars()

@register_command("processes", registry=GET_REGISTRY, help_text="get processes - Displays top CPU processes.")
def g_proc(): ComputerData.getprocesses()

@register_command("net", registry=GET_REGISTRY, help_text="get net - Displays network traffic statistics.")
def g_net(): TelemetryData.getnet()

@register_command("upt", registry=GET_REGISTRY, help_text="get upt - Displays system uptime.")
def g_upt(): TelemetryData.getupt()

@register_command("ip", registry=GET_REGISTRY, help_text="get ip - Displays local network IP addresses.")
def g_ip(): TelemetryData.getip()

@register_command("mac", registry=GET_REGISTRY, help_text="get mac - Displays primary MAC address.")
def g_mac(): TelemetryData.getmac()

@register_command("publicip", registry=GET_REGISTRY, help_text="get publicip - Displays public IP address.")
def g_pubip(): TelemetryData.getpublicip()

@register_command("netstats", registry=GET_REGISTRY, help_text="get netstats - Displays network adapter statuses.")
def g_netstat(): TelemetryData.getnetstats()

@register_command("connections", registry=GET_REGISTRY, help_text="get connections - Displays active network connections.")
def g_conn(): TelemetryData.getconnections()

@register_command("speedtest", registry=GET_REGISTRY, help_text="get speedtest - Performs network speed test.")
def g_speed(): TelemetryData.speedtest_network()

@register_command("threads", registry=GET_REGISTRY, help_text="get threads - Displays active background threads.")
def g_th(): ThreadData.getthreads()

@register_command("mathset", registry=GET_REGISTRY, help_text="get mathset - Displays available math functions/constants.")
def g_mset(): MathFunc.getmath()

@register_command("vars", aliases=["variables"], registry=GET_REGISTRY, help_text="get vars - Lists user math variables.")
def g_vars(): MathFunc.list_vars()

@register_command("appname", registry=GET_REGISTRY, help_text="get appname - Displays app name.")
def g_appn(): print(f"App name: {Fore.CYAN}{easysaxo.name}{Style.RESET_ALL}")

@register_command("appver", registry=GET_REGISTRY, help_text="get appver - Displays app version.")
def g_appv(): print(f"App version: {Fore.CYAN}{easysaxo.ver}{Style.RESET_ALL}")

@register_command("app", aliases=["appinfo"], registry=GET_REGISTRY, help_text="get app - Displays general app details.")
def g_app(): print(f"App: {Fore.CYAN}{easysaxo.name} {easysaxo.ver}{Style.RESET_ALL} by {easysaxo.dev}")

@register_command("attr", aliases=["attribute", "all"], registry=GET_REGISTRY, help_text="get attr - Fetches all telemetry and system specs.")
def g_all():
    print(f"{Fore.BLUE}== COMPUTER DATA =={Style.RESET_ALL}")
    for func in [g_cpu, g_arch, g_os, g_mboard, g_ram, g_gpu, g_disk, g_batt, g_user, g_py]: func()
    print(f"\n{Fore.BLUE}== TELEMETRY DATA =={Style.RESET_ALL}")
    for func in [g_net, g_upt, g_ip, g_mac, g_pubip, g_netstat]: func()
    print(f"\n{Fore.BLUE}== THREADING/MATH DATA =={Style.RESET_ALL}")
    g_th(); g_mset(); g_vars()


# =========== CORE COMMANDS + HELP ===========

@register_command("help", aliases=["?"], help_text="help [command] - Shows command list or syntax details for a target command.")
def c_help(arg):
    if not arg:
        print(f"{Fore.CYAN}COMMAND LIST: {Style.RESET_ALL}\n"
              f"{Fore.BLUE}help, save, load, delvar, get, set, math, runloc, fileloc, filecrt, filerd, "
              f"filedel, filewrt, jsonrd, regex, playaudio, stopaudio, timer, time, random, fileopn, filecls, exit{Style.RESET_ALL}.",
              f"\nRemember you can search for command's syntax and usage by using {Fore.GREEN}help <cmd/attr>{Style.RESET_ALL}")
    else:
        target = arg.lower().strip()
        if target in HELP_REGISTRY:
            print(f"\n{Fore.GREEN}=== Usage for '{target}' ==={Style.RESET_ALL}")
            print(f"{Fore.YELLOW}{HELP_REGISTRY[target]}{Style.RESET_ALL}\n")
        elif target in GET_REGISTRY and target in HELP_REGISTRY:
            print(f"\n{Fore.GREEN}=== Usage for 'get {target}' ==={Style.RESET_ALL}")
            print(f"{Fore.YELLOW}{HELP_REGISTRY[target]}{Style.RESET_ALL}\n")
        else:
            print(f"{Fore.RED}No usage details found for '{arg}'. Type 'help' for options.{Style.RESET_ALL}")

@register_command("clear", aliases=["clr", "clrscr"], help_text="clear - Clears the terminal screen.")
def c_clear(arg): os.system('cls' if os.name == 'nt' else 'clear')

@register_command("save", help_text="save [filepath.json] - Saves the current session state and math variables.")
def c_save(arg): SessionManager.save_session(ThreadData.current_user, arg)

@register_command("load", help_text="load <filepath.json> - Loads session state and variables from a file.")
def c_load(arg):
    if arg: ThreadData.current_user = SessionManager.load_session(arg)
    else: print(f"{Fore.RED}Usage: load <filepath.json>{Style.RESET_ALL}")

@register_command("delvar", help_text="delvar <var_name> - Deletes a user-defined math variable.")
def c_delvar(arg):
    if arg: MathFunc.del_var(arg); SessionManager.save_session(ThreadData.current_user)
    else: print(f"{Fore.RED}Usage: delvar <var_name>{Style.RESET_ALL}")

@register_command("del", help_text="del var <var_name> - Deletes a user-defined math variable.")
def c_del(arg):
    if arg and arg.lower().startswith("var "):
        MathFunc.del_var(arg.split(maxsplit=1)[1]); SessionManager.save_session(ThreadData.current_user)
    else: print(f"{Fore.RED}Usage: del var <var_name>{Style.RESET_ALL}")

@register_command("get", help_text="get <attribute|subcommand> - Fetches system metrics, variables, or specs.")
def c_get(arg):
    if not arg: print(f"{Fore.RED}Missing argument for 'get'. Type 'help' for options.{Style.RESET_ALL}")
    elif arg.startswith("module "): 
        mtocheck = arg.split(maxsplit=1)[1]
        for mod in mtocheck.replace(",", " ").split():
            clean = mod.strip().lower()
            if clean in required_modules: StHd.print_status(f"Module {Fore.BLUE}{clean.upper()}{Style.RESET_ALL}", True)
            else: StHd.print_status(f"Module {Fore.BLUE}{clean.upper()}{Style.RESET_ALL}", False, "Not required")
    elif arg == "module":
        for mod in required_modules: StHd.print_status(f"Module {Fore.BLUE}{mod.upper()}{Style.RESET_ALL}", True)
    elif arg in GET_REGISTRY: GET_REGISTRY[arg]()
    else: MathFunc.getvar(arg)

@register_command("runloc", help_text="runloc - Prints the current working directory path.")
def c_runloc(arg): DirLocation.runloc()

@register_command("fileopn", help_text="fileopn <filepath> - Opens a file with the default system application.")
def c_fileopn(arg): DirLocation.fileopn(arg) if arg else print(f"{Fore.RED}Missing filepath.{Style.RESET_ALL}")

@register_command("filecls", help_text="filecls <process_name> - Terminates process(es) matching the given name.")
def c_filecls(arg): DirLocation.filecls(arg) if arg else print(f"{Fore.RED}Missing process name.{Style.RESET_ALL}")

@register_command("fileloc", help_text="fileloc <filename> - Searches and locates a file within the working directory.")
def c_fileloc(arg): DirLocation.fileloc(arg) if arg else print(f"{Fore.RED}Missing filename.{Style.RESET_ALL}")

@register_command("filecrt", help_text="filecrt <filepath> - Creates an empty file at the designated location.")
def c_filecrt(arg): DirLocation.filecrt(arg) if arg else print(f"{Fore.RED}Missing filepath.{Style.RESET_ALL}")

@register_command("filerd", help_text="filerd <filepath> - Reads and prints text content from a target file.")
def c_filerd(arg): DirLocation.filerd(arg) if arg else print(f"{Fore.RED}Missing filepath.{Style.RESET_ALL}")

@register_command("filedel", help_text="filedel <filepath> - Permanently removes a file from disk.")
def c_filedel(arg): DirLocation.filedel(arg) if arg else print(f"{Fore.RED}Missing filepath.{Style.RESET_ALL}")

@register_command("filewrt", help_text="filewrt <filepath> <content> - Overwrites target file with text content.")
def c_filewrt(arg):
    parts = arg.split(maxsplit=1) if arg else []
    if len(parts) == 2: DirLocation.filewrt(parts[0], parts[1])
    else: print(f"{Fore.RED}Usage: filewrt <filepath> <content>{Style.RESET_ALL}")

@register_command("jsonrd", help_text="jsonrd <filepath> - Parses and pretty-prints JSON file contents.")
def c_jsonrd(arg): JsonData.jsonrd(arg) if arg else print(f"{Fore.RED}Missing filepath.{Style.RESET_ALL}")

@register_command("regex", help_text="regex <pattern> <text> - Evaluates regex pattern against input text string.")
def c_regex(arg):
    parts = arg.split(maxsplit=1) if arg else []
    if len(parts) == 2: RegexData.match_pattern(parts[0], parts[1])
    else: print(f"{Fore.RED}Usage: regex <pattern> <text>{Style.RESET_ALL}")

@register_command("playaudio", help_text="playaudio <filepath> - Plays an audio file asynchronously.")
def c_playaudio(arg): MediaData.playaudio(arg) if arg else print(f"{Fore.RED}Missing filepath.{Style.RESET_ALL}")

@register_command("stopaudio", help_text="stopaudio - Stops currently playing audio playback.")
def c_stopaudio(arg): MediaData.stopaudio()

@register_command("set", help_text="set name <new_name> | set var <var_name> <value> - Updates session username or math variables.")
def c_set(arg):
    if not arg: print(f"{Fore.RED}Usage: set name <new_name> OR set var <var_name> <value>{Style.RESET_ALL}")
    else:
        parts = arg.split(maxsplit=2)
        if parts[0].lower() == "name" and len(parts) >= 2:
            ThreadData.current_user = parts[1]
            print(f"User name replaced to {Fore.GREEN}{parts[1]}{Style.RESET_ALL}.")
            SessionManager.save_session(ThreadData.current_user)
        elif parts[0].lower() in ["var", "variable"] and len(parts) == 3:
            MathFunc.set_var(parts[1], parts[2]); SessionManager.save_session(ThreadData.current_user)
        else: print(f"{Fore.RED}Unknown/malformed set subcommand.{Style.RESET_ALL}")

@register_command("timer", help_text="timer <seconds> [message] - Sets a non-blocking background countdown timer alert.")
def c_timer(arg):
    parts = arg.split(maxsplit=1) if arg else []
    if len(parts) >= 1: ThreadData.set_timer(parts[0], parts[1] if len(parts)==2 else None)
    else: print(f"{Fore.RED}Usage: timer <seconds> <message>{Style.RESET_ALL}")

@register_command("import", help_text="import - Re-checks required system module imports.")
def c_import(arg): module_importing()

@register_command("math", help_text="math <expression> - Evaluates mathematical expressions safely (e.g., math 2 + sqrt(16)).")
def c_math(arg): MathFunc.evaluate(arg) if arg else print(f"{Fore.RED}Usage: math <expression>{Style.RESET_ALL}")

@register_command("random", help_text="random [max] OR random [min] [max] - Generates a random integer.")
def c_rand(arg):
    if arg:
        try:
            nums = [int(x) for x in arg.split()]
            MathFunc.rtool(nums[0]) if len(nums) == 1 else MathFunc.rtool(nums[0], nums[1])
        except ValueError: print(f"{Fore.RED}Provide valid integers.{Style.RESET_ALL}")
    else: MathFunc.rtool()

@register_command("mathhelp", aliases=["mhelp"], help_text="mathhelp <attribute> - Displays help details for a specific MathSet function or constant.")
def c_mathhelp(arg):
    if not arg:
        print(f"{Fore.RED}Usage: mathhelp <attribute>{Style.RESET_ALL}")
        print(f"Available attributes: {Fore.CYAN}{', '.join(MathFunc.mathset.keys())}{Style.RESET_ALL}")
    else:
        MathFunc.help_attribute(arg)

@register_command("time", aliases=["date"], help_text="time - Displays current system date and time.")
def c_time(arg): hrs()

@register_command("whatsnew", aliases=["news"], help_text="whatsnew - Displays software changelog highlights.")
def c_whatsnew(arg): whats_new()
