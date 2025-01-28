from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import engine , Base , SessionLocal
from models import  User
import auth
from fastapi.middleware.cors import CORSMiddleware


Base.metadata.create_all(bind=engine)

app = FastAPI()

# Configure CORS
origins = [
    "http://localhost:8080",  # Address of your frontend
]


db = SessionLocal()


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.post("/signup")
async def signup(user: auth.UserCreate):
    print(user.username, user.password, user.email)
    hashed_password = auth.get_password_hash(user.password)
    new_user = User(username=user.username, password_hash=hashed_password, emails=user.email)
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"msg": "User created successfully"}


# @app.post("/login")
# async def login(username: str, password: str, db: Session = Depends(get_db)):
#     user = db.query(User).filter(User.username == username).first()
    
#     if not user or not auth.verify_password(password, user.hashed_password):
#         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
#                             detail="Incorrect username or password")
    
#     access_token = auth.create_access_token(data={"sub": user.username})
    
#     return {"access_token": access_token, "token_type": "bearer"}


