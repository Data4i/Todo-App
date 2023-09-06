from app import app, db

def create_db():
    with app.app_context():
        return db.create_all()
    
