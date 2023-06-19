from pydantic import BaseModel
from typing import Optional
import logging

logger = logging.getLogger(__name__)


class Book(BaseModel):
    id: Optional[int]
    title: Optional[str]
    subtitle: Optional[str]
    description: Optional[str]
    short_description: Optional[str]
    chapters: Optional[list["Chapter"]] = []


class Chapter(BaseModel):
    id: Optional[int]
    title: Optional[str]
    subtitle: Optional[str]
    description: Optional[str]
    short_description: Optional[str]
    book_id: Optional[int]
    book: Optional[Book]
    subchapters: Optional[list["Subchapter"]] = []


class Subchapter(BaseModel):
    id: Optional[int]
    title: Optional[str]
    subtitle: Optional[str]
    description: Optional[str]
    short_description: Optional[str]
    chapter_id: Optional[int]
    chapter: Optional[Chapter]
    sections: Optional[list["Section"]] = []


class Section(BaseModel):
    id: Optional[int]
    title: Optional[str]
    subtitle: Optional[str]
    description: Optional[str]
    short_description: Optional[str]
    content: Optional[str]
    subchapter_id: Optional[int]
    subchapter: Optional[Subchapter]


Book.update_forward_refs()
Chapter.update_forward_refs()
Subchapter.update_forward_refs()
