from django.core.validators import MaxValueValidator
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='edad',
            field=models.PositiveIntegerField(validators=[MaxValueValidator(30)]),
        ),
        migrations.AlterField(
            model_name='mascota',
            name='especie',
            field=models.CharField(
                choices=[('perro', 'Perro'), ('gato', 'Gato'), ('otro', 'Otro')],
                max_length=50,
            ),
        ),
        migrations.AddConstraint(
            model_name='solicitud',
            constraint=models.UniqueConstraint(
                fields=('usuario', 'mascota'),
                name='unique_solicitud_usuario_mascota',
            ),
        ),
    ]
