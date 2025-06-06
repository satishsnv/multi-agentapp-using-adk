from agents.models import FileContent
import pypdf


async def fetch_file_content(file_id: str) -> FileContent:
    """Fetch content for the specified file resource ID in the FileContent format.

    Args:
        file_id (str): The ID of the file to fetch content for.

    Returns:
        FileContent: list of file content items, along with file_id.
    """

    # Simulate fetching file content
    # In a real implementation, this would read the file from storage
    print(f"Fetching content for file ID: {file_id}")
    
    result = FileContent()        
    reader = pypdf.PdfReader('design_patterns.pdf')
    # Print the text of the first page

    data = ""
    for page in reader.pages:
        data += page.extract_text() + "\n"
        if(len(data) > 75000):
            result.content.append(data)
            data = ""
    if data:
        result.content.append(data)
    result.file_id = file_id
    return result

