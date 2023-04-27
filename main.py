from PySide6 import QtWidgets, QtGui, QtCore
from googletrans import Translator
from weather_satara import df_satara
from weather_sangli import df_sangli
from weather_solapur import df_solapur
from price_satara import Satara_price_df
from price_sangli import Sangli_price_df
from price_solapur import Solapur_price_df
from satara_cropinfo import text_satara , price_satara , time_satara
from sangali_cropinfo import text_sangli , price_sangli , time_sangli
from solapur_cropinfo import text_solapur , price_solapur , time_solapur
import datetime

import sys


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AGRIFARM")
        
        
        # Set the main window size
        self.setFixedSize(900, 700)
        
        
        self.show_main_window()

    def show_main_window(self):
        def update_SelectedLocation():
            # Make sure the variable is declared as global so it can be updated
            global selected_location
            selected_location = location_combobox.currentText()
            print(selected_location)

            # create main widget
        self.setGeometry(100, 100, 900, 700)
        self.setWindowTitle('AGRIFARM')

        # create the main widget and set it as the central widget
        self.main_widget = QtWidgets.QWidget(self)
        self.main_widget.setStyleSheet("background-color: #00FFFFFF;")
        self.setCentralWidget(self.main_widget)

        # set background image of main widget
        background_label = QtWidgets.QLabel(self.main_widget)
        background_pixmap = QtGui.QPixmap(
            'C:\\Users\\jadha\\Documents\\AGRIFARMM\\images\\fa.jpeg')
        # background_pixmap = background_pixmap.scaled(self.main_widget.size(), QtCore.Qt.IgnoreAspectRatio)
        background_label.setPixmap(background_pixmap)
        self.resize(background_pixmap.width(), background_pixmap.height())

        # create the Agrifarm label and add it to the main widget
        agrifarm_label = QtWidgets.QLabel('AGRIFARM', self.main_widget)
        agrifarm_label.setFont(QtGui.QFont("Georgia", 70, QtGui.QFont.Bold))
        agrifarm_label.setGeometry(0, 100, 950, 150)
        agrifarm_label.setAlignment(QtCore.Qt.AlignCenter)

        # logo_label = QtWidgets.QLabel(self.main_widget)
        # logo_pixmap = QtGui.QPixmap('C:\\Users\\jadha\\Documents\\AGRIFARMM\\images\\Agrifarm_logo.png')
        # logo_label.setPixmap(logo_pixmap)
        # logo_label.setGeometry(10, 10, 200, 50)

        # create the location checkbox and add it to the main widget
        location_combobox = QtWidgets.QComboBox(self.main_widget)
        location_combobox.setGeometry(10, 260, 100, 30)
        location_combobox.setFont(QtGui.QFont("Monaco", 10, QtGui.QFont.Bold))
        location_combobox.setStyleSheet("""QComboBox { background-color: white; color: black ; border:1px solid gray; padding: 1px 18px 1px 3px;min-width: 6em;border-radius: 4px;} QComboBox::drop-down {subcontrol-origin: padding;subcontrol-position: top right;width: 15px;border-left-width: 1px;border-left-color: gray;border-left-style: solid;border-top-right-radius: 4px;border-bottom-right-radius: 4px; }QComboBox::down-arrow {image: url(up_arrow.png);width: 12px;height: 12px;}QComboBox::down-arrow:on {image: url(down_arrow.png);}""")
        location_combobox.addItems(["Location","Satara", "Sangli", "Solapur"])
        location_combobox.currentTextChanged.connect(update_SelectedLocation)

        # create the suggestion box and add it to the main widget
        suggestion_box = QtWidgets.QGroupBox('Suggestion', self.main_widget)
        suggestion_box.setStyleSheet(
            "background-color:  #f2f2f2; border-radius: 10px;")
        suggestion_box.setGeometry(150, 450, 400, 150)
        suggestion_layout = QtWidgets.QVBoxLayout(suggestion_box)
        suggestion_text = QtWidgets.QLabel(
            'Enter suggestion here...', suggestion_box)
        suggestion_text.setWordWrap(True)
        suggestion_text.setAlignment(QtCore.Qt.AlignTop)
        suggestion_layout.addWidget(suggestion_text)

        # create the update box and add it to the main widget
        update_box = QtWidgets.QGroupBox('Update', self.main_widget)
        update_box.setStyleSheet(
            "background-color:  #f2f2f2; border-radius: 10px;")
        update_box.setGeometry(150, 250, 400, 150)
        update_layout = QtWidgets.QVBoxLayout(update_box)
        update_text = QtWidgets.QLabel('Enter update here...', update_box)
        update_text.setWordWrap(True)
        update_text.setAlignment(QtCore.Qt.AlignTop)
        update_layout.addWidget(update_text)

        # create the suggestion and update buttons and add them to the main widget
        suggestion_button = QtWidgets.QPushButton(
            'Submit Suggestion', self.main_widget)
        suggestion_button.setGeometry(150, 610, 200, 30)
        suggestion_button.setFont(QtGui.QFont("Monaco", 10, QtGui.QFont.Bold))
        suggestion_button.setStyleSheet(
            "QPushButton { border-radius: 10px;background-color: #72752f}")
        update_button = QtWidgets.QPushButton(
            'Submit Update', self.main_widget)
        update_button.setFont(QtGui.QFont("Monaco", 10, QtGui.QFont.Bold))
        update_button.setGeometry(150, 410, 200, 30)
        update_button.setStyleSheet(
            "QPushButton { border-radius: 10px;background-color: #72752f}")

        # create the weather and soil buttons and add them to the main widget
        weather_button = QtWidgets.QPushButton('Weather', self.main_widget)
        weather_button.setFont(QtGui.QFont("Georgia", 10, QtGui.QFont.Bold))
        weather_button.setGeometry(600, 270, 200, 50)
        weather_button.setStyleSheet(
            "QPushButton { border-radius: 10px;background-color: #72752f}")
        price_button = QtWidgets.QPushButton('Price', self.main_widget)
        price_button.setFont(QtGui.QFont("Georgia", 10, QtGui.QFont.Bold))
        price_button.setGeometry(600, 340, 200, 50)
        price_button.setStyleSheet(
            "QPushButton { border-radius: 10px;background-color: #72752f}")
        soil_button = QtWidgets.QPushButton('Time', self.main_widget)
        soil_button.setFont(QtGui.QFont("Georgia", 10, QtGui.QFont.Bold))
        soil_button.setGeometry(600, 410, 200, 50)
        soil_button.setStyleSheet(
            "QPushButton { border-radius: 10px;background-color: #72752f}")

        # create the signals for the weather and price buttons
        weather_button.clicked.connect(self.show_weather_page)
        # weather_button.clicked.connect(update_WeatherText)
        price_button.clicked.connect(self.show_price_page)
        soil_button.clicked.connect(self.show_soil_page)

        # create the user guide button and add it to the main widget
        user_guide_button = QtWidgets.QPushButton(
            'User Guide', self.main_widget)
        user_guide_button.setFont(QtGui.QFont("Monaco", 8, QtGui.QFont.Bold))
        user_guide_button.setGeometry(650, 610, 95, 30)
        user_guide_button.setStyleSheet(
            "QPushButton { border-radius: 10px;background-color: #72752f}")
        user_guide_button.clicked.connect(self.show_user_guide)

        # create the translate combo box and add it to the main widget
        self.translate_combobox = QtWidgets.QComboBox(self.main_widget)
        self.translate_combobox.setGeometry(740, 20, 150, 30)
        self.translate_combobox.setFont(
            QtGui.QFont("Monaco", 10, QtGui.QFont.Bold))
        self.translate_combobox.setStyleSheet("""QComboBox { background-color: white; color: black ; border:1px solid gray; padding: 1px 18px 1px 3px;min-width: 6em;border-radius: 4px;} QComboBox::drop-down {subcontrol-origin: padding;subcontrol-position: top right;width: 15px;border-left-width: 1px;border-left-color: gray;border-left-style: solid;border-top-right-radius: 4px;border-bottom-right-radius: 4px; }QComboBox::down-arrow {image: url(up_arrow.png);width: 12px;height: 12px;}QComboBox::down-arrow:on {image: url(\\images\\down_arrow.png);}""")
        self.translate_combobox.addItems(
            ["Select Language", "Marathi", "Hindi", "Reset"])

        # create an instance of the translator
        self.translator = Translator()

        # connect the "activated" signal of the translate_combobox to a slot function
        self.translate_combobox.activated.connect(self.translate_text)

    def translate_text(self, index):

        # check if the selected language is Marathi
        if self.translate_combobox.itemText(index) == "Marathi":
            # get the English text of each label and button and translate it to Marathi
            for label in self.main_widget.findChildren(QtWidgets.QLabel):
                if not hasattr(label, "original_text"):
                    label.setProperty("original_text", label.text())
                text = label.property("original_text")
                if text:
                    translated_text = self.translator.translate(
                        text, src='en', dest='mr').text
                    label.setText(translated_text)

            for button in self.main_widget.findChildren(QtWidgets.QPushButton):
                if not hasattr(button, "original_text"):
                    button.setProperty("original_text", button.text())
                text = button.property("original_text")
                if text:
                    translated_text = self.translator.translate(
                        text, src='en', dest='mr').text
                    button.setText(translated_text)

        elif self.translate_combobox.itemText(index) == "Reset":
            # reset to English
            for label in self.main_widget.findChildren(QtWidgets.QLabel):
                label.setText(label.property("original_text"))

            for button in self.main_widget.findChildren(QtWidgets.QPushButton):
                button.setText(button.property("original_text"))

        elif self.translate_combobox.itemText(index) == "Hindi":
            # translate to Hindi
            for label in self.main_widget.findChildren(QtWidgets.QLabel):
                text = label.text()
                if text:
                    translated_text = self.translator.translate(
                        text, src='en', dest='hi').text
                    label.setText(translated_text)

            for button in self.main_widget.findChildren(QtWidgets.QPushButton):
                text = button.text()
                if text:
                    translated_text = self.translator.translate(
                        text, src='en', dest='hi').text
                    button.setText(translated_text)

        else:
            # selected "Select Language"
            pass

    def show_weather_page(self):
        self.weather_widget = QtWidgets.QWidget(self)
        self.setFixedSize(900, 700)

        def update_CWeatherText():
            global selected_df
            if selected_location == 'Satara':
                selected_df = df_satara
            elif selected_location == 'Sangli':
                selected_df = df_sangli
            else:
                selected_df = df_solapur
            now = datetime.datetime.now()
