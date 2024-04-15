import torch
from diffusers import StableDiffusionPipeline, AutoencoderTiny, AutoencoderKL
import argparse
import os
from datetime import datetime
import time

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument(
    '--prompt',
    default='A majestic goat with a realistic sunset and a blue lake, very detailed, a masterpiece',
    help='The prompt for the image generation')
parser.add_argument(
    '--large_vae',
    action='store_true')
args = parser.parse_args()

repo = 'IDKiro/sdxs-512-dreamshaper'

prompt = args.prompt
device = 'cpu'  # "cuda" | "cpu"
weight_type = torch.float32  # only torch.float32 for CPU

if args.large_vae:
    vae = AutoencoderKL.from_pretrained(repo, subfolder='vae_large')
else:
    vae = AutoencoderTiny.from_pretrained(repo, subfolder='vae')
vae.to(device, dtype=weight_type)

pipe = StableDiffusionPipeline.from_pretrained(
    repo,
    safety_checker=None,
    low_cpu_mem_usage=False,
    device_map=None,
    torch_dtype=weight_type)
pipe.vae = vae
pipe.to(torch_device=device, torch_dtype=weight_type)

start_time = time.perf_counter()

generator = torch.Generator(device=device)
image = pipe(
    prompt=prompt,
    guidance_scale=0.0,
    num_inference_steps=1,
    generator=generator.manual_seed(generator.seed())
).images[0]

end_time = time.perf_counter()

elapsed_time = end_time - start_time
print(f"Execution time: {round(elapsed_time, 3)} seconds")

formatted_now = datetime.now().strftime("%Y-%m-%d_%H%M%S")
img_folder_name = 'output'
output_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    img_folder_name,
    f"{formatted_now}.png")
os.makedirs(os.path.dirname(output_path), exist_ok=True)
image.save(output_path)

print(f"File saved: {output_path}")
