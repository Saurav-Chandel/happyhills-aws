# STATICFILES_DIRS = (os.path.join(BASE_DIR, "static_dev"),)
AWS_ACCESS_KEY_ID = "AKIA2K5WZGM5LPVKVIKY"
AWS_SECRET_ACCESS_KEY = "biovwSYM8PUJPK1IqkOdpWZHZy3VzQUIFezO7LM"
AWS_FILE_EXPIRE=2000
AWS_S3_REGION_NAME = "us-east-1"  # e.g. us-east-2
AWS_STORAGE_BUCKET_NAME = "happyhills-s3"
AWS_S3_CUSTOM_DOMAIN = "%s.s3.amazonaws.com" % AWS_STORAGE_BUCKET_NAME
# AWS_S3_CUSTOM_DOMAIN = "d2dr6wwncpi0to.cloudfront.net"
AWS_S3_OBJECT_PARAMETERS = {
    "CacheControl": "max-age=86400",
}
AWS_LOCATION = "static"
STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
STATICFILES_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
DEFAULT_FILE_STORAGE = "main.storage_backends.MediaStorage"