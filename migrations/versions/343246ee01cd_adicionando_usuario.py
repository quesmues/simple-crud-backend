"""Adicionando Usuario

Revision ID: 343246ee01cd
Revises: 
Create Date: 2023-06-03 00:10:08.641402

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '343246ee01cd'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('apps_v1_usuario',
    sa.Column('id', sa.String(length=36), nullable=False),
    sa.Column('username', sa.String(length=256), nullable=True),
    sa.Column('password', sa.String(length=256), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('apps_v1_usuario')
    # ### end Alembic commands ###