import sqlalchemy.ext.declarative as _declarative
import os

DATABASE_PARAMS = {"db_url": os.environ.get('DATABASE_DSN')}

Base = _declarative.declarative_base()
