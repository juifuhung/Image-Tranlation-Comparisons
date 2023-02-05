import torch
import albumentations as A
from albumentations.pytorch import ToTensorV2

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
TRAIN_DIR = "ink2photo"
VAL_DIR = "ink2photo"
BATCH_SIZE = 1
LEARNING_RATE = 1e-5
LAMBDA_IDENTITY = 0.0
LAMBDA_CYCLE = 10
NUM_WORKERS = 4
NUM_EPOCHS = 100
LOAD_MODEL = True
SAVE_MODEL = False
CHECKPOINT_GEN_S = "ink_sobel2.genh.pth.tar"
CHECKPOINT_GEN_P = "ink_sobel2.genz.pth.tar"
CHECKPOINT_CRITIC_S = "ink_sobel2.critich.pth.tar"
CHECKPOINT_CRITIC_P = "ink_sobel2.criticz.pth.tar"
GENERATOR = "unet"

transforms = A.Compose(
    [
        A.Resize(width=256, height=256),
        #A.HorizontalFlip(p=0.5),
        A.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5], max_pixel_value=255),
        ToTensorV2(),
     ],
    additional_targets={"image0": "image"},
)