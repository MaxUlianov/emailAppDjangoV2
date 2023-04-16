from dotenv import load_dotenv, set_key, find_dotenv
from collections import defaultdict
from pathlib import Path
import os


def write_user_credentials(email: str, password: str, host: str, port: str):
    env_path = Path('.env')

    set_key(dotenv_path=env_path, key_to_set='CUSTOM_EMAIL_HOST_USER', value_to_set=email)
    set_key(dotenv_path=env_path, key_to_set='CUSTOM_EMAIL_HOST_PASSWORD', value_to_set=password)
    set_key(dotenv_path=env_path, key_to_set='CUSTOM_EMAIL_HOST', value_to_set=host)
    set_key(dotenv_path=env_path, key_to_set='CUSTOM_EMAIL_HOST_PORT', value_to_set=port)
    return


def read_user_credentials():
    login_data = defaultdict(None)

    load_dotenv(find_dotenv())

    email = os.environ.get('CUSTOM_EMAIL_HOST_USER', '').strip()
    password = os.environ.get('CUSTOM_EMAIL_HOST_PASSWORD', '').strip()
    host = os.environ.get('CUSTOM_EMAIL_HOST', '').strip()
    port = os.environ.get('CUSTOM_EMAIL_HOST_PORT', '').strip()

    if email and password and host and port:
        login_data['email'] = email
        login_data['password'] = password
        login_data['host'] = host
        login_data['port'] = port
        return login_data
    else:
        return None


def user_credentials_available():
    login_data = read_user_credentials()

    if login_data is None:
        return False
    else:
        return True


def erase_user_credentials():
    env_path = Path('.env')

    set_key(dotenv_path=env_path, key_to_set='CUSTOM_EMAIL_HOST_USER', value_to_set='')
    set_key(dotenv_path=env_path, key_to_set='CUSTOM_EMAIL_HOST_PASSWORD', value_to_set='')
    set_key(dotenv_path=env_path, key_to_set='CUSTOM_EMAIL_HOST', value_to_set='')
    set_key(dotenv_path=env_path, key_to_set='CUSTOM_EMAIL_HOST_PORT', value_to_set='')
