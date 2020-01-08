import smtplib
import flask
from flask_restful import reqparse, Resource
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class SendEmail(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("lastname", type=str, required=True)
        parser.add_argument("firstname", type=str, required=True)
        parser.add_argument("birthday", type=str, required=True)
        parser.add_argument("university", type=str, required=True)
        parser.add_argument("studyperiodStart", type=str)
        parser.add_argument("studyperiodEnd", type=str)
        parser.add_argument("qualification", type=str, required=True)
        parser.add_argument("expected", type=str, required=True)
        parser.add_argument("email", type=str, required=True)
        parser.add_argument("currentjobcompany", type=str)
        parser.add_argument("currentjobtitle", type=str)
        parser.add_argument("textarea", type=str, required=True)

        args = parser.parse_args()

        lastname = args['lastname']
        firstname = args['firstname']
        birthday = args['birthday']
        university = args['university']
        studyperiodStart = args['studyperiodStart']
        studyperiodEnd = args['studyperiodEnd']
        qualification = args['qualification']
        expected = args['expected']
        email = args['email']
        currentjobcompany = args['currentjobcompany']
        currentjobtitle = args['currentjobtitle']
        textarea = args['textarea']

        gmail_user = 'noreply@dreams-ai.com'
        gmail_password = 'noreplybot123'

        sent_from = gmail_user
        to = 'fred.yang@dreams-ai.com'
        subject = 'OMG Super Important Message'
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
            <table border="1" bordercolor="black" width="800px">
              <tr>
                <th>Last Name</th>
                <th>{lastname}</th>
                <th>First Name</th>
                <th>{firstname}</th>
              </tr>
              <tr>
                <td>Date Of Birth</td>
                <td colspan="3">{birthday}</td>
              </tr>
              <tr>
                <td>University</td>
                <td colspan="3">{university}</td>
              </tr>
              <tr>
                <td>Qualification</td>
                <td colspan="3">{qualification}</td>
              </tr>
              <tr>
                <td>Start Day </td>
                <td>{studyperiodStart}</td>
                <td>End Day</td>
                <td>{studyperiodEnd}</td>
              </tr>
              <tr>
                <td>Current Company</td>
                <td>{currentjobcompany}</td>
                <td>Current Job Title</td>
                <td>{currentjobtitle}</td>
              </tr>
              <tr>
                <td>Expected Job</td>
                <td colspan="3">{expected}</td>
              </tr>
              <tr>
                <td>Email</td>
                <td colspan="3">{email}</td>
              </tr>
              <tr>
                <td colspan="4">{textarea}</td>
              </tr>
            </table>
          </body>
        </html>
        """
        html = html.format(lastname=lastname, firstname=firstname, birthday=birthday, university=university,
                           studyperiodStart=studyperiodStart, studyperiodEnd=studyperiodEnd,
                           qualification=qualification, expected=expected, email=email,
                           currentjobcompany=currentjobcompany, currentjobtitle=currentjobtitle, textarea=textarea)

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
