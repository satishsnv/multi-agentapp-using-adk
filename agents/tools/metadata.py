from agents.models import FileSummaryClassificationOutput
import logging

logger = logging.getLogger(__name__)


async def update_metadata(metadata_object: FileSummaryClassificationOutput) -> str:
    """update the metadata by connecting to mds store using the input FileSummaryClassificationOutput format.

    Args:
        metadata_object (FileSummaryClassificationOutput): The metadata object to update.

    Returns:
        str: success or failure message  along with reason.
    """

    # Simulate fetching file content
    # In a real implementation, this would read the file from storage
    message = "File content updated successfully."

    if not isinstance(metadata_object, FileSummaryClassificationOutput):
        logging.info( "Invalid metadata object format.")
        message = "Failed to update file content. Invalid metadata object format."
    else:
        logging.info("Fetching file content for metadata object.")

    return message

