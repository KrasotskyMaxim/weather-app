from PyQt5.QtWidgets import QMainWindow, QCompleter
from PyQt5.QtCore import QTimer, QTime, QDate
from PyQt5 import QtGui

from templates import Ui_HomeForm

from exceptions import show_exception, CityException


class HomeView(QMainWindow):
    '''Home view class.'''
    
    datetime_html = "<p align='center'><span style='font-size: 11pt; font-family: Arial;'><b>{current_time}</b><br>{current_date}</span></p>"
    weather_html = "<p align='center'><strong>{city}</strong></p><p><strong>Weather:</strong> {main} <em>({description})</em><br><strong>Temp:</strong> {temp}°C<br><strong>Feels like:</strong> {feels_like}°C</p><strong>Wind:</strong> {wind_speed}m/s<br><strong>Sunrise time:</strong> {sunrise_time}<br><strong>Sunset time:</strong> {sunset_time}<br><strong>Humidity:</strong> {humidity}% </p><br><p align='center'><em>actual on: {current_time}</em></p>"

    def __init__(self, controller):
        super(HomeView, self).__init__()
        # self.current_city = 
        self.ui = Ui_HomeForm(self)
        self.controller = controller
        self.init_UI()

    def init_UI(self):
        timer = QTimer(self)
        timer.timeout.connect(self.update_time)
        timer.start(1000)

        cities = self.controller.get_cities()
        completer = QCompleter(cities)
        self.ui.search_lineEdit.setCompleter(completer)

        self.hide_interface()
                
    def hide_interface(self):
        pass
    
    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss")
        current_date = QDate.currentDate().toString("ddd MMM d yyyy")
        html = self.datetime_html.format(current_time=current_time, current_date=current_date)
        self.ui.current_datetime_textBrowser.setHtml(html)

    def update_weather(self, weather_data):
        html = self.weather_html.format(
            city=weather_data.city,
            main=weather_data.main,
            description=weather_data.description,
            temp=weather_data.temp,
            feels_like=weather_data.feels_like,
            wind_speed=weather_data.wind_speed,
            sunrise_time=weather_data.sunrise_time,
            sunset_time=weather_data.sunset_time,
            humidity=weather_data.humidity,
            current_time=weather_data.current_time
        )
        self.ui.weather_icon_label.setPixmap(QtGui.QPixmap(weather_data.icon))
        self.ui.weather_info_textBrowser.setHtml(html)

    def refresh(self):
        self.controller.refresh_weather()
        
    def search(self):
        try:
            self.controller.search_city(self.ui.search_lineEdit.text())
            self.ui.search_lineEdit.clear()
        except CityException as e:
            show_exception("City error", str(e))
