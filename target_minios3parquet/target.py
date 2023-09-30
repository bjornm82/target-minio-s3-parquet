"""MinioS3Parquet target class."""

from __future__ import annotations

from singer_sdk import typing as th
from singer_sdk.target_base import Target

from target_minios3parquet.sinks import (
    MinioS3ParquetSink,
)


class TargetMinioS3Parquet(Target):
    """Sample target for MinioS3Parquet."""

    name = "target-minios3parquet"

    config_jsonschema = th.PropertiesList(
        th.Property(
            "AWS_ACCESS_KEY_ID",
            th.StringType,
            description="Specifies an AWS access key associated with an IAM account.",
            required=True,
        ),
        th.Property(
            "AWS_SECRET_ACCESS_KEY",
            th.StringType,
            description="Specifies the secret key associated with the access key. This is essentially the \"password\" for the access key.",
            required=True,
            secret=True,
        ),
        th.Property(
            "AWS_REGION",
            th.StringType,
            description="The AWS SDK compatible environment variable that specifies the AWS Region to send the request to.",
            required=False,
        ),
        th.Property(
            "AWS_ENDPOINT_URL",
            th.StringType,
            description="Specifies the endpoint that is used for all service requests.",
            required=False,
        ),
        th.Property(
            "bucket",
            th.StringType,
            description="The bucket that is used to store the data in.",
        ),
        th.Property(
            "folder_structure",
            th.StringType,
            description="Enumeration of the structure"
        ),
    ).to_dict()

    default_sink_class = MinioS3ParquetSink


if __name__ == "__main__":
    TargetMinioS3Parquet.cli()
