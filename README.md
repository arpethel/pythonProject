# pythonProject - A Speech to Text Application
This application converts speech from a microphone to text using Google's Web Speech API, then uses the OpenAI API to generate a text response to the transcribed speech.

## Installation

First, clone the repository:
```bash
git clone https://github.com/arpethel/pythonProject.git
cd repositoryName
```

Then, install the necessary Python packages:
```bash
pip install openai
pip install SpeechRecognition
pip install pillow
```
Note: You may need to use `pip3`, depending on what version of Python you have installed.

You'll also need to set your OpenAI API key as an environment variable. In a UNIX shell (like bash or zsh), you would use the export command:
```bash
export OPENAI_KEY="your-key-here"
```

In a Windows command prompt, you would use the `set` command:
```cmd
set OPENAI_KEY=your-key-here
```

In a Windows PowerShell, you would use the `$env`:
```powershell
$env:OPENAI_KEY="your-key-here"
```

The `os.getenv` function retrieves the value of the environment variable with the specified name.

Please note that environment variables set in this way are usually only available for the current session. If you close the terminal or command prompt and open a new one, you'll need to set the environment variable again.

To make environment variables persist across sessions, you need to set them in your shell's startup script (like ~/.bashrc or ~/.zshrc for bash or zsh, respectively) on Unix, or through the System Properties → Advanced → Environment Variables menu on Windows.

For production settings, consider using more advanced techniques for managing environment variables or secrets, such as dotenv files, or secret management services provided by cloud platforms.

## Usage
Run the script:
```bash
python program.py
```
Note: You may need to use `python3`, depending on what version of Python you have installed.

Speak into the microphone when prompted. The script will print the transcribed speech and the generated response.