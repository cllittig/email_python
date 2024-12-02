from functions.cleanEmail import CleanEmail

# Configurações
IMAP_SERVER = "imap.gmail.com"
EMAIL = "carlosaugusto98p@gmail.com"
PASSWORD = "sdmx qxwy vesm yqvr"

# Conexão ao servidor IMAP

if __name__ == "__main__":
    CleanEmail(EMAIL, PASSWORD, IMAP_SERVER)
