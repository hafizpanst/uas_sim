from psycopg2 import connect


const = {
    "delimiter" : "|",
}


def connDB():
    conn = connect(
        host = "localhost",
        port = "5432",
        database = "kms_oc",
        user = "kms_oc",
        password = "kms_oc",
    )
    return conn