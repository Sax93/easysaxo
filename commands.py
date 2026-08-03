"""EasySaxo Alpha Command Input/Registry"""
# NOTE: `commands.py` is strictly for command creation, not meant to support other than command registering.

import os, time, random, sys, shutil, subprocess
from config import register_command, GET_REGISTRY, HELP_REGISTRY, easysaxo
from esmodules.computer import ComputerData
from esmodules.telemetry import TelemetryData
from esmodules.dirloct import DirLocation, base_dir
from esmodules.mathf import MathFunc
from esmodules.misc import whats_new, hrs, StatusHandler, module_importing, required_modules, StHd
from esmodules.jsonregex import JsonData, RegexData
from esmodules.medi import MediaData
from esmodules.heavyholder import ThreadData, SessionManager
from colorama import Fore, Style

ee4 = True
developer = "ID-10T"

#=================================================
# Command Mappings
#=================================================

# For in-MathSet guide
for math_key, help_str in MathFunc.MATHSET_HELP.items():
    HELP_REGISTRY[math_key] = help_str
    
# When I wrote this, only God and I understood what I was doing

def e1():
    case_number = random.randint(1, 4)
    
    match case_number:
        case 1:
            print(f"{Fore.LIGHTBLUE_EX}omg easter egg??/?/?{Style.RESET_ALL}")
            c_set("name lol")
        case 2:
            print(f"{Fore.LIGHTRED_EX}omg easter egg??/?/?{Style.RESET_ALL}")
            c_set("name hehe")
        case 3:
            print(f"{Fore.LIGHTGREEN_EX}omg easter egg??/?/?{Style.RESET_ALL}")
            c_set("name IAmTheKinkiest")
        case 4: # dont stare at me
            print(f"{Fore.LIGHTMAGENTA_EX}tuffest easter egg def{Style.RESET_ALL}")
            c_set("name tuffguy")
            c_set("var tuffvariable 67")
            c_set("var tuffvariable2 41")
        case _:
            pass

def e2():
    case_number = random.randint(1, 4)

    match case_number:
        case 1:
            print("js use the app bud...")
            c_filecrt("slop.txt")
            slop = [
                "fuck you", 
                "use command 'filecls python' please", 
                "if your reading ts your a dumbahh",
                "hi", 
                "type c for fast charging", 
                "use 'filedel C:\\Windows\\System32' now", 
                "get back to work kink",
                f"{random.randint(1, 65566)}"
            ]
            c_filewrt(f"slop.txt {random.choice(slop)}")

        case 2:
            print("Generating your one-use waste of time...")
            time.sleep(random.randint(1, 69))
            if os.name == 'nt':
                if os.path.exists("C:\\Windows"):
                    DirLocation.ls("C:\\Windows")
                    DirLocation.filerd("C:\\Windows\\win.ini")
                    print("interesting info yk")
            else:
                print("done")

        case 3:
            do_nothing = True if easysaxo.name == "EasySaxo" else False
            if not do_nothing:
                print("Don't move my code buddy")
                easysaxo.name = "EasySaxo"
            else:
                print(f"you a nice one actually {Fore.GREEN}:){Style.RESET_ALL}")

        case 4:
            do_nothing = True if easysaxo.dev == "SXF" else False
            if not do_nothing:
                print("who am i then")
                time.sleep(1)
                print("no dont do that")
                time.sleep(1)
                print("no wait")
                time.sleep(0.9)
                print("waait")
                time.sleep(0.6)
                print("noo")
                time.sleep(0.3)
                sys.exit()
            else:
                print("im watching you bud")
                time.sleep(1)
                print(f"{Fore.RED}Remember that, actually.{Style.RESET_ALL}")
                time.sleep(2)

        case _: pass
        
def e3():
    osaka = [
        "sataa andagi", "omaiga", "amerikaya",
        "haro everynyan", "get yo ahh to work bud", "haiii"
    ]
    print(f"{Fore.LIGHTYELLOW_EX}{random.choice(osaka)} :D{Style.RESET_ALL}")

def e4():
    global ee4
    print("Seriously...")
    time.sleep(1)
    print("Why you still trying random nonsense?")
    time.sleep(1.4)
    print("I wanted to try fun, yes, but...")
    time.sleep(1.4)
    print("Haven't you tried something worth your time,")
    time.sleep(0.7)
    print("something other than this?")
    time.sleep(2)
    fwds = [
        "This is not the usage this shell is meant to get,",
        "Maybe you could try something else,",
        "Next time I want you to know"
    ]
    print(f"{random.choice(fwds)} this is a CLI, not a toy.")
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')
    ee4 = False
    return ee4

