import os

from django.core.mail import EmailMessage


def email_admin(subj, body ):
    subject, from_email, to = subj, os.environ.get('MAIL_USERNAME'), os.environ.get('MAIL_RECIPIENTS')
    html_content = body
    msg = EmailMessage(subj, body, from_email, [to])
    msg.content_subtype = "html"
    return msg.send()