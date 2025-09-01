"""
Basic tests for AI Development Framework
"""

import os
import sys

import pytest

# Add the parent directory to the path so we can import our modules
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestBasicFunctionality:
    """Test basic functionality of the framework"""

    def test_python_version(self):
        """Test that we're using Python 3.11+"""
        assert sys.version_info >= (3, 11), "Python 3.11+ required"

    def test_imports(self):
        """Test that we can import our main modules"""
        try:
            import crewai
            import duckdb
            import langchain
            import numpy
            import openai
            import pandas
            import torch
            import transformers

            assert True
        except ImportError as e:
            pytest.fail(f"Failed to import required module: {e}")

    def test_duckdb_connection(self):
        """Test DuckDB connection"""
        import duckdb

        conn = duckdb.connect(":memory:")
        result = conn.execute("SELECT 1 as test").fetchone()
        assert result[0] == 1
        conn.close()

    def test_pandas_import(self):
        """Test pandas functionality"""
        import pandas as pd

        df = pd.DataFrame({"test": [1, 2, 3]})
        assert len(df) == 3
        assert df["test"].sum() == 6


class TestConfiguration:
    """Test configuration loading"""

    def test_config_file_exists(self):
        """Test that config directory exists"""
        config_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "config")
        assert os.path.exists(config_dir), "Config directory should exist"

    def test_tools_directory_exists(self):
        """Test that tools directory exists"""
        tools_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "tools")
        assert os.path.exists(tools_dir), "Tools directory should exist"


class TestDocumentation:
    """Test documentation files"""

    def test_readme_exists(self):
        """Test that README.md exists"""
        readme_path = os.path.join(
            os.path.dirname(os.path.dirname(__file__)), "README.md"
        )
        assert os.path.exists(readme_path), "README.md should exist"

    def test_requirements_exists(self):
        """Test that requirements.txt exists"""
        req_path = os.path.join(
            os.path.dirname(os.path.dirname(__file__)), "requirements.txt"
        )
        assert os.path.exists(req_path), "requirements.txt should exist"

    def test_todo_exists(self):
        """Test that TODO.md exists"""
        todo_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "TODO.md")
        assert os.path.exists(todo_path), "TODO.md should exist"


if __name__ == "__main__":
    pytest.main([__file__])