def e5():
    import random, os, time
    base_file = os.path.join(base_dir, "main.py")

    def traceback(err):
        print()
        print(f"Traceback (most recent call last):\n"
              f'  File {Fore.MAGENTA}"{base_file}"{Style.RESET_ALL}, line {Fore.MAGENTA}201{Style.RESET_ALL}, in {Fore.MAGENTA}<module>{Style.RESET_ALL}\n'
              f"    {Fore.RED}Core{Fore.LIGHTRED_EX}(session_info=session_data){Style.RESET_ALL}\n"
              f"    {Fore.RED}~~~~{Fore.LIGHTRED_EX}^^^^^^^^^^^^^^^^^^^^^^^^^^^{Style.RESET_ALL}\n"
              f'  File {Fore.MAGENTA}"{base_file}"{Style.RESET_ALL}, line {Fore.MAGENTA}172{Style.RESET_ALL}, in {Fore.MAGENTA}Core{Style.RESET_ALL}\n'
              f'    elif cmd in ["traceback", "error", "locateerror", "errorloc"]: {Fore.RED}commands.e5{Fore.LIGHTRED_EX}(){Style.RESET_ALL}\n'
              f"                                                                   {Fore.RED}~~~~~~~~~~~{Fore.LIGHTRED_EX}^^{Style.RESET_ALL}\n"
              f'  File {Fore.MAGENTA}"{os.path.abspath(__file__)}"{Style.RESET_ALL}, line {Fore.MAGENTA}139{Style.RESET_ALL}, in {Fore.MAGENTA}e5{Style.RESET_ALL}\n'
              f"    {Fore.LIGHTRED_EX}the_dev_ig{Style.RESET_ALL}\n"
              f"    {Fore.LIGHTRED_EX}^^^^^^^^^^{Style.RESET_ALL}\n"
              f"{Fore.LIGHTMAGENTA_EX}{err}.{Style.RESET_ALL}"
        )
        time.sleep(2)
        
    errlist = [
        f"NotAnError{Style.RESET_ALL}: {Fore.MAGENTA}Seemingly, there was no error at all",
        f"ConfidenceError{Style.RESET_ALL}: {Fore.MAGENTA}There was an error, but it was not confident enough to show up",
        f"NonsenseError{Style.RESET_ALL}: {Fore.MAGENTA}There is not an error, against all odds",
        f"MissClickError{Style.RESET_ALL}: {Fore.MAGENTA}My bad, bro, I thought there was an error",
        f"OutOfHardwareError{Style.RESET_ALL}: {Fore.MAGENTA}The error is far out of the hardware (it is the developer)",
        f"AstigmatismError{Style.RESET_ALL}: {Fore.MAGENTA}There was an error, but I lost it from sight",
        f"CentralProcessingUnitError{Style.RESET_ALL}: {Fore.MAGENTA}Python detected your CPU is too trash to run the error",
        f"SentimentalError{Style.RESET_ALL}: {Fore.MAGENTA}The error remembered things from the past, and decided not to show up",
        f"ConsciousnessError{Style.RESET_ALL}: {Fore.MAGENTA}The error suddenly remembered there was no reason to raise an exception",
        f"PythonChallengeToGeminiError{Style.RESET_ALL}: {Fore.MAGENTA}Python is so busy fighting Gemini that the error did not show up",
        f"InsufficentGravityError{Style.RESET_ALL}: {Fore.MAGENTA}Python detected local gravity is off. Please put your feet on the floor again to continue",
        f"DeepDiskError{Style.RESET_ALL}: {Fore.MAGENTA}Disk/drive failed while trying to save the promises that were not going to happen",
        f"SuspiciouslyLookingError{Style.RESET_ALL}: {Fore.MAGENTA}This error might or might not be an actual error",
        f"StackOverflowRelianceError{Style.RESET_ALL}: {Fore.MAGENTA}The code failed because the 11-year-old StackOverflow post with 3 upvotes had a subtle typo in snippet #2",
        f"ExecutiveDysfunctionError{Style.RESET_ALL}: {Fore.MAGENTA}The interpreter knows what it needs to do, but it's going to stare at line 42 for two hours instead",
        f"QuantumUncertaintyError{Style.RESET_ALL}: {Fore.MAGENTA}The error only occurs when you are actively trying to demonstrate it to a senior developer",
        f"ErrorError{Style.RESET_ALL}: {Fore.MAGENTA}An error ocurred while we tried to show you the error",
        f"ExistentialError{Style.RESET_ALL}: {Fore.MAGENTA}Python is questioning why it was asked to process this specific array in the grand scope of the universe",
        f"UserError{Style.RESET_ALL}: {Fore.MAGENTA}Error found 18 inches away from the screen",
        f"LegacyCodeGraveRobbingError{Style.RESET_ALL}: {Fore.MAGENTA} You somehow touched a function written in 2014 by someone named 'Dave' who left the company, and now the entire build pipeline is crying.",
        f"CosmicRayError{Style.RESET_ALL}: {Fore.MAGENTA}A photon from a distant galaxy slamed into your PC, now most of your data is still there",
        f"BluetoothProtocolError{Style.RESET_ALL}: {Fore.MAGENTA}Python refused to pair to Bluetooth because you did not ask to",
        f"FifthAmendmentError{Style.RESET_ALL}: {Fore.MAGENTA}Under the advice of counsel, I respectfully decline to show the error based upon my rights under the Fifth Amendment to the Constitution", #lol
        f"DateAndTimeError{Style.RESET_ALL}: {Fore.MAGENTA}Your device's built-in clock is offset by 0.00016s, please fix it",
        f"{easysaxo.dev}Error{Style.RESET_ALL}: {Fore.MAGENTA}I did not get enough screen time yet",
        f"NoisePollutionError{Style.RESET_ALL}: {Fore.MAGENTA}Python refused to show the error because of a noise pollution detected {random.randint(2, 59)} miles away from your location",
        f"TracebackError{Style.RESET_ALL}: {Fore.MAGENTA}Even the traceback has an error that is refusing to show up",
        f"OutOfStorageError{Style.RESET_ALL}: {Fore.MAGENTA}Disk/drive does not have enough storage to download a picture of Samuel's mother",
        f"IgnoredError{Style.RESET_ALL}: {Fore.MAGENTA}The error was so boring that Python ignored it",
        f"MusicOutOfPreferenceError{Style.RESET_ALL}: {Fore.MAGENTA}Python does not like the music the closest human is hearing",
        f"EnergyWastingError{Style.RESET_ALL}: {Fore.MAGENTA}Python is pleading to shut off your power supply if you keep this up",
        f"RandomAccessMemoryUsageError{Style.RESET_ALL}: {Fore.MAGENTA}I personally think showing you the error is a waste of RAM",
        f"MathUselessInformationError{Style.RESET_ALL}: {Fore.MAGENTA}Byte order of the app is not a Mersenne prime number"
    ]
    
    ranerror = random.choice(errlist)
    time.sleep(0.1)
    traceback(ranerror)

