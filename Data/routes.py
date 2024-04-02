from rest_framework.routers import DefaultRouter
from Data.views.Employeeview import EmployeeViewSet
from Data.views.Managerview import ManagerViewSet

router = DefaultRouter()
router.register(r"Employee", EmployeeViewSet)
router.register(r"Manager", ManagerViewSet)
