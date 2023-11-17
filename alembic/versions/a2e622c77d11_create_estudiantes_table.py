"""create estudiantes table

Revision ID: a2e622c77d11
Revises: 83522d08bb32
Create Date: 2023-11-17 03:03:05.915046

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a2e622c77d11'
down_revision: Union[str, None] = '83522d08bb32'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('estudiantes',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('iniciales', sa.String(), nullable=True),
    sa.Column('usuario_id', sa.BigInteger(), nullable=True),
    sa.Column('grupo_id', sa.BigInteger(), nullable=True),
    sa.Column('seccion_id', sa.BigInteger(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('NOW()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('NOW()'), nullable=False),
    sa.ForeignKeyConstraint(['grupo_id'], ['grupos.id'], ),
    sa.ForeignKeyConstraint(['seccion_id'], ['secciones.id'], ),
    sa.ForeignKeyConstraint(['usuario_id'], ['usuarios.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_estudiantes_id'), 'estudiantes', ['id'], unique=False)
    op.create_index(op.f('ix_estudiantes_iniciales'), 'estudiantes', ['iniciales'], unique=False)


def downgrade() -> None:
    op.drop_index(op.f('ix_estudiantes_iniciales'), table_name='estudiantes')
    op.drop_index(op.f('ix_estudiantes_id'), table_name='estudiantes')
    op.drop_table('estudiantes')