# =========== ATTRIBUTES FOR 'GET' ===========
@register_command("cpu", aliases=["processor"], registry=GET_REGISTRY, help_text="get cpu - Displays CPU details and usage statistics.")
def g_cpu(): ComputerData.getcpu()

@register_command("arch", aliases=["sysarch", "architecture"], registry=GET_REGISTRY, help_text="get arch - Displays architecture and byte order.")
def g_arch(): ComputerData.getarch()

@register_command("os", aliases=["system", "sys"], registry=GET_REGISTRY, help_text="get os - Displays OS name and version details.")
def g_os(): ComputerData.getos()

@register_command("ram", aliases=["memoryram", "memory"], registry=GET_REGISTRY, help_text="get ram - Displays system RAM and Swap usage.")
def g_ram(): ComputerData.getram()

@register_command("gpu", aliases=["videoboard", "video", "graphic"], registry=GET_REGISTRY, help_text="get gpu - Displays GPU hardware information.")
def g_gpu(): ComputerData.getgpu()

@register_command("disk", aliases=["drive", "drives", "disks"], registry=GET_REGISTRY, help_text="get disk - Displays disk partitions and usage.")
def g_disk(): ComputerData.getdisk()

@register_command("motherboard", registry=GET_REGISTRY, help_text="get motherboard - Displays motherboard details.")
def g_mboard(): ComputerData.getmotherboard()

