"""empty message

Revision ID: b165fe1df3e3
Revises: e261ec3be283
Create Date: 2021-04-04 11:47:16.844219

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b165fe1df3e3'
down_revision = 'e261ec3be283'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('question', 'user_id')
    op.alter_column('user', 'password',
               existing_type=sa.VARCHAR(length=150),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'password',
               existing_type=sa.VARCHAR(length=150),
               nullable=True)
    op.add_column('question', sa.Column('user_id', sa.INTEGER(), server_default=sa.text("'1'"), nullable=True))
    # ### end Alembic commands ###
