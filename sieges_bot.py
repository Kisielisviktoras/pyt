from pages.home.home_screen import HomeScreen
from pages.siege_pop.siege_pop import SiegePop
from pages.sieges.sieges import Sieges
from utils import *

home_screen = HomeScreen()
click(home_screen.siege.click_point)

sieges_pop = SiegePop()
click(sieges_pop.sieges.click_point)

sieges = Sieges()
click(sieges.track_boss.click_point)
