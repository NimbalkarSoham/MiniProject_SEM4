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
        self.main_widget.setStyleSheet("background-color: #cccead;")
        self.setCentralWidget(self.main_widget)

        # create the Agrifarm label and add it to the main widget
        agrifarm_label = QtWidgets.QLabel('AGRIFARM', self.main_widget)
        agrifarm_label.setFont(QtGui.QFont("Georgia", 70, QtGui.QFont.Bold))
        agrifarm_label.setGeometry(0, 100, 900, 70)
        agrifarm_label.setAlignment(QtCore.Qt.AlignCenter)

        # create the location checkbox and add it to the main widget
        location_combobox = QtWidgets.QComboBox(self.main_widget)
        location_combobox.setGeometry(10, 260, 100, 30)
        location_combobox.setFont(QtGui.QFont("Monaco", 10, QtGui.QFont.Bold))
        location_combobox.setStyleSheet("""QComboBox { background-color: white; color: black ; border:1px solid gray; padding: 1px 18px 1px 3px;min-width: 6em;border-radius: 4px;} QComboBox::drop-down {subcontrol-origin: padding;subcontrol-position: top right;width: 15px;border-left-width: 1px;border-left-color: gray;border-left-style: solid;border-top-right-radius: 4px;border-bottom-right-radius: 4px; }QComboBox::down-arrow {image: url(up_arrow.png);width: 12px;height: 12px;}QComboBox::down-arrow:on {image: url(down_arrow.png);}""")
        location_combobox.addItems(["Location 1", "Location 2", "Location 3"])

        # create the suggestion box and add it to the main widget
        suggestion_box = QtWidgets.QGroupBox('Suggestion', self.main_widget)
        suggestion_box.setGeometry(150, 450, 400, 150)
        suggestion_layout = QtWidgets.QVBoxLayout(suggestion_box)
        suggestion_text = QtWidgets.QLabel('Enter suggestion here...', suggestion_box)
        suggestion_text.setWordWrap(True)
        suggestion_text.setAlignment(QtCore.Qt.AlignTop)
        suggestion_layout.addWidget(suggestion_text)

        # create the update box and add it to the main widget
        update_box = QtWidgets.QGroupBox('Update', self.main_widget)
        update_box.setGeometry(150, 250, 400, 150)
        update_layout = QtWidgets.QVBoxLayout(update_box)
        update_text = QtWidgets.QLabel('Enter update here...', update_box)
        update_text.setWordWrap(True)
        update_text.setAlignment(QtCore.Qt.AlignTop)
        update_layout.addWidget(update_text)

        # create the suggestion and update buttons and add them to the main widget
        suggestion_button = QtWidgets.QPushButton('Submit Suggestion', self.main_widget)
        suggestion_button.setGeometry(150, 610, 200, 30)
        suggestion_button.setFont(QtGui.QFont("Monaco", 10, QtGui.QFont.Bold))
        suggestion_button.setStyleSheet("QPushButton { border-radius: 10px;background-color: #72752f}")
        update_button = QtWidgets.QPushButton('Submit Update', self.main_widget)
        update_button.setFont(QtGui.QFont("Monaco", 10, QtGui.QFont.Bold))
        update_button.setGeometry(150, 410, 200, 30)
        update_button.setStyleSheet("QPushButton { border-radius: 10px;background-color: #72752f}")

        # create the weather and price buttons and add them to the main widget
        weather_button = QtWidgets.QPushButton('Weather', self.main_widget)
        weather_button.setFont(QtGui.QFont("Georgia", 10, QtGui.QFont.Bold))
        weather_button.setGeometry(600, 270, 200, 50)
        weather_button.setStyleSheet("QPushButton { border-radius: 10px;background-color: #72752f}")
        price_button = QtWidgets.QPushButton('Price', self.main_widget)
        price_button.setFont(QtGui.QFont("Georgia", 10, QtGui.QFont.Bold))
        price_button.setGeometry(600, 340, 200, 50)
        price_button.setStyleSheet("QPushButton { border-radius: 10px;background-color: #72752f}")
        soil_button = QtWidgets.QPushButton('Soil', self.main_widget)
        soil_button.setFont(QtGui.QFont("Georgia", 10, QtGui.QFont.Bold))
        soil_button.setGeometry(600, 410, 200, 50)
        soil_button.setStyleSheet("QPushButton { border-radius: 10px;background-color: #72752f}")

        # create the signals for the weather and price buttons
        weather_button.clicked.connect(self.show_weather_page)
        price_button.clicked.connect(self.show_price_page)
        soil_button.clicked.connect(self.show_soil_page)

        # create the user guide button and add it to the main widget
        user_guide_button = QtWidgets.QPushButton('User Guide', self.main_widget)
        user_guide_button.setFont(QtGui.QFont("Monaco", 8, QtGui.QFont.Bold))
        user_guide_button.setGeometry(650, 610, 80, 30)
        user_guide_button.setStyleSheet("QPushButton { border-radius: 10px;background-color: #72752f}")
        user_guide_button.clicked.connect(self.show_user_guide)

    def show_weather_page(self):

        self.weather_widget = QtWidgets.QWidget()
        # create layout for weather widget
        weather_layout = QtWidgets.QVBoxLayout(self.weather_widget)

