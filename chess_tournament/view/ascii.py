from chess_tournament.view.bcolors import Bcolors


def show_banner():
    """Display the banner in the console"""
    print(
        f"{Bcolors.OKBLUE}"
        r"""
  _____                            _       _ _   __      _               
 |_   _|__  _   _ _ __ _ __   ___ (_)   __| ( ) /_/  ___| |__   ___  ___ 
   | |/ _ \| | | | '__| '_ \ / _ \| |  / _` |/ / _ \/ __| '_ \ / _ \/ __|
   | | (_) | |_| | |  | | | | (_) | | | (_| | |  __/ (__| | | |  __/ (__ 
   |_|\___/ \__,_|_|  |_| |_|\___/|_|  \__,_|  \___|\___|_| |_|\___|\___|
        """
        f"{Bcolors.ENDC}"
    )
