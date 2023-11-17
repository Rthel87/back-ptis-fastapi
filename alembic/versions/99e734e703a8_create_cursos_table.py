"""create cursos table

Revision ID: 99e734e703a8
Revises: f788889fa01b
Create Date: 2023-11-17 03:02:32.969469

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '99e734e703a8'
down_revision: Union[str, None] = 'f788889fa01b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('cursos',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('nombre', sa.String(), nullable=True),
    sa.Column('codigo', sa.String(), unique=True, nullable=True),
    sa.Column('borrado', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('NOW()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('NOW()'), nullable=True),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_cursos_codigo'), 'cursos', ['codigo'], unique=True)
    op.create_index(op.f('ix_cursos_id'), 'cursos', ['id'], unique=False)
    op.create_index(op.f('ix_cursos_nombre'), 'cursos', ['nombre'], unique=False)


def downgrade() -> None:
    op.drop_index(op.f('ix_cursos_nombre'), table_name='cursos')
    op.drop_index(op.f('ix_cursos_id'), table_name='cursos')
    op.drop_index(op.f('ix_cursos_codigo'), table_name='cursos')
    op.drop_table('cursos')