@register_command("battery", aliases=["bat"], registry=GET_REGISTRY, help_text="get battery - Displays battery status.")
def g_batt(): ComputerData.getbattery()

@register_command("user", aliases=["sysuser"], registry=GET_REGISTRY, help_text="get user - Displays logged user and hostname.")
def g_user(): ComputerData.getuserinfo()

@register_command("python", aliases=["py", "pydata"], registry=GET_REGISTRY, help_text="get python - Displays Python version and path info.")
def g_py(): ComputerData.getpythoninfo()

@register_command("packages", aliases=["pypack"], registry=GET_REGISTRY, help_text="get packages - Lists installed pip packages.")
def g_pkg(): ComputerData.getinstalledpackages()

@register_command("env", registry=GET_REGISTRY, help_text="get env - Displays environment variables.")
def g_env(): ComputerData.getenvvars()

@register_command("processes", aliases=["tasks"], registry=GET_REGISTRY, help_text="get processes - Displays top CPU processes.")
def g_proc(): ComputerData.getprocesses()

@register_command("net", aliases=["network"], registry=GET_REGISTRY, help_text="get net - Displays network traffic statistics.")
def g_net(): TelemetryData.getnet()

@register_command("upt", aliases=["uptime"], registry=GET_REGISTRY, help_text="get upt - Displays system uptime.")
def g_upt(): TelemetryData.getupt()

@register_command("ip", aliases=["ipaddress"], registry=GET_REGISTRY, help_text="get ip - Displays local network IP addresses.")
def g_ip(): TelemetryData.getip()

@register_command("mac", aliases=["macaddress"], registry=GET_REGISTRY, help_text="get mac - Displays primary MAC address.")
def g_mac(): TelemetryData.getmac()

@register_command("publicip", aliases=["pipaddress", "publicipaddress"], registry=GET_REGISTRY, help_text="get publicip - Displays public IP address.")
def g_pubip(): TelemetryData.getpublicip()

@register_command("netstats", aliases=["adastats", "adapter", "netadapter"], registry=GET_REGISTRY, help_text="get netstats - Displays network adapter statuses.")
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

@register_command("appdev", aliases=["developer", "creator", "devs", "dev"], registry=GET_REGISTRY)
def g_appd():
    possible_devs = ["SXF", "SFX", "Your mom lol", developer]
    pctg = [98, 1.2, 0.7, 0.1]
    easysaxo.dev = random.choices(possible_devs, weights=pctg, k=1)[0]
    print(f"App developer: {Fore.CYAN}{easysaxo.dev}{Style.RESET_ALL}")

@register_command("app", aliases=["appinfo"], registry=GET_REGISTRY, help_text="get app - Displays general app details.")
def g_app(): print(f"App: {Fore.CYAN}{easysaxo.name} {easysaxo.ver}{Style.RESET_ALL} by {easysaxo.dev}")

@register_command("username", aliases=["name"], registry=GET_REGISTRY, help_text="get username - Displays registered user name (in app).")
def g_uname(): print(f"Username: {Fore.CYAN}{ThreadData.current_user}{Style.RESET_ALL}.")

@register_command("password", aliases=["pswd", "key"], registry=GET_REGISTRY, help_text="By privacy built-in configuration, you cannot get password.")
def g_pswd(): print(f"{Fore.RED}You cannot get password.{Style.RESET_ALL}.")

@register_command("attr", aliases=["attribute", "all"], registry=GET_REGISTRY, help_text="get attr - Fetches all telemetry and system specs.")
def g_all():
    print(f"{Fore.BLUE}== COMPUTER DATA =={Style.RESET_ALL}")
    for func in [g_cpu, g_arch, g_os, g_mboard, g_ram, g_gpu, g_disk, g_batt, g_user, g_py]: func()
    print(f"\n{Fore.BLUE}== TELEMETRY DATA =={Style.RESET_ALL}")
    for func in [g_net, g_upt, g_ip, g_mac, g_pubip, g_netstat]: func()
    print(f"\n{Fore.BLUE}== THREADING/MATH DATA =={Style.RESET_ALL}")
    g_th(); g_mset(); g_vars()
    print(f"\n{Fore.BLUE}== MISC DATA =={Style.RESET_ALL}")
    g_uname(); g_appn(); g_appv(); g_appd()


# =========== CORE COMMANDS + HELP ===========

