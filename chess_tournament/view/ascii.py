from chess_tournament.view.bcolors import Bcolors


def show_banner():
    """Display the banner in the console"""
    print(
        f"{Bcolors.OKBLUE}"
        f"  _____                            _       _ _   __      _               \n"
        f" |_   _|__  _   _ _ __ _ __   ___ (_)   __| ( ) /_/  ___| |__   ___  ___ \n"
        f"   | |/ _ \| | | | '__| '_ \ / _ \| |  / _` |/ / _ \/ __| '_ \ / _ \/ __|\n"
        f"   | | (_) | |_| | |  | | | | (_) | | | (_| | |  __/ (__| | | |  __/ (__ \n"
        f"   |_|\___/ \__,_|_|  |_| |_|\___/|_|  \__,_|  \___|\___|_| |_|\___|\___|\n"
        f"{Bcolors.ENDC}"
    )