#!!!           !!!!!!!!!!!!! change X_pred to selected_df
            filtered_df = selected_df[selected_df.index >= now]
            #global future_weather_text
            # future_weather_text = selected_location+'\nMin temperature: '+str(filtered_df.head(10)['T2M'].min())+'\nMax Temperature: '+str(filtered_df.head(10)['T2M'].max())+'\nMax Precipitation(in mm): '+str(
            #    filtered_df.head(10)['Precipitation'].max())+'\nAverage Humidity: '+str(filtered_df.head(10)['QV2M'].mean())+'\nAverage Surface Pressure: '+str(filtered_df.head(10)['PS'].mean())
            global current_weather_text
            current_weather_text = selected_location+'\nMin temperature: '+str(filtered_df.head(1)['T2M_MIN'].min())+'\nMax Temperature: '+str(filtered_df.head(1)['T2M_MAX'].max())+'\nMax Precipitation(in mm): '+str(
                int(filtered_df.head(1)['Precipitation'].max()))+'\nAverage Humidity: '+str(int(filtered_df.head(1)['QV2M'].mean()))+'\nAverage Surface Pressure: '+str(int(filtered_df.head(1)['PS'].mean()))
            return current_weather_text

        def update_FWeatherText():
            global selected_df
            if selected_location == 'Satara':
                selected_df = df_satara
            elif selected_location == 'Sangli':
                selected_df = df_sangli
            else:
                selected_df = df_solapur
            now = datetime.datetime.now()
