from typing import Optional

METADATA =\
{
	'name': 'NTHX Fusion',
	'description': 'Local AI face and media manipulation studio',
	'version': '0.1.0',
	'license': 'OpenRAIL-AS',
	'author': 'NTHX Lab',
	'url': 'http://localhost:7860'
}


def get(key : str) -> Optional[str]:
	return METADATA.get(key)
