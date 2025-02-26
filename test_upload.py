import os
import django

# Manually load Django settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fashioneer_backend.settings")
django.setup()

from django.conf import settings
from storages.backends.gcloud import GoogleCloudStorage  # Manually import GCS storage
from django.core.files.uploadedfile import SimpleUploadedFile

# Debug: Print which storage backend is being used
print(f"DEFAULT FILE STORAGE: {settings.DEFAULT_FILE_STORAGE}")

# Manually instantiate Google Cloud Storage instead of default_storage
storage_instance = GoogleCloudStorage()
print(f"Manually loaded storage backend: {storage_instance.__class__.__name__}")

# Test file upload using Google Cloud Storage explicitly
file = SimpleUploadedFile("test_upload.jpg", b"dummydata")
path = storage_instance.save("profiles/test_upload.jpg", file)

# Output result
print(f"File saved to: {path}")
print(f"Accessible URL: {storage_instance.url(path)}")
