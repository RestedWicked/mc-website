from flask import Flask

app = Flask(__name__)




import mc_website.views # Circular import on purpose - This is just to make sure the module is loaded.
