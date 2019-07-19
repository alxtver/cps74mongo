from django.db import models


class TypeComponents(models.Model):
    name_type = models.CharField('Тип', max_length=200)

    def __str__(self):
        """String for representing the Model object."""
        return self.name_type

    class Meta:
        verbose_name = 'Тип ПКИ'
        verbose_name_plural = 'Типы ПКИ'


class Country(models.Model):
    id = models.AutoField(primary_key=True)
    country = models.CharField(max_length=100)

    def __str__(self):
        """String for representing the Model object."""
        return self.country

    class Meta:
        verbose_name = 'Страна произвоздства'
        verbose_name_plural = 'Страны производства'


class Part(models.Model):
    id = models.AutoField(primary_key=True)
    part_name = models.CharField(max_length=100)

    def __str__(self):
        """String for representing the Model object."""
        return self.part_name

    class Meta:
        verbose_name = 'Партия'
        verbose_name_plural = 'Партии'


class CompItems(models.Model):
    comp = models.ForeignKey('Comp', verbose_name='Серийный номер машины', on_delete=models.CASCADE)
    items = models.ForeignKey('TypeComponents', verbose_name='Тип', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        """String for representing the Model object."""
        return self.comp.serial_number

    class Meta:
        verbose_name = 'Состав машины'
        verbose_name_plural = 'Составы машин'


class Comp(models.Model):
    serial_number = models.CharField(max_length=200, default=None, unique=True)
    items = models.ManyToManyField(TypeComponents, through=CompItems, related_name='all_items')
    part = models.ForeignKey(Part, null=True, on_delete=models.CASCADE)

    def get_items(self):
        return [item for item in self.items.all()]

    def __str__(self):
        """String for representing the Model object."""
        return self.serial_number

    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'


class Pki(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Наименование', max_length=200)
    serial_number = models.CharField('Серийный номер', max_length=255, unique=True)
    name_type = models.ForeignKey(TypeComponents, verbose_name='Тип',
                                  null=False, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, verbose_name='Страна производства',
                                on_delete=models.SET_NULL, null=True, blank=True)
    date_of_arrival = models.DateTimeField('Дата', auto_now_add=True)
    part_name = models.ForeignKey(Part, verbose_name='Партия', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        """String for representing the Model object."""
        return '{0}, Серийный номер - {1}'.format(self.name, self.serial_number)

    class Meta:
        verbose_name = 'ПКИ'
        verbose_name_plural = 'ПКИ'
