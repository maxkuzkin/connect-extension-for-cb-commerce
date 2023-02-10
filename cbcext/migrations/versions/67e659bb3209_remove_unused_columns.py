"""remove unused columns

Revision ID: 67e659bb3209
Revises: 505535721e47
Create Date: 2023-02-09 14:29:27.415387

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '67e659bb3209'
down_revision = '505535721e47'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('configuration', 'api_url')
    op.drop_column('configuration', 'provider_api_key')
    op.drop_column('configuration', 'api_key')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        'configuration',
        sa.Column(
            'api_key',
            sa.VARCHAR(length=100),
            autoincrement=False,
            nullable=True,
        ),
    )
    op.add_column(
        'configuration',
        sa.Column(
            'provider_api_key',
            sa.VARCHAR(length=100),
            autoincrement=False,
            nullable=True,
        ),
    )
    op.add_column(
        'configuration',
        sa.Column(
            'api_url',
            sa.VARCHAR(length=100),
            autoincrement=False,
            nullable=True,
        ),
    )
    # ### end Alembic commands ###
