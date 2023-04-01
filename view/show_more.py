from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtGui

from templates import Ui_ShowMoreForm
from model.data import WeatherData


class ShowMoreView(QMainWindow):
    
    forecast_html = "<p><strong>Weather:</strong><br> {main}<em>({description})</em><br><strong>Temp:</strong> {temp}°C<br><strong>Wind:</strong> {wind_speed}m/s<strong><br>Humidity:</strong> {humidity}</p><p align='center'><em>{date}</em></p>"
    
    def __init__(self):
        super(ShowMoreView, self).__init__()
        self.ui = Ui_ShowMoreForm(self)
        self.init_UI()

    def init_UI(self):
        self.hide_interface()

    def hide_interface(self):
        pass
    
    def set_forecast(self, forecast: list[WeatherData]):
        html = self.forecast_html.format(
            main=forecast[0].main,
            description=forecast[0].description,
            temp=forecast[0].temp,
            feels_like=forecast[0].feels_like,
            wind_speed=forecast[0].wind_speed,
            humidity=forecast[0].humidity,
            date=forecast[0].current_time
        )
        self.ui.one_icon_label.setPixmap(QtGui.QPixmap(forecast[0].icon))
        self.ui.one_textBrowser.setHtml(html)

        html = self.forecast_html.format(
            main=forecast[1].main,
            description=forecast[1].description,
            temp=forecast[1].temp,
            feels_like=forecast[1].feels_like,
            wind_speed=forecast[1].wind_speed,
            humidity=forecast[1].humidity,
            date=forecast[1].current_time
        )
        self.ui.two_icon_label.setPixmap(QtGui.QPixmap(forecast[1].icon))
        self.ui.two_textBrowser.setHtml(html)

        html = self.forecast_html.format(
            main=forecast[2].main,
            description=forecast[2].description,
            temp=forecast[2].temp,
            feels_like=forecast[2].feels_like,
            wind_speed=forecast[2].wind_speed,
            humidity=forecast[2].humidity,
            date=forecast[2].current_time
        )
        self.ui.three_icon_label.setPixmap(QtGui.QPixmap(forecast[2].icon))
        self.ui.three_textBrowser.setHtml(html)

        html = self.forecast_html.format(
            main=forecast[3].main,
            description=forecast[3].description,
            temp=forecast[3].temp,
            feels_like=forecast[3].feels_like,
            wind_speed=forecast[3].wind_speed,
            humidity=forecast[3].humidity,
            date=forecast[3].current_time
        )
        self.ui.four_icon_label.setPixmap(QtGui.QPixmap(forecast[3].icon))
        self.ui.four_textBrowser.setHtml(html)

        html = self.forecast_html.format(
            main=forecast[4].main,
            description=forecast[4].description,
            temp=forecast[4].temp,
            feels_like=forecast[4].feels_like,
            wind_speed=forecast[4].wind_speed,
            humidity=forecast[4].humidity,
            date=forecast[4].current_time
        )
        self.ui.five_icon_label.setPixmap(QtGui.QPixmap(forecast[4].icon))
        self.ui.five_textBrowser.setHtml(html)
