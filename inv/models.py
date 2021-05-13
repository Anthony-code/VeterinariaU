from django.db import models

from bases.models import ClaseModelo

class Categoria(ClaseModelo):
    descripcion = models.CharField(
        max_length=100,
        help_text='Descripcion de la categoria',
        unique=True,
    )
    #Para cuando se haga referencia a categoria muestre la descripcion#
    def __str__(self):
        return '{}'.format(self.descripcion)
    #Para guaradar la categoria en mayuscula#
    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Categoria, self).save()
    #Para guardar el nombre cuando django se refiera a este modelo en plural #    
    class Meta:
        verbose_name_plural = "Categorias"

class SubCategoria(ClaseModelo):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descripcion = models.CharField(
        max_length=100,
        help_text='Descripcion de la categoria',
        
    )

    def __str__(self):
        return '{}:{}'.format(self.categoria.descripcion,self.descripcion)
    #Para guaradar la categoria en mayuscula#
    def save(self):
        self.descripcion = self.descripcion.upper()
        super(SubCategoria, self).save()
    #Para guardar el nombre cuando django se refiera a este modelo en plural #    
    class Meta:
        verbose_name_plural = "Sub-Categorias"
        unique_together = ('categoria', 'descripcion')

class Marca(ClaseModelo):
    descripcion = models.CharField(
        max_length=100,
        help_text='Descripcion de la marca',
        unique=True,
    )
    #Para cuando se haga referencia a categoria muestre la descripcion#
    def __str__(self):
        return '{}'.format(self.descripcion)
    #Para guaradar la categoria en mayuscula#
    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Marca, self).save()
    #Para guardar el nombre cuando django se refiera a este modelo en plural #    
    class Meta:
        verbose_name_plural = "Marcas"

class UnidadMedida(ClaseModelo):
    descripcion = models.CharField(
        max_length=100,
        help_text='Descripcion de la Unidad Medida',
        unique=True,
    )
    #Para cuando se haga referencia a categoria muestre la descripcion#
    def __str__(self):
        return '{}'.format(self.descripcion)
    #Para guaradar la categoria en mayuscula#
    def save(self):
        self.descripcion = self.descripcion.upper()
        super(UnidadMedida, self).save()
    #Para guardar el nombre cuando django se refiera a este modelo en plural #    
    class Meta:
        verbose_name_plural = "Unidades de Medidas"


class Producto(ClaseModelo):
    codigo = models.CharField(
        max_length=20,
        unique=True
    )
    codigo_barra = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    precio = models.FloatField(default=0)
    # precio = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    existencia = models.IntegerField(default=0)
    ultima_compra = models.DateField(null=True, blank=True)

    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    unidad_medida = models.ForeignKey(UnidadMedida, on_delete=models.CASCADE)
    subcategoria = models.ForeignKey(SubCategoria, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.descripcion)
    
    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Producto,self).save()
    
    class Meta:
        verbose_name_plural = "Productos"
        unique_together = ('codigo','codigo_barra')