from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class BaseModelModify(BaseModel):
    id: Optional[int] = 1


class Clients(BaseModelModify):
    FirstName: str
    LastName: str
    PhoneNumber: str
    Email: str
    Address: str


class Orders(BaseModelModify):
    ClientID: int
    OrderDate: datetime
    TotalAmount: float
    Status: str


class Employees(BaseModelModify):
    FirstName: str
    LastName: str
    PhoneNumber: str
    Email: str
    Position: str
    Salary: float


class Services(BaseModelModify):
    ServiceName: str
    Description: str
    Price: float


class Inventory(BaseModelModify):
    ItemName: str
    Quantity: int
    Price: float


class Jobs(BaseModelModify):
    OrderID: int
    ServiceID: int
    EmployeeID: int
    StartTime: datetime
    EndTime: datetime


class Payments(BaseModelModify):
    OrderID: int
    Amount: float
    PaymentDate: datetime


class Reviews(BaseModelModify):
    OrderID: int
    Rating: int
    Comment: str


class JobTypes(BaseModelModify):
    TypeName: str
    Description: str


class Materials(BaseModelModify):
    MaterialName: str
    Quantity: int
    Price: float


class JobTypeAssignments(BaseModelModify):
    JobID: int
    JobTypeID: int


class MaterialAssignments(BaseModelModify):
    JobID: int
    MaterialID: int
    Quantity: int
