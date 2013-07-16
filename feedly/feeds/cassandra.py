from feedly.feeds.base import BaseFeed
from feedly.storage.cassandra import CassandraActivityStorage
from feedly.storage.cassandra import CassandraTimelineStorage
from feedly.storage.utils.serializers.cassandra import ActivitySerializer
from feedly import settings


class CassandraFeed(BaseFeed):
    timeline_storage_class = CassandraTimelineStorage
    activity_storage_class = CassandraActivityStorage
    activity_serializer = ActivitySerializer

    keyspace = 'test_feedly'
    timeline_cf = 'timeline'
    activity_cf = 'activity'

    @classmethod
    def get_timeline_storage(cls):
        timeline_storage_options = {
            'keyspace_name': cls.keyspace,
            'hosts': settings.FEEDLY_CASSANDRA_HOSTS,
            'column_family_name': cls.timeline_cf,
            'serializer_class': cls.timeline_serializer
        }
        timeline_storage = cls.timeline_storage_class(
            **timeline_storage_options)
        return timeline_storage

    @classmethod
    def get_activity_storage(cls):
        activity_storage_options = {
            'keyspace_name': cls.keyspace,
            'hosts': settings.FEEDLY_CASSANDRA_HOSTS,
            'column_family_name': cls.activity_cf,
            'serializer_class': cls.activity_serializer
        }
        activity_storage = cls.activity_storage_class(
            **activity_storage_options)
        return activity_storage