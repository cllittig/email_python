import imaplib
import email
from email.header import decode_header
import datetime

# Configurações
IMAP_SERVER = "imap.gmail.com"
EMAIL = "carlosaugusto98p@gmail.com"
PASSWORD = "sdmx qxwy vesm yqvr"

# Conexão ao servidor IMAP
def CleanEmail():
    try:
        mail = imaplib.IMAP4_SSL(IMAP_SERVER)
        mail.login(EMAIL, PASSWORD)
        print("Conectado ao servidor IMAP.")
        
        mail.select("inbox")
        
        date = (datetime.date(2024, 6, 1)).strftime("%d-%b-%Y")
        status, messages = mail.search(None, f"BEFORE {date}")
        
        email_ids = messages[0].split()
        print(f"{len(email_ids)} emails encontrados para apagar.")
        
        total = len(email_ids)
        for email_id in email_ids:
            mail.store(email_id, "+FLAGS", "\\Deleted")
            print(f" Email {email_id} de {total} apagado.")
        
        mail.expunge()
        mail.logout()
        print("Emails apagados com sucesso.")
    except Exception as e:
        print(f"Erro ao limpar emails: {e}")

if __name__ == "__main__":
    CleanEmail()
