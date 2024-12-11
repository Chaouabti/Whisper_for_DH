```markdown
# Whisper Transcription Project

This project provides a tool for transcribing audio files using OpenAI's Whisper model. It includes functionalities for managing Whisper models (downloading if needed) and transcribing audio files, with support for saving results in JSON and plain text formats.

---

## Features

- **Model Management**: Automatically downloads the required Whisper model if not already available.
- **Audio Transcription**: Transcribes audio files and saves results in `.json` and `.txt` formats.
- **Flexible Setup**: Supports installation with Conda (`environment.yml`) or a standard Python virtual environment (`requirements.txt`).

---

## Setup Instructions

> **Note**: This project requires **Python 3.10** or higher. Ensure that your environment meets this requirement before proceeding.

You can set up the project environment using either **Conda** or a **Python virtual environment**. Follow the steps for your preferred method.

---

### 1. Using Conda

#### Step 1: Clone the repository
```bash
git clone <https://github.com/Chaouabti/Whisper_for_DH.git>
cd <Whisper_for_DH>
```

#### Step 2: Create and activate the Conda environment
```bash
conda env create -f environment.yml
conda activate whisperenv
```

#### Step 3: Add the environment as a Jupyter kernel
If you plan to use the notebook, register the Conda environment as a Jupyter kernel:
```bash
python -m ipykernel install --user --name whisperenv --display-name "Python (whisperenv)"
```

---

### 2. Using a Python virtual environment

#### Step 1: Clone the repository
```bash
git clone <https://github.com/Chaouabti/Whisper_for_DH.git>
cd <Whisper_for_DH>
```

#### Step 2: Create and activate the virtual environment
Ensure that you are using Python 3.10 or higher when creating the virtual environment:
```bash
python -m venv whisperenv
source whisperenv/bin/activate  # On Windows: whisperenv\Scripts\activate
```

#### Step 3: Install dependencies
Install all required packages from the provided `requirements.txt` file:
```bash
pip install -r requirements.txt
```

#### Step 4: Add the environment as a Jupyter kernel (optional)
If you plan to use the notebook, register the virtual environment as a Jupyter kernel:
```bash
python -m ipykernel install --user --name whisperenv --display-name "Python (whisperenv)"
```

---

## Usage

1. **Launch Jupyter Notebook**:
   ```bash
   jupyter notebook
   ```
   Open the notebook `Whisper.ipynb` and ensure the kernel `Python (whisperenv)` is selected.

2. **Run the Notebook**:
   Follow the instructions in the notebook to download Whisper models, transcribe audio files, and save transcription results.

---

## Requirements

### Key Dependencies

- **Python**: 3.10 or higher
- **Conda**: (if using Conda setup)
- **PyTorch**: 2.5.1
- **OpenAI Whisper**: Latest version from GitHub
- **ffmpeg**: Must be installed and accessible via `PATH`.

---

## Notes

- Ensure `ffmpeg` is installed on your system. For Conda, it can be installed with:
  ```bash
  conda install -c conda-forge ffmpeg
  ```
  For other setups, refer to the [FFmpeg installation guide](https://ffmpeg.org/download.html).

- GPU support requires a CUDA-compatible device and appropriate CUDA libraries. Ensure PyTorch is configured to utilize CUDA for better performance.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
```