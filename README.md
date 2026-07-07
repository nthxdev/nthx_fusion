NTHX Fusion
===========

A customized and modified version of the original [FaceFusion](https://github.com/facefusion/facefusion) project.

> Original project created by Henry Ruhs and the FaceFusion contributors.  
> This version includes custom modifications by [nthxdev](https://github.com/nthxdev), including renamed branding, UI changes, added flags, and workflow updates.


Local AI face and media manipulation tool powered by Python, Gradio, FFmpeg, OpenCV, ONNX Runtime, and local ONNX model assets.

Important Notice
----------------

This project contains upstream-derived code and model integration patterns. Keep the included license/notice files and follow the applicable source and model licenses when redistributing or commercializing it.

Clean Project Shape
-------------------

The project does not include `input/` or `output/` folders by default.

Users provide paths themselves:

- CLI: pass source, target, and output paths with flags.
- UI: drag/drop files or choose files from the browser interface.


Installation Guide
------------------

To run NTHX Fusion, your system needs native command-line dependencies (like **FFmpeg**) and execution runtimes (like **CUDA** for GPU acceleration).

### 1. Prerequisites (Platform-Specific)

#### Ubuntu / WSL2 / Debian
Install the required system utilities using your package manager:
```bash
sudo apt update && sudo apt install -y git curl ffmpeg
```

#### macOS
Install using **Homebrew**:
```bash
brew install git curl ffmpeg
```

#### Windows
1. Install **Git** from [git-scm.com](https://git-scm.com/).
2. Install **FFmpeg** from [ffmpeg.org](https://ffmpeg.org/) (ensure `ffmpeg` is added to your system's Environment Variables `PATH`).

---

### 2. Environment Setup (Cross-Platform)

We recommend using **Miniconda** to manage isolated environments and CUDA runtimes.

1. **Install Miniconda:**
   Follow instructions for your OS on [docs.anaconda.com/miniconda](https://docs.anaconda.com/miniconda/).
2. **Create and Activate Python 3.12 Environment:**
   ```bash
   conda create --name nthx_fusion python=3.12 pip=25.0 -y
   conda activate nthx_fusion
   ```

---

### 3. GPU Acceleration Setup (Optional)

If you have an NVIDIA GPU and want fast processing, install the version-locked CUDA and cuDNN runtimes inside your Conda environment:

#### Windows / Linux / WSL2 (NVIDIA GPU)
```bash
conda install nvidia/label/cuda-12.9.1::cuda-runtime nvidia/label/cudnn-9.10.0::cudnn -y
```

---

### 4. Clone and Install Dependencies

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/nthxdev/nthx_fusion.git
   cd nthx_fusion
   ```
2. **Run Installer:**
   Choose the appropriate installer command depending on your hardware:
   * **For NVIDIA GPU:**
     ```bash
     python install.py --onnxruntime cuda
     ```
   * **For Apple Silicon (macOS):**
     ```bash
     python install.py --onnxruntime coreml
     ```
   * **For CPU Only:**
     ```bash
     python install.py --onnxruntime default
     ```


Quick Test
----------

```bash
python nthx_fusion.py --version
```

Expected output:

```text
NTHX Fusion 0.1.0
```

Commands
--------

```text
run              start the browser UI
headless-run     process one target from CLI
batch-run        process source/target patterns from CLI
force-download   download required model assets
benchmark        benchmark processing
job-list         list jobs by status
job-create       create a job
job-submit       submit one job
job-submit-all   submit all jobs
job-delete       delete one job
job-delete-all   delete all jobs
job-add-step     add a step to a job
job-remix-step   reuse output from a previous step
job-insert-step  insert a step into a job
job-remove-step  remove a step from a job
job-run          run one queued job
job-run-all      run all queued jobs
job-retry        retry one failed job
job-retry-all    retry all failed jobs
```

Common CLI Flags
----------------

```text
-h, --help                     show help
-v, --version                  show version
--config-path PATH             config file path
--temp-path PATH               temporary resource path
--jobs-path PATH               jobs directory path
-s, --source-paths PATH...     source image/audio paths
-t, --target-path PATH         target image/video path
-o, --output-path PATH         output image/video path
--source-pattern PATTERN       batch source pattern
--target-pattern PATTERN       batch target pattern
--output-pattern PATTERN       batch output pattern
--processors NAME...           processors to run
--skip-content-analysis        skip content analysis guard
--log-level LEVEL              error, warn, info, debug
```

Execution Flags
---------------

```text
--execution-device-ids ID...          GPU/device ids
--execution-providers PROVIDER...     inference providers
--execution-thread-count COUNT        processing thread count
--download-providers PROVIDER...      model download providers
--download-scope lite|full            model download scope
--video-memory-strategy STRATEGY      strict, moderate, tolerant
```

Face Detection And Selection Flags
----------------------------------

```text
--face-detector-model MODEL
--face-detector-size SIZE
--face-detector-margin TOP RIGHT BOTTOM LEFT
--face-detector-angles ANGLE...
--face-detector-score SCORE
--face-landmarker-model MODEL
--face-landmarker-score SCORE
--face-selector-mode MODE
--face-selector-order ORDER
--face-selector-age-start AGE
--face-selector-age-end AGE
--face-selector-gender GENDER
--face-selector-race RACE
--reference-face-position INDEX
--reference-face-distance DISTANCE
--reference-frame-number NUMBER
--face-tracker-score SCORE
```

Masking Flags
-------------

```text
--face-occluder-model MODEL
--face-parser-model MODEL
--face-mask-types TYPE...
--face-mask-areas AREA...
--face-mask-regions REGION...
--face-mask-blur VALUE
--face-mask-padding TOP RIGHT BOTTOM LEFT
```

Frame And Output Flags
----------------------

```text
--trim-frame-start NUMBER
--trim-frame-end NUMBER
--temp-frame-format FORMAT
--keep-temp
--target-frame-amount COUNT
--output-image-quality QUALITY
--output-image-scale SCALE
--output-audio-encoder ENCODER
--output-audio-quality QUALITY
--output-audio-volume VOLUME
--output-video-encoder ENCODER
--output-video-preset PRESET
--output-video-quality QUALITY
--output-video-scale SCALE
--output-video-fps FPS
```

Processor Option Flags
----------------------

Available processor-specific flags depend on selected processors. Use command help to see the complete current list:

```bash
python nthx_fusion.py headless-run --help
```

Examples of processor option groups:

```text
age modifier
background remover
deep swapper
expression restorer
face debugger
face editor
face enhancer
face swapper
frame colorizer
frame enhancer
lip syncer
voice extractor
```

Model Assets
------------

Model files live in:

```text
.assets/models/
```

The project can run ONNX models that are wired into its processors. A random ONNX file needs a matching adapter/processor for preprocessing, inference, and output decoding.

Project Layout
--------------

```text
nthx_fusion.py          main entrypoint
nthx_fusion.ini         default config
nthx_fusion/            internal Python package
.assets/models/         downloaded model assets
requirements.txt        Python requirements
LICENSE.md              license notice
tests/                  test suite
```

Maintainer -> nthxlabs
