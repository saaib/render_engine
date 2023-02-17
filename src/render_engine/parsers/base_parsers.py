import pathlib
from typing import Any, Type

import frontmatter


def check_for_attrs(page, attrs):
    missing_attrs = []
    for attr in attrs:
        if not getattr(page, attr, None):
            missing_attrs.append(attr)
    return missing_attrs


class BasePageParser:
    configuration_values: list[str]

    def get_configuration_values(self, page):
        return {attr: getattr(page, attr, None) for attr in self.configuration_values}

    def raise_for_errors(self, page):
        if missing_attrs := check_for_attrs(
            page, getattr(self, "configuration_values", [])
        ):
            raise ValueError(
                f"Missing configuration values for {self.__class__.__name__}: {missing_attrs}"
            )

    @staticmethod
    def parse_content_path(content_path):
        """
        Fething content from a content_path and set attributes.
        """
        return pathlib.Path(content_path).read_text()

    @staticmethod
    def parse_content(content: str):
        """Fething content and atttributes from a content_path"""
        return frontmatter.parse(content)

    @staticmethod
    def markup(content: str, page: "Page"):
        """Convert the raw_content into HTML"""
        return content