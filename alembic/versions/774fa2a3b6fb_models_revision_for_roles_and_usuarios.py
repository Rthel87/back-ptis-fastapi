"""Models revision for roles and usuarios

Revision ID: 774fa2a3b6fb
Revises: 33702a0f197e
Create Date: 2023-11-17 02:38:39.746646

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '774fa2a3b6fb'
down_revision: Union[str, None] = '33702a0f197e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('roles', 'id',
               existing_type=sa.INTEGER(),
               type_=sa.BigInteger(),
               existing_nullable=False) #,
               # autoincrement=True)
    op.alter_column('roles', 'rol',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('roles', 'rango',
               existing_type=sa.INTEGER(),
               nullable=True)
    # op.drop_constraint('roles_rango_key', 'roles', type_='unique')
    op.create_index(op.f('ix_roles_id'), 'roles', ['id'], unique=False)
    # op.create_index(op.f('ix_roles_rango'), 'roles', ['rango'], unique=True)
    op.create_index(op.f('ix_roles_rol'), 'roles', ['rol'], unique=False)
    op.add_column('usuarios', sa.Column('rol_id', sa.BigInteger(), nullable=True))
    op.alter_column('usuarios', 'id',
               existing_type=sa.INTEGER(),
               type_=sa.BigInteger(),
               existing_nullable=False) #,
               # autoincrement=True)
    # op.drop_constraint('usuarios_correo_elec_key', 'usuarios', type_='unique')
    op.create_index(op.f('ix_usuarios_apellido_materno'), 'usuarios', ['apellido_materno'], unique=False)
    op.create_index(op.f('ix_usuarios_apellido_paterno'), 'usuarios', ['apellido_paterno'], unique=False)
    # op.create_index(op.f('ix_usuarios_correo_elec'), 'usuarios', ['correo_elec'], unique=True)
    op.create_index(op.f('ix_usuarios_id'), 'usuarios', ['id'], unique=False)
    op.create_index(op.f('ix_usuarios_nombre'), 'usuarios', ['nombre'], unique=False)
    op.create_index(op.f('ix_usuarios_run'), 'usuarios', ['run'], unique=False)
    op.create_foreign_key(None, 'usuarios', 'roles', ['rol_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    # op.drop_constraint(None, 'usuarios', type_='foreignkey')
    op.drop_index(op.f('ix_usuarios_run'), table_name='usuarios')
    op.drop_index(op.f('ix_usuarios_nombre'), table_name='usuarios')
    op.drop_index(op.f('ix_usuarios_id'), table_name='usuarios')
    # op.drop_index(op.f('ix_usuarios_correo_elec'), table_name='usuarios')
    op.drop_index(op.f('ix_usuarios_apellido_paterno'), table_name='usuarios')
    op.drop_index(op.f('ix_usuarios_apellido_materno'), table_name='usuarios')
    # op.create_unique_constraint('usuarios_correo_elec_key', 'usuarios', ['correo_elec'])
    op.alter_column('usuarios', 'id',
               existing_type=sa.BigInteger(),
               type_=sa.INTEGER(),
               existing_nullable=False) #,
               # autoincrement=True)
    op.drop_column('usuarios', 'rol_id')
    op.drop_index(op.f('ix_roles_rol'), table_name='roles')
    # op.drop_index(op.f('ix_roles_rango'), table_name='roles')
    op.drop_index(op.f('ix_roles_id'), table_name='roles')
    # op.create_unique_constraint('roles_rango_key', 'roles', ['rango'])
    op.alter_column('roles', 'rango',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('roles', 'rol',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('roles', 'id',
               existing_type=sa.BigInteger(),
               type_=sa.INTEGER(),
               existing_nullable=False) #,
               # autoincrement=True)
    # ### end Alembic commands ###
