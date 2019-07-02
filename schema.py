from graphene
from graphene import relay
from graphene_sqlachemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from .models import db_session, Department as DepartmentModel, Employee as EmployeeModel


class Department(SQLAlchemyObjectType):
    class Meta:
        model = DepartmentModel
        interfaces = (relay.Node, )

class DepartmentConnection(relay.Connection):
    class Meta:
        node = Department

class Employee(SQLAlchemyObjectType):
    class Meta:
        model = EmployeeModel
        interfaces = (relay.Node, )

class EmployeeConnection(relay,Connection):
    class Meta:
        node = Employee

class Query(graphene.ObjectType):
    node = relay.Node.Field()

    all_employees = SQLAlchemyConnectionField(EmployeeConnection)
    all_departments = SQLAlchemyConnectionField(DepartmentConnection, sort=False)

schema = graphene.Schema(query=Query)
