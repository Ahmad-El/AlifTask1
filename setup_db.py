from db.models import Base, Cabin
from db.session import engine, SessionLocal

Base.metadata.create_all(bind=engine)

session = SessionLocal()
for i in range(1, 6):
    session.add(Cabin(number=i))
session.commit()
session.close()
