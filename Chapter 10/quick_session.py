
from flask import Flask, session

app = Flask(__name__)

app.secret_key = 'YouWillNeverGuess'
# secret key is used by Flask to encrypt your cookie
#once session is imported and secret key is set 'session' can be used as a dictionary 

@app.route('/setuser/<user>')
def setuser(user: str) -> str:
	session['user'] = user
	return 'User value set to : '+session['user']


@app.route('/getuser')
def getuser() -> str:
	return 'User value is currently set to: '+session['user']


if __name__=='__main__':
	app.run(debug=True)

