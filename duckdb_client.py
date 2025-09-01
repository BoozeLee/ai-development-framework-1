#!/usr/bin/env python3
"""
DuckDB Client for Local Data Analysis

This module provides a simple interface for analyzing local data files
using DuckDB, a fast analytical database system.
"""

import sys
sys.path.insert(0, '/home/booze/ai-development/aws-env/lib/python3.11/site-packages')

import duckdb
from typing import Optional, Union


class LocalDataAnalyzer:
    """
    A client for performing local data analysis using DuckDB.
    
    This class provides methods to query CSV, JSON, and other data files
    using SQL syntax through DuckDB's interface.
    """
    
    def __init__(self, database_path: Optional[str] = None):
        """
        Initialize the DuckDB connection.
        
        Args:
            database_path: Optional path to a persistent database file.
                          If None, uses in-memory database.
        """
        self.conn = duckdb.connect(database_path)
    
    def query_csv(self, file_path: str, limit: int = 10):
        """
        Query a CSV file and return results.
        
        Args:
            file_path: Path to the CSV file to query
            limit: Maximum number of rows to return (default: 10)
            
        Returns:
            DuckDB result object containing the query results
        """
        return self.conn.sql(f"SELECT * FROM '{file_path}' LIMIT {limit}")
    
    def query_json(self, file_path: str):
        """
        Query a JSON file and return results.
        
        Args:
            file_path: Path to the JSON file to query
            
        Returns:
            DuckDB result object containing the query results
        """
        return self.conn.sql(f"SELECT * FROM '{file_path}'")
    
    def analyze_folder(self, pattern: str):
        """
        Analyze multiple files in a folder using a pattern.
        
        Args:
            pattern: Glob pattern to match files (e.g., '*.csv')
            
        Returns:
            DuckDB result object containing the analysis results
        """
        return self.conn.sql(f"SELECT * FROM '{pattern}'")
    
    def close(self):
        """Close the DuckDB connection."""
        if self.conn:
            self.conn.close()


# Ready to use
analyzer = LocalDataAnalyzer()
print("🦆 DuckDB ready for local data analysis")