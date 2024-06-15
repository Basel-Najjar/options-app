from tastytrade import CertificationSession
from dotenv import load_dotenv
from os import getenv

def auth() -> CertificationSession:
    load_dotenv()
    return CertificationSession(getenv('username'), getenv('password'))