"""Tests standard target features using the built-in SDK tests library."""

from __future__ import annotations

import typing as t

import pytest
from singer_sdk.testing import get_target_test_class, SuiteConfig
from singer_sdk.testing.templates import TargetTestTemplate, TargetFileTestTemplate

from target_minios3parquet.target import TargetMinioS3Parquet

# TODO: Initialize minimal target config
SAMPLE_CONFIG: dict[str, t.Any] = {
    "AWS_ACCESS_KEY_ID": "minio",
    "AWS_SECRET_ACCESS_KEY": "minio123",
    "AWS_ENDPOINT_URL": "http://minio:9000",
    "bucket": "test-bucket",
    "folder_structure": "simple",
}

# Run standard built-in target tests from the SDK:
StandardTargetTests = get_target_test_class(
    target_class=TargetMinioS3Parquet,
    config=SAMPLE_CONFIG,
)

class TestTargetMinioS3Parquet(StandardTargetTests):  # type: ignore[misc, valid-type]  # noqa: E501
    """Standard Target Tests."""

    @pytest.fixture(scope="class")
    def resource(self):  # noqa: ANN201
        """Generic external resource.

        This fixture is useful for setup and teardown of external resources,
        such output folders, tables, buckets etc. for use during testing.

        Example usage can be found in the SDK samples test suite:
        https://github.com/meltano/sdk/tree/main/tests/samples
        """
        return "resource"
