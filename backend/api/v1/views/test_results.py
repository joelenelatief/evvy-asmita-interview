"""
Test Results API View
"""
from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

from test_results.models import TestResult


class TestResultsView(APIView):
    """
    View that is called by the frontend to fetch test results
    """
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        is_positive = request.query_params.get('is_positive', 'all')
        test_results = list(TestResult.objects.all())
        if is_positive == 'true':
            test_results = [test_result for test_result in test_results if test_result.is_positive]
        elif is_positive == 'false':
            test_results = [test_result for test_result in test_results if not test_result.is_positive]

        return Response(
            {'data':[{
                'barcode': test_result.barcode,
                'patient_name': test_result.patient_name,
                'test_type': test_result.test_type,
                'status': test_result.status,
                'is_positive': test_result.is_positive,
                'results_completed_at': test_result.results_completed_at,
                'sample_taken_at': test_result.sample_taken_at
                } for test_result in test_results]
            }
        )
