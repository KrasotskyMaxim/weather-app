import random

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow
from templates import Ui_ChooseEnterForm


class ChooseEnterView(QMainWindow):
    mixed_tips = [
        "During a <b>thunderstorm</b>, stay <b>indoors</b> and avoid using <b>electronic devices</b> or appliances that are plugged in.",
        "If you are caught outside during a <b>thunderstorm</b>, seek <b>shelter</b> in a low-lying area or in a car <i>(with windows closed)</i>.",
        "During a <b>hurricane</b>, secure <b>outdoor</b> furniture and objects to prevent them from becoming projectiles.",
        "If you are in a low-lying area or near the coast during a <b>hurricane</b>, evacuate.",
        "During a <b>snowstorm</b>, dress warmly and in layers to stay <b>warm</b>.",
        "If you have to shovel snow during a <b>snowstorm</b>, do it in small amounts to avoid <b>overexertion</b>.",
        "During a <b>heatwave</b>, stay <b>indoors</b> in a cool place, drink plenty of water, and avoid alcohol or caffeine.",
        "If you have to go outside during a <b>heatwave</b>, wear <b>loose</b>, light-colored <b>clothing</b> and a <b>hat</b>.",
        "During a <b>tornado</b>, seek <b>shelter</b> in a basement or <b>interior room</b> on the lowest level of a building.",
        "If you are caught outside during a <b>tornado</b>, seek <b>shelter</b> in a low-lying area or in a ditch, and cover your <b>head</b> and <b>neck</b> with your arms or a blanket to protect yourself from flying debris.",
        "During a <b>rainy weather</b>, carry an <b>umbrella</b> or wear a <b>raincoat</b> to stay <b>dry</b>.",
        "If you need to drive during a <b>rainy weather</b>, slow down and increase your following distance from other vehicles.",
        "During <b>cold weather</b>, dress in layers to stay warm and protect your extremities <i>(hands, feet, head)</i>.",
        "If you have to be outside in <b>cold weather</b>, avoid <b>overexerting</b> yourself and take frequent breaks to warm up.",
        "During <b>hot weather</b>, stay hydrated by <b>drinking</b> plenty of water and avoid alcohol or caffeine.",
        "If you have to be outside in <b>hot weather</b>, take frequent <b>breaks</b> in a cool place and wear loose, light-colored clothing."
    ]

    def __init__(self):
        super(ChooseEnterView, self).__init__()
        random.shuffle(self.mixed_tips)
        self.tip_index = 0
        self.ui = Ui_ChooseEnterForm(self)
        self.init_UI()

    def init_UI(self):
        self.ui.tip_textBrowser.setStyleSheet("font-size: 20px; font-family: 'Arial';")
        self.ui.tip_textBrowser.setText(self.mixed_tips[0])
        
        self.ui.next_tip_login_pushButton.clicked.connect(self.next_tip)
        self.ui.prev_tip_login_pushButton.clicked.connect(self.prev_tip)

        self.hide_interface()
                
    def hide_interface(self):
        pass
    
    def next_tip(self):
        if not (next_index := self.tip_index + 1) >= len(self.mixed_tips):
            self.ui.tip_textBrowser.setText(self.mixed_tips[next_index])
            self.tip_index = next_index
    
    def prev_tip(self):
        if not (prev_index := self.tip_index - 1) < 0:
            self.ui.tip_textBrowser.setText(self.mixed_tips[prev_index])
            self.tip_index = prev_index
    