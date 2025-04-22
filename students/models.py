from django.db import models


class Group(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name="Nombre del grupo")

    class Meta:
        verbose_name = "Grupo"
        verbose_name_plural = "Grupos"

    def __str__(self):
        return self.name


class Percentage(models.Model):
    PARTIALS = (
        ("1", "1er Parcial"),
        ("2", "2do Parcial"),
        ("3", "3er Parcial"),
    )

    id = models.AutoField(primary_key=True)
    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        related_name="percentages",
        verbose_name="Grupo",
    )
    partial = models.CharField(
        max_length=1,
        choices=PARTIALS,
        default="1",
        verbose_name="Parcial",
    )
    exam_points = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=30,
        verbose_name="Puntos examen",
        help_text="Puntos / aciertos que se le asignan al examen. Ejemplo: 30.00",
    )
    assistances_amount = models.IntegerField(
        default=3,
        verbose_name="Asistencias",
        help_text="Número de asistencias que se le asignan al examen. Ejemplo: 3",
    )
    exam_percentage = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=50,
        verbose_name="Porcentaje examen",
        help_text=(
            "Porcentaje de la calificación que se le asigna al examen. Ejemplo: 50.00"
        ),
    )
    assistances_percentage = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=10,
        verbose_name="Porcentaje asistencias",
        help_text=(
            "Porcentaje de la calificación que se le asigna a las asistencias. "
            "Ejemplo: 10.00"
        )
    )
    homework_percentage = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=25,
        verbose_name="Porcentaje tareas",
        help_text=(
            "Porcentaje de la calificación que se le asigna a las tareas. "
            "Ejemplo: 15.00",
        )
    )
    class_work_percentage = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=15,
        verbose_name="Porcentaje trabajo en clase",
        help_text=(
            "Porcentaje de la calificación que se le asigna al trabajo en clase. "
            "Ejemplo: 20.00",
        )
    )

    class Meta:
        unique_together = ("group", "partial")
        verbose_name = "Porcentaje"
        verbose_name_plural = "Porcentajes"

    def __str__(self):
        return f"{self.group.name} - {self.partial}"


class Student(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100, verbose_name="Nombre")
    last_name = models.CharField(max_length=100, verbose_name="Apellido")
    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        related_name="students",
        verbose_name="Grupo",
    )
    age = models.IntegerField(null=True, blank=True, verbose_name="Edad")
    email = models.EmailField(
        max_length=100,
        unique=True,
        null=True,
        blank=True,
        verbose_name="Correo electrónico",
    )
    phone_number = models.CharField(
        max_length=15,
        unique=True,
        null=True,
        blank=True,
        verbose_name="Número de teléfono",
    )
    address = models.TextField(null=True, blank=True, verbose_name="Dirección")
    enrollment_date = models.DateField(
        auto_now_add=True, verbose_name="Fecha de inscripción"
    )

    class Meta:
        verbose_name = "Estudiante"
        verbose_name_plural = "Estudiantes"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# class Rate(models.Model):
#     id = models.AutoField(primary_key=True)
#     student = models.ForeignKey(
#         Student,
#         on_delete=models.CASCADE,
#         related_name="rates",
#         verbose_name="Estudiante",
#     )
#     percentage = models.ForeignKey(
#         Percentage,
#         on_delete=models.CASCADE,
#         related_name="rates",
#         verbose_name="Porcentaje",
#     )
#     value = models.DecimalField(
#         max_digits=5,
#         decimal_places=2,
#         verbose_name="Valor. Ejemplo: 8.00",
#     )

#     class Meta:
#         unique_together = ("student", "percentage")
#         verbose_name = "Calificación"
#         verbose_name_plural = "Calificaciones"

#     def __str__(self):
#         return f"{self.student} - {self.percentage} - {self.value}"
