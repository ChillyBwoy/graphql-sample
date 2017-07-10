import importlib

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Populate database with test data'

    def add_arguments(self, parser):
        parser.add_argument('model_class', help='Model to populate')
        parser.add_argument(
            '--count',
            dest='count',
            default=10,
            help='How much')

    def handle(self, *args, **options):
        count = options['count']
        model_class_app, model_class_name = options['model_class'].split('.')

        module_inst = importlib.import_module(
            "catalog.{app}.factories".format(app=model_class_app))

        try:
            factory_class = getattr(
                module_inst, "{0}Factory".format(model_class_name))
        except AttributeError:
            self.stdout.write(self.style.ERROR(
                "Error loading '{0}Factory'".format(model_class_name)))
            return

        self.stdout.write("Populating '{0}' model...".format(model_class_name))

        index = 0
        for _ in range(int(count)):
            try:
                inst = factory_class.create()
                index += 1
                self.stdout.write(str(inst))
            except Exception as e:
                self.stdout.write(str(e))

        self.stdout.write(self.style.SUCCESS(
            "Created {0} instances of {1}".format(index, model_class_name)))
