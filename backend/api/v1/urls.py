from django.urls import path


from . import views

urlpatterns = [
    path(r'test-results/', views.TestResultsView.as_view(), name="test-results"),
]