# create label for Weather
        weather_label = QtWidgets.QLabel("Weather", alignment=QtCore.Qt.AlignCenter)
        weather_label.setFont(QtGui.QFont("Georgia", 70, QtGui.QFont.Bold))

        # create GroupBox for current weather
        current_weather_groupbox = QtWidgets.QGroupBox("Current Weather:")
        current_weather_groupbox.setStyleSheet("QGroupBox { font-size: 20px; font-weight: bold; }")
        current_weather_layout = QtWidgets.QHBoxLayout(current_weather_groupbox)
        current_weather_value_label = QtWidgets.QLabel("Sunny")
        current_weather_layout.addWidget(current_weather_value_label)
        current_weather_layout.addStretch()

# create GroupBox for past weather
        past_weather_groupbox = QtWidgets.QGroupBox("Past Weather Condition:")
        past_weather_groupbox.setStyleSheet("QGroupBox { font-size: 20px; font-weight: bold; }")
        past_weather_layout = QtWidgets.QHBoxLayout(past_weather_groupbox)
        past_weather_value_label = QtWidgets.QLabel("Cloudy")
        past_weather_layout.addWidget(past_weather_value_label)
        past_weather_layout.addStretch()

        # create graph button
        graph_button = QtWidgets.QPushButton("  Graph  ")
        graph_button.setStyleSheet("QPushButton { border-radius: 5px;background-color: #72752f; padding: 10px 20px; }")
        graph_button.setFont(QtGui.QFont("Monaco", 10, QtGui.QFont.Bold))
        graph_button.clicked.connect(self.show_graph_page)

        back_button = QtWidgets.QPushButton(' Back ', self)
        back_button.setStyleSheet("QPushButton { border-radius: 5px;background-color: #72752f ; padding: 10px 20px; }")
        back_button.setFont(QtGui.QFont("Monaco", 10, QtGui.QFont.Bold))
        back_button.clicked.connect(self.show_main_window)

# create button layout
        buttons_layout = QtWidgets.QHBoxLayout()
        buttons_layout.addWidget(back_button, alignment=QtCore.Qt.AlignLeft)
        buttons_layout.addWidget(graph_button, alignment=QtCore.Qt.AlignRight)
        buttons_layout.setContentsMargins(10, 10, 10, 20)

# create weather widget layout
        weather_layout.addWidget(weather_label, alignment=QtCore.Qt.AlignCenter)
        weather_layout.addWidget(current_weather_groupbox)
        weather_layout.addWidget(past_weather_groupbox)
        weather_layout.addLayout(buttons_layout)

# set weather widget as central widget
        self.setCentralWidget(self.weather_widget)

# set size of main window
        self.setFixedSize(900, 700)

# set stylesheet for main window
        self.setStyleSheet("background-color: #cccead;")

       
    def show_price_page(self):
        self.price_widget = QtWidgets.QWidget()
        # create layout for weather widget
        price_layout = QtWidgets.QVBoxLayout(self.price_widget)