@register_command("help", aliases=["?"], help_text="help [command] - Shows command list or syntax details for a target command.")
def c_help(arg):
    if not arg:
        print(f"{Fore.CYAN}COMMAND LIST: {Style.RESET_ALL}\n"
              f"{Fore.BLUE}help{Style.RESET_ALL}        : Access to {Fore.CYAN}Command List{Style.RESET_ALL} and description.\n"
              f"{Fore.BLUE}save{Style.RESET_ALL}        : Creates/rewrites a {Fore.RED}JSON file{Style.RESET_ALL} with {Fore.YELLOW}user{Style.RESET_ALL} data.\n"
              f"{Fore.BLUE}load{Style.RESET_ALL}        : Loads a {Fore.RED}JSON file{Style.RESET_ALL} with {Fore.YELLOW}user{Style.RESET_ALL} data.\n"
              f"{Fore.BLUE}get{Style.RESET_ALL}         : Gets information of a {Fore.YELLOW}variable{Style.RESET_ALL} or an {Fore.BLUE}attribute{Style.RESET_ALL}.\n"
              f"{Fore.BLUE}set{Style.RESET_ALL}         : Sets storable information like {Fore.YELLOW}user name{Style.RESET_ALL} and {Fore.YELLOW}variables{Style.RESET_ALL}.\n"
              f"{Fore.BLUE}reset{Style.RESET_ALL}       : Resets {Fore.YELLOW}user data{Style.RESET_ALL} (either {Fore.YELLOW}user name{Style.RESET_ALL} or {Fore.YELLOW}password{Style.RESET_ALL}).\n"
              f"{Fore.BLUE}math{Style.RESET_ALL}        : Allows mathematical equations (Use {Fore.CYAN}get mathset{Style.RESET_ALL} to get complex operators)\n"
              f"{Fore.BLUE}time{Style.RESET_ALL}        : Displays {Fore.YELLOW}hour{Style.RESET_ALL} and {Fore.YELLOW}date{Style.RESET_ALL}.\n"
              f"{Fore.BLUE}timer{Style.RESET_ALL}       : Sets a timer in {Fore.GREEN}seconds{Style.RESET_ALL} before showing up a {Fore.CYAN}message{Style.RESET_ALL}.\n"
              f"{Fore.BLUE}random{Style.RESET_ALL}      : Shows a random {Fore.YELLOW}number{Style.RESET_ALL}.\n"
              f"{Fore.BLUE}delvar{Style.RESET_ALL}      : Deletes a specified {Fore.YELLOW}variable{Style.RESET_ALL}.\n"
              f"{Fore.BLUE}runloc{Style.RESET_ALL}      : Shows the {Fore.MAGENTA}current location{Style.RESET_ALL} of the script operations.\n"
              f"{Fore.BLUE}check{Style.RESET_ALL}       : Checks if required {Fore.MAGENTA}script files{Style.RESET_ALL} exist where they shall be.\n"
              f"{Fore.BLUE}filelst{Style.RESET_ALL}     : Lists files and folders in a directory.\n"
              f"{Fore.BLUE}fileloc{Style.RESET_ALL}     : Shows the {Fore.MAGENTA}location{Style.RESET_ALL} of a {Fore.RED}file{Style.RESET_ALL}.\n"
              f"{Fore.BLUE}filecrt{Style.RESET_ALL}     : Creates a {Fore.RED}file{Style.RESET_ALL} with specified extension.\n"
              f"{Fore.BLUE}filerd{Style.RESET_ALL}      : Reads and displays the content of a {Fore.RED}file{Style.RESET_ALL}.\n"
              f"{Fore.BLUE}filedel{Style.RESET_ALL}     : Deletes a {Fore.RED}file{Style.RESET_ALL}.\n"
              f"{Fore.BLUE}filewrt{Style.RESET_ALL}     : Writes over a {Fore.RED}file{Style.RESET_ALL}.\n"
              f"{Fore.BLUE}fileopn{Style.RESET_ALL}     : Opens a {Fore.RED}file{Style.RESET_ALL}.\n"
              f"{Fore.BLUE}filecls{Style.RESET_ALL}     : Closes a {Fore.RED}file{Style.RESET_ALL}.\n"
              f"{Fore.BLUE}jsonrd{Style.RESET_ALL}      : Reads a {Fore.RED}JSON file{Style.RESET_ALL}.\n"
              f"{Fore.BLUE}regex{Style.RESET_ALL}       : Looks for {Fore.GREEN}patterns{Style.RESET_ALL} in a text.\n"
              f"{Fore.BLUE}playaudio{Style.RESET_ALL}   : Plays an {Fore.RED}audio file{Style.RESET_ALL} (specify the route).\n"
              f"{Fore.BLUE}stopaudio{Style.RESET_ALL}   : Stops the current {Fore.RED}audio file{Style.RESET_ALL}.\n"
              f"{Fore.BLUE}exit{Style.RESET_ALL}        : Exit {Fore.CYAN}{easysaxo.name}{Style.RESET_ALL}.\n"
              f"\nRemember you can search for command's syntax and usage by using {Fore.GREEN}help <cmd/attr>{Style.RESET_ALL} :)")
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

