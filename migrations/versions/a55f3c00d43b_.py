"""empty message

Revision ID: a55f3c00d43b
Revises: 265d5533c50f
Create Date: 2021-04-04 11:55:38.346393

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a55f3c00d43b'
down_revision = '265d5533c50f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('question', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.Integer(), nullable=False))
        batch_op.create_foreign_key(batch_op.f('fk_question_user_id_user'), 'user', ['user_id'], ['id'], ondelete='CASCADE')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('question', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_question_user_id_user'), type_='foreignkey')
        batch_op.drop_column('user_id')

    # ### end Alembic commands ###
