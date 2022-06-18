from enum import Enum 

IMAGES_OUTPUT_DIR = 'generations'

# DALL-E model
DALLE_MODEL_MINI = "dalle-mini/dalle-mini/mini-1:v0"  # the original DALL-E Mini. Fastest yet suboptimal results
DALLE_COMMIT_ID = None

# generation parameters
GEN_TOP_K = None
GEN_TOP_P = None
TEMPERATURE  = None
COND_SCALE = 10.0

# VQGAN model
VQGAN_REPO = "dalle-mini/vqgan_imagenet_f16_16384"
VQGAN_COMMIT_ID = "e93a26e7707683d349bf5d5c41c5b0ef69b677a9"

# model size
class ModelSize(Enum):
    MINI = "Mini"