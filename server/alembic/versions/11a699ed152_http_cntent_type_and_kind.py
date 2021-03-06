"""http cntent type and kind

Revision ID: 11a699ed152
Revises: 33bd8a99c52
Create Date: 2015-10-31 13:10:30.219418

"""

# revision identifiers, used by Alembic.
revision = '11a699ed152'
down_revision = '33bd8a99c52'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('task', sa.Column('kind', sa.String(length=128), nullable=True))
    op.create_index(op.f('ix_task_kind'), 'task', ['kind'], unique=False)
    op.add_column('web', sa.Column('content_length', sa.Integer(), nullable=True))
    op.add_column('web', sa.Column('content_type', sa.String(length=128), nullable=True))
    op.add_column('web', sa.Column('kind', sa.String(length=128), nullable=True))
    op.create_index(op.f('ix_web_content_type'), 'web', ['content_type'], unique=False)
    op.create_index(op.f('ix_web_kind'), 'web', ['kind'], unique=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_web_kind'), table_name='web')
    op.drop_index(op.f('ix_web_content_type'), table_name='web')
    op.drop_column('web', 'kind')
    op.drop_column('web', 'content_type')
    op.drop_column('web', 'content_length')
    op.drop_index(op.f('ix_task_kind'), table_name='task')
    op.drop_column('task', 'kind')
    ### end Alembic commands ###
