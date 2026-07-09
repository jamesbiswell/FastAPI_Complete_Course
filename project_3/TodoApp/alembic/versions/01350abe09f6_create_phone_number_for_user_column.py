"""Create phone number for user column

Revision ID: 01350abe09f6
Revises: 
Create Date: 2026-07-09 15:01:23.593845

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '01350abe09f6'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('users', sa.Column('phone_number', sa.String(20), nullable = True))


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('users', 'phone_number')
