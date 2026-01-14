from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app import models
from passlib.context import CryptContext

# Password hashing 
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify a password against its hash."""
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    """Hash a password - let passlib handle any truncation internally."""
    return pwd_context.hash(password)

def get_users(db: Session, skip: int = 0, limit: int = 100):
    """Get all users with pagination."""
    return db.query(models.User).offset(skip).limit(limit).all()

def get_user_by_id(db: Session, user_id: int):
    """Get a user by ID."""
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_username(db: Session, username: str):
    """Get a user by username."""
    return db.query(models.User).filter(models.User.username == username).first()

def get_user_by_email(db: Session, email: str):
    """Get a user by email."""
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: Session, user_data):
    """Create a new user with hashed password."""
    # Check if username or email already exists
    if get_user_by_username(db, user_data.username):
        raise ValueError("Username already exists")
    
    if get_user_by_email(db, user_data.email):
        raise ValueError("Email already exists")
    
    # Create user with hashed password
    db_user = models.User(
        username=user_data.username,
        email=user_data.email,
        full_name=user_data.full_name,
        hashed_password=get_password_hash(user_data.password)
    )
    
    try:
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    except IntegrityError:
        db.rollback()
        raise ValueError("User with this username or email already exists")

def delete_user(db: Session, user_id: int):
    """Delete a user by ID."""
    user = get_user_by_id(db, user_id)
    if not user:
        return None
    
    db.delete(user)
    db.commit()
    return user

def update_user(db: Session, user_id: int, user_update):
    """Update user information."""
    user = get_user_by_id(db, user_id)
    if not user:
        return None
    
    # Check for duplicate username (if username is being updated)
    if hasattr(user_update, 'username') and user_update.username and user_update.username != user.username:
        if get_user_by_username(db, user_update.username):
            raise ValueError("Username already exists")
    
    # Check for duplicate email (if email is being updated)
    if hasattr(user_update, 'email') and user_update.email and user_update.email != user.email:
        if get_user_by_email(db, user_update.email):
            raise ValueError("Email already exists")
    
    # Update fields
    if hasattr(user_update, 'username') and user_update.username is not None:
        user.username = user_update.username
    if hasattr(user_update, 'email') and user_update.email is not None:
        user.email = user_update.email
    if hasattr(user_update, 'full_name') and user_update.full_name is not None:
        user.full_name = user_update.full_name
    if hasattr(user_update, 'password') and user_update.password:
        user.hashed_password = get_password_hash(user_update.password)
    
    try:
        db.commit()
        db.refresh(user)
        return user
    except IntegrityError:
        db.rollback()
        raise ValueError("Update failed due to constraint violation")