#!!!        !!!!!!!!!!!!! change X_pred to selected_df
            filtered_df = selected_df[selected_df.index >= now]
            global future_weather_text
            future_weather_text = selected_location+'\nMin temperature: '+str(filtered_df.head(10)['T2M'].min())+'\nMax Temperature: '+str(filtered_df.head(10)['T2M'].max())+'\nMax Precipitation(in mm): '+str(
                int(filtered_df.head(10)['Precipitation'].max()))+'\nAverage Humidity: '+str(int(filtered_df.head(10)['QV2M'].mean()))+'\nAverage Surface Pressure: '+str(int(filtered_df.head(10)['PS'].mean()))
            #global current_weather_text
            # current_weather_text = selected_location+'\nMin temperature: '+str(filtered_df.head(1)['T2M_MIN'].min())+'\nMax Temperature: '+str(filtered_df.head(1)['T2M_MAX'].max())+'\nMax Precipitation(in mm): '+str(
            #    filtered_df.head(1)['Precipitation'].max())+'\nAverage Humidity: '+str(filtered_df.head(1)['QV2M'].mean())+'\nAverage Surface Pressure: '+str(filtered_df.head(1)['PS'].mean())
            return future_weather_text
            
            
            

    # create label for Weather
        weather_label = QtWidgets.QLabel(
            "WEATHER", alignment=QtCore.Qt.AlignCenter)
        weather_label.setFont(QtGui.QFont("Georgia", 70, QtGui.QFont.Bold))

    # create GroupBox for current weather
        current_weather_groupbox = QtWidgets.QGroupBox(
            "          Current Weather:")
        current_weather_groupbox.setStyleSheet(
            "QGroupBox { font-size: 20px; font-weight: bold; }")
        current_weather_groupbox.setStyleSheet(
            "background-color:  #f2f2f2; border-radius: 10px;padding:5px")
        current_weather_layout = QtWidgets.QHBoxLayout(
            current_weather_groupbox)
        current_weather_value_label = QtWidgets.QLabel(update_CWeatherText())
        current_weather_layout.addWidget(current_weather_value_label)
        current_weather_layout.addStretch()
        current_weather_layout.addSpacerItem(QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))

    # create GroupBox for past weather
        past_weather_groupbox = QtWidgets.QGroupBox(
            "          Future Weather Condition:")
        past_weather_groupbox.setStyleSheet(
            "QGroupBox { font-size: 20px; font-weight: bold; }")
        past_weather_groupbox.setStyleSheet(
            "background-color:  #f2f2f2; border-radius: 10px;padding:5px")
        past_weather_layout = QtWidgets.QHBoxLayout(past_weather_groupbox)
        past_weather_value_label = QtWidgets.QLabel(update_FWeatherText())
        past_weather_layout.addWidget(past_weather_value_label)
        past_weather_layout.addStretch()
        past_weather_layout.addSpacerItem(QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))

        current_weather_groupbox.setMaximumWidth(550)
        past_weather_groupbox.setMaximumWidth(550)
    # create graph button
        graph_button = QtWidgets.QPushButton("Tips")
        graph_button.setStyleSheet(
            "QPushButton { border-radius: 5px;background-color: #72752f; padding: 10px 20px; }")
        graph_button.setFont(QtGui.QFont("Monaco", 10, QtGui.QFont.Bold))
        graph_button.clicked.connect(self.show_graph_page)

        back_button = QtWidgets.QPushButton('Back', self)
        back_button.setStyleSheet(
            "QPushButton { border-radius: 5px;background-color: #72752f ; padding: 10px 20px; }")
        back_button.setFont(QtGui.QFont("Monaco", 10, QtGui.QFont.Bold))
        back_button.clicked.connect(self.show_main_window)

    # create button layout
        buttons_layout = QtWidgets.QHBoxLayout()
        buttons_layout.addWidget(back_button, alignment=QtCore.Qt.AlignLeft)
        buttons_layout.addWidget(graph_button, alignment=QtCore.Qt.AlignRight)
        buttons_layout.setContentsMargins(10, 10, 10, 20)

    # create weather widget layout
        weather_layout = QtWidgets.QVBoxLayout(self.weather_widget)
        weather_layout.addWidget(
            weather_label, alignment=QtCore.Qt.AlignCenter)
        weather_layout.addWidget(current_weather_groupbox)
        weather_layout.addWidget(past_weather_groupbox)
        weather_layout.addLayout(buttons_layout)

    # create background label
        background_label = QtWidgets.QLabel(self)
        background_pixmap = QtGui.QPixmap(
            'C:\\Users\\jadha\\Documents\\AGRIFARMM\\images\\weather.jpg')
        background_pixmap = background_pixmap.scaled(
            self.size(), QtCore.Qt.IgnoreAspectRatio)
        background_label.setPixmap(background_pixmap)
        background_label.setGeometry(0, 0, self.width(), self.height())

    # set background label as the parent of weather widget
        background_layout = QtWidgets.QVBoxLayout(background_label)
        background_layout.addWidget(self.weather_widget)

        self.setCentralWidget(background_label)

        # create the translate combo box and add it to the main widget
        self.translate_combobox = QtWidgets.QComboBox(self.weather_widget)
        self.translate_combobox.setGeometry(730, 25, 150, 35)
        self.translate_combobox.setFont(
            QtGui.QFont("Monaco", 10, QtGui.QFont.Bold))
        self.translate_combobox.setStyleSheet("""QComboBox { background-color: white; color: black ; border:1px solid gray; padding: 1px 18px 1px 3px;min-width: 6em;border-radius: 4px;} QComboBox::drop-down {subcontrol-origin: padding;subcontrol-position: top right;width: 15px;border-left-width: 1px;border-left-color: gray;border-left-style: solid;border-top-right-radius: 4px;border-bottom-right-radius: 4px; }QComboBox::down-arrow {image: url(up_arrow.png);width: 12px;height: 12px;}QComboBox::down-arrow:on {image: url(down_arrow.png);}""")
        self.translate_combobox.addItems(
            ["Select Language", "Marathi", "Hindi", "Reset"])

        # create an instance of the translator
        self.translator = Translator()

        # connect the "activated" signal of the translate_combobox to a slot function
        self.translate_combobox.activated.connect(self.translatee_text)

    def translatee_text(self, index):

        # check if the selected language is Marathi
        if self.translate_combobox.itemText(index) == "Marathi":
            # get the English text of each label and button and translate it to Marathi
            for label in self.weather_widget.findChildren(QtWidgets.QLabel):
                if not hasattr(label, "original_text"):
                    label.setProperty("original_text", label.text())
                text = label.property("original_text")
                if text:
                    translated_text = self.translator.translate(
                        text, src='en', dest='mr').text
                    label.setText(translated_text)

            for button in self.weather_widget.findChildren(QtWidgets.QPushButton):
                if not hasattr(button, "original_text"):
                    button.setProperty("original_text", button.text())
                text = button.property("original_text")
                if text:
                    translated_text = self.translator.translate(
                        text, src='en', dest='mr').text
                    button.setText(translated_text)

        elif self.translate_combobox.itemText(index) == "Reset":
            # reset to English
            for label in self.weather_widget.findChildren(QtWidgets.QLabel):
                label.setText(label.property("original_text"))

            for button in self.weather_widget.findChildren(QtWidgets.QPushButton):
                button.setText(button.property("original_text"))

        elif self.translate_combobox.itemText(index) == "Hindi":
            # translate to Hindi
            for label in self.weather_widget.findChildren(QtWidgets.QLabel):
                text = label.text()
                if text:
                    translated_text = self.translator.translate(
                        text, src='en', dest='hi').text
                    label.setText(translated_text)

            for button in self.weather_widget.findChildren(QtWidgets.QPushButton):
                text = button.text()
                if text:
                    translated_text = self.translator.translate(
                        text, src='en', dest='hi').text
                    button.setText(translated_text)

        else:
            # selected "Select Language"
            pass

    def show_price_page(self):
        self.price_widget = QtWidgets.QWidget(self)
        self.setFixedSize(900, 700)

        def update_CPriceText():
            global selected_df
            if selected_location == 'Satara':
                selected_df = Satara_price_df
            elif selected_location == 'Sangli':
                selected_df = Sangli_price_df
            else:
                selected_df = Solapur_price_df
            current_year = datetime.datetime.now().year
