import pymysql

#añado esta linea para evitar el error, con el numero especifico de version, ya que el archivo base.py
#existe un condicional, en este caso que el paqueta "mysqlcliente" debe tener la version 1.4.3 o posterior, por lo cual añado esa linea con la version requerida
#raise ImproperlyConfigured: django.core.exceptions.ImproperlyConfigured: mysqlclient 1.4.3 or newer is required; you have 1.0.3.
pymysql.version_info = (1,4,3)

pymysql.install_as_MySQLdb()