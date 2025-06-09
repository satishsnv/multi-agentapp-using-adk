from typing import List
from pydantic import BaseModel, Field


class Sentiment(BaseModel):
    label: str = Field(default="neutral", description="Sentiment label, e.g., positive, negative, neutral")
    score: float = Field(default=0.0, description="Sentiment score, between -1 and 1")


class FileSummaryClassificationOutput(BaseModel):
    file_id: str = Field(default="", description="Unique identifier for the file")
    summary: List[str] = Field(default=[], description="Summary of the file content in a list of strings")
    classification: List[str] = Field(default=[], description="List of classifications for the file content")
    sentiment: Sentiment = Field(default=Sentiment(label="neutral", score=0.0), description="Sentiment analysis result")


class FileContent(BaseModel):
    file_content: List[str] = Field(default=[], description="List of file content items")
    file_id: str = Field(default="", description="Unique identifier for the file")