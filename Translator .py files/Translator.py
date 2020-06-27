from translate import Translator

translator = Translator(to_lang="es")
try:
    with open('./hello.txt', mode='r') as myfile:
        text = myfile.read()
        translation = translator.translate(text)
        print(translation)
    with open('./trans-Ja.txt',mode='w') as myfile2:
    	myfile2.write(translation)
    
except FileNotFoundError as err:
        print('you are silly!!')
  