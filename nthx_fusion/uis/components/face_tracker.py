from typing import Optional

import gradio

import nthx_fusion.choices
from nthx_fusion import state_manager, translator
from nthx_fusion.common_helper import calculate_float_step
from nthx_fusion.types import Score
from nthx_fusion.uis.core import register_ui_component

FACE_TRACKER_SCORE_SLIDER : Optional[gradio.Slider] = None


def render() -> None:
	global FACE_TRACKER_SCORE_SLIDER

	FACE_TRACKER_SCORE_SLIDER = gradio.Slider(
		label = translator.get('uis.face_tracker_score_slider'),
		value = state_manager.get_item('face_tracker_score'),
		step = calculate_float_step(nthx_fusion.choices.face_tracker_score_range),
		minimum = nthx_fusion.choices.face_tracker_score_range[0],
		maximum = nthx_fusion.choices.face_tracker_score_range[-1]
	)
	register_ui_component('face_tracker_score_slider', FACE_TRACKER_SCORE_SLIDER)


def listen() -> None:
	FACE_TRACKER_SCORE_SLIDER.release(update_face_tracker_score, inputs = FACE_TRACKER_SCORE_SLIDER)


def update_face_tracker_score(face_tracker_score : Score) -> None:
	state_manager.set_item('face_tracker_score', face_tracker_score)
