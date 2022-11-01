from utils import *

class SiegePop:
    sieges_icon = 'pages/siege_pop/icons/sieges_btn.png'
    sieges = 0
    def __init__(self):
        self.initialize()

    def initialize(self):
        self.sieges = wait_find(self.sieges_icon, True)
