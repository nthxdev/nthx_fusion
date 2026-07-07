from pathlib import Path
import re
from typing import Any, List, Optional
import gradio

from nthx_fusion.execution import get_available_execution_providers
from nthx_fusion.filesystem import get_file_name, resolve_file_paths

MODEL_MANAGER_DATAFRAME : Optional[gradio.Dataframe] = None
MODEL_MANAGER_REFRESH_BUTTON : Optional[gradio.Button] = None
MODEL_MANAGER_SUMMARY : Optional[gradio.Markdown] = None


def render() -> None:
	global MODEL_MANAGER_DATAFRAME
	global MODEL_MANAGER_REFRESH_BUTTON
	global MODEL_MANAGER_SUMMARY

	with gradio.Column(elem_classes = [ 'nthx-panel', 'nthx-reveal' ]):
		gradio.Markdown('### Model Manager')
		MODEL_MANAGER_SUMMARY = gradio.Markdown(value = summarize_models())
		MODEL_MANAGER_DATAFRAME = gradio.Dataframe(
			headers = [ 'model', 'size_mb', 'status', 'used_by' ],
			datatype = [ 'str', 'str', 'str', 'str' ],
			value = collect_model_rows(),
			interactive = False,
			wrap = True,
			show_label = False
		)
		MODEL_MANAGER_REFRESH_BUTTON = gradio.Button(value = 'Refresh models', size = 'sm')


def listen() -> None:
	MODEL_MANAGER_REFRESH_BUTTON.click(refresh, outputs = [ MODEL_MANAGER_SUMMARY, MODEL_MANAGER_DATAFRAME ])


def refresh() -> tuple[str, List[List[str]]]:
	return summarize_models(), collect_model_rows()


def get_all_referenced_models() -> dict[str, List[str]]:
	referenced_models = {}
	code_files = [ path for path in Path('nthx_fusion').rglob('*.py') ]
	for code_file in code_files:
		content = code_file.read_text(errors = 'ignore')
		matches = re.findall(r'\.assets/models/([^/\'\"]+\.onnx)', content)
		for m in matches:
			if m not in referenced_models:
				referenced_models[m] = []
			category = code_file.parts[-2] if len(code_file.parts) > 2 else code_file.name
			referenced_models[m].append(category)
	return referenced_models


def summarize_models() -> str:
	referenced = get_all_referenced_models()
	downloaded = []
	for m in referenced.keys():
		if (Path('.assets/models') / m).exists():
			downloaded.append(m)

	total_bytes = sum(path.stat().st_size for path in Path('.assets/models').glob('*') if path.is_file())
	processors = [ get_file_name(file_path) for file_path in resolve_file_paths('nthx_fusion/processors/modules') ]
	providers = ', '.join(get_available_execution_providers())
	return f'ONNX Models: **{len(downloaded)}** / **{len(referenced)}** Downloaded | Asset size: **{total_bytes / 1024 / 1024 / 1024:.2f} GB** | Processors: **{len(processors)}** | Providers: **{providers}**'


def collect_model_rows() -> List[List[Any]]:
	rows = []
	models_dir = Path('.assets/models')
	referenced = get_all_referenced_models()

	for model_name in sorted(referenced.keys()):
		onnx_path = models_dir / model_name
		categories = sorted(set(referenced[model_name]))
		used_by = ', '.join(categories) or 'not wired'

		if onnx_path.exists():
			status = 'Downloaded'
			size_val = str(round(onnx_path.stat().st_size / 1024 / 1024, 2))
		else:
			status = 'Not Downloaded'
			size_val = '-'

		rows.append(
		[
			model_name,
			size_val,
			status,
			used_by
		])
	return rows
