"""empty message

Revision ID: 265d5533c50f
Revises: 509bb09194c0
Create Date: 2021-04-04 11:54:18.854162

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '265d5533c50f'
down_revision = '509bb09194c0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('question', schema=None) as batch_op:
        batch_op.drop_column('user_id')

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('password',
               existing_type=sa.VARCHAR(length=150),
               nullable=False)
        batch_op.create_unique_constraint(batch_op.f('uq_user_email'), ['email'])
        batch_op.create_unique_constraint(batch_op.f('uq_user_username'), ['username'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('uq_user_username'), type_='unique')
        batch_op.drop_constraint(batch_op.f('uq_user_email'), type_='unique')
        batch_op.alter_column('password',
               existing_type=sa.VARCHAR(length=150),
               nullable=True)

    with op.batch_alter_table('question', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.INTEGER(), server_default=sa.text("'1'"), nullable=True))

    # ### end Alembic commands ###
