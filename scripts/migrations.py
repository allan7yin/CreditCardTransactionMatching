# run_migrations.py
from alembic import command
from alembic.config import Config


def start():
    print("Hello")


def main(migration_message):
    alembic_cfg = Config("alembic.ini")

    # Generate a new migration with the provided message
    command.revision(alembic_cfg, message=migration_message, autogenerate=True)

    # Upgrade the database to the latest version
    command.upgrade(alembic_cfg, "head")


if __name__ == "__main__":
    import sys

    # Get the migration message from the command-line arguments
    migration_message = sys.argv[1] if len(sys.argv) > 1 else None

    # Check if a migration message was provided
    if not migration_message:
        print("Error: Please provide a migration message as an argument.")
        sys.exit(1)

    # Run migrations with the provided message
    main(migration_message)
