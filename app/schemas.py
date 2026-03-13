from datetime import datetime
from typing import Optional, Annotated
from pydantic import BaseModel, EmailStr, Field
from pydantic.types import conint

class PostBase(BaseModel):
  title: str
  content: str
  published: bool = True

class PostCreate(PostBase):
  pass

class UserOut(BaseModel):
  id: int
  email: EmailStr
  created_at: datetime

  class Config:
    # orm_mode = True
    from_attributes = True

class Post(PostBase):
  id: int
  created_at: datetime
  owner_id: int
  owner: UserOut

  class Config:
    # orm_mode = True
    from_attributes = True

class PostOut(BaseModel):
  Post: Post
  votes: int

  class Config:
    from_attributes = True

class UserCreate(BaseModel):
  email: EmailStr
  password: str

class UserUpdate(BaseModel):
  email: Optional[EmailStr] = None
  phone_number: Optional[str] = None

class ChangePassword(BaseModel):
  old_password: str
  new_password: str

class UserLogin(BaseModel):
  email: EmailStr
  password: str

class Token(BaseModel):
  access_token: str
  token_type: str

class TokenData(BaseModel):
  id: Optional[str] = None

class Vote(BaseModel):
  post_id: int
  dir: Annotated[int, Field(ge=0, le=1)]
  