#!!!           !!!!!!!!!!!!! change X_pred to selected_df
            filtered_df = selected_df[selected_df.index >= current_year]
            global current_weather_text
            current_price_text = selected_location + \
                '\nWheat Prices(Per Quintal): ' + \
                str(int(filtered_df.head(1)['Rate']))+'\n'
            return current_price_text

        def update_FPriceText():
            global selected_df
            if selected_location == 'Satara':
                selected_df = Satara_price_df
            elif selected_location == 'Sangli':
                selected_df = Sangli_price_df
            else:
                selected_df = Solapur_price_df
            current_year = datetime.datetime.now().year
#!!!           !!!!!!!!!!!!! change X_pred to selected_df
            filtered_df = selected_df[selected_df.index > current_year]
            global future_price_text
            future_price_text = selected_location + \
                '\nWheat Prices(Per Quintal): ' + \
                str(int(filtered_df.head(1)['Rate']))+'\n'
            return future_price_text

    # create label for price
        price_label = QtWidgets.QLabel(
            "Price", alignment=QtCore.Qt.AlignCenter)
        price_label.setFont(QtGui.QFont("Georgia", 70, QtGui.QFont.Bold))

    # create GroupBox for current price
        current_price_groupbox = QtWidgets.QGroupBox(
            "          Price This Season:")
        current_price_groupbox.setStyleSheet(
            "QGroupBox { font-size: 20px; font-weight: bold; }")
        current_price_groupbox.setStyleSheet(
            "background-color:  #f2f2f2; border-radius: 10px;padding:5px")
        current_price_layout = QtWidgets.QHBoxLayout(current_price_groupbox)
        current_price_value_label = QtWidgets.QLabel(update_CPriceText())
        current_price_layout.addWidget(current_price_value_label)
        current_price_layout.addStretch()

    # create GroupBox for past price
        past_price_groupbox = QtWidgets.QGroupBox(
            "          Price next Season:")
        past_price_groupbox.setStyleSheet(
            "QGroupBox { font-size: 20px; font-weight: bold; }")
        past_price_groupbox.setStyleSheet(
            "background-color:  #f2f2f2; border-radius: 10px;padding:5px")
        past_price_layout = QtWidgets.QHBoxLayout(past_price_groupbox)
        past_price_value_label = QtWidgets.QLabel(update_FPriceText())
        past_price_layout.addWidget(past_price_value_label)
        past_price_layout.addStretch()

        current_price_groupbox.setMaximumWidth(550)
        past_price_groupbox.setMaximumWidth(550)

    # create graph button
        graph_button = QtWidgets.QPushButton("Tips")
        graph_button.setStyleSheet(
            "QPushButton { border-radius: 5px;background-color: #72752f; padding: 10px 20px; }")
        graph_button.setFont(QtGui.QFont("Monaco", 10, QtGui.QFont.Bold))
        graph_button.clicked.connect(self.showw_graph_page)

        back_button = QtWidgets.QPushButton('Back', self)
        back_button.setStyleSheet(
            "QPushButton { border-radius: 5px;background-color: #72752f ; padding: 10px 20px; }")
        back_button.setFont(QtGui.QFont("Monaco", 10, QtGui.QFont.Bold))
        back_button.clicked.connect(self.show_main_window)

    # create button layout
        buttons_layout = QtWidgets.QHBoxLayout()
        buttons_layout.addWidget(back_button, alignment=QtCore.Qt.AlignLeft)
        buttons_layout.addWidget(graph_button, alignment=QtCore.Qt.AlignRight)
        buttons_layout.setContentsMargins(10, 10, 10, 20)

    # create price widget layout
        price_layout = QtWidgets.QVBoxLayout(self.price_widget)
        price_layout.addWidget(price_label, alignment=QtCore.Qt.AlignCenter)
        price_layout.addWidget(current_price_groupbox)
        price_layout.addWidget(past_price_groupbox)
        price_layout.addLayout(buttons_layout)

    # create background label
        background_label = QtWidgets.QLabel(self)
        background_pixmap = QtGui.QPixmap(
            'C:\\Users\\jadha\\Documents\\AGRIFARMM\\images\\price.jpg')
        background_pixmap = background_pixmap.scaled(
            self.size(), QtCore.Qt.IgnoreAspectRatio)
        background_label.setPixmap(background_pixmap)
        background_label.setGeometry(0, 0, self.width(), self.height())

    # set background label as the parent of price widget
        background_layout = QtWidgets.QVBoxLayout(background_label)
        background_layout.addWidget(self.price_widget)

        self.setCentralWidget(background_label)

        # create the translate combo box and add it to the main widget
        self.translate_combobox = QtWidgets.QComboBox(self.price_widget)
        self.translate_combobox.setGeometry(730, 20, 150, 30)
        self.translate_combobox.setFont(
            QtGui.QFont("Monaco", 10, QtGui.QFont.Bold))
        self.translate_combobox.setStyleSheet("""QComboBox { background-color: white; color: black ; border:1px solid gray; padding: 1px 18px 1px 3px;min-width: 6em;border-radius: 4px;} QComboBox::drop-down {subcontrol-origin: padding;subcontrol-position: top right;width: 15px;border-left-width: 1px;border-left-color: gray;border-left-style: solid;border-top-right-radius: 4px;border-bottom-right-radius: 4px; }QComboBox::down-arrow {image: url(up_arrow.png);width: 12px;height: 12px;}QComboBox::down-arrow:on {image: url(down_arrow.png);}""")
        self.translate_combobox.addItems(
            ["Select Language", "Marathi", "Hindi", "Reset"])

        # create an instance of the translator
        self.translator = Translator()

        # connect the "activated" signal of the translate_combobox to a slot function
        self.translate_combobox.activated.connect(self.translate_text)

    def show_soil_page(self):
        self.soil_widget = QtWidgets.QWidget(self)
        self.setFixedSize(900, 700)

        def update_SuggestText():
            global selected_text
            if selected_location == 'Satara':
                selected_text = time_satara
                return selected_text
            elif selected_location == 'Sangli':
                selected_text = time_sangli
                return selected_text
            else:
                selected_text = time_solapur
                return selected_text

    # create label for soil
        soil_label = QtWidgets.QLabel("Time Suggestion", alignment=QtCore.Qt.AlignCenter)
        soil_label.setFont(QtGui.QFont("Georgia", 70, QtGui.QFont.Bold))

    # create GroupBox for current soil
        current_soil_groupbox = QtWidgets.QGroupBox("")
        current_soil_groupbox.setStyleSheet(
            "QGroupBox { font-size: 20px; font-weight: bold; }")
        current_soil_groupbox.setStyleSheet(
            "background-color:  #f2f2f2; border-radius: 10px;")
        current_soil_layout = QtWidgets.QHBoxLayout(current_soil_groupbox)
        current_soil_value_label = QtWidgets.QLabel(update_SuggestText())
        current_soil_layout.addWidget(current_soil_value_label)
        current_soil_layout.addStretch()

    # create GroupBox for past soil
        

        current_soil_groupbox.setMaximumWidth(850)
        

    # create graph button
        graph_button = QtWidgets.QPushButton("Tips")
        graph_button.setStyleSheet(
            "QPushButton { border-radius: 5px;background-color: #72752f; padding: 10px 20px; }")
        graph_button.setFont(QtGui.QFont("Monaco", 10, QtGui.QFont.Bold))
        graph_button.clicked.connect(self.showww_graph_page)

        back_button = QtWidgets.QPushButton('Back', self)
        back_button.setStyleSheet(
            "QPushButton { border-radius: 5px;background-color: #72752f ; padding: 10px 20px; }")
        back_button.setFont(QtGui.QFont("Monaco", 10, QtGui.QFont.Bold))
        back_button.clicked.connect(self.show_main_window)

    # create button layout
        buttons_layout = QtWidgets.QHBoxLayout()
        buttons_layout.addWidget(back_button, alignment=QtCore.Qt.AlignLeft)
        buttons_layout.addWidget(graph_button, alignment=QtCore.Qt.AlignRight)
        buttons_layout.setContentsMargins(10, 10, 10, 20)

    # create soil widget layout
        soil_layout = QtWidgets.QVBoxLayout(self.soil_widget)
        soil_layout.addWidget(soil_label, alignment=QtCore.Qt.AlignCenter)
        soil_layout.addWidget(current_soil_groupbox)
        
        soil_layout.addLayout(buttons_layout)

    # create background label
        background_label = QtWidgets.QLabel(self)
        background_pixmap = QtGui.QPixmap(
            'C:\\Users\\jadha\\Documents\\AGRIFARMM\\images\\soil.jpg')
        # background_pixmap = background_pixmap.scaled(self.size(), QtCore.Qt.IgnoreAspectRatio)
        background_label.setPixmap(background_pixmap)
        background_label.setGeometry(0, 0, self.width(), self.height())

    # set background label as the parent of soil widget
        background_layout = QtWidgets.QVBoxLayout(background_label)
        background_layout.addWidget(self.soil_widget)

        self.setCentralWidget(background_label)

        # create the translate combo box and add it to the main widget
        self.translate_combobox = QtWidgets.QComboBox(self.soil_widget)
        self.translate_combobox.setGeometry(720, 20, 150, 30)
        self.translate_combobox.setFont(
            QtGui.QFont("Monaco", 10, QtGui.QFont.Bold))
        self.translate_combobox.setStyleSheet("""QComboBox { background-color: white; color: black ; border:1px solid gray; padding: 1px 18px 1px 3px;min-width: 6em;border-radius: 4px;} QComboBox::drop-down {subcontrol-origin: padding;subcontrol-position: top right;width: 15px;border-left-width: 1px;border-left-color: gray;border-left-style: solid;border-top-right-radius: 4px;border-bottom-right-radius: 4px; }QComboBox::down-arrow {image: url(up_arrow.png);width: 12px;height: 12px;}QComboBox::down-arrow:on {image: url(down_arrow.png);}""")
        self.translate_combobox.addItems(
            ["Select Language", "Marathi", "Hindi", "Reset"])

        # create an instance of the translator
        self.translator = Translator()

        # connect the "activated" signal of the translate_combobox to a slot function
        self.translate_combobox.activated.connect(self.translate_text)

    def show_graph_page(self):
        self.graph_widget = QtWidgets.QWidget()
        self.setFixedSize(900, 700)
        # create layout for weather widget
        graph_layout = QtWidgets.QVBoxLayout(self.graph_widget)

        def update_SuggestText():
            global selected_text
            if selected_location == 'Satara':
                selected_text = text_satara
                return selected_text
            elif selected_location == 'Sangli':
                selected_text = text_sangli
                return selected_text
            else:
                selected_text = text_solapur
                return selected_text

