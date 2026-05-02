from app import app
from extensions import db
from models import Interview, Answer


with app.app_context():

    Answer.query.filter_by(interview_id=8).delete()
    Interview.query.filter_by(id=8).delete()

    db.session.commit()

print("Interview 6 deleted successfully")