# International Scholarships Alert

This is a really simple AWS lambda function that alerts information about scholarships from embassies and consulates in Brazil through email (for now).

Countries currently available:
- China
- Japan
- Korea

# How to use

- Create a new email to send those messages;
- Install dependencies in the same folder, by running:  
`pip install -r requirements -t .`

- Then Zip everything
- Configure AWS Lamnbda and upload there
- Configure CloudWatch

#### OBS.: You can create a cronjob at your local machine too

# Enviroment variables

EMAIL=               Sender email  
EMAIL_PASSWORD=     Sender password  
EMAIL_RECEIVER_1=   Recipient email  
EMAIL_RECEIVER_2=    Another recipient email  

# TODO:
- Add more embassies and consulates
- Telegram Integration
- Email database
- Front-end for email register
- Huge refactor (code is currently really bad, and it's kinda embarrassing)