from pathlib import Path

import gradio

from nthx_fusion import metadata
from nthx_fusion.execution import get_available_execution_providers
from nthx_fusion.filesystem import get_file_name, resolve_file_paths


def render() -> None:
	model_count = len(list(Path('.assets/models').glob('*.onnx')))
	model_size = sum(path.stat().st_size for path in Path('.assets/models').glob('*') if path.is_file())
	model_size_gb = model_size / 1024 / 1024 / 1024
	processors = [ get_file_name(file_path) for file_path in resolve_file_paths('nthx_fusion/processors/modules') ]
	providers = get_available_execution_providers()

	gradio.HTML(
		f'''
		<section class="nthx-hero nthx-reveal">
			<div class="nthx-hero-copy">
				<div class="nthx-kicker">NTHX Lab / Local AI Studio</div>
				<h1>{metadata.get('name')}</h1>
				<p>{metadata.get('description')}. Build image and video face workflows with local ONNX models, GPU acceleration, and a focused browser control surface.</p>
				<div class="nthx-chip-row">
					<span>{len(processors)} processors</span>
					<span>{model_count} ONNX models</span>
					<span>{model_size_gb:.2f} GB assets</span>
					<span>{' / '.join(providers)}</span>
				</div>
			</div>
			<div class="nthx-orbit" aria-hidden="true">
				<div class="nthx-orbit-core">NX</div>
				<span></span><span></span><span></span>
			</div>
		</section>
		'''
	)


def listen() -> None:
	pass
