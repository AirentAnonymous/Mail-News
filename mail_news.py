import smtplib
import getpass
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def get_credentials():
    """Get Gmail credentials and recipient list from user"""
    email = input('Enter your Gmail address: ')
    password = getpass.getpass('Enter your Gmail app password: ')
    recipients = input('Enter recipient email addresses (comma-separated): ').split(',')
    recipients = [email.strip() for email in recipients]
    return email, password, recipients

def send_email(sender_email, password, recipients, headline):
    """Send email with news headline to all recipients"""
    # Create message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = ', '.join(recipients)
    msg['Subject'] = 'Today\'s Top News Headline'
    
    # Add body
    body = f"Today's most discussed headline:\n\n{headline}"
    msg.attach(MIMEText(body, 'plain'))
    
    try:
        # Create secure SSL/TLS connection
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(sender_email, password)
        
        # Send email
        server.send_message(msg)
        print('Email sent successfully!')
        
    except Exception as e:
        print(f'An error occurred: {str(e)}')
    
    finally:
        server.quit()

def main():
    print('Welcome to Mail News!')
    print('Note: You need to use an App Password for Gmail. Generate one at:')
    print('https://myaccount.google.com/security > 2-Step Verification > App passwords')
    
    # Get credentials and recipient list
    sender_email, password, recipients = get_credentials()
    
    # Get headline (in a real application, this would come from a news API)
    headline = input('Enter the news headline to send: ')
    
    # Send the email
    send_email(sender_email, password, recipients, headline)

if __name__ == '__main__':
    main()