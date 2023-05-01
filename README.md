### Django Email Project V2
#### A re-make of HTML email Django project 'email sender'

Email sending Django module (app) for mailings


Made using Django and Celery + Redis as message broker

Web UI (HTML, Bulma CSS) at
> <_hostname_>/email_sender/

#### Main functions:

- Sending emails to recipients using your mailbox connection 
  (default email credentials are saved in .env file from app server settings)
  
- Sending emails from any other mailbox: enter user email credentials
  using UI at 
  > <_hostname_>email_sender/login_form/
  
- Preview HTML email content using "Preview HTML" section at
  > <_hostname_>email_sender/preview_html/
  
#### Features in development:

- Delayed emails
- Multiple-recipient mailings
- Optional contacts book