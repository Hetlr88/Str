import os

ENVIRONMENT = os.environ.get('ENVIRONMENT', False)

if ENVIRONMENT:
    try:
        API_ID = int(os.environ.get('API_ID', 29452145))
    except ValueError:
        raise Exception("Your API_ID is not a valid integer.")
    API_HASH = os.environ.get('API_HASH', 5a2784e571fe5043852d32396a34a13b)
    BOT_TOKEN = os.environ.get('BOT_TOKEN', 7352645964:AAHjLhEQ17cBn2xnFWLazCwA_eOeP-JRWcE)
    DATABASE_URL = os.environ.get('DATABASE_URL', mongodb+srv://KannadaMagaa:KannadaMagaa@kannadamagaaclone.kweqbmy.mongodb.net/?retryWrites=true&w=majority)
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")  # Sqlalchemy dropped support for "postgres" name.
    # https://stackoverflow.com/questions/62688256/sqlalchemy-exc-nosuchmoduleerror-cant-load-plugin-sqlalchemy-dialectspostgre
    MUST_JOIN = os.environ.get('MUST_JOIN', None)
    if MUST_JOIN.startswith("@"):
        MUST_JOIN = MUST_JOIN.replace("@", "x_xf8")
else:
    # Fill the Values
    API_ID = 0
    API_HASH = ""
    BOT_TOKEN = ""
    DATABASE_URL = ""
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")
    MUST_JOIN = ""
    if MUST_JOIN.startswith("@"):
        MUST_JOIN = MUST_JOIN[1:]
