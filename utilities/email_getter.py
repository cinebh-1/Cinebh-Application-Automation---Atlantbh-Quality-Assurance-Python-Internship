import imaplib
import email
import time
import re
from datetime import datetime
from bs4 import BeautifulSoup
class EmailExtractor:
    @staticmethod
    def extract_verification_code(target_email, gmail_app_password, timeout=100):
        host = "imap.gmail.com"
        user = "marionizic.ecom@gmail.com"
        today = datetime.now().strftime("%d-%b-%Y")
        start_time = time.time()
        while time.time() - start_time < timeout:
            try:
                mail = imaplib.IMAP4_SSL(host)
                mail.login(user, gmail_app_password)
                for folder in ["INBOX"]:
                    mail.select(folder)
                    status, messages = mail.search(None, f'(TO "{target_email}" SENTSINCE {today}) X-GM-RAW "Category:Primary"')
                    if status == 'OK' and messages[0]:
                        mail_ids = messages[0].split()
                        for mid in reversed(mail_ids):
                            _, data = mail.fetch(mid, '(RFC822)')
                            msg = email.message_from_bytes(data[0][1])
                            email_to = msg.get("To", "").lower()
                            if target_email.lower() not in email_to:
                                continue
                            body = ""
                            if msg.is_multipart():
                                for part in msg.walk():
                                    if part.get_content_type() == "text/html":
                                        body = part.get_payload(decode=True).decode()
                                    elif part.get_content_type() == "text/plain" and not body:
                                        body = part.get_payload(decode=True).decode()
                            else:
                                body = msg.get_payload(decode=True).decode()
                            soup = BeautifulSoup(body, "html.parser")
                            verification_code = soup.find('h1').get_text(strip=True)
                            return verification_code
                    mail.logout()
            except Exception as e:
                print(f"[DEBUG] Search error: {e}")
            print(f"[DEBUG] Waiting for email to arrive... ({int(time.time() - start_time)}s)")
            time.sleep(5)
        raise TimeoutError(f"Email for {target_email} never arrived.")