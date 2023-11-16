"""create roles table

Revision ID: 818ba4254403
Revises:
Create Date: 2023-11-15 01:50:56.034545

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy import text


# revision identifiers, used by Alembic.
revision: str = '818ba4254403'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'roles',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('rol', sa.String, nullable=False),
        sa.Column('rango', sa.Integer, unique=True, nullable=False),
        sa.Column('borrado', sa.Boolean, default=False),
        sa.Column('created_at', sa.DateTime, server_default=text('NOW()')),
        sa.Column('updated_at', sa.DateTime, server_default=text('NOW()')),
        sa.Column('deleted_at', sa.DateTime)
    )


def downgrade() -> None:
    op.drop_table('roles')
