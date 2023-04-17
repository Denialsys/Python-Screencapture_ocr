import easyocr
import os
class CharacterRecognition:

    def __init__(self, language, is_gpu_enabled=False):
        self.__language = language
        self.reader = easyocr.Reader([self.__language], gpu=is_gpu_enabled)
        self.cwd = os.getcwd()
        self.outputfile_raw = os.path.join(os.getcwd(), 'raw.png')


    def get_text(self, image):
        '''

        :param image: Pillow image data
        :param language: String, what language to use
        :return:
        '''
        # Load the OCR model for Japanese

        image.save('D:\\Desktop\\file_name.png')
        # Read the text from the screenshot
        result = self.reader.readtext('D:\\Desktop\\file_name.png', paragraph=True)
        # Extract the Japanese text from the OCR result
        extracted_text = ''.join(item[1] for item in result)
        return extracted_text

