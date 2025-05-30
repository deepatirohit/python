import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label = QLabel("Enter city Name: ", self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get Weather", self)
        self.temperature_label = QLabel( self)
        self.emoji_label = QLabel(self)
        self.description_label = QLabel(self)
        self.initUI()
        
     #Weather app interface 
    def initUI(self):
        self.setWindowTitle("Weather App")
        
        vbox = QVBoxLayout()
        
        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label )
        
        self.setLayout(vbox)
        
        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)
        
        
        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.temperature_label.setObjectName("temperature_label")
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setObjectName("description_label")
        
        # stylesheet
        self.setStyleSheet("""
            QLabel, QPushButton{
                font-family: calibri;
            }
            QLabel#city_label{
                font-size:40px;
                font-style:italic;
            }
            QLineEdit#city_input{
                font-size: 40px;
            }
            QPushButton#get_weather_button{
                font-size: 30px;
                font-weight: bold;
            }
            QLabel#temperature_label{
                font-size: 75px;
            }
            QLabel#emoji_label{
                font-size: 100px;
                font-family:segoe UI emoji;
            }
            QLabel#description_label{
                font-size: 50px;
            }
                           """)
        
        self.get_weather_button.clicked.connect(self.get_weather)
        
        
    def get_weather(self):
        api_key = "39f939c5c90b7c99a037f6f73e21b37b"
        city = self.city_input.text()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        
        try:
            response = requests.get(url)
            response.raise_for_status() # Raises HTTPError, if one occurred.
            data = response.json()
            
            if data["cod"] == 200:
                self.display_weather(data)
                
        except requests.exceptions.HTTPError:
            if response.status_code == 400:
                self.display_error("Bad request:\nPlease check your input.")
            elif response.status_code == 401:
                self.display_error("Unauthorized:\nInvalid API key.")
            elif response.status_code == 403:
                self.display_error("Forbidden:\nAccess is denied")
            elif response.status_code == 404:
                self.display_error("Not found:\nThe resource could not be located.")
            elif response.status_code == 500:
                self.display_error("Internal Server Error:\nPlease try again later.")
            elif response.status_code == 502:
                self.display_error("Bad Gateway:\nInvalid response from the server.")
            elif response.status_code == 503:
                self.display_error("Service Unavailable:\nServer is down.")
            elif response.status_code == 504:
                self.display_error("Gateway Timeout:\nNo response from the server.")
            else:
                self.display_error(f"Unexpected status code: {response.status_code}")


        except requests.exceptions.ConnectionError:
            self.display_error("Connection Error:\nCheck your internet connection")
        except requests.exceptions.Timeout:
            self.display_error("Timeout Error:\nThe request timed out")
        except requests.exceptions.TooManyRedirects:
            self.display_error("Too many Redirects:\nCheck the URL")
                    
        # request exception due to network problem, invalid url
        except requests.exceptions.RequestException as req_error:
            self.display_error(f"Request Error:\n{req_error}")
        
            
    def display_error(self, message):
        self.temperature_label.setStyleSheet("font-size: 30px;")
        self.temperature_label.setText(message)
    
    def display_weather(self, data):
        self.temperature_label.setStyleSheet("font-size: 40px;")
        temperature_k = data["main"]["temp"]
        temperature_c = temperature_k - 273.15
        weather_id = data["weather"][0]["id"]
        weather_description = data["weather"][0]["description"]
        
        
        self.temperature_label.setText(f"{int(temperature_c)}°")
        self.emoji_label.setText(self.get_weather_emoji(weather_id))
        self.description_label.setText(f"{weather_description}")
    
    @staticmethod  
    def get_weather_emoji(weather_id):
        if 200 <= weather_id < 300:
            return "⛈️"  
        elif 300 <= weather_id < 400:
            return "🌦️"  
        elif 500 <= weather_id < 600:
            return "🌧️"  
        elif 600 <= weather_id < 700:
            return "❄️"  
        elif 700 <= weather_id < 800:
            return "🌫️"  
        elif weather_id == 800:
            return "☀️"  
        elif 801 <= weather_id < 900:
            return "☁️"  
        else:
            return ""  


    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())