"""Add cb_game_id to Question model

Revision ID: 13612e1c2aa8
Revises: f21ce0b7ddc4
Create Date: 2023-01-18 14:28:17.588123

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import Column, Integer


# revision identifiers, used by Alembic.
revision = '13612e1c2aa8'
down_revision = 'f21ce0b7ddc4'
branch_labels = None
depends_on = None


def upgrade() -> None:
    sa.Column('cb_game_id', Integer(), nullable=False)


def downgrade() -> None:
    op.drop_column("questions", "cb_game_id")
