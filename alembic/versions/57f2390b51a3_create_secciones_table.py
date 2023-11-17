"""create secciones table

Revision ID: 57f2390b51a3
Revises: 99e734e703a8
Create Date: 2023-11-17 03:02:39.236505

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '57f2390b51a3'
down_revision: Union[str, None] = '99e734e703a8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('secciones',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('codigo', sa.String(), unique=True, nullable=True),
    sa.Column('borrado', sa.Boolean(), nullable=True),
    sa.Column('jornada_id', sa.BigInteger(), nullable=True),
    sa.Column('semestre_id', sa.BigInteger(), nullable=True),
    sa.Column('curso_id', sa.BigInteger(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('NOW()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('NOW()'), nullable=False),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['curso_id'], ['cursos.id'], ),
    sa.ForeignKeyConstraint(['jornada_id'], ['jornadas.id'], ),
    sa.ForeignKeyConstraint(['semestre_id'], ['semestres.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # op.create_index(op.f('ix_secciones_codigo'), 'secciones', ['codigo'], unique=True)
    op.create_index(op.f('ix_secciones_id'), 'secciones', ['id'], unique=False)


def downgrade() -> None:
    op.drop_index(op.f('ix_secciones_id'), table_name='secciones')
    # op.drop_index(op.f('ix_secciones_codigo'), table_name='secciones')
    op.drop_table('secciones')