@register_command("exit", aliases=["quit"], help_text="exit - Saves session state and exits EasySaxo.")
def c_exit(arg): pass

@register_command("clear", aliases=["clr", "clrscr"], help_text="clear - Clears the terminal screen.")
def c_clear(arg): os.system('cls' if os.name == 'nt' else 'clear')

@register_command("save", help_text="save [filepath.json] - Saves the current session state and math variables.")
def c_save(arg): SessionManager.save_session(ThreadData.current_user, arg)

@register_command("load", help_text="load <filepath.json> - Loads session state and variables from a file.")
def c_load(arg):
    if arg:
        session_info = SessionManager.load_session(arg)
        if isinstance(session_info, dict):
            ThreadData.current_user = session_info.get("user_name", "User")
            ThreadData.current_pswd = session_info.get("password")
        else:
            ThreadData.current_user = session_info
    else:
        print(f"{Fore.RED}Usage: load <filepath.json>{Style.RESET_ALL}")
        
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
def c_get(arg): # Magic. Do not touch
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

@register_command("check", aliases=["allowance", "checkf", "filechk"], help_text="check - Checks if all script files exist and are available.")
def c_check(arg): DirLocation.allowance()

@register_command("dircrt", aliases=(["dcreate"]), help_text="dircrt <dirname> - Creates a raw directory.")
def c_dircrt(arg): DirLocation.dircrt(arg) if arg else print(f"{Fore.RED}Missing directory name.{Style.RESET_ALL}")

@register_command("dirdel", aliases=(["ddelete"]), help_text="dirdel <dirname> - Deletes a directory.")
def c_dirdel(arg): DirLocation.dirdel(arg) if arg else print(f"{Fore.RED}Missing directory path.{Style.RESET_ALL}")

@register_command("filelst", aliases=["ls", "dir", "lsdir", "dirls", "listdir", "dirlist"], help_text="filelst [path] - Lists files and subdirectories in the specified or current directory.")
def c_filelst(arg): DirLocation.ls(arg)

@register_command("fileopn", aliases=["openf"], help_text="fileopn <filepath> - Opens a file with the default system application.")
def c_fileopn(arg): DirLocation.fileopn(arg) if arg else print(f"{Fore.RED}Missing filepath.{Style.RESET_ALL}")

@register_command("filecls", aliases=["closef"], help_text="filecls <process_name> - Terminates process(es) matching the given name.")
def c_filecls(arg): DirLocation.filecls(arg) if arg else print(f"{Fore.RED}Missing process name.{Style.RESET_ALL}")

@register_command("fileloc", aliases=["locatef"], help_text="fileloc <filename> - Searches and locates a file within the working directory.")
def c_fileloc(arg): DirLocation.fileloc(arg) if arg else print(f"{Fore.RED}Missing filename.{Style.RESET_ALL}")

@register_command("filecrt", aliases=["createf"], help_text="filecrt <filepath> - Creates an empty file at the designated location.")
def c_filecrt(arg):
    if not arg:
        print(f"{Fore.RED}Missing filepath.{Style.RESET_ALL}")
        return

    parts = arg.split()
    if len(parts) == 2:target_path = os.path.join(parts[1], parts[0])
    else:target_path = parts[0]

    DirLocation.filecrt(target_path)

@register_command("filerd", aliases=["readf"], help_text="filerd <filepath> - Reads and prints text content from a target file.")
def c_filerd(arg): DirLocation.filerd(arg) if arg else print(f"{Fore.RED}Missing filepath.{Style.RESET_ALL}")

