
import sys

src_path = './src'

if not src_path in sys.path:
    sys.path.append(src_path)

import os
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logging.basicConfig(filename='log.log', filemode='w', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

import smtplib
from email.message import EmailMessage


import events

def read_creds():
    """Reads the credentials.txt file and gets the mail account credentials to login

    Returns:
        string:  username and password
    """
    ### see the personal credentials from credentials.txt and convert them to user and passw variables ###
    user = passw = ""
    with open("./src/credentials.txt", "r") as f:
        file = f.readlines()
        user, passw = file[0].strip(), file[1].strip()

    return user, passw

def send_mail(to, subject, text, attach=None, *args, **kwargs):
    """Send mail function

    Args:
        to (string): receiver mail account
        subject (string): mail subject
        text (string): main body text
        attach (string): file path that you want to attach in the mail
    """


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
        logger.info("Attached to mail: {}".format(attach))

    ### send the mail with stmplib library ###
    logging.info("Starting to send mail")
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender, password)
        server.send_message(msg)

    logger.debug("Sent email to {}!".format(to))
    print("Sent email to {}!".format(to))



def create_file(name, path, *args, **kwargs):
    """Create a txt file based on the arguments

    Args:
        name (string): name of the file want to create
        path (string): the file path

    Returns:
        [String]: path of the created file
    """

    ### set the file path with his name ###
    file = '{}/{}.txt'.format(path, name)

    ### check if the path exist, if not create it ###
    if os.path.exists(path):
        pass
    else:
        os.mkdir(path)

    ### create the file ###
    with open(file, 'w') as f:
        pass

    ### save on logger ###
    logger.debug("File saved: {}!".format(file))
    print('File created: {}'.format(file))

    return file

def write_file(file, text, *args, **kwargs):
    """Write text on file

    Args:
        file (string): file path to write the text
        text (string): text you want to write in file
    """

    ### write the file with given text ###
    with open(file, 'w') as f:
        f.write(text)

    ### save on logger ###
    logger.debug('Text added to file: {}'.format(file))
    print('Text added to file: {}'.format(file))

def new_asset(*args, **kwargs):
    """Check the arguments and call other functions to create new asset like new txt fail and can send e-mail

    Args:
        name (string, optional): name of the file
        user (string, optional): your user
        path (string, optional): path where want to save the file
        text (string, optional): text to write in the file
        mail (bool, optional): True if want to send e-mail, False if don't
        to (string, optional): the receiver mail account
        subject (string, optional): mail subject
        mail_text (string, optional): mail body text
        attach (bool, optional): True if want to attach file on e-mail, False if don't
        attach_path (string, optional): the path of the file that want to attach
    """
    ### catch all the given arguments in a variable ###
    given_args = args[1]

    ### create the main list with all the varibles to check what of them are given from the user ###
    main_args = ['name', 'user', 'path', 'text', 'mail', 'to', 'subject', 'mail_text', 'attach', 'attach_path']

    ### compare given_args with main_args and get the matches ###
    passed_args = set(given_args).intersection(main_args)

    ### check that the name and path variables are not empty ###
    name = given_args.get('name')
    path = given_args.get('path')
    if name != None:
        pass
    else:
        raise IOError('Must add the name argument')

    if path != None:
        pass
    else:
        raise IOError('Must add the path argument')

    ### call create_file module to create the file ###
    file = create_file(given_args.get('name'), given_args.get('path'))

    ### check if text is in passed arguments. If True call write_file module to write on file ###
    if 'text' in passed_args:
        text = given_args.get('text')
        write_file(file, text)
    else:
        pass
    ### check if mail is in passed arguments. If True call send_mail module to send the e-mail ###
    if 'mail' in passed_args:
        mail = given_args.get('mail')
        if mail:
            to = given_args.get('to')
            subject = given_args.get('subject')
            mail_text = given_args.get('mail_text')
            attach = given_args.get('attach')
            attach_path = given_args.get('attach_path')
            if attach:
                send_mail(to, subject, mail_text, attach_path)
            else:
                send_mail(to, subject, mail_text)

def receiveEvent(event_type, *args, **kwargs):
    """Receive the event and check the events dictionary to call the actions
    All the args in receiveEvent are based on *args and **kwargs

    Args:
        event_type (string): event name
        name (string, optional): name of the file
        user (string, optional): your user
        path (string, optional): path where want to save the file
        text (string, optional): text to write in the file
        mail (bool, optional): True if want to send e-mail, False if don't
        to (string, optional): the receiver mail account
        subject (string, optional): mail subject
        mail_text (string, optional): mail body text
        attach (bool, optional): True if want to attach file on e-mail, False if don't
        attach_path (string, optional): the path of the file that want to attach

        *args: Variable length argument list.
    """

    ### call the module depends on the event_type ###
    eval(events.EVENTS.get(event_type))(args, kwargs)

if __name__ == "__main__":

    ### Test it ###
    receiveEvent("New Asset", name='Char_Lookdeev', user='harriet.landa', path='/Users/haarrii/Documents/skydance', text='This is a text test', mail=1, to='ximharri@gmail.com', subject='Renders', mail_text='Here are your renders', attach=0)

