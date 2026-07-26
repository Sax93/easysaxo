#=================================================
# Telemetry and Identification Access
#=================================================

import time, socket, uuid, re
import urllib
from colorama import Fore, Style

class TelemetryData:
    @staticmethod
    def getnet():
        import psutil
        net_io = psutil.net_io_counters()
        print("\n--- Network Traffic Statistics ---")
        print(f"Bytes Sent/Recv: {Fore.CYAN}{net_io.bytes_sent / (1024**2):.2f} MB{Style.RESET_ALL} / {Fore.CYAN}{net_io.bytes_recv / (1024**2):.2f} MB{Style.RESET_ALL}")
        print(f"Packets Sent/Recv: {Fore.CYAN}{net_io.packets_sent}{Style.RESET_ALL} / {Fore.CYAN}{net_io.packets_recv}{Style.RESET_ALL}")

    @staticmethod
    def getupt():
        import psutil
        uptime = time.time() - psutil.boot_time()
        hrs_val, remainder = divmod(int(uptime), 3600)
        mins, secs = divmod(remainder, 60)
        days, hrs_val = divmod(hrs_val, 24)
        print(f"System Uptime: {Fore.MAGENTA}{days}d {hrs_val}h {mins}m {secs}s{Style.RESET_ALL}")

    @staticmethod
    def getip():
        import psutil
        print("\n--- Network Interfaces & IP Addresses ---")
        for interface, addrs in psutil.net_if_addrs().items():
            print(f"Interface: {Fore.YELLOW}{interface}{Style.RESET_ALL}")
            for addr in addrs:
                if addr.family == socket.AF_INET: print(f"  IPv4: {Fore.GREEN}{addr.address}{Style.RESET_ALL}")
                elif addr.family == socket.AF_INET6: print(f"  IPv6: {Fore.CYAN}{addr.address}{Style.RESET_ALL}")

    @staticmethod
    def getmac():
        mac = ":".join(re.findall("..", "%012x" % uuid.getnode()))
        print(f"Primary MAC Address: {Fore.BLUE}{mac.upper()}{Style.RESET_ALL}")

    @staticmethod
    def getpublicip():
        print("Fetching public IP address...")
        try:
            pub_ip = urllib.request.urlopen("https://api.ipify.org", timeout=4).read().decode("utf-8")
            print(f"Public IP Address: {Fore.GREEN}{pub_ip}{Style.RESET_ALL}")
        except Exception:
            print(f"Public IP: {Fore.RED}Unable to fetch public IP (Offline or Timeout){Style.RESET_ALL}")

    @staticmethod
    def getnetstats():
        import psutil
        stats = psutil.net_if_stats()
        print("\n--- Network Adapter Hardware Status ---")
        for nic, stat in stats.items():
            status = f"{Fore.GREEN}UP{Style.RESET_ALL}" if stat.isup else f"{Fore.RED}DOWN{Style.RESET_ALL}"
            print(f"Adapter {Fore.YELLOW}{nic}{Style.RESET_ALL}: Status [{status}] | Speed: {stat.speed}MB | MTU: {stat.mtu}")

    @staticmethod
    def getconnections():
        import psutil
        print("\n--- Active Connections (Sample) ---")
        try:
            conns = psutil.net_connections(kind="inet")
            for conn in conns[:10]:
                laddr = f"{conn.laddr.ip}:{conn.laddr.port}" if conn.laddr else "N/A"
                raddr = f"{conn.raddr.ip}:{conn.raddr.port}" if conn.raddr else "N/A"
                print(f"Proto: {conn.type.name} | Local: {Fore.GREEN}{laddr:<20}{Style.RESET_ALL} -> Remote: {Fore.CYAN}{raddr:<20}{Style.RESET_ALL} Status: {conn.status}")
        except Exception as e:
            print(f"{Fore.RED}Could not fetch active connections: {e}{Style.RESET_ALL}")

    @staticmethod
    def speedtest_network():
        try: import speedtest
        except ImportError: speedtest = None
        
        if not speedtest:
            print(f"{Fore.YELLOW}Speedtest package not installed. Install with 'pip install speedtest-cli'.{Style.RESET_ALL}")
            return
        print("Testing network speed (this may take a few seconds)...")
        try:
            st = speedtest.Speedtest()
            st.get_best_server()
            print(f"Download Speed: {Fore.GREEN}{st.download() / (1024**2):.2f} Mbps{Style.RESET_ALL}")
            print(f"Upload Speed: {Fore.GREEN}{st.upload() / (1024**2):.2f} Mbps{Style.RESET_ALL}")
            print(f"Ping: {Fore.CYAN}{st.results.ping} ms{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}Speed test failed: {e}{Style.RESET_ALL}")
