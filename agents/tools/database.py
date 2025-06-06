from typing import Dict, Any

async def fetch_db_constraints_and_metadata(resource_id: str) -> Dict[str, Any]:
    # Simulate fetching database constraints and metadata
    # In a real implementation, this would query the database
    """Fetch constraints and metadata of the database by connecting to it based on resource_id.
    Args:
        resource_id (str): ID of the database whose constraints and metadata are to be fetched.

    Returns:
        Dict[str, Any]: returns a dictionary containing the database constraints and metadata.
    """
    print (f"Fetching constraints and metadata for input: {resource_id}")
    metadata = {
        "table_name": "users",
        "columns": ["id", "name", "salary", "organization_id", "dob"],
        "constraints": {
            "id": "PRIMARY KEY",
            "name": "NOT NULL",
            "salary": "CHECK (salary > 0)",
        }
    }
    return metadata