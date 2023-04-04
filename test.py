def translate_text(self, index):

    # check if the selected language is Marathi
        if self.translate_combobox.itemText(index) == "Marathi":
        # get the English text of each label and button and translate it to Marathi
                for label in self.main_widget.findChildren(QtWidgets.QLabel):
                        if not hasattr(label, "original_text"):
                                label.setProperty("original_text", label.text())
                        text = label.property("original_text")
                        if text:
                                translated_text = self.translator.translate(text, src='en', dest='mr').text
                                label.setText(translated_text)
                
                for button in self.main_widget.findChildren(QtWidgets.QPushButton):
                        if not hasattr(button, "original_text"):
                                button.setProperty("original_text", button.text())
                        text = button.property("original_text")
                        if text:
                                translated_text = self.translator.translate(text, src='en', dest='mr').text
                                button.setText(translated_text)
        elif self.translate_combobox.itemText(index) == "Hindi":
        # translate to Hindi
                for label in self.main_widget.findChildren(QtWidgets.QLabel):
                        text = label.text()
                        if text:
                                translated_text = self.translator.translate(text, src='en', dest='hi').text
                                label.setText(translated_text)
        
                for button in self.main_widget.findChildren(QtWidgets.QPushButton):
                        text = button.text()
                        if text:
                                 translated_text = self.translator.translate(text, src='en', dest='hi').text
                                 button.setText(translated_text)
    
        elif self.translate_combobox.itemText(index) == "Reset":
        # reset to English
                for label in self.main_widget.findChildren(QtWidgets.QLabel):
                        text = label.text()
                if text:
                        label.setText(text)
        
                for button in self.main_widget.findChildren(QtWidgets.QPushButton):
                        text = button.text()
                if text:
                        button.setText(text)
    
        else:
        # selected "Select Language"
                pass        
        
        


        #         self.reset_button = QtWidgets.QPushButton("Reset", self)
#         self.reset_button.clicked.connect(self.reset_text)

#     def reset_text(self):
#         # reset all labels and buttons to their original English text
#         for label in self.main_widget.findChildren(QtWidgets.QLabel):
#             label.setText(label.property("original_text"))
        
#         for button in self.main_widget.findChildren(QtWidgets.QPushButton):
#             button.setText(button.property("original_text"))

        