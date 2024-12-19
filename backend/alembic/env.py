from logging.config import fileConfig
from app.models import Base
from dotenv import load_dotenv
import os

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context

# Loading environment variables
load_dotenv()

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Setting the connection string
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")
if not SQLALCHEMY_DATABASE_URL:
    raise RuntimeError("DATABASE_URL is not set in the environment variables.")
config.set_main_option("sqlalchemy.url", SQLALCHEMY_DATABASE_URL)

# Interpreting the configuration file for the Python logger
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Adding model metadata
target_metadata = Base.metadata


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

    print("Migrations ran successfully in offline mode.")


def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            render_as_batch=True,
        )

        with context.begin_transaction():
            context.run_migrations()

    print("Migrations ran successfully in online mode.")


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
