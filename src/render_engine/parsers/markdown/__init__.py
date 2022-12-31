import pathlib
from typing import Any

import frontmatter
from markdown2 import markdown

from ..base_parsers import BasePageParser


def _attrs_from_content(content):
    """fetches the content"""
    return frontmatter.parse(content)


class MarkdownParser(BasePageParser):
    markdown_extras: list[str] | None

    @property
    def configuration_values(self) -> list[str]:
        """Returns the configuration values that are used by the parser"""
        return ["markdown_extras"]

    def attrs_from_content_path(self, content_path):
        """fetches the content"""
        content = pathlib.Path(content_path).read_text()
        return _attrs_from_content(content)

    def attrs_from_content(self, content):
        """fetches the content"""
        return _attrs_from_content(content)

    def parse(self, content) -> str:
        """Parses the content with the parser"""
        return markdown(content, extras=self.markdown_extras or [])
