from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Float
from sqlalchemy import String
from sqlalchemy import DateTime

from datetime import datetime

from database import Base


class OceanData(Base):

    __tablename__ = "ocean_data"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    location = Column(
        String,
        nullable=False
    )

    temperature = Column(
        Float,
        nullable=False
    )

    salinity = Column(
        Float,
        nullable=False
    )

    turbidity = Column(
        Float,
        nullable=False
    )

    chlorophyll = Column(
        Float,
        nullable=False
    )

    ph = Column(
        Float,
        nullable=False
    )

    recorded_at = Column(
        DateTime,
        default=datetime.utcnow
    )