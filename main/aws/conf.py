# STATICFILES_DIRS = (os.path.join(BASE_DIR, "static_dev"),)
import datetime
AWS_ACCESS_KEY_ID = "AKIA2K5WZGM5HMPRGT7A"
AWS_SECRET_ACCESS_KEY = "YeeGKMTZdd/8lzvpLwiQNnbW+cA7urSA07gsv+3e"
AWS_FILE_EXPIRE=200
AWS_PRELOAD_METADATA = True
AWS_QUERYSTRING_AUTH = True
AWS_S3_REGION_NAME = "us-east-1"  # e.g. us-east-2
AWS_STORAGE_BUCKET_NAME = "happyhills-s3"
AWS_DEFAULT_ACL=None
# AWS_S3_CUSTOM_DOMAIN = "%s.s3.amazonaws.com" % AWS_STORAGE_BUCKET_NAME
# AWS_S3_CUSTOM_DOMAIN = "d2dr6wwncpi0to.cloudfront.net"
# AWS_S3_OBJECT_PARAMETERS = {
#     "CacheControl": "max-age=86400",
# }
# AWS_LOCATION = "static"
# STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
STATICFILES_STORAGE = "main.aws.utils.MediaRootS3BotoStorage"
DEFAULT_FILE_STORAGE = "main.aws.utils.StaticRootS3BotoStorage"
AWS_S3_SIGNATURE_VERSION="s3v4"




