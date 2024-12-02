from functions.cleanEmail import CleanEmail

# Configurações
IMAP_SERVER = "imap.gmail.com"
EMAIL = "seu email"
PASSWORD = "senha app externo"

# Conexão ao servidor IMAP

if __name__ == "__main__":
    CleanEmail(EMAIL, PASSWORD, IMAP_SERVER)
