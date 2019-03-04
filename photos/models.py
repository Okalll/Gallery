from django.db import models


class Topic(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def save_topic(self):
        self.save()

class Location(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def save_location(self):
        self.save()

    @classmethod
    def delete_location(cls,name):
        cls.objects.filter(name = name).delete()

class Photo(models.Model):
    photo = models.ImageField(upload_to='photos')
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, default='LOCATION')



    def save_photo(self):
        self.save()

    @classmethod
    def search_by_topic(cls,search_term):
        photo = cls.objects.filter(topic__name__contains = search_term)
        return photo
