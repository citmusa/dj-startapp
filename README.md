# dj-startapp
Django startapp --template
A modified version of django's template for the *./manage.py startapp* command. 

All this because I forget from where to make imports XD

### Features

  * Unicode encoding in each file
  * Common imports in `views.py` ( a function view, and a ClassBasedView)
  * Mini-examples in `admin.py`, `forms.py`, `models.py` and `urls.py`
  * `migrations` folder, `app.py` and `test.py` also present (as in the original version)

## Usage
```
$ ./manage.py startapp --template=https://github.com/citmusa/dj-startapp/archive/master.zip myapp
```

#### Comments, suggestions and contributions are welcome.
