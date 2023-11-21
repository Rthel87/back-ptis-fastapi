"""create profesores table

Revision ID: 83522d08bb32
Revises: 57f2390b51a3
Create Date: 2023-11-17 03:02:45.720743

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '83522d08bb32'
down_revision: Union[str, None] = '57f2390b51a3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('profesores',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('usuario_id', sa.BigInteger(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('NOW()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('NOW()'), nullable=False),
    sa.ForeignKeyConstraint(['usuario_id'], ['usuarios.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_profesores_id'), 'profesores', ['id'], unique=False)


def downgrade() -> None:
    op.drop_index(op.f('ix_profesores_id'), table_name='profesores')
    op.drop_table('profesores')
