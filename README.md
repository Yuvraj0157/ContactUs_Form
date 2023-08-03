
![ContactUs page Screenshot](https://github.com/Yuvraj0157/ContactUs_Form/assets/82658229/adfcd300-f3d1-46ec-a538-7a95270ee452)

# Project - Contact Form

This project implements a contact form functionality. It allows users to submit their queries through the contact form and receive a response directly to their email address.


## Technologies Used

- Python
- Django
- HTML
- CSS


## Project Setup

1. Navigate to the project directory.
```shell
cd contact_proj
```

2. Apply the database migrations.
```shell
python manage.py migrate
```

3. Set up the email configuration in the settings.py file.
```python
# Email Configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'your_smtp_server'
EMAIL_PORT = 587  # Update with the appropriate port number
EMAIL_HOST_USER = 'your_email@example.com'  # Your email address
EMAIL_HOST_PASSWORD = 'your_email_password'  # Your email password
EMAIL_USE_TLS = True  # Enable TLS encryption

# Default email address for sending emails
DEFAULT_FROM_EMAIL = 'xyz@example.com'
```
4. Run the development server.
```shell
python manage.py runserver
```

5. Access the application in your web browser.

    http://127.0.0.1:8000/contact_us/



## Usage

- Fill in the required details: Full Name, Email ID, Phone Number, and Query.
- Click the Submit button to send the query.
- Upon successful submission, the user will receive a confirmation email.
- The company team will receive the query via email and can respond to the user's query.
