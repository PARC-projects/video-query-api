from django.db import models

from queries.models import Video, VideoClip

"""
Identifies a collection of videos to search, and the clip duration for the search.
Only one clip duration is allowed because the similarity algorithm has only been
tested for comparisons of clips of the same size.
Example of creating a SearchSet object and then add videos with id=1 and 2 to it:

>>> s1 = SearchSet.object.create(name='set 1')
>>> s1.videos.add(Video.object.get(id=1), Video.object.get(id=2))
"""


class SearchSet(models.Model):
    # Display name of Search Set
    name = models.CharField(max_length=254, unique=True)
    # Many to many relationship between Search Set and Video (search_set_videos)
    videos = models.ManyToManyField(Video)
    # Duration of video to use
    duration = models.PositiveIntegerField(default=10)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'search_set'

    def list_of_clip_ids(self):
        id_of_videos = self.videos.all().values_list('id', flat=True)
        video_clip_objects = VideoClip.objects.filter(video__in=id_of_videos, duration=self.duration)
        return video_clip_objects.values_list('id', flat=True)
