from google.appengine.ext import db

class Quote(db.Model):
  quote = db.TextProperty(required=True)
