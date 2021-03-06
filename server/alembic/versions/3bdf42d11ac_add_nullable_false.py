"""add nullable false

Revision ID: 3bdf42d11ac
Revises: 11a699ed152
Create Date: 2015-11-03 01:49:46.668458

"""

# revision identifiers, used by Alembic.
revision = '3bdf42d11ac'
down_revision = '11a699ed152'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('file', 'task_id',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=False)
    op.alter_column('task', 'name',
               existing_type=mysql.VARCHAR(length=1024),
               nullable=False)
    op.alter_column('user', 'date',
               existing_type=sa.DATE(),
               nullable=False)
    op.alter_column('user', 'src_ip',
               existing_type=mysql.VARCHAR(length=15),
               nullable=False)
    op.alter_column('visit', 'timestamp',
               existing_type=mysql.DATETIME(),
               nullable=False)
    op.alter_column('visit', 'user_id',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=False)
    op.alter_column('visit', 'web_id',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=False)
    op.alter_column('web', 'http_status',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=False)
    op.alter_column('web', 'task_id',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=False)
    op.alter_column('web', 'url',
               existing_type=mysql.TEXT(),
               nullable=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('web', 'url',
               existing_type=mysql.TEXT(),
               nullable=True)
    op.alter_column('web', 'task_id',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.alter_column('web', 'http_status',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.alter_column('visit', 'web_id',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.alter_column('visit', 'user_id',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.alter_column('visit', 'timestamp',
               existing_type=mysql.DATETIME(),
               nullable=True)
    op.alter_column('user', 'src_ip',
               existing_type=mysql.VARCHAR(length=15),
               nullable=True)
    op.alter_column('user', 'date',
               existing_type=sa.DATE(),
               nullable=True)
    op.alter_column('task', 'name',
               existing_type=mysql.VARCHAR(length=1024),
               nullable=True)
    op.alter_column('file', 'task_id',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    ### end Alembic commands ###
