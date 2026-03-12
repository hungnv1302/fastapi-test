"""add content column to posts table

Revision ID: d19675e7ed04
Revises: dac4c8b94471
Create Date: 2026-03-12 18:26:05.035995

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd19675e7ed04'
down_revision: Union[str, Sequence[str], None] = 'dac4c8b94471'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column("posts", "content")
    pass
