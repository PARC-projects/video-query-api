from django.db import models


class Feature(models.Model):
    # id bigint NOT NULL DEFAULT nextval('features_id_seq'::regclass),
    # video_clip_id bigint NOT NULL,
    # cnn_stream character varying COLLATE pg_catalog."default" NOT NULL,
    # cnn_stream_split smallint NOT NULL,
    # feature_name character varying(80) COLLATE pg_catalog."default" NOT NULL,
    # cnn_weights_file_uri character varying(256) COLLATE pg_catalog."default" NOT NULL,
    # feature double precision[] NOT NULL,


    class Meta:
        db_table = 'signature'
