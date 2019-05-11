from students.api.viewsets import StudentViewSet
from schools.api.viewsets import SchoolViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('students', StudentViewSet)
router.register('schools', SchoolViewSet)