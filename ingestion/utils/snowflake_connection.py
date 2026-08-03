from snowflake.snowpark import Session
from dotenv import load_dotenv
from cryptography.hazmat.primitives import serialization
import os

load_dotenv()


def get_snowflake_session(schema):

    with open(os.getenv("SNOWFLAKE_PRIVATE_KEY_PATH"), "rb") as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=os.getenv("SNOWFLAKE_PRIVATE_KEY_PASSPHRASE").encode(),
        )

    private_key_bytes = private_key.private_bytes(
        encoding=serialization.Encoding.DER,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption(),
    )

    connection_parameters = {
        "account": os.getenv("SNOWFLAKE_ACCOUNT"),
        "user": os.getenv("SNOWFLAKE_USER"),
        "private_key": private_key_bytes,
        "warehouse": os.getenv("SNOWFLAKE_WAREHOUSE"),
        "database": os.getenv("SNOWFLAKE_DATABASE"),
    }

    session = Session.builder.configs(connection_parameters).create()

    session.use_schema(schema)

    return session