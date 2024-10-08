import os

ODP_CORE_S3_BUCKET_URI = 's3://geoglows-v2'
ODP_FORECAST_S3_BUCKET_URI = 's3://geoglows-v2-forecasts'
ODP_RETROSPECTIVE_S3_BUCKET_URI = 's3://geoglows-v2-retrospective'
ODP_S3_BUCKET_REGION = 'us-west-2'

METADATA_TABLE_PATH = os.getenv(
    'PYGEOGLOWS_METADATA_TABLE_PATH',
    os.path.join(os.path.dirname(__file__), 'data', 'metadata-tables.parquet')
)

SABER_ASSIGN_TABLE_PATH = os.getenv(
    'PYGEOGLOWS_SABER_ASSIGN_TABLE_PATH',
    os.path.join(os.path.dirname(__file__), 'data', 'saber-assign-table.parquet'))

SFDC_TABLE_PATH = os.getenv(
    'PYGEOGLOWS_SFDC_TABLE_PATH',
    os.path.join(os.path.dirname(__file__), 'data', 'sfdc-removing-zero.parquet'))

FDC_TABLE_PATH = os.getenv(
    'PYGEOGLOWS_FDC_TABLE_PATH',
    os.path.join(os.path.dirname(__file__), 'data', 'simulated_monthly.parquet'))


def get_metadata_table_path() -> str:
    return METADATA_TABLE_PATH


def set_metadata_table_path(path: str) -> str:
    global METADATA_TABLE_PATH
    METADATA_TABLE_PATH = path
    return METADATA_TABLE_PATH

def get_saber_assign_table_path() -> str:
    return SABER_ASSIGN_TABLE_PATH

def set_saber_assign_table_path(path: str) -> str:
    global SABER_ASSIGN_TABLE_PATH
    SABER_ASSIGN_TABLE_PATH = path
    return SABER_ASSIGN_TABLE_PATH

def get_sfdc_table_path() -> str:
    return SFDC_TABLE_PATH

def set_sfdc_table_path(path: str) -> str:
    global SFDC_TABLE_PATH
    SFDC_TABLE_PATH = path
    return SFDC_TABLE_PATH

def get_fdc_table_path() -> str:
    return FDC_TABLE_PATH

def set_fdc_table_path(path: str) -> str:
    global FDC_TABLE_PATH
    FDC_TABLE_PATH = path
    return FDC_TABLE_PATH