from imapclient import IMAPClient
import datetime

IMAP_SERVER = "imap.gmail.com"
EMAIL = "carlosaugusto98p@gmail.com"
PASSWORD = "32130708Aa."

CRITERIA = {
    "before": datetime.date(2024,6,1)
}

def CleanEmail():
    with IMAPClient(IMAP_SERVER) as client:
        client.login(EMAIL, PASSWORD)
        print("conectado ao servidor")
        
        client.select_folder("INBOX")
        
        search_criteria =[]
        if "before" in CRITERIA:
            search_criteria.append(f"BEFORE {CRITERIA['before'].strftime('%d-%b-%Y')}")
        
        messages = client.search(search_criteria)
        
        print(f"{len(messages)} emails encontrados")
        
        if messages:
            client.delete_messages(messages)
            client.expunge()
            print("emails deletados")