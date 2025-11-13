from dotenv import load_dotenv
load_dotenv()
import os
import dataclasses


@dataclasses.dataclass
class User:
    email: str
    password: str


admin = User(
    email=os.getenv("LOGIN_ADMIN"),
    password=os.getenv("PASSWORD_ADMIN")
)

guest = User(
    email=os.getenv("LOGIN_USER"),
    password=os.getenv("PASSWORD_USER")
)
