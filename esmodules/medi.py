#=================================================
# 8. Multimedia
#=================================================

import os
from esmodules.dirloct import DirLocation
from colorama import Fore, Style

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