# create label for Weather
        graph_label = QtWidgets.QLabel(
            "Suggestion", alignment=QtCore.Qt.AlignCenter)
        graph_label.setFont(QtGui.QFont("Georgia", 70, QtGui.QFont.Bold))

        # create GroupBox for current weather
        Graph_groupbox = QtWidgets.QGroupBox("Suggestion Corner:")
        Graph_groupbox.setStyleSheet(
            "QGroupBox { font-size: 20px; font-weight: bold;background-color:  #f2f2f2;border-radius: 10px; }")
        Graph_layout = QtWidgets.QHBoxLayout(Graph_groupbox)
        Graph_value_label = QtWidgets.QLabel(update_SuggestText())
        Graph_layout.addWidget(Graph_value_label)
        
        Graph_layout.addStretch()
        

        back_button = QtWidgets.QPushButton(' Back ', self)
        back_button.setStyleSheet(
            "QPushButton { border-radius: 5px;background-color: #72752f ; padding: 10px 20px; }")
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

        background_label = QtWidgets.QLabel(self)
        background_pixmap = QtGui.QPixmap(
            'C:\\Users\\jadha\\Documents\\AGRIFARMM\\images\\cotton.jpg')
        background_pixmap = background_pixmap.scaled(
            self.size(), QtCore.Qt.IgnoreAspectRatio)
        background_label.setPixmap(background_pixmap)
        background_label.setGeometry(0, 0, self.width(), self.height())

    # set background label as the parent of price widget
        background_layout = QtWidgets.QVBoxLayout(background_label)
        background_layout.addWidget(self.graph_widget)

        self.setCentralWidget(background_label)

