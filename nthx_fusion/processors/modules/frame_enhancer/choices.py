from typing import List, Sequence, get_args

from nthx_fusion.common_helper import create_int_range
from nthx_fusion.processors.modules.frame_enhancer.types import FrameEnhancerModel

frame_enhancer_models : List[FrameEnhancerModel] = list(get_args(FrameEnhancerModel))

frame_enhancer_blend_range : Sequence[int] = create_int_range(0, 100, 1)
