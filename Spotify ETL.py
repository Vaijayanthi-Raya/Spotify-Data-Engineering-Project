import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Script generated for node artists
artists_node1727578716506 = glueContext.create_dynamic_frame.from_options(format_options={"quoteChar": "\"", "withHeader": True, "separator": ",", "optimizePerformance": False}, connection_type="s3", format="csv", connection_options={"paths": ["s3://spotify-staging-vaijayanthi/staging-spotify/artists.csv"], "recurse": True}, transformation_ctx="artists_node1727578716506")

# Script generated for node tracks
tracks_node1727578717073 = glueContext.create_dynamic_frame.from_options(format_options={"quoteChar": "\"", "withHeader": True, "separator": ",", "optimizePerformance": False}, connection_type="s3", format="csv", connection_options={"paths": ["s3://spotify-staging-vaijayanthi/staging-spotify/tracks.csv"], "recurse": True}, transformation_ctx="tracks_node1727578717073")

# Script generated for node albums
albums_node1727578441340 = glueContext.create_dynamic_frame.from_options(format_options={"quoteChar": "\"", "withHeader": True, "separator": ",", "optimizePerformance": False}, connection_type="s3", format="csv", connection_options={"paths": ["s3://spotify-staging-vaijayanthi/staging-spotify/albums.csv"], "recurse": True}, transformation_ctx="albums_node1727578441340")

# Script generated for node Join
Join_node1727578762106 = Join.apply(frame1=albums_node1727578441340, frame2=artists_node1727578716506, keys1=["artist_id"], keys2=["id"], transformation_ctx="Join_node1727578762106")

# Script generated for node Join tracks
Jointracks_node1727578787637 = Join.apply(frame1=tracks_node1727578717073, frame2=Join_node1727578762106, keys1=["track_id"], keys2=["track_id"], transformation_ctx="Jointracks_node1727578787637")

# Script generated for node Drop Fields
DropFields_node1727578818055 = DropFields.apply(frame=Jointracks_node1727578787637, paths=["`.track_id`", "id"], transformation_ctx="DropFields_node1727578818055")

# Script generated for node Destination
Destination_node1727578835404 = glueContext.write_dynamic_frame.from_options(frame=DropFields_node1727578818055, connection_type="s3", format="glueparquet", connection_options={"path": "s3://spotify-staging-vaijayanthi/datawarehouse/", "partitionKeys": []}, format_options={"compression": "snappy"}, transformation_ctx="Destination_node1727578835404")

job.commit()