import smtplib

try:
    s = smtplib.SMTP('smtp.gmail.com', 587)
    sender_email_id='plmkfake@gmail.com'
    sender_email_id_password='@ompk123'
    receiver_email_id="omjhainfo@yahoo.com"
    message = "Message_you_need_to_send"
    s.starttls()
    s.login(sender_email_id, sender_email_id_password)
    s.sendmail(sender_email_id, receiver_email_id, message)
    s.quit()
except Exception as e:
    print(e)
    print('Something went wrong...')