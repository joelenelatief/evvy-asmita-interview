import datetime
import hashlib

from django.contrib.auth.models import User
from django.db import models

def _create_random_hash(length=20):
    """
    This function generates a hash of length 20 chars by default
    """
    hash = hashlib.sha1()
    seed = str(datetime.datetime.now()).encode('utf-8')
    hash.update(seed)
    return hash.hexdigest()[:length]

class TestResult(models.Model):
    """
    Model to store test results
    """
    id = models.AutoField(primary_key=True)
    # barcode identifier for the test
    barcode = models.CharField(max_length=20, default=_create_random_hash)
    patient_name = models.CharField(max_length=100)
    # test type, can be either sti or yeast-infection
    TEST_TYPE_STI = 'sti'
    TEST_TYPE_YEAST_INFECTION = 'yeast-infection'
    TEST_TYPE_CHOICES = [
        (TEST_TYPE_STI, 'STI'),
        (TEST_TYPE_YEAST_INFECTION, 'Yeast Infection'),
    ]
    test_type = models.CharField(
        max_length=20,
        choices=TEST_TYPE_CHOICES,
        default=TEST_TYPE_STI,
    )
    # status, can have in-progress and complete
    STATUS_IN_PROGRESS = 'in-progress'
    STATUS_COMPLETE = 'complete'
    STATUS_CHOICES = [
        (STATUS_IN_PROGRESS, 'In Progress'),
        (STATUS_COMPLETE, 'Complete'),
    ]
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=STATUS_IN_PROGRESS,
    )
    # whether the test result was positive or negative. Is null if the test is in progress
    is_positive = models.BooleanField(null=True, blank=True, default=None)
    # when the results were completed
    results_completed_at = models.DateTimeField(null=True, blank=True)
    # when the test sample was actually taken
    sample_taken_at = models.DateTimeField(null=True, blank=True)
