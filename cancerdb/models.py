# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Biomarker(models.Model):
    biomarker_id = models.CharField(primary_key=True, max_length=4)
    gene_symbol = models.CharField(max_length=30, blank=True, null=True)
    gene_full_name = models.CharField(max_length=100, blank=True, null=True)
    gene_function = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Biomarker'


class BiomarkerImpact(models.Model):
    impact_id = models.CharField(primary_key=True, max_length=6)
    biomarker = models.ForeignKey(Biomarker, models.DO_NOTHING)
    cancer = models.ForeignKey('Cancer', models.DO_NOTHING)
    biomarker_role = models.TextField(blank=True, null=True)
    mutation_type = models.TextField(blank=True, null=True)
    clinical_implication = models.TextField(blank=True, null=True)
    pathway_involvement = models.TextField(blank=True, null=True)
    treatment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Biomarker_Impact'


class BiomarkerImpactReference(models.Model):
    pk = models.CompositePrimaryKey('impact_id', 'reference_id')
    impact = models.ForeignKey(BiomarkerImpact, models.DO_NOTHING)
    reference = models.ForeignKey('Ref', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Biomarker_Impact_Reference'
        unique_together = (('impact', 'reference'),)


class Cancer(models.Model):
    cancer_id = models.CharField(primary_key=True, max_length=4)
    cancer_name = models.CharField(max_length=30, blank=True, null=True)
    subtype_name = models.TextField(blank=True, null=True)
    icd = models.CharField(db_column='ICD', max_length=30, blank=True, null=True)  # Field name made lowercase.
    cancer_description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Cancer'


class Ref(models.Model):
    reference_id = models.IntegerField(primary_key=True)
    url = models.URLField(db_column='URL', blank=True, null=True)  # Field name made lowercase.
    title = models.TextField(blank=True, null=True)
    source = models.CharField(max_length=300, blank=True, null=True)
    publication_year = models.TextField(blank=True, null=True)  # This field type is a guess.
    primary_author = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Ref'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
