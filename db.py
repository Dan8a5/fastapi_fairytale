from sqlmodel import SQLModel, create_engine, SQLModel, Session

DATABASE_URL = "postgresql://postgres.shlpxirwffgjdudmxkuo:week6codeschool@aws-0-us-east-1.pooler.supabase.com:6543/postgres"
engine = create_engine(DATABASE_URL, echo=True)

def init_db():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session