from your_app import db  # Import the SQLAlchemy database object
from your_app.models import Patients  # Import the Patients model

# Create 10 sample patient records
sample_patients = [
    Patients(
        first_name='John',
        last_name='Doe',
        other_name='Middle',
        date_of_birth=datetime.fromisoformat('1990-05-15'),
        gender='Male',
        phone_number='1234567890',
        email_address='john.doe@example.com',
        hashed_password=generate_password_hash('hashed_password_1')
    ),
    Patients(
        first_name='Jane',
        last_name='Smith',
        date_of_birth='1985-08-25',
        gender='Female',
        phone_number='9876543210',
        email_address='jane.smith@example.com',
        hashed_password='hashed_password_2'
    ),
    Patients(
        first_name='Bob',
        last_name='Johnson',
        date_of_birth='1977-02-10',
        gender='Male',
        phone_number='5555555555',
        email_address='bob.johnson@example.com',
        hashed_password='hashed_password_3'
    ),
    Patients(
        first_name='Alice',
        last_name='Brown',
        date_of_birth='1995-11-20',
        gender='Female',
        phone_number='7777777777',
        email_address='alice.brown@example.com',
        hashed_password='hashed_password_4'
    ),
    Patients(
        first_name='David',
        last_name='Wilson',
        date_of_birth='1980-04-12',
        gender='Male',
        phone_number='3333333333',
        email_address='david.wilson@example.com',
        hashed_password='hashed_password_5'
    ),
    Patients(
        first_name='Sarah',
        last_name='Miller',
        date_of_birth='1992-09-08',
        gender='Female',
        phone_number='9999999999',
        email_address='sarah.miller@example.com',
        hashed_password='hashed_password_6'
    ),
    Patients(
        first_name='Michael',
        last_name='Clark',
        date_of_birth='1987-03-30',
        gender='Male',
        phone_number='8888888888',
        email_address='michael.clark@example.com',
        hashed_password='hashed_password_7'
    ),
    Patients(
        first_name='Emily',
        last_name='Anderson',
        date_of_birth='1998-06-05',
        gender='Female',
        phone_number='6666666666',
        email_address='emily.anderson@example.com',
        hashed_password='hashed_password_8'
    ),
    Patients(
        first_name='William',
        last_name='Thomas',
        date_of_birth='1983-12-15',
        gender='Male',
        phone_number='4444444444',
        email_address='william.thomas@example.com',
        hashed_password='hashed_password_9'
    ),
    Patients(
        first_name='Olivia',
        last_name='White',
        date_of_birth='1994-07-18',
        gender='Female',
        phone_number='2222222222',
        email_address='olivia.white@example.com',
        hashed_password='hashed_password_10'
    )
]

# Add the sample patients to the database
for patient in sample_patients:
    db.session.add(patient)

# Commit the changes to the database
db.session.commit()

sample_doctors = [
    Doctors(
        first_name='Abdulrasheed',
        last_name='Bello',
        gender='Male',
        phone_number='1123111111',
        email_address='bell.rash@example.com',
        specialty='Cardiology',
        license_number='12356',
        hashed_password=generate_password_hash('hashed_password_1'),
        healthcare_id=1
    ),
    Doctors(
        first_name='Jane',
        last_name='Doe',
        gender='Female',
        phone_number='2222222222',
        email_address='jane.doe@example.com',
        specialty='Dermatology',
        license_number='67890',
        password='hashed_password_2',
        healthcare_id=2  # Link to an existing healthcare center (change this as needed)
    ),
    # Add more doctor records and associate them with healthcare centers as needed
]

# Add the sample doctor records to the database
for doctor in sample_doctors:
    db.session.add(doctor)

# Commit the changes to the database
db.session.commit()
In this example, we've created two sample doctor records and associated them with healthcare centers by setting the healthcare_id field to the primary key of the corresponding healthcare centers. You can add more doctor records and associate them with different healthcare centers as required. Ensure that you replace 'your_app' and 'your_app.models' with the actual names of your application and the module where the Doctors and Healthcares models are defined.


from your_app import db  # Import the SQLAlchemy database object
from your_app.models import Healthcares  # Import the Healthcares model

# Create 10 sample healthcare records
sample_healthcares = [
    Healthcares(
        name='Healthcare Center 1',
        email_address='healthcare1@example.com',
        address='123 Main Street',
        contact_number='111-111-1111',
        hashed_password=generate_password_hash('hashed_password_1')
    ),
    Healthcares(
        name='Healthcare Center 2',
        email_address='healthcare2@example.com',
        address='456 Elm Avenue',
        contact_number='222-222-2222',
        hashed_password='hashed_password_2'
    ),
    Healthcares(
        name='Healthcare Center 3',
        email_address='healthcare3@example.com',
        address='789 Oak Lane',
        contact_number='333-333-3333',
        hashed_password='hashed_password_3'
    ),
    Healthcares(
        name='Healthcare Center 4',
        email_address='healthcare4@example.com',
        address='101 Pine Road',
        contact_number='444-444-4444',
        hashed_password='hashed_password_4'
    ),
    Healthcares(
        name='Healthcare Center 5',
        email_address='healthcare5@example.com',
        address='202 Cedar Drive',
        contact_number='555-555-5555',
        hashed_password='hashed_password_5'
    ),
    Healthcares(
        name='Healthcare Center 6',
        email_address='healthcare6@example.com',
        address='303 Birch Street',
        contact_number='666-666-6666',
        hashed_password='hashed_password_6'
    ),
    Healthcares(
        name='Healthcare Center 7',
        email_address='healthcare7@example.com',
        address='404 Maple Avenue',
        contact_number='777-777-7777',
        hashed_password='hashed_password_7'
    ),
    Healthcares(
        name='Healthcare Center 8',
        email_address='healthcare8@example.com',
        address='505 Walnut Lane',
        contact_number='888-888-8888',
        hashed_password='hashed_password_8'
    ),
    Healthcares(
        name='Healthcare Center 9',
        email_address='healthcare9@example.com',
        address='606 Spruce Road',
        contact_number='999-999-9999',
        hashed_password='hashed_password_9'
    ),
    Healthcares(
        name='Healthcare Center 10',
        email_address='healthcare10@example.com',
        address='707 Oak Avenue',
        contact_number='101-101-1010',
        hashed_password='hashed_password_10'
    )
]

# Add the sample healthcare records to the database
for healthcare in sample_healthcares:
    db.session.add(healthcare)

# Commit the changes to the database
db.session.commit()

TimeSlots(doctor_id=2, start_time=time(9, 0, 0), end_time=time(15, 0, 0), day_of_the_week="Tuesday")