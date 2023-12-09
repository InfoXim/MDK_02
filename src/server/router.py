from src.server.database import models as database_models
from src.server.database import pydantic_models
from src.server.service import RouterManager

router_clients = RouterManager(
    database_model=database_models.Clients,
    pydantic_model=pydantic_models.Clients,
    prefix='/clients',
    tags=['Clients']
).fastapi_router

router_orders = RouterManager(
    database_model=database_models.Orders,
    pydantic_model=pydantic_models.Orders,
    prefix='/orders',
    tags=['Orders']
).fastapi_router

router_employees = RouterManager(
    database_model=database_models.Employees,
    pydantic_model=pydantic_models.Employees,
    prefix='/employees',
    tags=['Employees']
).fastapi_router

router_services = RouterManager(
    database_model=database_models.Services,
    pydantic_model=pydantic_models.Services,
    prefix='/services',
    tags=['Services']
).fastapi_router

router_inventory = RouterManager(
    database_model=database_models.Inventory,
    pydantic_model=pydantic_models.Inventory,
    prefix='/inventory',
    tags=['Inventory']
).fastapi_router

router_jobs = RouterManager(
    database_model=database_models.Jobs,
    pydantic_model=pydantic_models.Jobs,
    prefix='/jobs',
    tags=['Jobs']
).fastapi_router

router_payments = RouterManager(
    database_model=database_models.Payments,
    pydantic_model=pydantic_models.Payments,
    prefix='/payments',
    tags=['Payments']
).fastapi_router

router_reviews = RouterManager(
    database_model=database_models.Reviews,
    pydantic_model=pydantic_models.Reviews,
    prefix='/reviews',
    tags=['Reviews']
).fastapi_router

router_job_types = RouterManager(
    database_model=database_models.JobTypes,
    pydantic_model=pydantic_models.JobTypes,
    prefix='/job_types',
    tags=['JobTypes']
).fastapi_router

router_materials = RouterManager(
    database_model=database_models.Materials,
    pydantic_model=pydantic_models.Materials,
    prefix='/materials',
    tags=['Materials']
).fastapi_router

router_job_type_assignments = RouterManager(
    database_model=database_models.JobTypeAssignments,
    pydantic_model=pydantic_models.JobTypeAssignments,
    prefix='/job_type_assignments',
    tags=['JobTypeAssignments']
).fastapi_router

router_material_assignments = RouterManager(
    database_model=database_models.MaterialAssignments,
    pydantic_model=pydantic_models.MaterialAssignments,
    prefix='/material_assignments',
    tags=['MaterialAssignments']
).fastapi_router

# Список роутеров
routers = (
    router_clients,
    router_orders,
    router_employees,
    router_services,
    router_inventory,
    router_jobs,
    router_payments,
    router_reviews,
    router_job_types,
    router_materials,
    router_job_type_assignments,
    router_material_assignments,
)