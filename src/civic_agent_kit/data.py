"""Data loaders for Kenya civic datasets."""
import pandas as pd
from pathlib import Path

_DATA_DIR = Path(__file__).parent.parent.parent / "civic_data"


class KenyaBudgetData:
    """Controller of Budget county budget execution data."""
    @staticmethod
    def load(data_dir: Path = None) -> pd.DataFrame:
        path = (data_dir or _DATA_DIR) / "county_budgets_fy2223.csv"
        if not path.exists():
            raise FileNotFoundError(f"Budget data not found at {path}. Download from https://doi.org/10.34740/kaggle/dsv/15473045")
        return pd.read_csv(path)


class KenyaParliamentData:
    """Kenya 13th Parliament data — MPs, bills, CDF."""
    @staticmethod
    def load_mps(data_dir: Path = None) -> pd.DataFrame:
        return pd.read_csv((data_dir or _DATA_DIR) / "mps_seed.csv")

    @staticmethod
    def load_bills(data_dir: Path = None) -> pd.DataFrame:
        return pd.read_csv((data_dir or _DATA_DIR) / "bills_seed.csv")

    @staticmethod
    def load_cdf(data_dir: Path = None) -> pd.DataFrame:
        return pd.read_csv((data_dir or _DATA_DIR) / "cdf_seed.csv")


class KenyaSACCOData:
    """SASRA SACCO registry."""
    @staticmethod
    def load(data_dir: Path = None) -> pd.DataFrame:
        return pd.read_csv((data_dir or _DATA_DIR) / "saccos_seed.csv")