# set weather widget as central widget
        

# set size of main window
        

# set stylesheet for main window
        # self.setStyleSheet("background-color: #cccead;")

        # create the translate combo box and add it to the main widget
        self.translate_combobox = QtWidgets.QComboBox(self.graph_widget)
        self.translate_combobox.setGeometry(720, 20, 150, 30)
        self.translate_combobox.setFont(
            QtGui.QFont("Monaco", 10, QtGui.QFont.Bold))
        self.translate_combobox.setStyleSheet("""QComboBox { background-color: white; color: black ; border:1px solid gray; padding: 1px 18px 1px 3px;min-width: 6em;border-radius: 4px;} QComboBox::drop-down {subcontrol-origin: padding;subcontrol-position: top right;width: 15px;border-left-width: 1px;border-left-color: gray;border-left-style: solid;border-top-right-radius: 4px;border-bottom-right-radius: 4px; }QComboBox::down-arrow {image: url(up_arrow.png);width: 12px;height: 12px;}QComboBox::down-arrow:on {image: url(down_arrow.png);}""")
        self.translate_combobox.addItems(
            ["Select Language", "Marathi", "Hindi", "Reset"])

        # create an instance of the translator
        self.translator = Translator()

        # connect the "activated" signal of the translate_combobox to a slot function
        self.translate_combobox.activated.connect(self.translate_text)

    def showw_graph_page(self):
        self.graph_widget = QtWidgets.QWidget()
        self.setFixedSize(900, 700)
        # create layout for weather widget
        graph_layout = QtWidgets.QVBoxLayout(self.graph_widget)

        def update_SuggestText():
            global selected_text
            if selected_location == 'Satara':
                selected_text = price_satara
                return selected_text
            elif selected_location == 'Sangli':
                selected_text = price_sangli
                return selected_text
            else:
                selected_text = price_solapur
                return selected_text

