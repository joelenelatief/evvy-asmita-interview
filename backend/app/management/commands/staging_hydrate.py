import os
from datetime import datetime, timedelta
from django.core.management.base import BaseCommand

from test_results.models import TestResult


class Command(BaseCommand):
    help = 'Creates a few Tests in the DB to start the env off'

    def handle(self, *args, **options):
        if not TestResult.objects.exists():
            # list of 10 strings which represent patient first and last names
            patient_names = [
                'John Doe',
                'Jane Doe',
                'Alice Smith',
                'Bob Johnson',
                'Charlie Brown',
                'David Lee',
                'Eve Jackson',
                'Frank White',
                'Grace Adams',
                'Henry Davis',
            ]
            for i, patient_name in enumerate(patient_names):
                # if even, then test_type is sti, else yeast-infection
                test_type = TestResult.TEST_TYPE_STI if i % 2 == 0 else TestResult.TEST_TYPE_YEAST_INFECTION
                # if even, then status is in-progress, else complete
                status = TestResult.STATUS_IN_PROGRESS if i % 2 == 0 else TestResult.STATUS_COMPLETE
                # if complete, then is_positive is True if i is divisible by 3, else False
                is_positive = None
                if status == TestResult.STATUS_COMPLETE:
                    is_positive = i % 3 == 0
                test_result, created = TestResult.objects.get_or_create(
                    patient_name=patient_name,
                    defaults={
                        'test_type': test_type,
                        'status': status,
                        'is_positive': is_positive,
                        'results_completed_at': datetime.now(),
                        # random number of days between 1 and 10 before now
                        'sample_taken_at': datetime.now() - timedelta(days=i % 10 + 1),
                    }
                )
