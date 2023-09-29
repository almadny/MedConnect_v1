from datetime import datetime
from your_app import db  # Replace 'your_app' with the actual name of your Flask application

class Posts(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctors.id'), nullable=False)
    title = db.Column(db.String(30), nullable=False)
    category = db.Column(db.String(15), nullable=True, index=True)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"Post('{self.id}': '{self.title}' '{self.category}' '{self.date_posted}')"

# Example data creation
posts_data = [
    Posts(
    doctor_id=1,
    title="The Importance of Regular Exercise",
    category="Fitness",
    content="Regular exercise has numerous health benefits, including improved cardiovascular health and weight management.",
    date_posted=datetime.fromisoformat('2023-09-15')
    )
    Posts(
        doctor_id= 1,
        title= "Healthy Eating Habits for a Strong Immune System",
        category= "Popular",
        content= "A balanced diet rich in fruits, vegetables, and whole grains can help boost your immune system.",
        date_posted= datetime(2023, 9, 27, 15, 45)
    ),
    Posts(
        doctor_id= 1,
        title= "The Benefits of Meditation",
        category= "Latest",
        content= "Meditation can reduce stress and anxiety, leading to better mental and physical health.",
        date_posted= datetime(2023, 9, 26, 14, 15),
    ),
    Posts(
        doctor_id= 4,
        title= "Tips for a Good Night's Sleep",
        category= "Latest",
        content= "Getting enough quality sleep is crucial for overall health and well-being.",
        date_posted= datetime(2023, 9, 25, 22, 0),
    ),
    Posts(
        doctor_id= 5,
        title= "The Benefits of Drinking Water",
        category= "Popular",
        content= "Staying hydrated is essential for maintaining bodily functions and good health.",
        date_posted= datetime(2023, 9, 24, 11, 30)
    ),
    {
        "doctor_id": 6,  # Replace with the actual doctor ID
        "title": "Managing Stress for Better Health",
        "category": "Latest",
        "content": "Chronic stress can have negative effects on your health, so it's important to find healthy ways to manage it.",
        "date_posted": datetime(2023, 9, 23, 16, 0),  # Replace with the actual date and time
    },
    {
        "doctor_id": 7,  # Replace with the actual doctor ID
        "title": "The Importance of Regular Checkups",
        "category": "Latest",
        "content": "Regular medical checkups can help detect and prevent health issues before they become serious.",
        "date_posted": datetime(2023, 9, 22, 9, 30),  # Replace with the actual date and time
    },
    {
        "doctor_id": 8,  # Replace with the actual doctor ID
        "title": "Benefits of a Balanced Diet",
        "category": "Popular",
        "content": "A balanced diet provides essential nutrients and supports overall health.",
        "date_posted": datetime(2023, 9, 21, 14, 45),  # Replace with the actual date and time
    },
    {
        "doctor_id": 9,  # Replace with the actual doctor ID
        "title": "Exercising Safely in Hot Weather",
        "category": "Latest",
        "content": "Tips for staying safe and healthy while exercising in hot weather conditions.",
        "date_posted": datetime(2023, 9, 20, 18, 15),  # Replace with the actual date and time
    },
    {
        "doctor_id": 10,  # Replace with the actual doctor ID
        "title": "Healthy Snacking Habits",
        "category": "Popular",
        "content": "Choosing healthy snacks can help you maintain a balanced diet and support your health goals.",
        "date_posted": datetime(2023, 9, 19, 12, 0),  # Replace with the actual date and time
    },
]

# Create and add the posts to the database session
for post_data in posts_data:
    post = Posts(**post_data)
    db.session.add(post)

db.session.commit()