# create label for Weather
        graph_label = QtWidgets.QLabel(
            "Suggestion", alignment=QtCore.Qt.AlignCenter)
        graph_label.setFont(QtGui.QFont("Georgia", 70, QtGui.QFont.Bold))

        # create GroupBox for current weather
        Graph_groupbox = QtWidgets.QGroupBox("Suggestion Corner:")
        Graph_groupbox.setStyleSheet(
            "QGroupBox { font-size: 20px; font-weight: bold;background-color:  #f2f2f2;border-radius: 10px; }")
        Graph_layout = QtWidgets.QHBoxLayout(Graph_groupbox)
        Graph_value_label = QtWidgets.QLabel(update_SuggestText())
        Graph_layout.addWidget(Graph_value_label)
        
        Graph_layout.addStretch()
        

        back_button = QtWidgets.QPushButton(' Back ', self)
        back_button.setStyleSheet(
            "QPushButton { border-radius: 5px;background-color: #72752f ; padding: 10px 20px; }")
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

        background_label = QtWidgets.QLabel(self)
        background_pixmap = QtGui.QPixmap(
            'C:\\Users\\jadha\\Documents\\AGRIFARMM\\images\\cotton.jpg')
        background_pixmap = background_pixmap.scaled(
            self.size(), QtCore.Qt.IgnoreAspectRatio)
        background_label.setPixmap(background_pixmap)
        background_label.setGeometry(0, 0, self.width(), self.height())

    # set background label as the parent of price widget
        background_layout = QtWidgets.QVBoxLayout(background_label)
        background_layout.addWidget(self.graph_widget)

        self.setCentralWidget(background_label)

# set weather widget as central widget
        

# set size of main window
        

# set stylesheet for main window
        # self.setStyleSheet("background-color: #cccead;")

        # create the translate combo box and add it to the main widget
        self.translate_combobox = QtWidgets.QComboBox(self.graph_widget)
        self.translate_combobox.setGeometry(720, 20, 150, 30)
        self.translate_combobox.setFont(
            QtGui.QFont("Monaco", 10, QtGui.QFont.Bold))
        self.translate_combobox.setStyleSheet("""QComboBox { background-color: white; color: black ; border:1px solid gray; padding: 1px 18px 1px 3px;min-width: 6em;border-radius: 4px;} QComboBox::drop-down {subcontrol-origin: padding;subcontrol-position: top right;width: 15px;border-left-width: 1px;border-left-color: gray;border-left-style: solid;border-top-right-radius: 4px;border-bottom-right-radius: 4px; }QComboBox::down-arrow {image: url(up_arrow.png);width: 12px;height: 12px;}QComboBox::down-arrow:on {image: url(down_arrow.png);}""")
        self.translate_combobox.addItems(
            ["Select Language", "Marathi", "Hindi", "Reset"])

        # create an instance of the translator
        self.translator = Translator()

        # connect the "activated" signal of the translate_combobox to a slot function
        self.translate_combobox.activated.connect(self.translate_text)

    def showww_graph_page(self):
        self.graph_widget = QtWidgets.QWidget()
        self.setFixedSize(900, 700)
        # create layout for weather widget
        graph_layout = QtWidgets.QVBoxLayout(self.graph_widget)

        def update_SuggestText():
            global selected_text
            if selected_location == 'Satara':
                selected_text = price_satara
                return selected_text
            elif selected_location == 'Sangli':
                selected_text = price_sangli
                return selected_text
            else:
                selected_text = price_solapur
                return selected_text

# create label for Weather
        graph_label = QtWidgets.QLabel(
            "Suggestion", alignment=QtCore.Qt.AlignCenter)
        graph_label.setFont(QtGui.QFont("Georgia", 70, QtGui.QFont.Bold))

        # create GroupBox for current weather
        Graph_groupbox = QtWidgets.QGroupBox("Suggestion Corner:")
        Graph_groupbox.setStyleSheet(
            "QGroupBox { font-size: 20px; font-weight: bold;background-color:  #f2f2f2;border-radius: 10px; }")
        Graph_layout = QtWidgets.QHBoxLayout(Graph_groupbox)
        Graph_value_label = QtWidgets.QLabel(update_SuggestText())
        Graph_layout.addWidget(Graph_value_label)
        
        Graph_layout.addStretch()
        

        back_button = QtWidgets.QPushButton(' Back ', self)
        back_button.setStyleSheet(
            "QPushButton { border-radius: 5px;background-color: #72752f ; padding: 10px 20px; }")
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

        background_label = QtWidgets.QLabel(self)
        background_pixmap = QtGui.QPixmap(
            'C:\\Users\\jadha\\Documents\\AGRIFARMM\\images\\cotton.jpg')
        background_pixmap = background_pixmap.scaled(
            self.size(), QtCore.Qt.IgnoreAspectRatio)
        background_label.setPixmap(background_pixmap)
        background_label.setGeometry(0, 0, self.width(), self.height())

    # set background label as the parent of price widget
        background_layout = QtWidgets.QVBoxLayout(background_label)
        background_layout.addWidget(self.graph_widget)

        self.setCentralWidget(background_label)

