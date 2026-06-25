from django.contrib import admin


from .models import TestResult


class TestResultAdmin(admin.ModelAdmin):
    model = TestResult
    list_display = ('barcode', 'patient_name', 'test_type', 'status', 'is_positive', 'results_completed_at', 'sample_taken_at')
    search_fields = ('barcode', 'patient_name')
    list_filter = ('test_type', 'status', 'is_positive')

admin.site.register(TestResult, TestResultAdmin)
