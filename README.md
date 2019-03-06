This is "building gap resolution overnight" repository
for [Meanotek](meanotek.io) submission for [AGRR competition](https://github.com/dialogue-evaluation/AGRR-2019)

## Installation

 1. First, install [NeuThink](https://github.com/meanotekai/neuthink) library. 
 2. Then clone this repository. 
 3. Download pre-trained context embedding model from [here](https://www.dropbox.com/s/pffktcd2p51kzih/model3000x2x20482.mod?dl=1) and put in into the model3000x2x20482 folder

## Usage

To Train model:
1. Convert train data to conll using agrr2conll.py. You will need to change input and output file names in the script
2. Run train.py (ensure that you have converted file in the same directory). The script requires you to have GPU (8Gb GPU  RAM is needed).
3. Wait for completion
4. Run predict_gap.py for test file
5. convert data back to agrr format with conll2agrr.py


please contact dtarasov@meanotek.io if you have any problems
