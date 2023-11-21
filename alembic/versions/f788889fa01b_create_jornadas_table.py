"""create jornadas table

Revision ID: f788889fa01b
Revises: ea29abee349f
Create Date: 2023-11-17 02:55:20.922786

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f788889fa01b'
down_revision: Union[str, None] = 'ea29abee349f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('jornadas',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('nombre', sa.String(), nullable=True),
    sa.Column('identificador', sa.Integer(), unique=True, nullable=True),
    sa.Column('borrado', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('NOW()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('NOW()'), nullable=False),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_jornadas_id'), 'jornadas', ['id'], unique=False)
    # op.create_index(op.f('ix_jornadas_identificador'), 'jornadas', ['identificador'], unique=True)
    op.create_index(op.f('ix_jornadas_nombre'), 'jornadas', ['nombre'], unique=False)

def downgrade() -> None:
    op.drop_index(op.f('ix_jornadas_nombre'), table_name='jornadas')
    # op.drop_index(op.f('ix_jornadas_identificador'), table_name='jornadas')
    op.drop_index(op.f('ix_jornadas_id'), table_name='jornadas')
    op.drop_table('jornadas')
