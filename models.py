from sqlalchemy import orm
from sqlalchemy import Column, Integer, String, Boolean, Numeric, JSON, Date
from sqlalchemy import create_engine

Base = orm.declarative_base()

class Rocket(Base):
    __tablename__ = 'rocket'
    id = Column(String, primary_key=True)
    name = Column(String)
    type = Column(String)
    active = Column(Boolean)
    boosters = Column(Integer)
    company = Column(String)
    cost_per_launch = Column(Integer)
    country = Column(String)
    description = Column(String)
    diameter_meters = Column(Numeric)
    height_meters = Column(Numeric)
    mass_kg = Column(Integer)
    engines = Column(JSON, default={})
    first_flight = Column(Date)
    stages = Column(Integer)
    first_stage_burn_time_sec = Column(Integer)
    first_stage_engines = Column(Integer)
    first_stage_fuel_amount_tons = Column(Numeric)
    first_stage_reusable = Column(Boolean)
    first_stage_thrust_sea_level_kn = Column(Numeric)
    first_stage_thrust_vacuum_kn = Column(Numeric)
    second_stage_burn_time_sec = Column(Integer)
    second_stage_engines = Column(Integer)
    second_stage_fuel_amount_tons = Column(Numeric)
    second_stage_thrust_kn = Column(Numeric)
    second_stage_payloads_composite_fairing_diameter_meters = Column(Numeric)
    second_stage_payloads_composite_fairing_height_meters = Column(Numeric)
    second_stage_payloads_option_1 = Column(String)
    success_rate_pct = Column(Integer)
    landing_legs_material = Column(String)
    landing_legs_number = Column(Integer)
    wikipedia = Column(String)
    payload_weights = Column(JSON, default={})

def create_tables(db: str):
    engine = create_engine(db)
    Base.metadata.create_all(engine)
    print('Tables created')