#to active the enviroment just type . bin/activate
from domo_flask import application
#First. we imported the Flask class and a function render_template.
from flask import render_template, request, flash
#Importing forms, preventing a CSRF attack
from forms import ContactForm

from flask.ext.mail import Message, Mail 
mail = Mail() 

#from raspi.Raspi import Raspi
#domo_raspi = Raspi()  

from raspi.RaspiOSX import RaspiOSX
domo_raspi = RaspiOSX()
 
#We then mapped the URL / to the function home(). Now, when someone visits this URL, the function home() will execute. 
@application.route('/')
def home():#The function home() uses the Flask function render_template() to render the home.html template we just created from the templates/ folder to the browser.
  return render_template('home.html')

@application.route('/about')
def about():
  return render_template('about.html')

@application.route('/turnon')
def turnOn():
  domo_raspi.turnOn()
  return "Turned on"

@application.route('/turnoff')
def turnOff():
  domo_raspi.turnOff()
  return "Turned off"

@application.route('/contact', methods=['GET', 'POST'])
def contact():
  form = ContactForm()
 
  if request.method == 'POST':
    if form.validate() == False:
      flash('All fields are required.')
      return render_template('contact.html', form=form)
    else:
      msg = Message(form.subject.data, sender='ricardo@myapp.com', recipients=['moises.full.ios@gmail.com'])
      msg.body = """
      From: %s <%s>
      %s
      """ % (form.name.data, form.email.data, form.message.data)
      mail.send(msg)
 
      return render_template('contact.html', success=True)
 
  elif request.method == 'GET':
    return render_template('contact.html', form=form)




#Finally, we use run() to run our app on a local server. 
#We'll set the debug flag to true, so we can view any applicable error messages if something goes wrong, 
#and so that the local server automatically reloads after we've made changes to the code. 
if __name__ == '__main__':
  application.run(debug=True)