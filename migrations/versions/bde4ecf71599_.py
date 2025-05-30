"""empty message

Revision ID: bde4ecf71599
Revises: 
Create Date: 2025-04-30 14:15:07.304681

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bde4ecf71599'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('mensagem',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('conteudo', sa.String(length=500), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('mensagem')
    # ### end Alembic commands ###
