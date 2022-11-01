from ScreenTarget import Target, Monitor
from utils import *

class HomeScreen:
    siege_icon = 'pages/home/icons/siege_tower_btn.png'
    siege = 0
    def __init__(self):
        self.initialize()

    def initialize(self):
        self.siege = wait_find(self.siege_icon, True)
