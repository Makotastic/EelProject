import eel
import time
from random_word import RandomWords

# Set web files folder
eel.init('.\\web')
rw = RandomWords()

@eel.expose                         # Expose this function to Javascript
def say_hello_py(x):
    print('Hello from %s' % x)

@eel.expose
def requestNewMessage_py():
    eel.newQuestionRequest()
    for i in range(100):
        eel.appendResponseData(rw.get_random_word() + " ")
        time.sleep(0.1)



say_hello_py('Python World!')
eel.say_hello_js('Python World!')   # Call a Javascript function

eel.start('Team5.html', port=8080, size=(1280, 800))  # Start