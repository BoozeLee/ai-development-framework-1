#!/usr/bin/env python3
import sys
sys.path.insert(0, '/home/booze/ai-development/aws-env/lib/python3.11/site-packages')

from aws_athena_client import AthenaClient

# Test Athena connection
athena = AthenaClient()
print("✅ AWS Athena client ready")
print(f"Account: 022787321020")
print(f"User: Boozelee")
print(f"S3 Output: {athena.s3_output}")