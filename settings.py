import os

MYSQL_USERNAME = os.environ.get("MYSQL_USERNAME", "root")
MYSQL_PASSWD = os.environ.get("MYSQL_PASSWD", "selmon#123")
MYSQL_HOST = os.environ.get("MYSQL_HOST", "localhost")
MYSQL_DATABASE = os.environ.get("MYSQL_DATABASE", "simprosys")
