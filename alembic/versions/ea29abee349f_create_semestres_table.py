"""create semestres table

Revision ID: ea29abee349f
Revises: e0fec20fd377
Create Date: 2023-11-17 02:55:12.589159

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ea29abee349f'
down_revision: Union[str, None] = 'e0fec20fd377'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('semestres',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('numero', sa.Integer(), nullable=True),
    sa.Column('agno', sa.Integer(), nullable=True),
    sa.Column('identificador', sa.String(), unique=True, nullable=True),
    sa.Column('activo', sa.Boolean(), nullable=True),
    sa.Column('inicio', sa.Date(), nullable=True),
    sa.Column('fin', sa.Date(), nullable=True),
    sa.Column('borrado', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('NOW()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('NOW()'), nullable=False),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_semestres_agno'), 'semestres', ['agno'], unique=False)
    op.create_index(op.f('ix_semestres_id'), 'semestres', ['id'], unique=False)
    # op.create_index(op.f('ix_semestres_identificador'), 'semestres', ['identificador'], unique=True)
    op.create_index(op.f('ix_semestres_numero'), 'semestres', ['numero'], unique=False)


def downgrade() -> None:
    op.drop_index(op.f('ix_semestres_numero'), table_name='semestres')
    # op.drop_index(op.f('ix_semestres_identificador'), table_name='semestres')
    op.drop_index(op.f('ix_semestres_id'), table_name='semestres')
    op.drop_index(op.f('ix_semestres_agno'), table_name='semestres')
    op.drop_table('semestres')
