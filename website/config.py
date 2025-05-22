import os

# Secret key (environment variable takes precedence)
SECRET_KEY = os.getenv("SECRET_KEY", "aabbccddeeffgghhiijjkkllmmnnoopp112233445566778899")

SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI", "postgresql://monsys-admin:monsys1@db:5432/monsys_postgres_db")

# Disable SQLAlchemy event system to improve performance
SQLALCHEMY_TRACK_MODIFICATIONS = False