# create label for Weather
        price_label = QtWidgets.QLabel("Price", alignment=QtCore.Qt.AlignCenter)
        price_label.setFont(QtGui.QFont("Georgia", 70, QtGui.QFont.Bold))

        # create GroupBox for current weather
        current_price_groupbox = QtWidgets.QGroupBox("Current price:")
        current_price_groupbox.setStyleSheet("QGroupBox { font-size: 20px; font-weight: bold; }")
        current_price_layout = QtWidgets.QHBoxLayout(current_price_groupbox)
        current_price_value_label = QtWidgets.QLabel("Sunny")
        current_price_layout.addWidget(current_price_value_label)
        current_price_layout.addStretch()

# create GroupBox for past weather
        past_price_groupbox = QtWidgets.QGroupBox("Past price Condition:")
        past_price_groupbox.setStyleSheet("QGroupBox { font-size: 20px; font-weight: bold; }")
        past_price_layout = QtWidgets.QHBoxLayout(past_price_groupbox)
        past_price_value_label = QtWidgets.QLabel("Cloudy")
        past_price_layout.addWidget(past_price_value_label)
        past_price_layout.addStretch()

        # create graph button
        graph_button = QtWidgets.QPushButton("  Graph  ")
        graph_button.setStyleSheet("QPushButton { border-radius: 5px;background-color: #72752f; padding: 10px 20px; }")
        graph_button.setFont(QtGui.QFont("Monaco", 10, QtGui.QFont.Bold))
        graph_button.clicked.connect(self.show_graph_page)

        back_button = QtWidgets.QPushButton(' Back ', self)
        back_button.setStyleSheet("QPushButton { border-radius: 5px;background-color: #72752f ; padding: 10px 20px; }")
        back_button.setFont(QtGui.QFont("Monaco", 10, QtGui.QFont.Bold))
        back_button.clicked.connect(self.show_main_window)

# create button layout
        buttons_layout = QtWidgets.QHBoxLayout()
        buttons_layout.addWidget(back_button, alignment=QtCore.Qt.AlignLeft)
        buttons_layout.addWidget(graph_button, alignment=QtCore.Qt.AlignRight)
        buttons_layout.setContentsMargins(10, 10, 10, 20)

# create weather widget layout
        price_layout.addWidget(price_label, alignment=QtCore.Qt.AlignCenter)
        price_layout.addWidget(current_price_groupbox)
        price_layout.addWidget(past_price_groupbox)
        price_layout.addLayout(buttons_layout)

# set weather widget as central widget
        self.setCentralWidget(self.price_widget)

# set size of main window
        self.setFixedSize(900, 700)

# set stylesheet for main window
        self.setStyleSheet("background-color: #cccead;")
    def show_soil_page(self):
        self.weather_widget = QtWidgets.QWidget()
        # create layout for weather widget
        weather_layout = QtWidgets.QVBoxLayout(self.weather_widget)

# create label for Weather
        weather_label = QtWidgets.QLabel("Weather", alignment=QtCore.Qt.AlignCenter)
        weather_label.setFont(QtGui.QFont("Georgia", 70, QtGui.QFont.Bold))

        # create GroupBox for current weather
        current_weather_groupbox = QtWidgets.QGroupBox("Current Weather:")
        current_weather_groupbox.setStyleSheet("QGroupBox { font-size: 20px; font-weight: bold; }")
        current_weather_layout = QtWidgets.QHBoxLayout(current_weather_groupbox)
        current_weather_value_label = QtWidgets.QLabel("Sunny")
        current_weather_layout.addWidget(current_weather_value_label)
        current_weather_layout.addStretch()

# create GroupBox for past weather
        past_weather_groupbox = QtWidgets.QGroupBox("Past Weather Condition:")
        past_weather_groupbox.setStyleSheet("QGroupBox { font-size: 20px; font-weight: bold; }")
        past_weather_layout = QtWidgets.QHBoxLayout(past_weather_groupbox)
        past_weather_value_label = QtWidgets.QLabel("Cloudy")
        past_weather_layout.addWidget(past_weather_value_label)
        past_weather_layout.addStretch()

        # create graph button
        graph_button = QtWidgets.QPushButton("  Graph  ")
        graph_button.setStyleSheet("QPushButton { border-radius: 5px;background-color: #72752f; padding: 10px 20px; }")
        graph_button.setFont(QtGui.QFont("Monaco", 10, QtGui.QFont.Bold))
        graph_button.clicked.connect(self.show_graph_page)

        back_button = QtWidgets.QPushButton(' Back ', self)
        back_button.setStyleSheet("QPushButton { border-radius: 5px;background-color: #72752f ; padding: 10px 20px; }")
        back_button.setFont(QtGui.QFont("Monaco", 10, QtGui.QFont.Bold))
        back_button.clicked.connect(self.show_main_window)

