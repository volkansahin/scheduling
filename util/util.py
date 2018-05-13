
class Util:

    @staticmethod
    def write(content):
        file = open('result.txt', 'a', encoding='UTF-8')
        file.write(content)
        file.close()

    @staticmethod
    def reset_file():
        file = open('result.txt', 'w', encoding='UTF-8')
        file.write('')
        file.close()