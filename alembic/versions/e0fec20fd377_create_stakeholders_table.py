"""create stakeholders table

Revision ID: e0fec20fd377
Revises: b6e3c68c3bad
Create Date: 2023-11-17 02:54:56.842133

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e0fec20fd377'
down_revision: Union[str, None] = 'b6e3c68c3bad'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('stakeholders',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('iniciales', sa.String(), nullable=True),
    sa.Column('usuario_id', sa.BigInteger(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('NOW()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('NOW()'), nullable=False),
    sa.ForeignKeyConstraint(['usuario_id'], ['usuarios.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_stakeholders_id'), 'stakeholders', ['id'], unique=False)
    op.create_index(op.f('ix_stakeholders_iniciales'), 'stakeholders', ['iniciales'], unique=False)


def downgrade() -> None:
    op.drop_index(op.f('ix_stakeholders_iniciales'), table_name='stakeholders')
    op.drop_index(op.f('ix_stakeholders_id'), table_name='stakeholders')
    op.drop_table('stakeholders')
