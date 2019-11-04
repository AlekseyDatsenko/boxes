from django.db import models

class About(models.Model):
    text = models.TextField(verbose_name="О нас")
    title = 'О нас'

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = ("информацию")
        verbose_name_plural = ("О нас")

class Contact(models.Model):
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    adress = models.CharField(max_length=200, verbose_name="Адрес", blank=True)

    def __str__(self):
        return self.phone

    class Meta:
        verbose_name = ("контакт")
        verbose_name_plural = ("Контакты")

class Stock(models.Model):
    image = models.ImageField(upload_to='media/image', verbose_name="Картинка")
    text = models.TextField(verbose_name="Описание")
	
    def __str__(self):
        return self.text

    class Meta:
        verbose_name = ("акцию")
        verbose_name_plural = ("Акции")

class Delivery(models.Model):
    text = models.TextField(verbose_name="Доставка/оплата")
    title = 'Доставка/оплата'

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = ("информацию")
        verbose_name_plural = ("Доставка/оплата")

class Box_1(models.Model):
    image_1 = models.ImageField(upload_to='media/image', verbose_name="Картинка 1")
    image_2 = models.ImageField(upload_to='media/image', verbose_name="Картинка 2")
    image_3 = models.ImageField(upload_to='media/image', verbose_name="Картинка 3")
    name = models.CharField(max_length=50, verbose_name="Название")
    size = models.CharField(max_length=25, verbose_name="Габариты")
    price_1 = models.CharField(max_length=25, verbose_name="Цена от 1 до 10")
    price_2 = models.CharField(max_length=25, verbose_name="Цена от 11 до 50")
    price_3 = models.CharField(max_length=25, verbose_name="Цена от 50 до 100")
    price_4 = models.CharField(max_length=25, verbose_name="Цена от 101")
	
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ("коробку")
        verbose_name_plural = ("Коробки_колонка_1")

class Box_2(models.Model):
    image_1 = models.ImageField(upload_to='media/image', verbose_name="Картинка 1")
    image_2 = models.ImageField(upload_to='media/image', verbose_name="Картинка 2")
    image_3 = models.ImageField(upload_to='media/image', verbose_name="Картинка 3")
    name = models.CharField(max_length=50, verbose_name="Название")
    size = models.CharField(max_length=25, verbose_name="Габариты")
    price_1 = models.CharField(max_length=25, verbose_name="Цена от 1 до 10")
    price_2 = models.CharField(max_length=25, verbose_name="Цена от 11 до 50")
    price_3 = models.CharField(max_length=25, verbose_name="Цена от 50 до 100")
    price_4 = models.CharField(max_length=25, verbose_name="Цена от 101")
	
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ("коробку")
        verbose_name_plural = ("Коробки_колонка_2")

class Box_3(models.Model):
    image_1 = models.ImageField(upload_to='media/image', verbose_name="Картинка 1")
    image_2 = models.ImageField(upload_to='media/image', verbose_name="Картинка 2")
    image_3 = models.ImageField(upload_to='media/image', verbose_name="Картинка 3")
    name = models.CharField(max_length=50, verbose_name="Название")
    size = models.CharField(max_length=25, verbose_name="Габариты")
    price_1 = models.CharField(max_length=25, verbose_name="Цена от 1 до 10")
    price_2 = models.CharField(max_length=25, verbose_name="Цена от 11 до 50")
    price_3 = models.CharField(max_length=25, verbose_name="Цена от 50 до 100")
    price_4 = models.CharField(max_length=25, verbose_name="Цена от 101")
	
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ("коробку")
        verbose_name_plural = ("Коробки_колонка_3")
