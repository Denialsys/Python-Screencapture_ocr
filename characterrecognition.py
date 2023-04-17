import easyocr

class CharacterRecognition:
    def get_text(self, image, language):
        '''

        :param image: Pillow image data
        :param language: String, what language to use
        :return:
        '''
        # Load the OCR model for Japanese
        reader = easyocr.Reader([language])

        # Read the text from the screenshot
        result = reader.readtext(image.tobytes())

        # Extract the Japanese text from the OCR result
        extracted_text = ''.join([item[1] for item in result if item[0][1] == language])
        return extracted_text

