from flask import Flask

#we created a new instance of the Flask class.
application = Flask(__name__)  

#fill data with your enviroment details
application.secret_key = 'hehe'

from routes import mail#This line is require to use routes.py file
#mail.init_app(application)

 
application.run(host='0.0.0.0', port=5000, debug=False)