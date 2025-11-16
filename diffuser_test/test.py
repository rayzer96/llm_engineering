import os
from diffusers import StableDiffusionPipeline
import torch

pipe = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5", 
    torch_dtype=torch.float16, 
    safety_checker=None
)
pipe = pipe.to("cuda")
prompt = "black and white long haired cat"
image = pipe(prompt, guidance_scale=5, num_inference_steps=50).images[0]
image.save(os.path.abspath("./astronaut_riding_horse.png"))