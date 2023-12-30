"""Renaming students to scholars

Revision ID: 5d86f1707cd1
Revises: 791279dd0760
Create Date: 2023-12-30 12:06:25.930043

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5d86f1707cd1'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
   op.rename_table('scholars', 'students')
