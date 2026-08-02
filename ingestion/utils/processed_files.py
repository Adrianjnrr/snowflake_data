import hashlib
from uuid import uuid4


def calculate_file_hash(file_path):
    """
    Calculate an MD5 hash for a file.
    Files with identical content will have the same hash.
    """

    hash_md5 = hashlib.md5()

    with open(file_path, "rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            hash_md5.update(chunk)

    return hash_md5.hexdigest()


def is_file_processed(session, file_hash):

    result = session.sql(f"""
        SELECT 1
        FROM PROCESSED_FILES
        WHERE file_hash = '{file_hash}'
        LIMIT 1
    """).collect()

    return len(result) > 0



def mark_file_processed(
    session,
    file_name,
    file_hash,
    table_name,
    status
):

    session.sql(f"""
        INSERT INTO PROCESSED_FILES
        (
            file_name,
            file_hash,
            table_name,
            status,
            pipeline_run_id,
            processed_at
        )
        VALUES
        (
            '{file_name}',
            '{file_hash}',
            '{table_name}',
            '{status}',
            '{uuid4()}',
            CURRENT_TIMESTAMP()
        )
    """).collect()