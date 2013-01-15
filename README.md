django-angularjs-rest
=====================

Django + AngularJS + django-rest-framework + Twitter Bootstrap(angular-ui) project starter/demo.

<h1>Behaviour-driven development with Salad: aka Lettuce & Splinter</h1>

    https://github.com/wieden-kennedy/salad
    https://github.com/gabrielfalcao/lettuce
    http://github.com/cobrateam/splinter/
    
    http://cilliano.com/blog/2011/02/07/django-bdd-with-lettuce-and-splinter/
    http://lettuce.it/
    http://splinter.cobrateam.info/docs/

Test of Django Project Example:
    https://github.com/gabrielfalcao/lettuce/tree/master/tests/integration/django/alfaces/

<h3>Run Test</h3>
Example:
    user@machine:~projects/djangoproject $ python manage.py harvest

<h3>Specifying feature files</h3>
Example:
    user@machine:~projects/djangoproject $ python manage.py harvest path/to/my-test.feature

<h1>devserver runserver commands:</h1>
https://github.com/dcramer/django-devserver

    --werkzeug 	Tells Django to use the Werkzeug interactive debugger, instead of it's own.
    --forked 	Use a forking (multi-process) web server instead of threaded.
    --dozer 	Enable the dozer memory debugging middleware (at /_dozer)
    --wsgi-app 	Load the specified WSGI app as the server endpoint.

<h1>iPython shell_plus & Notebook</h1>
shell_plus = Django shell with autoloading of the apps database models

<h3>ipython notebook:</h3>
interactive Python shell with web browser as user interface, code & results can be saved to notebooks.
Apps database models are autoloading.
http://ipython.org/ipython-doc/dev/interactive/htmlnotebook.html
    ./manage.py shell_plus --notebook

    requirements:
        ipython
        django_extensions  #imports django app models into ipython notebook
        tornado
        pip install pyzmq --install-option="--zmq=bundled"

<h1></h1>