# create button layout
        buttons_layout = QtWidgets.QHBoxLayout()
        buttons_layout.addWidget(back_button, alignment=QtCore.Qt.AlignLeft)
        buttons_layout.addWidget(graph_button, alignment=QtCore.Qt.AlignRight)
        buttons_layout.setContentsMargins(10, 10, 10, 20)

# create weather widget layout
        weather_layout.addWidget(weather_label, alignment=QtCore.Qt.AlignCenter)
        weather_layout.addWidget(current_weather_groupbox)
        weather_layout.addWidget(past_weather_groupbox)
        weather_layout.addLayout(buttons_layout)

# set weather widget as central widget
        self.setCentralWidget(self.weather_widget)

# set size of main window
        self.setFixedSize(900, 700)

# set stylesheet for main window
        self.setStyleSheet("background-color: #cccead;")
        
    def show_graph_page(self):
        self.graph_widget = QtWidgets.QWidget()
        # create layout for weather widget
        graph_layout = QtWidgets.QVBoxLayout(self.graph_widget)

# create label for Weather
        graph_label = QtWidgets.QLabel("Graph", alignment=QtCore.Qt.AlignCenter)
        graph_label.setFont(QtGui.QFont("Georgia", 70, QtGui.QFont.Bold))

        # create GroupBox for current weather
        Graph_groupbox = QtWidgets.QGroupBox("Graph:")
        Graph_groupbox.setStyleSheet("QGroupBox { font-size: 20px; font-weight: bold; }")
        Graph_layout = QtWidgets.QHBoxLayout(Graph_groupbox)
        Graph_value_label = QtWidgets.QLabel(" ")
        Graph_layout.addWidget(Graph_value_label)
        Graph_layout.addStretch()



        back_button = QtWidgets.QPushButton(' Back ', self)
        back_button.setStyleSheet("QPushButton { border-radius: 5px;background-color: #72752f ; padding: 10px 20px; }")
        back_button.setFont(QtGui.QFont("Monaco", 10, QtGui.QFont.Bold))
        back_button.clicked.connect(self.show_main_window)

# create button layout
        buttons_layout = QtWidgets.QHBoxLayout()
        buttons_layout.addWidget(back_button, alignment=QtCore.Qt.AlignLeft)

        buttons_layout.setContentsMargins(10, 10, 10, 20)

# create weather widget layout
        graph_layout.addWidget(graph_label, alignment=QtCore.Qt.AlignCenter)
        graph_layout.addWidget(Graph_groupbox)
        graph_layout.addLayout(buttons_layout)

# set weather widget as central widget
        self.setCentralWidget(self.graph_widget)

# set size of main window
        self.setFixedSize(900, 700)

# set stylesheet for main window
        self.setStyleSheet("background-color: #cccead;")
        
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

        back_button = QtWidgets.QPushButton(' Back ', self)
        back_button.setStyleSheet("QPushButton { border-radius: 5px;background-color: #72752f ; padding: 10px 20px; }")
        back_button.setFont(QtGui.QFont("Monaco", 10, QtGui.QFont.Bold))
        back_button.clicked.connect(self.show_main_window)

# create button layout
        buttons_layout = QtWidgets.QHBoxLayout()
        buttons_layout.addWidget(back_button, alignment=QtCore.Qt.AlignLeft)

        buttons_layout.setContentsMargins(10, 10, 10, 20)

    # add widgets and layouts to user guide layout
        user_guide_layout.addWidget(user_guide_label)
        user_guide_layout.addWidget(user_guide_content)
        user_guide_layout.addLayout(buttons_layout)

    # set user guide widget as central widget
        self.setCentralWidget(self.user_guide_widget)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