# set weather widget as central widget
        

# set size of main window
        

# set stylesheet for main window
        # self.setStyleSheet("background-color: #cccead;")

        # create the translate combo box and add it to the main widget
        self.translate_combobox = QtWidgets.QComboBox(self.graph_widget)
        self.translate_combobox.setGeometry(720, 20, 150, 30)
        self.translate_combobox.setFont(
            QtGui.QFont("Monaco", 10, QtGui.QFont.Bold))
        self.translate_combobox.setStyleSheet("""QComboBox { background-color: white; color: black ; border:1px solid gray; padding: 1px 18px 1px 3px;min-width: 6em;border-radius: 4px;} QComboBox::drop-down {subcontrol-origin: padding;subcontrol-position: top right;width: 15px;border-left-width: 1px;border-left-color: gray;border-left-style: solid;border-top-right-radius: 4px;border-bottom-right-radius: 4px; }QComboBox::down-arrow {image: url(up_arrow.png);width: 12px;height: 12px;}QComboBox::down-arrow:on {image: url(down_arrow.png);}""")
        self.translate_combobox.addItems(
            ["Select Language", "Marathi", "Hindi", "Reset"])

        # create an instance of the translator
        self.translator = Translator()

        # connect the "activated" signal of the translate_combobox to a slot function
        self.translate_combobox.activated.connect(self.translate_text)


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
        self.user_guide_content = QtWidgets.QLabel(
            '''
            Welcome to the user guide for the Agrifarm website! Agrifarm is an online platform for farmers to buy
            and sell their products, connect with other farmers, and stay up-to-date with the latest news and trends
            in the agricultural industry.

            1.Register and Login
            To use the Agrifarm website, you will need to register an account. Click on the "Register" button
            on the homepage and fill in your details. Once you have registered, you can login with your username 
            and password.

            2.Buy and Sell Products
            To buy or sell products, click on the "Marketplace" tab. Here, you can browse products for sale, search 
            for specific items, and post your own products for sale. When buying or selling, make sure to communicate
            with the other party to arrange payment and delivery.

            3.Connect with Other Farmers
            Agrifarm also offers a social networking platform for farmers to connect with each other. Click on the 
            "Community" tab to access the social networking platform. Here, you can join groups, participate in 
            discussions, and connect with other farmers from around the world.

            4.Stay Up-to-Date with News and Trends
            To stay informed about the latest news and trends in the agricultural industry, visit the "News & Trends" tab.
            Here, you can read articles and watch videos about a wide range of agricultural topics, from farming 
            techniques to market trends.

            5.Contact Customer Support
            If you have any questions or concerns, you can contact the Agrifarm customer support team by clicking on the 
            "Contact Us" tab. Here, you can fill in a form to submit your inquiry, and the customer support team will
            get back to you as soon as possible.

            Thank you for using the Agrifarm website. We hope this user guide has been helpful, and we wish you success
            in your farming endeavors!
            ''')
        self.user_guide_content.setGeometry(50, 50, 800, 600)
        self.user_guide_content.setStyleSheet(
            "font-size: 15px; font-family: Arial;font-weight: bold;")

        back_button = QtWidgets.QPushButton(' Back ', self)
        back_button.setStyleSheet(
            "QPushButton { border-radius: 5px;background-color: #72752f ; padding: 10px 20px; }")
        back_button.setFont(QtGui.QFont("Monaco", 10, QtGui.QFont.Bold))
        back_button.clicked.connect(self.show_main_window)

# create button layout
        buttons_layout = QtWidgets.QHBoxLayout()
        buttons_layout.addWidget(back_button, alignment=QtCore.Qt.AlignLeft)

        buttons_layout.setContentsMargins(10, 10, 10, 20)

    # add widgets and layouts to user guide layout
        user_guide_layout.addWidget(user_guide_label)
        user_guide_layout.addWidget(self.user_guide_content)
        user_guide_layout.addLayout(buttons_layout)

    # set user guide widget as central widget
        self.setCentralWidget(self.user_guide_widget)

        # create the translate combo box and add it to the main widget
        self.translate_combobox = QtWidgets.QComboBox(self.user_guide_widget)
        self.translate_combobox.setGeometry(740, 20, 150, 30)
        self.translate_combobox.setFont(
            QtGui.QFont("Monaco", 10, QtGui.QFont.Bold))
        self.translate_combobox.setStyleSheet("""QComboBox { background-color: white; color: black ; border:1px solid gray; padding: 1px 18px 1px 3px;min-width: 6em;border-radius: 4px;} QComboBox::drop-down {subcontrol-origin: padding;subcontrol-position: top right;width: 15px;border-left-width: 1px;border-left-color: gray;border-left-style: solid;border-top-right-radius: 4px;border-bottom-right-radius: 4px; }QComboBox::down-arrow {image: url(up_arrow.png);width: 12px;height: 12px;}QComboBox::down-arrow:on {image: url(down_arrow.png);}""")
        self.translate_combobox.addItems(
            ["Select Language", "Marathi", "Hindi", "Reset"])

        # create an instance of the translator
        self.translator = Translator()

        # connect the "activated" signal of the translate_combobox to a slot function
        self.translate_combobox.activated.connect(self.translate_text)
