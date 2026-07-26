from snowflake.snowpark import Session
from dotenv import load_dotenv
import os

load_dotenv()


def get_snowflake_session(schema):

    mfa_code = input("Enter your 6-digit MFA code: ")

    connection_parameters = {
        "account": os.getenv("SNOWFLAKE_ACCOUNT"),
        "user": os.getenv("SNOWFLAKE_USER"),
        "password": os.getenv("SNOWFLAKE_PASSWORD"),
        "warehouse": os.getenv("SNOWFLAKE_WAREHOUSE"),
        "database": os.getenv("SNOWFLAKE_DATABASE"),
        "passcode": mfa_code,
    }

    session = Session.builder.configs(connection_parameters).create()

    session.use_schema(schema)

    return session