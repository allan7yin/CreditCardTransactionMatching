"""2: Added relationships for tables

Revision ID: 962c9d8b39ed
Revises: 3906031c3328
Create Date: 2024-03-26 19:32:09.640921

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "962c9d8b39ed"
down_revision: Union[str, None] = "3906031c3328"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
