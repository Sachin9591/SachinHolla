from django.db import models
# from django.utils.translation import gettext
# from django.core.validators import RegexValidator


# Create your models here.
class PortfolioList(models.Model):
    pfoTitle = models.CharField(max_length=1000)
    pfoImages = models.ImageField(upload_to='Images')
    pfoDescr = models.TextField()
    pfoTagsName = models.TextField()


class ResumeUploadsList(models.Model):
    resumeTitle = models.CharField(max_length=255, verbose_name='Resume Name')
    resumeFile = models.FileField(upload_to='Docs', verbose_name='Resume File')
    resumeDateTime = models.DateTimeField(verbose_name='Upload DateTime')
    resumeActive = models.BooleanField(default=False, verbose_name='Resume Active')

    def __str__(self):
        return self.resumeTitle + " - " + str(self.resumeDateTime)


class ServicesIndexList(models.Model):
    servID = models.CharField(max_length=100, verbose_name='Service No', primary_key=True, unique=True)
    servHead = models.CharField(max_length=1000, verbose_name='Service Title')
    servClassIcon = models.CharField(max_length=1000, verbose_name='Class Name')
    servDescr = models.TextField(verbose_name='Service Description')
    servActive = models.BooleanField(default=False, verbose_name='Service Active')

    def __str__(self):
        return self.servHead


class TestimonialsList(models.Model):
    testMonID = models.CharField(max_length=100, verbose_name='Testimonial ID', primary_key=True, unique=True)
    testMonTitle = models.CharField(max_length=1000, verbose_name='Testimonial Title')
    testMonImage = models.ImageField(upload_to='Images/Testimonials', verbose_name='Testimonial Images')
    testMonDescr = models.TextField(verbose_name='Testimonial Description')

    def __str__(self):
        return self.testMonTitle


class TechnicalSkillsList(models.Model):
    tSkillId = models.CharField(max_length=100, verbose_name='Skills ID', primary_key=True, unique=True)
    tSkillTitle = models.CharField(max_length=1000, verbose_name='Skills Title')
    tSkillPercent = models.IntegerField(verbose_name='Skills Percent')
    tSkillActive = models.BooleanField(default=False, verbose_name='Skills Active')

    def __str__(self):
        return self.tSkillTitle


class BlogsList(models.Model):
    daysList = [(str(i), str(i)) for i in range(1, 32)]
    monthsList = [('1', 'Jan'), ('2', 'Feb'), ('3', 'Mar'), ('4', 'Apr'), ('5', 'May'), ('6', 'Jun'), ('7', 'Jul'),
                  ('8', 'Aug'), ('9', 'Sep'), ('10', 'Oct'), ('11', 'Nov'), ('12', 'Dec')]

    blID = models.CharField(max_length=100, verbose_name='Blogs ID', primary_key=True, unique=True)
    blTitle = models.CharField(max_length=1000, verbose_name='Blogs Title')
    blCommentsNo = models.IntegerField(verbose_name='Blogs Comment No.')
    blImages = models.ImageField(upload_to='Images/Blogs', verbose_name='Blogs Image')
    blDescr = models.TextField(max_length=2000, verbose_name='Blogs Description')
    blAuthor = models.CharField(max_length=1000, verbose_name='Blogs Author')
    blPublishedDate = models.DateField(verbose_name='Blogs Published Date')
    blPublishedDay = models.CharField(max_length=100, choices=daysList, verbose_name='Blogs Published Day')
    blPublishedMonth = models.CharField(max_length=100, choices=monthsList, verbose_name='Blogs Published Month')
    blPublishedYear = models.CharField(max_length=100, verbose_name='Blogs Published Year')
    blActive = models.BooleanField(default=False, verbose_name='Blogs Active')

    def __str__(self):
        return self.blTitle + " - " + self.blAuthor + " - " + str(self.blPublishedDate)
