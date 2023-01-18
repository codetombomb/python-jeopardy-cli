"""Add daily_double column, game_round column - update question to clue and answer to response

Revision ID: ed7e018608fd
Revises: 13612e1c2aa8
Create Date: 2023-01-18 14:52:36.159731

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import String, Boolean


# revision identifiers, used by Alembic.
revision = 'ed7e018608fd'
down_revision = '13612e1c2aa8'
branch_labels = None
depends_on = None


def upgrade() -> None:
    sa.Column("daily_double", Boolean(), nullable=False, default=False)
    sa.Column("game_round", String(), nullable=False )
    
    op.alter_column("questions", "question", new_column_name="clue")
    op.alter_column("questions", "answer", new_column_name="response")


def downgrade() -> None:
    op.drop_column("questions", "daily_double")
    op.drop_column("questions", "game_round")
    
    op.alter_column("questions", "clue", nullable=False, new_column_name="question")
    op.alter_column("questions", "response", nullable=False, new_column_name="answer")
