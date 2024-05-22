"""first migrations

Revision ID: 3906031c3328
Revises: 724f27d12e89
Create Date: 2024-03-24 16:16:56.375807

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "3906031c3328"
down_revision: Union[str, None] = "724f27d12e89"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
