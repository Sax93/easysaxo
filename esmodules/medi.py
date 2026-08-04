#=================================================
# 8. Multimedia
#=================================================

#`medi.py` ONLY FOR MULTIMEDIA FILE HANDLING COMMAND DEFINING

import os
from esmodules.dirloct import DirLocation
from colorama import Fore, Style

try: # we are trying to import asciiart here to avoid double check
    from ascii_magic import AsciiArt
    ASCII_AVAILABLE = True
except ImportError: ASCII_AVAILABLE = False

class MediaData:
    pygame_initialized = False

    @staticmethod
    def init_pygame():
        import pygame
        if not MediaData.pygame_initialized:
            os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
            pygame.mixer.init()
            MediaData.pygame_initialized = True
        return pygame

    @staticmethod
    def playaudio(filepath):
        try:
            pygame = MediaData.init_pygame()
            pygame.mixer.music.load(DirLocation._resolve_path(filepath))
            pygame.mixer.music.play()
            print(f"Playing audio: {Fore.GREEN}{filepath}{Style.RESET_ALL}")
        except Exception as e: print(f"{Fore.RED}Error playing audio file: {e}{Style.RESET_ALL}")

    @staticmethod
    def stopaudio():
        try:
            import pygame
            if MediaData.pygame_initialized and pygame.mixer.music.get_busy():
                pygame.mixer.music.stop()
                print(f"{Fore.GREEN}Audio stopped.{Style.RESET_ALL}")
            else: print(f"{Fore.YELLOW}No audio is currently playing.{Style.RESET_ALL}")
        except Exception as e: print(f"{Fore.RED}Error stopping audio: {e}{Style.RESET_ALL}")
    
    @staticmethod
    def render(filepath, colnum=80):
        if not ASCII_AVAILABLE:
            print(f"{Fore.RED}ASCII Art not available.{Style.RESET_ALL}")
            return

        VALID_EXTENSIONS = ('.png', '.jpg', '.jpeg', '.webp', '.bmp', '.gif')
        if not filepath.lower().endswith(VALID_EXTENSIONS):
            print(f"{Fore.RED}Error: Invalid image extension. Supported: {', '.join(VALID_EXTENSIONS)}{Style.RESET_ALL}")
            return

        if not os.path.isfile(filepath):
            print(f"{Fore.RED}Error: Image file '{filepath}' not found.{Style.RESET_ALL}")
            return

        try:
            print(f"{Fore.LIGHTMAGENTA_EX}Rendering your image...{Style.RESET_ALL}")
            cols = int(colnum) if str(colnum).isdigit() else 80
            ascii_r = AsciiArt.from_image(filepath)
            ascii_r.to_terminal(columns=cols)
        except Exception as e: print(f"{Fore.RED}Could not render: {e}{Style.RESET_ALL}")
        
# holy useless code