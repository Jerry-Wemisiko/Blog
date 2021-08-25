from flask import render_template
from . import main

@main.errorhandler(403)
def forbidden_access(error):
     
     return render_template('error.html',error = 'page')

@main.errorhandler(404)
def four_Ow_four(error):

    return render_template('error.html',error = 'page')

@main.errorhandler(500)
def server_error(error):

    return render_template('error.html',error = 'page')
    