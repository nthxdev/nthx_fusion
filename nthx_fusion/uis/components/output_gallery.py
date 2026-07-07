from pathlib import Path
from typing import List, Optional

import gradio

OUTPUT_GALLERY : Optional[gradio.Gallery] = None
OUTPUT_GALLERY_REFRESH_BUTTON : Optional[gradio.Button] = None
OUTPUT_GALLERY_INFO : Optional[gradio.Markdown] = None

MEDIA_EXTENSIONS = { '.bmp', '.jpeg', '.jpg', '.png', '.tiff', '.webp', '.gif', '.mp4', '.mov', '.webm', '.mkv' }


def render() -> None:
	global OUTPUT_GALLERY
	global OUTPUT_GALLERY_REFRESH_BUTTON
	global OUTPUT_GALLERY_INFO

	with gradio.Column(elem_classes = [ 'nthx-panel', 'nthx-reveal' ]):
		gradio.Markdown('### Output Gallery')
		OUTPUT_GALLERY_INFO = gradio.Markdown(value = summarize_outputs())
		OUTPUT_GALLERY = gradio.Gallery(value = collect_outputs(), columns = 4, object_fit = 'cover', show_label = False)
		OUTPUT_GALLERY_REFRESH_BUTTON = gradio.Button(value = 'Refresh gallery', size = 'sm')


def listen() -> None:
	OUTPUT_GALLERY_REFRESH_BUTTON.click(refresh, outputs = [ OUTPUT_GALLERY_INFO, OUTPUT_GALLERY ])


def refresh() -> tuple[str, List[str]]:
	return summarize_outputs(), collect_outputs()


def collect_outputs() -> List[str]:
	output_root = Path('output')
	if not output_root.exists():
		return []
	return [ str(path) for path in sorted(output_root.rglob('*'), key = lambda item: item.stat().st_mtime, reverse = True) if path.is_file() and path.suffix.lower() in MEDIA_EXTENSIONS ][:48]


def summarize_outputs() -> str:
	outputs = collect_outputs()
	if not outputs:
		return 'No output folder is bundled. Generated media appears here when users choose an output path inside `output/` or refresh after a run.'
	return f'Found **{len(outputs)}** recent media outputs.'
