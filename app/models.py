from pickle import PickleError
from . import db
from werkzeug.security import generate_password_hash

class UserProfile(db.Model):
    # You can use this to change the table name. The default convention is to use
    # the class name. In this case a class name of UserProfile would create a
    # user_profile (singular) table, but if we specify __tablename__ we can change it
    # to `user_profiles` (plural) or some other name.
    __tablename__ = 'user_profiles'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(255))

    def __init__(self,first_name,last_name,username,password):
        self.first_name=first_name
        self.last_name=last_name
        self.username=username
        self.password= generate_password_hash(password, method='pbkdf2:sha256')

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.username)

class property(db.Model):
    __tablename__ = 'property'

    id =db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    description =db.Column(db.String(250))
    no_rooms= db.Column(db.Integer)
    no_brooms= db.Column(db.Integer)
    price= db.Column(db.Integer)
    location = db.Column(db.String(80))
    type = db.Column(db.String(80))
    photo = db.Column(db.LargeBinary)

    def __init__(self,title,description,no_rooms,no_brooms,price,location,type,photo):
        self.title=title
        self.description=description
        self.no_rooms=no_rooms
        self.no_brooms=no_brooms
        self.price=price
        self.location=location
        self.type=type
        self.photo=photo
    
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<Title %r>' % (self.title)