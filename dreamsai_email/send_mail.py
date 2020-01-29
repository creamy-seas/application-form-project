import smtplib
import flask
from flask_restful import reqparse, Resource
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

class SendEmail(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("lastname", type=str, required=True)
        parser.add_argument("firstname", type=str, required=True)
        parser.add_argument("university", type=str, required=True)
        parser.add_argument("subject", type=str, required=True)
        parser.add_argument("qualification", type=str, required=True)
        parser.add_argument("year", type=str, required=True)
        parser.add_argument("expected", type=str, required=True)
        parser.add_argument("email", type=str, required=True)
        # parser.add_argument("currentjobcompany", type=str)
        # parser.add_argument("currentjobtitle", type=str)
        parser.add_argument("textarea", type=str, required=True)

        args = parser.parse_args()

        lastname = args['lastname']
        firstname = args['firstname']
        university = args['university']
        qualification = args['qualification']
        year = args['year']
        expected = args['expected']
        email = args['email']
        # currentjobcompany = args['currentjobcompany']
        # currentjobtitle = args['currentjobtitle']
        textarea = args['textarea']

        gmail_user = 'noreply@dreams-ai.com'
        gmail_password = 'noreplybot123'

        sent_from = gmail_user
        to = os.environ['EMAIL']
        subject = os.environ['SUBJECT']
        # Create message container - the correct MIME type is multipart/alternative.
        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
        msg['From'] = gmail_user
        msg['To'] = to

        # Create the body of the message (a plain-text and an HTML version).
        html = """\
        <html>
          <head></head>
          <body>
            <h2>Application Form<h2>
            <p style="font-size:15px;">lastname,firstname,university,qualification,subject,year,preferred,email,comments</p>
            <p style="font-size:15px;">{lastname},{firstname},{university},{qualification},{subject},{year},{expected},{email},{textarea}</p>
          </body>
        </html>
        """
        html = html.format(lastname=lastname, firstname=firstname, university=university, year=year, subject=subject,
                           qualification=qualification, expected=expected, email=email,
                           textarea=textarea)

        # Record the MIME types of both parts - text/plain and text/html.
        part2 = MIMEText(html, 'html')

        # Attach parts into message container.
        # According to RFC 2046, the last part of a multipart message, in this case
        # the HTML message, is best and preferred.
        msg.attach(part2)

        try:

            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.ehlo()
            server.login(gmail_user, gmail_password)
            server.sendmail(sent_from, to, msg.as_string())
            server.close()

            return {
                'status': 'success'
            }
        except Exception as e:
            print(e)
            return {
                'status': 'failed'
            }
