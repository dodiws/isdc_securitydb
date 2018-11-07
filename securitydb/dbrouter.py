MAP_APPS_TO_DB = {
    'contenttypes': 'default',
    'auth': 'default',
    'admin': 'default',
    'sessions': 'default',
    'messages': 'default',
    'securitydb': 'securitydb',
}
print 'dbrouter.py'

class securitydbrouter(object):
    # def db_for_read(self, model, **hints):
    #     print 'class securitydbrouter:db_for_read'
    #     return MAP_APPS_TO_DB.get(model._meta.app_label)

    # def db_for_write(self, model, **hints):
    #     print 'class securitydbrouter:db_for_write'
    #     return MAP_APPS_TO_DB.get(model._meta.app_label)

    # def allow_relation(self, obj1, obj2, **hints):
    #     print 'class securitydbrouter:allow_relation'
    #     """
    #     Allow relations if a model in the auth app is involved.
    #     """
    #     return None

    # def allow_migrate(self, db, app_label, model_name=None, **hints):
    #     print 'class securitydbrouter:allow_migrate'
    #     """
    #     Make sure the auth app only appears in the 'auth_db'
    #     database.
    #     """
    #     print 'db', db
    #     print 'app_label', app_label
    #     print 'model_name', model_name
    #     print '**hints', hints
    #     return None

    def db_for_read(self, model, **hints):

        if model._meta.app_label in MAP_APPS_TO_DB:
            return MAP_APPS_TO_DB[model._meta.app_label]
        return None

    def db_for_write(self, model, **hints):

        if model._meta.app_label in MAP_APPS_TO_DB:
            return MAP_APPS_TO_DB[model._meta.app_label]
        return None

    def allow_relation(self, obj1, obj2, **hints):

        db1 = MAP_APPS_TO_DB.get(obj1._meta.app_label)
        db2 = MAP_APPS_TO_DB.get(obj2._meta.app_label)
        if db1 and db2:
            return db1 == db2
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):

        if db in MAP_APPS_TO_DB.values():
            return MAP_APPS_TO_DB.get(app_label) == db
        elif app_label in MAP_APPS_TO_DB:
            return False
        return None
