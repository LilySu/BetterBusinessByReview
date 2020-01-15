import sys
import logging
import rds_config
import psycopg2-binary
#rds settings
rds_host  = rds_config.db_endpoint
name = rds_config.db_username
password = rds_config.db_password
db_name = rds_config.db_name

logger = logging.getLogger()
logger.setLevel(logging.INFO)

try:
    conn = psycopg2.connect(rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)
except psycopg2.OperationalError as e:
    logger.error("ERROR: Unexpected error: Could not connect to postGreSQL instance.")
    logger.error(e)
    sys.exit()

logger.info("SUCCESS: Connection to RDS postGreSQL instance succeeded")
def handler(event, context):
    """
    This function fetches content from postGreSQL RDS instance
    """

    item_count = 0

    with conn.cursor() as cur:
        cur.execute("create table Test ( TestID  int NOT NULL, Name varchar(255) NOT NULL, PRIMARY KEY (TestID))")
        cur.execute('insert into Test (TestID, Name) values(1, "Joe")')
        cur.execute('insert into Test (TestID, Name) values(2, "Bob")')
        cur.execute('insert into Test (TestID, Name) values(3, "Mary")')
        conn.commit()
        cur.execute("select * from Test")
        for row in cur:
            item_count += 1
            logger.info(row)
            #print(row)
    conn.commit()

    return "Added %d items from RDS postGreSQL table" %(item_count)