# Generated by Django 2.1.1 on 2018-09-02 23:02

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'utilisateur',
                'verbose_name_plural': 'utilisateurs',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name='UUID')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='date de création')),
                ('modification_date', models.DateTimeField(auto_now=True, verbose_name='date de modification')),
                ('type', models.CharField(choices=[('+', 'ajouter'), ('-', 'retirer')], default='+', max_length=1, verbose_name='type')),
                ('health', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='santé')),
                ('money', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='argent')),
                ('current_user', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='dernier utilisateur')),
            ],
            options={
                'verbose_name': 'action',
                'verbose_name_plural': 'actions',
            },
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name='UUID')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='date de création')),
                ('modification_date', models.DateTimeField(auto_now=True, verbose_name='date de modification')),
                ('name', models.CharField(blank=True, max_length=200, verbose_name='nom')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('image', models.ImageField(blank=True, null=True, upload_to='items', verbose_name='image')),
                ('current_user', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='dernier utilisateur')),
            ],
            options={
                'verbose_name': 'choix',
                'verbose_name_plural': 'choix',
            },
        ),
        migrations.CreateModel(
            name='Condition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name='UUID')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='date de création')),
                ('modification_date', models.DateTimeField(auto_now=True, verbose_name='date de modification')),
                ('type', models.CharField(choices=[('&', 'et'), ('|', 'ou')], default='&', max_length=1, verbose_name='type')),
                ('health', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='santé')),
                ('money', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='argent')),
                ('choice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='conditions', to='fmv.Choice', verbose_name='choix')),
                ('current_user', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='dernier utilisateur')),
            ],
            options={
                'verbose_name': 'condition',
                'verbose_name_plural': 'conditions',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name='UUID')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='date de création')),
                ('modification_date', models.DateTimeField(auto_now=True, verbose_name='date de modification')),
                ('name', models.CharField(blank=True, max_length=200, verbose_name='nom')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('image', models.ImageField(blank=True, null=True, upload_to='items', verbose_name='image')),
                ('current_user', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='dernier utilisateur')),
            ],
            options={
                'verbose_name': 'objet',
                'verbose_name_plural': 'objets',
            },
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name='UUID')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='date de création')),
                ('modification_date', models.DateTimeField(auto_now=True, verbose_name='date de modification')),
                ('name', models.CharField(blank=True, max_length=200, verbose_name='nom')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('image', models.ImageField(blank=True, null=True, upload_to='items', verbose_name='image')),
                ('ip', models.CharField(max_length=40, verbose_name='adresse IP')),
                ('health', models.SmallIntegerField(blank=True, null=True, verbose_name='santé')),
                ('money', models.SmallIntegerField(blank=True, null=True, verbose_name='argent')),
                ('current_user', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='dernier utilisateur')),
                ('items', models.ManyToManyField(blank=True, related_name='_player_items_+', to='fmv.Item', verbose_name='objets')),
            ],
            options={
                'verbose_name': 'joueur',
                'verbose_name_plural': 'joueurs',
            },
        ),
        migrations.CreateModel(
            name='Scenario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name='UUID')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='date de création')),
                ('modification_date', models.DateTimeField(auto_now=True, verbose_name='date de modification')),
                ('name', models.CharField(blank=True, max_length=200, verbose_name='nom')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('image', models.ImageField(blank=True, null=True, upload_to='items', verbose_name='image')),
                ('start_health', models.SmallIntegerField(blank=True, null=True, verbose_name='santé de départ')),
                ('start_money', models.SmallIntegerField(blank=True, null=True, verbose_name='argent de départ')),
                ('current_user', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='dernier utilisateur')),
            ],
            options={
                'verbose_name': 'scénario',
                'verbose_name_plural': 'scénarios',
            },
        ),
        migrations.CreateModel(
            name='Scene',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name='UUID')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='date de création')),
                ('modification_date', models.DateTimeField(auto_now=True, verbose_name='date de modification')),
                ('name', models.CharField(blank=True, max_length=200, verbose_name='nom')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('image', models.ImageField(blank=True, null=True, upload_to='items', verbose_name='image')),
                ('url', models.URLField(blank=True, verbose_name='URL')),
                ('current_user', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='dernier utilisateur')),
                ('scenario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='scenes', to='fmv.Scenario', verbose_name='scénario')),
            ],
            options={
                'verbose_name': 'scène',
                'verbose_name_plural': 'scènes',
            },
        ),
        migrations.AddField(
            model_name='scenario',
            name='intro',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='fmv.Scene', verbose_name='intro'),
        ),
        migrations.AddField(
            model_name='scenario',
            name='start_items',
            field=models.ManyToManyField(blank=True, related_name='_scenario_start_items_+', to='fmv.Item', verbose_name='objets de départ'),
        ),
        migrations.AddField(
            model_name='player',
            name='scenario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='players', to='fmv.Scenario', verbose_name='scénario'),
        ),
        migrations.AddField(
            model_name='player',
            name='scenes',
            field=models.ManyToManyField(blank=True, related_name='_player_scenes_+', to='fmv.Scene', verbose_name='scènes'),
        ),
        migrations.AddField(
            model_name='player',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='players', to=settings.AUTH_USER_MODEL, verbose_name='utilisateur'),
        ),
        migrations.AddField(
            model_name='condition',
            name='item',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='fmv.Item', verbose_name='objets'),
        ),
        migrations.AddField(
            model_name='condition',
            name='scene',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='fmv.Scene', verbose_name='scenes'),
        ),
        migrations.AddField(
            model_name='choice',
            name='scene_from',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='fmv.Scene', verbose_name='scène'),
        ),
        migrations.AddField(
            model_name='choice',
            name='scene_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='origins', to='fmv.Scene', verbose_name='destination'),
        ),
        migrations.AddField(
            model_name='action',
            name='item',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='fmv.Item', verbose_name='objets'),
        ),
        migrations.AddField(
            model_name='action',
            name='scene',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='actions', to='fmv.Scene', verbose_name='scène'),
        ),
        migrations.AlterUniqueTogether(
            name='player',
            unique_together={('ip', 'scenario')},
        ),
    ]
