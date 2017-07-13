from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.db import models
from django.conf import settings
import requests
import uuid


def image_path(self, filename):
	url = "original/%s/%s_%s" % (self.user_id, uuid.uuid4(), filename)
	return url


class Image(models.Model):
	user = models.ForeignKey(User, related_name='images')
	image = models.ImageField(upload_to=image_path)
	compressed_one = models.ForeignKey('CompressedImageOne', null=True, default=None)
	compressed_two = models.ForeignKey('CompressedImageTwo', null=True, default=None)

	@property
	def image_type(self):
		return self.image.name.split('.')[-1]


@receiver(post_save, sender=Image)
def image_post_save(sender, instance, **kwargs):
	if instance.compressed_one is None:
		print 'Set Compressed One'
		instance.compressed_one = CompressedImageOne.objects.create(original_image=instance)
		instance.save()

	if instance.compressed_two is None:
		print 'Set Compressed Two'
		instance.compressed_two = CompressedImageTwo.objects.create(original_image=instance)
		instance.save()


class CompressedImage(models.Model):
	BUCKET_FOLDER = 'compressed-images'
	QUALITY = 100

	JPEG_TYPE = 'jpg'
	PNG_TYPE = 'png'
	IMAGE_TYPES = [
		(JPEG_TYPE, JPEG_TYPE),
		(PNG_TYPE, PNG_TYPE)
	]

	original_image = models.ForeignKey(Image, related_name="%(class)s")
	url = models.CharField(max_length=300, default='')
	name = models.CharField(max_length=300, default='')
	size = models.IntegerField(default=0)
	image_type = models.CharField(max_length=5, choices=IMAGE_TYPES, default=JPEG_TYPE)

	@property
	def quality(self):
		return self.QUALITY

	def compress_image(self):
		lambda_compression_url = "https://jsiyitfs89.execute-api.us-east-1.amazonaws.com/prod/compressimage"
		print 'Original Image: '
		print self.original_image

		params = {
			'bucket': settings.AWS_STORAGE_BUCKET_NAME,
			'original_key': self.original_image.image.name,
			'compressed_key': '{}/{}'.format(self.BUCKET_FOLDER, self.name),
			'quality': self.QUALITY
		}
		print params

		resp = requests.post(lambda_compression_url, json=params)
		print resp

		self.url = resp.json()['url']
		self.size = resp.json()['size']

	class Meta:
		abstract = True


class CompressedImageOne(CompressedImage):
	BUCKET_FOLDER = 'compressed-1'
	QUALITY = 70


class CompressedImageTwo(CompressedImage):
	BUCKET_FOLDER = 'compressed-2'
	QUALITY = 30


@receiver(pre_save)
def compressed_image_pre_save(sender, instance, **kwargs):
	if issubclass(sender, CompressedImage):
		original_name = instance.original_image.image.name.split('/')[-1]
		instance.name = '{}_{}'.format('compressed1', original_name)
		instance.compress_image()
