import os

def _events():
    EVENTS = {
            "New Asset": new_asset,
            "Publish Asset" : pepito
        }
    return EVENTS

def read_creds():
    """Reads the credentials.txt file and gets the mail account credentials to login

    Returns:
        string:  username and password
    """
    user = passw = ""
    with open("./src/credentials.txt", "r") as f:
        file = f.readlines()
        user = file[0].strip()
        passw = file[1].strip()

    return user, passw

def send_mail(to, subject, text, attach, *args, **kwargs):
    """Send mail function

    Args:
        to (string): receiver mail account
        subject (string): mail subject
        text (string): main body text
        attach (string): file path that you want to attach in the mail
    """
    import smtplib
    from email.message import EmailMessage

    ### set the sender and the password from read_creds funciontion ###
    sender, password = read_creds()

    msg = EmailMessage()

    ### set the subject ###
    if subject == None:
        msg['Subject'] = "Test Mail"
    else:
        msg['Subject'] = subject

    msg['From'] = sender
    ### set the receiver mail account ###
    msg['To'] = to
    ### set the mail body ###
    msg.set_content(text)

    if attach == None:
        pass
    else:
        with open(attach, 'rb') as f:
            file_data = f.read()
            file_name = f.name

        msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)
        logging.info("Attached to mail: {}".format(attach))

    ### send the mail with stmplib library ###
    logging.info("Starting to send mail")
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender, password)
        server.send_message(msg)

    logging.info("Sent email to {}!".format(to))


def pepito():
    print('working well')
# send_mail('rpesca65@gmail.com', 'Jabon Lavadora', "comprar jabon lavadora", attach='/Users/haarrii/Desktop/code.png')

def create_file(name, path, *args, **kwargs):
    file = '{}/{}.txt'.format(path, name)
    with open(file, 'w') as f:
        pass
    print('File created: {}'.format(file))
    return file

def write_file(file, text, *args, **kwargs):
    with open(file, 'w') as f:
        f.write(text)
    print('Text added to file: {}'.format(file))




def new_asset(*args, **kwargs):

    try:
        name = args[1].get('name')
    except SyntaxError:
        print('Must add a name argument')

    try:
        user = args[1].get('user')
    except SyntaxError:
        print('Must add an user argument')

    try:
        path = args[1].get('path')
    except SyntaxError:
        print('Must add a path argument')

    file = create_file(name, path)

    try:
        text = args[1].get('text')
        write_file(file, text)
    except SyntaxError:
        pass

    try:
        mail = args[1].get('mail')
        if mail:
            send_mail(to, subject, text, attach)
    except SyntaxError:
        pass
