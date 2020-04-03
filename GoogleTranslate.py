from googletrans import Translator

translator = Translator()

src = input("Enter source language or code or leave blank to detect source language: ")
dest = input("Enter destination language or code (Default = English): ")
x = input("Enter text: ")

if src!='' and dest=='':
    print('Source Language =',translator.translate(x,src=src).src)
    print('Destination Language =',translator.translate(x,src=src).dest)
    print('Translation =',translator.translate(x,src=src).text)

elif dest!='' and src=='':
    print('Source Language =',translator.translate(x,dest=dest).src)
    print('Destination Language =',translator.translate(x,dest=dest).dest)
    print('Translation =',translator.translate(x,dest=dest).text)

elif src!='' and dest!='':
    print('Source Language =',translator.translate(x,src=src,dest=dest).src)
    print('Destination Language =',translator.translate(x,src=src,dest=dest).dest)
    print('Translation =',translator.translate(x,src=src,dest=dest).text)

else:
    print('Source Language =',translator.translate(x).src)
    print('Destination Language =',translator.translate(x).dest)
    print('Translation =',translator.translate(x).text)
