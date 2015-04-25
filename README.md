# Boston Manager Web Services #

The application for Boston needs web services for several modules. At the moment the Task Module is in development process 

### Instructions ###

* First, we need to set up the virtual environment
```
#!python

mkvirtualenv Boston
```

* Install the proper Django Version
```
#!python

pip install django==1.6
```

* Start developing

----------------------------------------------------------------------------------------------------------------
** Note: To deactivate a virtualenv just type in the following command:
```
#!python
deactivate
```

And to work on a virtualenv that has been already deactivated, just type in the following command:
```
#!python
workon <virtualenv_name>
```
My name for the virtualenv is "Boston"


-------------------------------------------------------------------------------------------------------------------
** Note: At the moment there is no database set up. So it can't be accesed to the admin area. We should take the decision of what database to use.