from sqlalchemy import Column, Integer, String, Float, Boolean
from app.core.database import Base

class Target(Base):
    __tablename__ = "targets"

    id = Column(Integer, primary_key=True, index=True)
    
    # Catalog identifiers
    name = Column(String, index=True)           # Common name e.g. "Andromeda Galaxy"
    messier_id = Column(String, nullable=True)  # e.g. "M31"
    ngc_id = Column(String, nullable=True)      # e.g. "NGC 224"
    
    # Sky coordinates
    ra = Column(Float)                          # Right Ascension (degrees)
    dec = Column(Float)                         # Declination (degrees)
    
    # Object properties
    object_type = Column(String)                # galaxy, nebula, cluster, etc
    constellation = Column(String)
    magnitude = Column(Float, nullable=True)    # Brightness
    distance_ly = Column(Float, nullable=True)  # Distance in light years
    
    # Description
    description = Column(String, nullable=True)
    
    # Flags
    is_messier = Column(Boolean, default=False)
    is_ngc = Column(Boolean, default=False)