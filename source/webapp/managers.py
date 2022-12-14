from django.db.models import Manager


class TaskManager(Manager):
    def with_deleted(self):
        return self.get_queryset().all()

    def all(self):
        return self.get_queryset().filter(is_deleted=False)