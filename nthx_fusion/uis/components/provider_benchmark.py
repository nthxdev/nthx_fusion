from typing import List, Optional

import gradio
import onnxruntime

from nthx_fusion.execution import get_available_execution_providers

PROVIDER_BENCHMARK_DATAFRAME : Optional[gradio.Dataframe] = None
PROVIDER_BENCHMARK_REFRESH_BUTTON : Optional[gradio.Button] = None


def render() -> None:
	global PROVIDER_BENCHMARK_DATAFRAME
	global PROVIDER_BENCHMARK_REFRESH_BUTTON

	with gradio.Column(elem_classes = [ 'nthx-panel', 'nthx-reveal' ]):
		gradio.Markdown('### CPU / CUDA / TensorRT Providers')
		PROVIDER_BENCHMARK_DATAFRAME = gradio.Dataframe(
			headers = [ 'provider', 'available', 'role' ],
			datatype = [ 'str', 'str', 'str' ],
			value = collect_provider_rows(),
			interactive = False,
			show_label = False
		)
		PROVIDER_BENCHMARK_REFRESH_BUTTON = gradio.Button(value = 'Refresh providers', size = 'sm')


def listen() -> None:
	PROVIDER_BENCHMARK_REFRESH_BUTTON.click(collect_provider_rows, outputs = PROVIDER_BENCHMARK_DATAFRAME)


def collect_provider_rows() -> List[List[str]]:
	available = set(get_available_execution_providers())
	runtime_available = set(onnxruntime.get_available_providers())
	provider_roles =\
	{
		'cpu': 'portable fallback',
		'cuda': 'NVIDIA GPU execution',
		'tensorrt': 'NVIDIA optimized engine',
		'directml': 'Windows GPU fallback',
		'coreml': 'Apple acceleration',
		'openvino': 'Intel acceleration'
	}
	rows = []
	for provider, role in provider_roles.items():
		runtime_key =\
		{
			'cpu': 'CPUExecutionProvider',
			'cuda': 'CUDAExecutionProvider',
			'tensorrt': 'TensorrtExecutionProvider'
		}.get(provider)
		is_available = provider in available or runtime_key in runtime_available
		rows.append([ provider, 'yes' if is_available else 'no', role ])
	return rows
