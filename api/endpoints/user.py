import datetime

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session
from passlib.context import CryptContext

import bcrypt


from db.config import get_db
from models import UserModel
from schemas.user import UserCreate, UserLogin

user_router = APIRouter(prefix="/user")

SECRET_KEY = "09d25e094faagjengjeodjtjgkrhf7099f6f0f4caa6cf63b88e8d3e7"
TOKEN_EXPIRE_MINUTES = 60


@user_router.get("")
def api_getuser(db: Session = Depends(get_db)):
    try:
        query = select(UserModel)
        user_list = db.execute(query).all()

        return {"abc": user_list}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")


@user_router.post("/signup")
def sign_up(user: UserCreate,db: Session = Depends(get_db)):
    try:
        query = select(UserModel).filter(UserModel.email == user.email)
        existing_user = db.execute(query).all()

        if len(existing_user):
            raise HTTPException(status_code=400, detail="Email Already registered")

        new_user = UserModel(
            username=user.email,
            email=user.email,
            password=hash_password(user.password)
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        return {"message": "User created successfully" }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")


@user_router.post("/login")
def login(user: UserLogin,db: Session = Depends(get_db)):
    try:
        query = select(UserModel).filter(UserModel.email == user.email)
        existing_user = db.execute(query).all()

        if not len(existing_user):
            raise HTTPException(status_code=404, detail="User Not Found")

        existing_user = existing_user[0][0]

        if not verify_password(user.password, existing_user.password):
            raise HTTPException(status_code=400, detail="Password does not match")

        access_token = create_access_token({"sub": existing_user.email})

        return {"access_token": access_token}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

def hash_password(password):
  """
  Hashes a password using bcrypt, a strong password hashing algorithm.

  Args:
    password: The plaintext password to hash.

  Returns:
    A bcrypt-hashed password (a string).
  """
  # Convert the password to bytes
  password_bytes = password.encode('utf-8')

  # Generate a salt (random data)
  salt = bcrypt.gensalt()

  # Hash the password using the salt
  hashed_password = bcrypt.hashpw(password_bytes, salt)

  # Return the hashed password as a string
  return hashed_password.decode('utf-8')

def verify_password(password, stored_hash):
    """
    Verifies a password against a stored hash using bcrypt.

    Args:
        password: The plaintext password to verify.
        stored_hash: The stored hash to compare against.

    Returns:
        True if the password matches the hash, False otherwise.
    """
    return bcrypt.checkpw(password.encode('utf-8'), stored_hash.encode('utf-8'))


def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.datetime.utcnow() + datetime.timedelta(minutes=TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm="HS256")


def decode_access_token(token : str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return {"email": payload.get("sub")}

    except Exception as e:
        return None

