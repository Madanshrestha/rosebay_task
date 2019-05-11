from django.urls import path, include

# from .views import StudentListView
from .api.viewsets import StudentViewSet
# from .router import router

app_name = 'students'

urlpatterns = [
    # path('students/', include('router.urls'))
    path('students/', StudentViewSet.as_view({'get': 'list'})),
    # path('students/<int:pk>/', StudentDetailView.as_view())
]
