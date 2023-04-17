import easyocr

class CharacterRecognition:

    def __init__(self, language):
        self.__language = language
        self.reader = easyocr.Reader([self.__language])


    def get_text(self, image):
        '''

        :param image: Pillow image data
        :param language: String, what language to use
        :return:
        '''
        # Load the OCR model for Japanese

        image.save('D:\\Desktop\\file_name.png')
        # Read the text from the screenshot
        result = self.reader.readtext('D:\\Desktop\\file_name.png')
        print(result)
        # Extract the Japanese text from the OCR result
        extracted_text = ''.join([item[1] for item in result if item[0][1] == self.__language])
        return extracted_text

