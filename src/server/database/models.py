from peewee import Model, SqliteDatabase, CharField, IntegerField, FloatField, DateTimeField, ForeignKeyField
import datetime


db = SqliteDatabase('database.db')


class BaseModel(Model):
    class Meta:
        database = db


class Clients(BaseModel):
    ClientID = IntegerField(primary_key=True)
    FirstName = CharField(default='')
    LastName = CharField(default='')
    PhoneNumber = CharField(default='')
    Email = CharField(default='')
    Address = CharField(default='')


class Orders(BaseModel):
    OrderID = IntegerField(primary_key=True)
    ClientID = ForeignKeyField(Clients, backref='orders')
    OrderDate = DateTimeField(default='')
    TotalAmount = FloatField(default=0.0)
    Status = CharField(default='')


class Employees(BaseModel):
    EmployeeID = IntegerField(primary_key=True)
    FirstName = CharField(default='')
    LastName = CharField(default='')
    PhoneNumber = CharField(default='')
    Email = CharField(default='')
    Position = CharField(default='')
    Salary = FloatField(default=0.0)


class Services(BaseModel):
    ServiceID = IntegerField(primary_key=True)
    ServiceName = CharField(default='')
    Description = CharField(default='')
    Price = FloatField(default=0.0)


class Inventory(BaseModel):
    InventoryID = IntegerField(primary_key=True)
    ItemName = CharField(default='')
    Quantity = IntegerField(default=0)
    Price = FloatField(default=0.0)


class Jobs(BaseModel):
    JobID = IntegerField(primary_key=True)
    OrderID = ForeignKeyField(Orders, backref='jobs')
    ServiceID = ForeignKeyField(Services, backref='jobs')
    EmployeeID = ForeignKeyField(Employees, backref='jobs')
    StartTime = DateTimeField(default='')
    EndTime = DateTimeField(default='')


class Payments(BaseModel):
    PaymentID = IntegerField(primary_key=True)
    OrderID = ForeignKeyField(Orders, backref='payments')
    Amount = FloatField(default=0.0)
    PaymentDate = DateTimeField(default='')


class Reviews(BaseModel):
    ReviewID = IntegerField(primary_key=True)
    OrderID = ForeignKeyField(Orders, backref='reviews')
    Rating = IntegerField(default=0)
    Comment = CharField(default='')


class JobTypes(BaseModel):
    JobTypeID = IntegerField(primary_key=True)
    TypeName = CharField(default='')
    Description = CharField(default='')


class Materials(BaseModel):
    MaterialID = IntegerField(primary_key=True)
    MaterialName = CharField(default='')
    Quantity = IntegerField(default=0)
    Price = FloatField(default=0.0)


class JobTypeAssignments(BaseModel):
    JobID = ForeignKeyField(Jobs, backref='job_type_assignments')
    JobTypeID = ForeignKeyField(JobTypes, backref='job_type_assignments')


class MaterialAssignments(BaseModel):
    JobID = ForeignKeyField(Jobs, backref='material_assignments')
    MaterialID = ForeignKeyField(Materials, backref='material_assignments')
    Quantity = IntegerField(default=0)


# Создание таблиц в базе данных
db.connect()
db.create_tables([Clients, Orders, Employees, Services, Inventory, Jobs, Payments, Reviews, JobTypes, Materials, JobTypeAssignments, MaterialAssignments])
