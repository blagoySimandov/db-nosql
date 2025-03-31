from pymongo import MongoClient


def main():
    # Connect to MongoDB
    client = MongoClient("mongodb://root:example@localhost:27017/")

    # Create or access a database
    db = client["example_db"]

    # Create or access a collection
    collection = db["example_collection"]

    # Example document
    example_document = {
        "name": "John Doe",
        "age": 30,
        "email": "john.doe@example.com",
        "address": {
            "street": "123 Main St",
            "city": "New York",
            "state": "NY",
            "zip": "10001",
        },
        "interests": ["programming", "database", "mongodb"],
    }

    # Insert the document
    result = collection.insert_one(example_document)

    # Print the document ID
    print(f"Document inserted with ID: {result.inserted_id}")

    # Query the document to verify
    inserted_doc = collection.find_one({"_id": result.inserted_id})
    print("Inserted document:")
    print(inserted_doc)


if __name__ == "__main__":
    main()