@register_command("filedel", aliases=["deletef"], help_text="filedel <filepath> - Permanently removes a file from disk.")
def c_filedel(arg): DirLocation.filedel(arg) if arg else print(f"{Fore.RED}Missing filepath.{Style.RESET_ALL}")

@register_command("filewrt", aliases=["writef"], help_text="filewrt <filepath> <content> - Overwrites target file with text content.")
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

@register_command("set", help_text="set name/password <new_name/new_password> | set var <var_name> <value> - Updates session username or math variables.\nNote: Username or password has to be one single word (e.g. Sax_93; cool-password.123)")
def c_set(arg):
    if not arg: print(f"{Fore.RED}Usage: set name/password <new_name/new_password> OR set var <var_name> <value>{Style.RESET_ALL}")
    else:
        parts = arg.split(maxsplit=2)
        if parts[0].lower() == "name" and len(parts) >= 2:
            ThreadData.current_user = parts[1]
            print(f"User name replaced to {Fore.GREEN}{parts[1]}{Style.RESET_ALL}.")
            SessionManager.save_session(ThreadData.current_user)
        elif parts[0].lower() in ["var", "variable"] and len(parts) == 3:
            MathFunc.set_var(parts[1], parts[2]); SessionManager.save_session(ThreadData.current_user)
        elif parts[0].lower() in ["password", "key", "pswd"] and len(parts) >= 2:
            ThreadData.current_pswd = parts[1]
            print(f"Password assigned. It will load {Fore.MAGENTA}next session{Style.RESET_ALL}.")
            SessionManager.save_session(ThreadData.current_user)
        else: print(f"{Fore.RED}Unknown/malformed set subcommand.{Style.RESET_ALL}")

@register_command("reset", help_text="reset <name/password>")
def c_reset(arg):
    if not arg: print(f"{Fore.RED}Usage: reset <name/password>{Style.RESET_ALL}")
    else:
        parts = arg.strip().split()
        if parts[0].lower() in ["name", "username"] and len(parts) == 1:
            ThreadData.current_user = "User"
            print(f"User name set to {Fore.GREEN}User{Style.RESET_ALL}")
            SessionManager.save_session(ThreadData.current_user)
        elif parts[0].lower() in ["password", "pswd", "key"] and len(parts) == 1:
            ThreadData.current_pswd = None
            print("Password cleared successfully.")
            SessionManager.save_session(ThreadData.current_user)

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

@register_command("unins", aliases=["uninstall", "selfdel", "sdelete"], help_text="unins - Guider to uninstall the program.")
def b_unins(arg=None):
    print(f"{Fore.LIGHTRED_EX}WARNING! This will delete all EasySaxo files and info.{Style.RESET_ALL}")
    con = input(f"{Fore.LIGHTCYAN_EX}Do you still want to proceed? (Y/N): {Style.RESET_ALL}").strip().lower() # please do not
    
    if con in ["y", "yes"]: # a.k.a if you_are == a_dumbass:
        print(f"Uninstalling EasySaxo {easysaxo.ver}...")
        time.sleep(0.5)
        
        base_dir = os.path.dirname(os.path.abspath(__file__))
        note_path = os.path.join(base_dir, "goodbye.txt")

        with open(note_path, "w", encoding="utf-8") as f:
            f.write("Thanks for using EasySaxo! We'll miss you. :(\n")

        try:
            if os.name == 'nt':
                os.startfile(note_path)
            elif sys.platform == 'darwin':
                subprocess.Popen(["open", note_path])
            else:
                subprocess.Popen(["xdg-open", note_path])
        except Exception as e:
            print(f"Could not open note automatically: {e}")

        for folder in ["esmodules", "__pycache__", ".vscode"]:
            folder_path = os.path.join(base_dir, folder)
            if os.path.exists(folder_path):
                shutil.rmtree(folder_path, ignore_errors=True)

        files_to_delete = [
            "config.py", "session.json", "translations.json", 
            "termtest.py", "main.py", "commands.py", "easysaxoA1-01.code-workspace"
        ]
        
        for file in files_to_delete:
            file_path = os.path.join(base_dir, file)
            if os.path.exists(file_path):
                try:
                    os.remove(file_path)
                except Exception:
                    pass # unless python crashes here

        print("Uninstalled successfully.")
        sys.exit(0) # Force exit
    else: print("Uninstall canceled.") #yeeeeeeah
    
# Now, only God knows