"""create usuarios table

Revision ID: 33702a0f197e
Revises: 818ba4254403
Create Date: 2023-11-15 01:56:00.565730

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy import text


# revision identifiers, used by Alembic.
revision: str = '33702a0f197e'
down_revision: Union[str, None] = '818ba4254403'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'usuarios',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('nombre', sa.String),
        sa.Column('apellido_paterno', sa.String),
        sa.Column('apellido_materno', sa.String),
        sa.Column('run', sa.String),
        sa.Column('correo_elec', sa.String, unique=True),
        sa.Column('password', sa.String),
        sa.Column('borrado', sa.Boolean),
        sa.Column('created_at', sa.DateTime, server_default=text('NOW()')),
        sa.Column('updated_at', sa.DateTime, server_default=text('NOW()')),
        sa.Column('deleted_at', sa.DateTime)
    )


def downgrade() -> None:
    op.drop_table('usuarios')
