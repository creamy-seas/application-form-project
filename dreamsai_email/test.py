import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

gmail_user = 'fred.feng0326@gmail.com'
gmail_password = '1126happy'

sent_from = gmail_user
to = 'fred.yang@dreams-ai.com'
subject = 'OMG Super Important Message'
# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart('alternative')
msg['Subject'] = subject
msg['From'] = gmail_user
msg['To'] = to
firstname = 'ydsads'
lastname = 'dsadsa'
# Create the body of the message (a plain-text and an HTML version).
html = """\
<html>
  <head></head>
  <body>
    <h2>Application Form<h2>
    <table border="1" bordercolor="black" width="800px">
      <tr>
        <th>First Name</th>
        <th>{firstname}</th>
        <th>Last Name</th>
        <th>{lastname}</th>
      </tr>
      <tr>
        <td>Date Of Birth</td>
        <td colspan="3">1992.03.26</td>
      </tr>
      <tr>
        <td>University</td>
        <td colspan="3">Hong Kong University of Technology</td>
      </tr>
      <tr>
        <td>Qualification</td>
        <td colspan="3">Master</td>
      </tr>
      <tr>
        <td>Start Day </td>
        <td></td>
        <td>End Day</td>
        <td></td>
      </tr>
      <tr>
        <td>Current Company</td>
        <td></td>
        <td>Current Job Title</td>
        <td></td>
      </tr>
      <tr>
        <td>Expected Job</td>
        <td colspan="3">Software Engineer</td>
      </tr>
      <tr>
        <td>Email</td>
        <td colspan="3">fred.feng0326@gmail.com</td>
      </tr>
    </table>
  </body>
</html>
"""

html = html.format(firstname=firstname,lastname=lastname)
# Record the MIME types of both parts - text/plain and text/html.
part2 = MIMEText(html, 'html')

# Attach parts into message container.
# According to RFC 2046, the last part of a multipart message, in this case
# the HTML message, is best and preferred.
msg.attach(part2)

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.ehlo()
server.login(gmail_user, gmail_password)
server.sendmail(sent_from, to, msg.as_string())
server.close()

print('Email sent!')
