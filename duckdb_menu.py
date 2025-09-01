#!/usr/bin/env python3
import sys

sys.path.insert(0, "/home/booze/ai-development/aws-env/lib/python3.11/site-packages")

import os

import duckdb


def show_menu():
    print("\n🦆 DuckDB Data Analyzer - Easy Mode")
    print("1. 📊 Browse my CSV files")
    print("2. 📄 Browse my JSON files")
    print("3. 🏠 Analyze home folder")
    print("4. 📁 Quick folder scan")
    print("5. 💻 Custom SQL (advanced)")
    print("6. ❓ Help & Examples")
    print("7. 🚪 Exit")
    return input("\n👉 Choose option (1-7): ")


def main():
    conn = duckdb.connect()

    while True:
        choice = show_menu()

        if choice == "1":
            print("\n📊 Finding CSV files in your home...")
            try:
                result = conn.sql("SELECT * FROM glob('/home/booze/**/*.csv') LIMIT 20")
                files = result.fetchall()
                if files:
                    for i, file in enumerate(files, 1):
                        print(f"{i}. {file[0]}")
                    choice = input("\nEnter file number to preview (or press Enter): ")
                    if choice.isdigit() and int(choice) <= len(files):
                        file_path = files[int(choice) - 1][0]
                        preview = conn.sql(f"SELECT * FROM '{file_path}' LIMIT 5")
                        print(f"\n📋 Preview of {file_path}:")
                        print(preview.fetchall())
                else:
                    print("No CSV files found")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "2":
            print("\n📄 Finding JSON files in your home...")
            try:
                result = conn.sql(
                    "SELECT * FROM glob('/home/booze/**/*.json') LIMIT 20"
                )
                files = result.fetchall()
                if files:
                    for i, file in enumerate(files, 1):
                        print(f"{i}. {file[0]}")
                else:
                    print("No JSON files found")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "3":
            print("\n🏠 Analyzing your home folder...")
            try:
                result = conn.sql(
                    """
                SELECT
                    regexp_extract(file, '\.([^.]+)$', 1) as type,
                    COUNT(*) as count
                FROM glob('/home/booze/**/*.*')
                WHERE type IS NOT NULL
                GROUP BY type
                ORDER BY count DESC
                LIMIT 10
                """
                )
                print("\n📈 Top file types:")
                for row in result.fetchall():
                    print(f"  .{row[0]}: {row[1]} files")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "4":
            folder = input("\n📁 Enter folder path: ")
            try:
                result = conn.sql(f"SELECT * FROM glob('{folder}/*.csv') LIMIT 10")
                print(result.fetchall())
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "5":
            query = input("\n💻 Enter SQL query: ")
            try:
                result = conn.sql(query)
                print(result.fetchall())
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "6":
            print("\n❓ DuckDB Examples:")
            print("• SELECT * FROM 'file.csv' LIMIT 10")
            print("• SELECT COUNT(*) FROM 'folder/*.json'")
            print("• SELECT column, AVG(value) FROM 'data.csv' GROUP BY column")
            input("\nPress Enter to continue...")

        elif choice == "7":
            print("\n👋 Goodbye!")
            break
        else:
            print("\n❌ Invalid option. Please choose 1-7.")


if __name__ == "__main__":
    print("🦆 Welcome to DuckDB Data Analyzer!")
    print("Analyze your local files with SQL - no setup required!")
    main()
