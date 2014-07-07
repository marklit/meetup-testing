```bash
$ touch base/local_settings.py
```

Add in `AWS_S3_ACCESS_KEY_ID`, `AWS_S3_SECRET_ACCESS_KEY` and `AWS_STORAGE_BUCKET_NAME`.

```bash
$ pip install -r requirements.txt
$ python manage.py syncdb
$ python manage.py runserver
```
