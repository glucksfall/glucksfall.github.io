from typing import Union
from docutils.nodes import document
from docutils.statemachine import StringList
from sphinx.parsers import RSTParser

class NoTabExpansionRSTParser(RSTParser):
	def parse(self, inputstring: Union[str, StringList], document: document) -> None:
		if isinstance(inputstring, str):
			lines = inputstring.splitlines()
			inputstring = StringList(lines, document.current_source)
		super().parse(inputstring, document)

def setup(app):
	app.add_source_parser(NoTabExpansionRSTParser, override=True)
