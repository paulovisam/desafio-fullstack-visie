"""create_table_pessoas

Revision ID: a9363553e9a7
Revises:
Create Date: 2023-11-13 20:59:55.304471
"""
from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = 'a9363553e9a7'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'pessoas',
        sa.Column(
            'id_pessoa', sa.Integer(), autoincrement=True, nullable=False
        ),
        sa.Column('nome', sa.String(100), nullable=False),
        sa.Column('rg', sa.String(100), nullable=False),
        sa.Column('cpf', sa.String(100), nullable=False),
        sa.Column('data_nascimento', sa.Date(), nullable=False),
        sa.Column('data_admissao', sa.Date(), nullable=False),
        sa.Column('funcao', sa.String(100), nullable=True),
        sa.PrimaryKeyConstraint('id_pessoa'),
    )


def downgrade() -> None:
    op.drop_table('pessoas')
