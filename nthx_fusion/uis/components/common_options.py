from typing import List, Optional

import gradio

from nthx_fusion import state_manager, translator
from nthx_fusion.uis import choices as uis_choices

COMMON_OPTIONS_CHECKBOX_GROUP : Optional[gradio.CheckboxGroup] = None


def render() -> None:
	global COMMON_OPTIONS_CHECKBOX_GROUP

	common_options = []

	if state_manager.get_item('keep_temp'):
		common_options.append('keep-temp')
	if state_manager.get_item('skip_content_analysis'):
		common_options.append('skip-content-analysis')

	COMMON_OPTIONS_CHECKBOX_GROUP = gradio.CheckboxGroup(
		label = translator.get('uis.common_options_checkbox_group'),
		choices = uis_choices.common_options,
		value = common_options
	)


def listen() -> None:
	COMMON_OPTIONS_CHECKBOX_GROUP.change(update, inputs = COMMON_OPTIONS_CHECKBOX_GROUP)


def update(common_options : List[str]) -> None:
	keep_temp = 'keep-temp' in common_options
	state_manager.set_item('keep_temp', keep_temp)
	skip_content_analysis = 'skip-content-analysis' in common_options
	state_manager.set_item('skip_content_analysis', skip_content_analysis)
