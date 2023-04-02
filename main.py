from PySide6 import QtWidgets, QtGui, QtCore
import sys


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AGRIFARM")
        self.setFixedSize(900, 700)

        self.show_main_window()

    def show_main_window(self):

        # create main widget
        self.setGeometry(100, 100, 900, 700)
        self.setWindowTitle('AGRIFARM')

        # create the main widget and set it as the central widget
        self.main_widget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.main_widget)

        # create the Agrifarm label and add it to the main widget
        agrifarm_label = QtWidgets.QLabel('AGRIFARM', self.main_widget)
        agrifarm_label.setFont(QtGui.QFont("Arial", 20, QtGui.QFont.Bold))
        agrifarm_label.setGeometry(0, 0, 900, 40)
        agrifarm_label.setAlignment(QtCore.Qt.AlignCenter)

        # create the location checkbox and add it to the main widget
        location_combobox = QtWidgets.QComboBox(self.main_widget)
        location_combobox.setGeometry(10, 50, 100, 30)
        location_combobox.addItems(["Location 1", "Location 2", "Location 3"])

        # create the suggestion box and add it to the main widget
        suggestion_box = QtWidgets.QGroupBox('Suggestion', self.main_widget)
        suggestion_box.setGeometry(150, 50, 400, 150)
        suggestion_layout = QtWidgets.QVBoxLayout(suggestion_box)
        suggestion_text = QtWidgets.QLabel('Enter suggestion here...', suggestion_box)
        suggestion_text.setWordWrap(True)
        suggestion_text.setAlignment(QtCore.Qt.AlignTop)
        suggestion_layout.addWidget(suggestion_text)

        # create the update box and add it to the main widget
        update_box = QtWidgets.QGroupBox('Update', self.main_widget)
        update_box.setGeometry(570, 50, 320, 150)
        update_layout = QtWidgets.QVBoxLayout(update_box)
        update_text = QtWidgets.QLabel('Enter update here...', update_box)
        update_text.setWordWrap(True)
        update_text.setAlignment(QtCore.Qt.AlignTop)
        update_layout.addWidget(update_text)

        # create the suggestion and update buttons and add them to the main widget
        suggestion_button = QtWidgets.QPushButton('Submit Suggestion', self.main_widget)
        suggestion_button.setGeometry(150, 210, 200, 30)
        update_button = QtWidgets.QPushButton('Submit Update', self.main_widget)
        update_button.setGeometry(570, 210, 200, 30)

        # create the weather and price buttons and add them to the main widget
        weather_button = QtWidgets.QPushButton('Weather', self.main_widget)
        weather_button.setGeometry(150, 270, 200, 50)
        price_button = QtWidgets.QPushButton('Price', self.main_widget)
        price_button.setGeometry(600, 270, 200, 50)
        soil_button = QtWidgets.QPushButton('Soil', self.main_widget)
        soil_button.setGeometry(380, 270, 200, 50)

        # create the signals for the weather and price buttons
        weather_button.clicked.connect(self.show_weather_page)
        price_button.clicked.connect(self.show_price_page)
        soil_button.clicked.connect(self.show_soil_page)

        # create the user guide button and add it to the main widget
        user_guide_button = QtWidgets.QPushButton('User Guide', self.main_widget)
        user_guide_button.setGeometry(800, 650, 80, 30)
        user_guide_button.clicked.connect(self.show_user_guide)

    def show_weather_page(self):
        # create weather widget
        self.weather_widget = QtWidgets.QWidget()

        # create layout for weather widget
        weather_layout = QtWidgets.QVBoxLayout(self.weather_widget)

        # create label for Weather
        weather_label = QtWidgets.QLabel(
            "Weather", alignment=QtCore.Qt.AlignCenter)
        weather_label.setFont(QtGui.QFont("Arial", 20, QtGui.QFont.Bold))

        # create layout for current weather
        current_weather_layout = QtWidgets.QHBoxLayout()
        current_weather_label = QtWidgets.QLabel("Current Weather:")
        current_weather_value_label = QtWidgets.QLabel("Sunny")
        current_weather_layout.addWidget(current_weather_label)
        current_weather_layout.addWidget(current_weather_value_label)

        # create layout for past weather
        past_weather_layout = QtWidgets.QHBoxLayout()
        past_weather_label = QtWidgets.QLabel("Past Weather Condition:")
        past_weather_value_label = QtWidgets.QLabel("Cloudy")
        past_weather_layout.addWidget(past_weather_label)
        past_weather_layout.addWidget(past_weather_value_label)

        # create button for graph
        graph_button = QtWidgets.QPushButton("Graph")
        graph_button.clicked.connect(self.show_graph_page)
        # create back button
        back_button = QtWidgets.QPushButton("Back")
        back_button.setGeometry(20, 20, 100, 30)
        back_button.clicked.connect(self.show_main_window)

        # add widgets and layouts to weather layout
        weather_layout.addWidget(weather_label)
        weather_layout.addLayout(current_weather_layout)
        weather_layout.addLayout(past_weather_layout)
        weather_layout.addWidget(graph_button)
        weather_layout.addWidget(back_button)

        # set weather widget as central widget
        self.setCentralWidget(self.weather_widget)

    def show_price_page(self):
        # create weather widget
                self.price_widget = QtWidgets.QWidget()

        # create layout for weather widget
                price_layout = QtWidgets.QVBoxLayout(self.price_widget)

        # create label for Weather
                price_label = QtWidgets.QLabel(
                    "Price", alignment=QtCore.Qt.AlignCenter)
                price_label.setFont(QtGui.QFont("Arial", 20, QtGui.QFont.Bold))

        # create layout for current weather
                current_price_layout = QtWidgets.QHBoxLayout()
                current_price_label = QtWidgets.QLabel("Current Rate:")
                current_price_value_label = QtWidgets.QLabel("---")
                current_price_layout.addWidget(current_price_label)
                current_price_layout.addWidget(current_price_value_label)

        # create layout for past weather
                past_price_layout = QtWidgets.QHBoxLayout()
                past_price_label = QtWidgets.QLabel("Past Rate:")
                past_price_value_label = QtWidgets.QLabel("---")
                past_price_layout.addWidget(past_price_label)
                past_price_layout.addWidget(past_price_value_label)

        # create button for graph
                graph_button = QtWidgets.QPushButton("Graph")
                graph_button.clicked.connect(self.show_graph_page)

        # create back button
                back_button = QtWidgets.QPushButton("Back")
                back_button.setGeometry(20, 20, 100, 30)
                back_button.clicked.connect(self.show_main_window)

        # add widgets and layouts to weather layout
                price_layout.addWidget(price_label)
                price_layout.addLayout(current_price_layout)
                price_layout.addLayout(past_price_layout)
                price_layout.addWidget(graph_button)
                price_layout.addWidget(back_button)

        # set weather widget as central widget
                self.setCentralWidget(self.price_widget)

    def show_soil_page(self):
        # create weather widget
                self.soil_widget = QtWidgets.QWidget()

        # create layout for weather widget
                soil_layout = QtWidgets.QVBoxLayout(self.soil_widget)

        # create label for Weather
                soil_label = QtWidgets.QLabel(
                    "Soil", alignment=QtCore.Qt.AlignCenter)
                soil_label.setFont(QtGui.QFont("Arial", 20, QtGui.QFont.Bold))

        # create layout for current weather
                current_soil_layout = QtWidgets.QHBoxLayout()
                current_soil_label = QtWidgets.QLabel("Current Rate:")
                current_soil_value_label = QtWidgets.QLabel("---")
                current_soil_layout.addWidget(current_soil_label)
                current_soil_layout.addWidget(current_soil_value_label)

        # create layout for past weather
                past_soil_layout = QtWidgets.QHBoxLayout()
                past_soil_label = QtWidgets.QLabel("Past Rate:")
                past_soil_value_label = QtWidgets.QLabel("---")
                past_soil_layout.addWidget(past_soil_label)
                past_soil_layout.addWidget(past_soil_value_label)

        # create button for graph
                graph_button = QtWidgets.QPushButton("Graph")
                graph_button.clicked.connect(self.show_graph_page)

        # create back button
                back_button = QtWidgets.QPushButton("Back")
                back_button.setGeometry(20, 20, 100, 30)
                back_button.clicked.connect(self.show_main_window)

        # add widgets and layouts to weather layout
                soil_layout.addWidget(soil_label)
                soil_layout.addLayout(current_soil_layout)
                soil_layout.addLayout(past_soil_layout)
                soil_layout.addWidget(graph_button)
                soil_layout.addWidget(back_button)

        # set weather widget as central widget
                self.setCentralWidget(self.soil_widget)
        
    def show_graph_page(self):
        # create weather widget
                self.graph_widget = QtWidgets.QWidget()

        # create layout for weather widget
                graph_layout = QtWidgets.QVBoxLayout(self.graph_widget)

        # create label for Weather
                graph_label = QtWidgets.QLabel(
                    "Graph", alignment=QtCore.Qt.AlignCenter)
                graph_label.setFont(QtGui.QFont("Arial", 20, QtGui.QFont.Bold))

        # create back button
                back_button = QtWidgets.QPushButton("Back")
                back_button.setGeometry(20, 20, 100, 30)
                back_button.clicked.connect(self.show_main_window)

        # add widgets and layouts to weather layout
                graph_layout.addWidget(graph_label)
                
                
                graph_layout.addWidget(back_button)

        # set weather widget as central widget
                self.setCentralWidget(self.graph_widget)
        
    def show_user_guide(self):
    # create user guide widget
        self.user_guide_widget = QtWidgets.QWidget()

    # create layout for user guide widget
        user_guide_layout = QtWidgets.QVBoxLayout(self.user_guide_widget)

    # create label for user guide
        user_guide_label = QtWidgets.QLabel(
        "User Guide", alignment=QtCore.Qt.AlignCenter)
        user_guide_label.setFont(QtGui.QFont("Arial", 20, QtGui.QFont.Bold))

    # create label for user guide content
        user_guide_content = QtWidgets.QLabel(
        "This is the user guide. It will provide instructions on how to use the Agrifarm application.",
        alignment=QtCore.Qt.AlignCenter)

    # create back button
        back_button = QtWidgets.QPushButton("Back")
        back_button.setGeometry(20, 20, 100, 30)
        back_button.clicked.connect(self.show_main_window)

    # add widgets and layouts to user guide layout
        user_guide_layout.addWidget(user_guide_label)
        user_guide_layout.addWidget(user_guide_content)
        user_guide_layout.addWidget(back_button)

    # set user guide widget as central widget
        self.setCentralWidget(self.user_guide_widget)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
