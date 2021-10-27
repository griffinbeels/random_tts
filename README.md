# Random TTS Generator
Given a lower and upper time bound, reads out a randomly selected user-defined TTS phrase.

# Installation

### Assumptions:

* MacOS -- I developed this on Mac, not sure how it fares on Windows. Create with `create_venv.sh`; activate using, `source ~/baccpack_tts/bin/activate`.
    
* Windows -- Create with `create_venv_windows.sh`; activate using `source ~/gym_venv/Scripts/activate`.
        
* Python3.7.3 -- I developed this using Python3.7.3, so if you use a different Python version, keep in mind that there *may* be issues.
* VSCode -- If I mention any IDE specific things, it will be in the context of VSCode.
* Git -- I will assume a basic understanding of Git and how to navigate directories.

# Getting Started

### Installation:

1. Clone this repo. If you don't have Git installed, [install it here](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git). Clone by running the following in your terminal:
```
git clone https://github.com/griffinbeels/random_tts.git
```

2. `cd` into the cloned directory.

3. Create a virtual environment, by running the following in your terminal (refer to the above if using Windows):
```
./create_venv.sh
```

4. If the virtual environment is not activated (make sure it's active every time you run this program), do so by entering:
```
source ~/tts/bin/activate 
```

5. To run, simply enter:
```
python3.7 tts.py
```


